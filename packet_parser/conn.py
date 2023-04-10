
import traceback
import threading
from typing import Type, Callable

from loginproxy import Conn, ConnStatus

from .packet import Packet
from .packets import V1_19
from .utils import *

class Listener:
	def __init__(self, callback: Callable[['Event'], None], priority: int | None = None):
		if priority is None:
			priority = 1000
		self.callback = callback
		self.priority = priority

	def insert_into(self, lst: list['Listener']) -> int:
		if len(lst) == 0:
			lst.append(self)
			return 0
		l, r = 0, len(lst) - 1
		m: int = 0
		while l <= r:
			m = (l + r) // 2
			o = lst[m].priority
			if o == self.priority:
				if m + 1 == len(lst) or lst[m + 1] != self.priority:
					lst.insert(m + 1, self)
					return m + 1
			if o > self.priority:
				r = m - 1
			else:
				l = m + 1
		if lst[m].priority >= self.priority:
			lst.insert(m + 1, self)
			return m + 1
		lst.insert(m, self)
		return m
		

class Event:
	_listener: dict[Type[Packet], list[Listener]] = {}
	def __init__(self, conn: Conn, pkt: Packet, *, cancelable: bool = False):
		self._conn = conn
		self._packet = pkt
		self._cancelable = False
		self._canceled = False

	@property
	def conn(self) -> Conn:
		return self._conn

	@property
	def status(self) -> ConnStatus:
		return self.conn.status

	@property
	def packet(self) -> Packet:
		return self._packet

	@property
	def cancelable(self) -> bool:
		return self._cancelable

	@property
	def canceled(self) -> bool:
		return self._canceled

	def cancel(self):
		if self.cancelable:
			self._canceled = True

	@classmethod
	def register(cls, pkt: Type[Packet], callback: Callable[['Event'], None], priority: int | None = None):
		l = Listener(callback, priority)
		if pkt not in Event._listener:
			Event._listener[pkt] = []
		l.insert_into(Event._listener[pkt])
		debug('Registered listener {0} (priority={1}) for {2}'.format(callback, priority, pkt))

	def trigger(self) -> bool:
		listeners = Event._listener.get(self._packet.__class__, None)
		if listeners is not None:
			for l in listeners:
				l.callback(self)
				if self.cancelable and self.canceled:
					break
			return True
		return False

def _disconnect(event: Event):
	event.conn.disconnect()

Event.register(V1_19.LoginDisconnectS2C, _disconnect)
Event.register(V1_19.PlayDisconnectS2C, _disconnect)

def _set_compression(event: Event):
	pkt = event.packet
	assert isinstance(pkt, V1_19.LoginSetCompressionS2C)
	conn = event.conn
	debug('Set compress threshold to', pkt.threshold)
	conn.compress_threshold = pkt.threshold

Event.register(V1_19.LoginSetCompressionS2C, _set_compression)

def _login_success(event: Event):
	conn = event.conn
	debug(f'Conn {conn.addr} logged success')
	conn.status = ConnStatus.PLAY

Event.register(V1_19.LoginSuccessS2C, _login_success)

@new_thread('parser_forwarder_c2s')
def forwarder_c2s(c: Conn, login_data: dict, final=None):
	try:
		protocol = login_data['protocol']
		while True:
			r = c.recvpkt()
			debug(f'[C2S] Parsing packet {r.id} with status {c.status}')
			try:
				pkt = Packet.parse(r, protocol, True, c.status)
			except Exception as e:
				log_error('[C2S] Error when parse package {0}: {1}: {2}'.format(
					Packet.get_packet_cls(protocol, True, c.status, r.id), type(e), e))
				debug(traceback.format_exc())
				pkt = None
			if pkt is None:
				log_warn(f'[C2S] Cannot parse package 0x{r.id:02x} with status {c.status} under protocol {protocol}')
				c.sendpkt2(r.data, None)
			else:
				e = Event(c, pkt, cancelable=True)
				e.trigger()
				if not e.canceled:
					c.sendpkt2(r.data, None)
	except (ConnectionAbortedError, ConnectionResetError, BrokenPipeError, OSError):
		pass
	except Exception as e:
		log_warn('Error when handle[{0[0]}:{0[1]}]: {1}'.format(c.addr, str(e)))
		traceback.print_exc()
	finally:
		if final is not None:
			final()

@new_thread('parser_forwarder_s2c')
def forwarder_s2c(c: Conn, login_data: dict, final=None):
	try:
		protocol = login_data['protocol']
		while True:
			r = c.recvpkt2()
			debug(f'[S2C] Parsing packet {r.id} with status {c.status}')
			try:
				pkt = Packet.parse(r, protocol, False, c.status)
			except Exception as e:
				log_error('[S2C] Error when parse package {0}: {1}: {2}'.format(
					Packet.get_packet_cls(protocol, False, c.status, r.id), type(e), e))
				debug(traceback.format_exc())
				pkt = None
			if pkt is None:
				log_warn(f'[S2C] Cannot parse package 0x{r.id:02x} with status {c.status} under protocol {protocol}')
				c.sendpkt2(r.data, None)
			else:
				if isinstance(pkt, V1_19.LoginSetCompressionS2C):
					c.sendpkt(r.data, None)
					e = Event(c, pkt, cancelable=False)
					e.trigger()
				else:
					e = Event(c, pkt, cancelable=True)
					e.trigger()
					if not e.canceled:
						c.sendpkt(r.data, None)
	except (ConnectionAbortedError, ConnectionResetError, BrokenPipeError, OSError):
		pass
	except Exception as e:
		log_warn('Error when handle[{0[0]}:{0[1]}]: {1}'.format(c.addr, str(e)))
		traceback.print_exc()
	finally:
		if final is not None:
			final()

def proxy_conn(conn: Conn, login_data: dict, *, final=None):
	cond = threading.Condition(threading.Lock())
	finished = False
	def waiter():
		with cond:
			if finished:
				return
			cond.wait()
	def final0():
		nonlocal finished
		with cond:
			if finished:
				return
			finished = True
			cond.notify_all()
		if final is not None:
			final()
	forwarder_c2s(conn, login_data, final=final0)
	forwarder_s2c(conn, login_data, final=final0)
