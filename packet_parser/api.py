
import mcdreforged.api.all as MCDR

from loginproxy import get_proxy
from loginproxy.server import ProxyServer, Conn, ConnStatus

from .conn import proxy_conn
from .utils import *

def on_login(self: ProxyServer, conn, addr: tuple[str, int], name: str, login_data: dict):
	log_info('Player {0}[[{1[0]}]:{1[1]}] trying to join'.format(name, addr))
	sokt = self.new_connection(login_data)
	c = Conn(name, addr, conn, self, sokt, login_data)
	def final():
		with self._conns:
			if self._conns.d.pop(c.name, None) is not None:
				c._set_close()
	with self._conns:
		self._conns.d[name] = c
	c.status = ConnStatus.LOGIN
	proxy_conn(c, login_data, final=final)
	return True

def on_load(server: MCDR.PluginServerInterface, prev_module):
	px = get_proxy()
	px.on_login = on_login

def on_unload(server: MCDR.PluginServerInterface):
	pass
