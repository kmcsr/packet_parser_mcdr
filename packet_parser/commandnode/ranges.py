
from typing import final, Self

from loginproxy import PacketBuffer, PacketReader

__all__ = [
	'IntRange',
	'LongRange',
	'FloatRange',
	'DoubleRange',
	'TimeRange',
]

@final
class IntRange:
	def __init__(self,
		flags: int, # Byte
		min: int | None, # Optional integer
		max: int | None, # Optional integer
	):
		self.flags = flags
		self.min = min
		self.max = max

	def write_to(self, b: PacketBuffer) -> None:
		b.write_byte(self.flags)
		if self.flags & 0x01:
			assert self.min is not None
			b.write_int(self.min)
		if self.flags & 0x02:
			assert self.max is not None
			b.write_int(self.max)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		flags = r.read_byte()
		min = r.read_int() if flags & 0x01 else None
		max = r.read_int() if flags & 0x02 else None
		return cls(flags, min, max)

@final
class LongRange:
	def __init__(self,
		flags: int, # Byte
		min: int | None, # Optional long
		max: int | None, # Optional long
	):
		self.flags = flags
		self.min = min
		self.max = max

	def write_to(self, b: PacketBuffer) -> None:
		b.write_byte(self.flags)
		if self.flags & 0x01:
			assert self.min is not None
			b.write_long(self.min)
		if self.flags & 0x02:
			assert self.max is not None
			b.write_long(self.max)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		flags = r.read_byte()
		min = r.read_long() if flags & 0x01 else None
		max = r.read_long() if flags & 0x02 else None
		return cls(flags, min, max)

@final
class FloatRange:
	def __init__(self,
		flags: int, # Byte
		min: float | None, # Optional float
		max: float | None, # Optional float
	):
		self.flags = flags
		self.min = min
		self.max = max

	def write_to(self, b: PacketBuffer) -> None:
		b.write_byte(self.flags)
		if self.flags & 0x01:
			assert self.min is not None
			b.write_float(self.min)
		if self.flags & 0x02:
			assert self.max is not None
			b.write_float(self.max)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		flags = r.read_byte()
		min = r.read_float() if flags & 0x01 else None
		max = r.read_float() if flags & 0x02 else None
		return cls(flags, min, max)

@final
class DoubleRange:
	def __init__(self,
		flags: int, # Byte
		min: float | None, # Optional double
		max: float | None, # Optional double
	):
		self.flags = flags
		self.min = min
		self.max = max

	def write_to(self, b: PacketBuffer) -> None:
		b.write_byte(self.flags)
		if self.flags & 0x01:
			assert self.min is not None
			b.write_double(self.min)
		if self.flags & 0x02:
			assert self.max is not None
			b.write_double(self.max)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		flags = r.read_byte()
		min = r.read_double() if flags & 0x01 else None
		max = r.read_double() if flags & 0x02 else None
		return cls(flags, min, max)

@final
class TimeRange:
	def __init__(self,
		min: int, # Integer
	):
		self.min = min

	def write_to(self, b: PacketBuffer) -> None:
		b.write_int(self.min)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		min = r.read_int()
		return cls(min)
