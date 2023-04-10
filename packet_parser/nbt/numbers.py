
import struct
from typing import final, Self

from loginproxy import PacketBuffer, PacketReader

from .nbt import NBT, NBTID

__all__ = [
	'Byte', 'Short', 'Int', 'Long',
	'Float', 'Double',
]

class _Integers(NBT):
	MIN_VALUE: int
	MAX_VALUE: int
	def __init_subclass__(cls, *, byten: int, **kwargs):
		super().__init_subclass__(**kwargs)
		mask = 1 << (8 * byten - 1)
		cls.MIN_VALUE = -mask
		cls.MAX_VALUE = mask - 1

	def __init__(self, value: int, name: str | None = None):
		cls = self.__class__
		if value < cls.MIN_VALUE or cls.MAX_VALUE < value:
			raise ValueError(f'Value {value} out of range [{cls.MIN_VALUE}, {cls.MAX_VALUE}]')
		super().__init__(name)
		self._value = value

	@property
	def value(self) -> int:
		return self._value

	@value.setter
	def value(self, value: int):
		self._value = value

	def as_str(self, *, indent: int = 0) -> str:
		return super().as_str(indent=indent) + ': {}'.format(self.value)

@final
class Byte(_Integers, id=NBTID.Byte, byten=1):
	def to_bytes_value(self, b: PacketBuffer) -> None:
		b.write_byte(self.value)

	@classmethod
	def parse_from(cls, r: PacketReader, name: str | None = None) -> Self:
		value = r.read_byte()
		return cls(value, name)

@final
class Short(_Integers, id=NBTID.Short, byten=2):
	def to_bytes_value(self, b: PacketBuffer) -> None:
		b.write_short(self.value)

	@classmethod
	def parse_from(cls, r: PacketReader, name: str | None = None) -> Self:
		value = r.read_short()
		return cls(value, name)

@final
class Int(_Integers, id=NBTID.Int, byten=4):
	def to_bytes_value(self, b: PacketBuffer) -> None:
		b.write_int(self.value)

	@classmethod
	def parse_from(cls, r: PacketReader, name: str | None = None) -> Self:
		value = r.read_int()
		return cls(value, name)

@final
class Long(_Integers, id=NBTID.Long, byten=8):
	def to_bytes_value(self, b: PacketBuffer) -> None:
		b.write_long(self.value)

	@classmethod
	def parse_from(cls, r: PacketReader, name: str | None = None) -> Self:
		value = r.read_long()
		return cls(value, name)

class _Decimals(NBT):
	def __init__(self, value: float, name: str | None = None):
		super().__init__(name)
		self._value = value

	@property
	def value(self) -> float:
		return self._value

	@value.setter
	def value(self, value: float):
		self._value = value

	def as_str(self, *, indent: int = 0) -> str:
		return super().as_str(indent=indent) + ': {}'.format(self.value)

@final
class Float(_Decimals, id=NBTID.Float):
	def to_bytes_value(self, b: PacketBuffer) -> None:
		b.write_float(self.value)

	@classmethod
	def parse_from(cls, r: PacketReader, name: str | None = None) -> Self:
		value = r.read_float()
		return cls(value, name)

@final
class Double(_Decimals, id=NBTID.Double):
	def to_bytes_value(self, b: PacketBuffer) -> None:
		b.write_double(self.value)

	@classmethod
	def parse_from(cls, r: PacketReader, name: str | None = None) -> Self:
		value = r.read_double()
		return cls(value, name)
