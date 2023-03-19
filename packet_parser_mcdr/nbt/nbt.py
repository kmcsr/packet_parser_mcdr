
import uuid
from typing import final, Self

from loginproxy import PacketBuffer, PacketReader

__all__ = [
	'NBT',
]

class NBT:
	def to_bytes(self, b: PacketBuffer) -> None:
		raise NotImplementedError()

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		raise NotImplementedError()
