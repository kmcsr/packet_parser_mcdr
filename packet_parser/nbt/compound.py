
import uuid
from typing import final, Self

from loginproxy import PacketBuffer, PacketReader

from .nbt import NBT

__all__ = [
	'Compound',
]

class Compound(NBT):
	def to_bytes(self, b: PacketBuffer) -> None:
		raise NotImplementedError()

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		raise NotImplementedError()
