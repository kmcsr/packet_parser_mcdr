
import traceback
import threading
from typing import Type, Callable

from loginproxy import Conn, ConnStatus

from .packet import Packet
from .utils import *

class Listener:
	def __init__(self, callback: Callable[['Event'], None], priority: int | None = None):
		if priority is None:
			priority = 1000
		self.callback = callback
		self.priority = priority

	def insert_into(self, lst: list[Listener]) -> int:
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
	def cancelable(self) -> bool:
		return self._cancelable

	@property
	def canceled(self) -> bool:
		return self._canceled

	def cancel(self):
		if self.cancelable:
			self._canceled = True

	@staticmethod
	def register(callback: Callable[['Event'], None], priority: int | None = None):
		l = Listener(callback, priority)

	def trigger(self) -> bool:
		listeners = Event._listener.get(self._packet.__class__, None)
		if listeners is not None:
			for l in listeners:
				l.callback(self)
				if self.cancelable and self.canceled:
					break
			return True
		return False

@new_thread('parser_forwarder_c2s')
def forwarder_c2s(c: Conn, login_data: dict, final=None):
	try:
		protocol = login_data['protocol']
		while True:
			r = c.recvpkt()
			pkt = Packet.parse(r, protocol, True, c.status)
			if pkt is None:
				log_warn(f'[C2S] Cannot parse package {r.id} with status {c.status} under protocol {protocol}')
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

@new_thread('parser_forwarder_c2s')
def forwarder_s2c(c: Conn, login_data: dict, final=None):
	try:
		protocol = login_data['protocol']
		while True:
			r = c.recvpkt2()
			pkt = Packet.parse(r, protocol, False, c.status)
			if pkt is None:
				log_warn(f'[S2C] Cannot parse package {r.id} with status {c.status} under protocol {protocol}')
				c.sendpkt2(r.data, None)
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
