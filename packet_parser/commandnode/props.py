
import enum
from typing import final, Self, ClassVar

from loginproxy import PacketBuffer, PacketReader

__all__ = [
	'NodeStringProp',
	'NodeEntityProp',
	'NodeScoreHolderProp',
	'ResourceOrTagProp',
	'ResourceOrTagKeyProp',
	'ResourceProp',
	'ResourceKeyProp',
	'ForgeEnumProp',
]

@final
class NodeStringProp(enum.Enum):
	SINGLE_WORD = 0
	QUOTABLE_PHRASE = 1
	GREEDY_PHRASE = 2

	def write_to(self, b: PacketBuffer) -> None:
		b.write_varint(self.value)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		value = r.read_varint()
		return cls(value)

@final
class NodeEntityProp:
	SINGLE_FLAG = 0x01
	PLAYER_FLAG = 0x02

	def __init__(self,
		flags: int, # Byte
	):
		self.flags = flags

	def write_to(self, b: PacketBuffer) -> None:
		b.write_byte(self.flags)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		flags = r.read_byte()
		return cls(flags)

@final
class NodeScoreHolderProp:
	MULTIPLE_FLAG = 0x01

	def __init__(self,
		flags: int, # Byte
	):
		self.flags = flags

	def write_to(self, b: PacketBuffer) -> None:
		b.write_byte(self.flags)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		flags = r.read_byte()
		return cls(flags)

class IdentifierBasedProp:
	def __init__(self,
		registry: str, # Identifier
	):
		self.registry = registry

	def write_to(self, b: PacketBuffer) -> None:
		b.write_string(self.registry)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		registry = r.read_string()
		return cls(registry)

@final
class ResourceOrTagProp(IdentifierBasedProp):
	pass

@final
class ResourceOrTagKeyProp(IdentifierBasedProp):
	pass

@final
class ResourceProp(IdentifierBasedProp):
	pass

@final
class ResourceKeyProp(IdentifierBasedProp):
	pass

@final
class ForgeEnumProp:
	def __init__(self,
		class_name: str, # String
	):
		self.class_name = class_name

	def write_to(self, b: PacketBuffer) -> None:
		b.write_string(self.class_name)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		class_name = r.read_string()
		return cls(class_name)
