
from typing import Any

from .nbt import NBT, NBTID
from .compound import End, Compound
from .lists import List, String, ByteArray, IntArray, LongArray
from .numbers import Byte, Short, Int, Long, Float, Double

__all__ = [
	'NBT', 'NBTID',
	'Byte', 'Short', 'Int', 'Long', 'Float', 'Double',
	'End', 'Compound', 'List', 'String',
	'ByteArray', 'IntArray', 'LongArray',
	'nbt_to_chat_object', 'chat_object_to_nbt',
]

def nbt_to_chat_object(tag: NBT) -> Any:
	if isinstance(tag, Byte):
		return tag.value != 0
	if isinstance(tag, String):
		return tag.value
	if isinstance(tag, List):
		return [nbt_to_chat_object(v) for v in tag.children]
	if isinstance(tag, Compound):
		data: dict[str, Any] = {}
		for v in tag:
			data[v.name] = nbt_to_chat_object(v)
		return data
	raise TypeError(f'Unexpected NBT tag: {repr(tag)}')

def chat_object_to_nbt(data: Any) -> NBT:
	if isinstance(data, bool):
		return Byte(1 if data else 0)
	if isinstance(data, str):
		return String(data)
	if isinstance(data, list):
		return List(NBTID.Compound, [Compound([String(v, 'text')]) if isinstance(v, str) else chat_object_to_nbt(v) for v in data])
	if isinstance(data, dict):
		compound = Compound([])
		for k, v in data.items():
			compound[k] = chat_object_to_nbt(v)
		return compound
	raise TypeError(f'Unexpected type "{k}": {type(v)}')
