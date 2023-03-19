
import mcdreforged.api.all as MCDR

from kpi.utils import *

__all__ = [
	'new_thread', 'tr', 'debug', 'log_info', 'log_warn', 'log_error',
	'get_server_instance',
	'new_timer', 'new_command', 'join_rtext', 'send_message', 'broadcast_message',
]

def new_thread(name_or_call):
	def wrapper(call):
		return MCDR.new_thread(name_or_call)(call)
	if isinstance(name_or_call, str):
		return wrapper
	assert callable(name_or_call)
	return wrapper('packet_parser')(name_or_call)

def tr(key: str, *args, **kwargs):
	return get_server_instance().rtr(f'packet_parser.{key}', *args, **kwargs)
