
import abc
import enum
import uuid
from abc import abstractmethod
from typing import final, Self, Type

from loginproxy import PacketBuffer, PacketReader

from .mutf8 import *

__all__ = [
	'NBTID',
	'NBT',
]

class NBTID(enum.Enum):
	Unknown    = -1
	End        = 0x00
	Byte       = 0x01
	Short      = 0x02
	Int        = 0x03
	Long       = 0x04
	Float      = 0x05
	Double     = 0x06
	Byte_Array = 0x07
	String     = 0x08
	List       = 0x09
	Compound   = 0x0a
	Int_Array  = 0x0b
	Long_Array = 0x0c

class NBT(abc.ABC):
	ID: NBTID
	_nbt_cls: dict[NBTID, Type['NBT']] = {}

	def __init_subclass__(cls, *, id: NBTID = NBTID.Unknown):
		super().__init_subclass__()
		if id != NBTID.Unknown:
			cls.ID = id
			NBT._nbt_cls[cls.ID] = cls

	def __init__(self, name: str | None):
		self._name = name

	@property
	def name(self) -> str:
		assert self._name is not None
		return self._name

	@name.setter
	def name(self, name: str):
		if self._name is None:
			self._name = name
		elif name != self._name:
			raise ValueError(f'Tag already have a name {repr(self._name)}, but trying to set to {repr(name)}')

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_byte(self.__class__.ID.value)
		if self.name is not None:
			name = utf8s_to_utf8m(self.name.encode('utf8'))
			b.write_short(len(name))
			b.write(name)
		self.to_bytes_value(b)

	@abstractmethod
	def to_bytes_value(self, b: PacketBuffer) -> None:
		raise NotImplementedError()

	@classmethod
	@abstractmethod
	def parse_from(cls, r: PacketReader, name: str | None = None) -> Self:
		raise NotImplementedError()

	@staticmethod
	def parse(r: PacketReader) -> 'NBT':
		id = NBTID(r.read_ubyte())
		name = utf8m_to_utf8s(r.read(r.read_ushort())).decode('utf8') if id != NBTID.End else None
		return NBT._nbt_cls[id].parse_from(r, name)
