
from typing import final, Self

from loginproxy import PacketBuffer, PacketReader

from .nbt import NBT, NBTID
from .numbers import Byte, Int, Long
from .mutf8 import *

__all__ = [
	'List',
	'Byte_Array', 'Int_Array', 'Long_Array',
]

@final
class List(NBT, id=NBTID.List):
	def __init__(self, element: NBTID, children: list[NBT], name: str | None = None):
		super().__init__(name)
		for tag in children:
			if tag.__class__.ID != element:
				raise ValueError(f'Element type must be {element}, but got {tag.__class__.ID}')
			if tag._name is not None:
				raise ValueError(f'Element name must be None, but got {tag.name}')
		self._element = element
		self._children = children

	@property
	def element(self) -> NBTID:
		return self._element

	@property
	def children(self) -> list[NBT]:
		return self._children

	def to_bytes_value(self, b: PacketBuffer) -> None:
		b.write_byte(self.element.value)
		b.write_int(len(self.children))
		for c in self.children:
			c.to_bytes_value(b)

	@classmethod
	def parse_from(cls, r: PacketReader, name: str | None = None) -> Self:
		element = NBTID(r.read_byte())
		eletyp = NBT._nbt_cls[element]
		children = [eletyp.parse_from(r) for _ in range(r.read_int())]
		return cls(element, children, name=name)

class String(NBT, id=NBTID.String):
	def __init__(self, value: str, name: str | None = None):
		super().__init__(name)
		self._value = value

	@property
	def value(self) -> str:
		return self._value

	def to_bytes_value(self, b: PacketBuffer) -> None:
		bts = utf8s_to_utf8m(self.value.encode('utf8'))
		b.write_short(len(bts))
		b.write(bts)

	@classmethod
	def parse_from(cls, r: PacketReader, name: str | None = None) -> Self:
		value = utf8m_to_utf8s(r.read(r.read_short())).decode('utf8')
		return cls(value, name)

class Byte_Array(NBT, id=NBTID.Byte_Array):
	def __init__(self, value: list[Byte] | list[int] | bytes | bytearray, name: str | None = None):
		super().__init__(name)
		if isinstance(value, (bytes, bytearray)):
			self._value = bytearray(value)
		else:
			self._value = bytearray([])
			for tag in value:
				if isinstance(tag, int):
					self._value.append(tag)
				else:
					if tag.__class__.ID != NBTID.Byte:
						raise ValueError(f'Element type must be nbt.Byte, but got {tag.__class__.ID}')
					if tag._name is not None:
						raise ValueError(f'Element name must be None, but got {tag.name}')
					self._value.append(tag.value)

	@property
	def value(self) -> bytearray:
		return self._value

	def to_bytes_value(self, b: PacketBuffer) -> None:
		b.write_int(len(self.value))
		b.write(bytes(self.value))

	@classmethod
	def parse_from(cls, r: PacketReader, name: str | None = None) -> Self:
		value = r.read(r.read_int())
		return cls(value, name)

class Int_Array(NBT, id=NBTID.Int_Array):
	def __init__(self, value: list[Int] | list[int], name: str | None = None):
		super().__init__(name)
		self._value: list[int] = []
		for tag in value:
			if isinstance(tag, int):
				self._value.append(tag)
			else:
				if tag.__class__.ID != NBTID.Int:
					raise ValueError(f'Element type must be nbt.Int, but got {tag.__class__.ID}')
				if tag._name is not None:
					raise ValueError(f'Element name must be None, but got {tag.name}')
				self._value.append(tag.value)

	@property
	def value(self) -> list[int]:
		return self._value

	def to_bytes_value(self, b: PacketBuffer) -> None:
		b.write_int(len(self.value))
		for v in self.value:
			Int(v).to_bytes_value(b)

	@classmethod
	def parse_from(cls, r: PacketReader, name: str | None = None) -> Self:
		value = [r.read_int() for _ in range(r.read_int())]
		return cls(value, name)

class Long_Array(NBT, id=NBTID.Long_Array):
	def __init__(self, value: list[Long] | list[int], name: str | None = None):
		super().__init__(name)
		self._value: list[int] = []
		for tag in value:
			if isinstance(tag, int):
				self._value.append(tag)
			else:
				if tag.__class__.ID != NBTID.Long:
					raise ValueError(f'Element type must be nbt.Long, but got {tag.__class__.ID}')
				if tag._name is not None:
					raise ValueError(f'Element name must be None, but got {tag.name}')
				self._value.append(tag.value)

	@property
	def value(self) -> list[int]:
		return self._value

	def to_bytes_value(self, b: PacketBuffer) -> None:
		b.write_int(len(self.value))
		for v in self.value:
			Long(v).to_bytes_value(b)

	@classmethod
	def parse_from(cls, r: PacketReader, name: str | None = None) -> Self:
		value = [r.read_long() for _ in range(r.read_int())]
		return cls(value, name)
