
import mcdreforged.api.all as MCDR

from . import api
from .api import *
from .utils import *

__all__ = []
__all__.extend(api.__all__)

def on_load(server: MCDR.PluginServerInterface, prev_module):
	if prev_module is None:
		log_info('PacketParser is on LOAD')
	else:
		log_info('PacketParser is on RELOAD')
	api.on_load(server, prev_module)

def on_unload(server: MCDR.PluginServerInterface):
	log_info('PacketParser is on UNLOAD')
	api.on_unload(server)
