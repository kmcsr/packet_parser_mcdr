
from typing import final, Self

from loginproxy import PacketBuffer, PacketReader

from .nbt import NBT, NBTID

__all__ = [
	'End',
	'Compound',
]

@final
class End(NBT, id=NBTID.End):
	_INSTANCE = None
	def __new__(cls):
		if cls._INSTANCE is None:
			cls._INSTANCE = super().__new__(cls)
			super().__init__(cls._INSTANCE, None)
		return cls._INSTANCE

	def __init__(self):
		pass

	def to_bytes_value(self, b: PacketBuffer):
		pass

	@classmethod
	def parse_from(cls, r: PacketReader, name: str | None = None) -> Self:
		assert name is None
		return cls()

@final
class Compound(NBT, id=NBTID.Compound):
	def __init__(self, children: list[NBT] | dict[str, NBT], name: str | None = None):
		super().__init__(name)
		if isinstance(children, dict):
			for key, tag in children.items():
				tag.name = key
			self._children = children
		else:
			self._children = {}
			for tag in children:
				self._children[tag.name] = tag

	@property
	def children(self) -> list[NBT]:
		return list(self._children.values())

	def to_bytes_value(self, b: PacketBuffer) -> None:
		for tag in self._children.values():
			tag.to_bytes(b)
		End().to_bytes(b)

	@classmethod
	def parse_from(cls, r: PacketReader, name: str | None = None) -> Self:
		children: list[NBT] = []
		while True:
			tag = NBT.parse(r)
			if tag.ID == NBTID.End:
				break
			children.append(tag)
		return cls(children, name=name)

	def add(self, tag: NBT):
		if tag.name in self._children:
			raise ValueError(f'Name {tag.name} already exists')
		self._children[tag.name] = tag

	def remove(self, tag: NBT) -> bool:
		t = self.get(tag.name, None)
		if t is not None and t == tag:
			del self[tag.name]
			return True
		return False

	def pop(self, name: str, default: NBT | None = None) -> NBT | None:
		return self._children.pop(name, None)

	def get(self, name: str, default: NBT | None = None) -> NBT | None:
		return self._children.get(name, default)

	def values(self):
		return self._children.values()

	def __len__(self) -> int:
		return len(self._children)

	def __iter__(self):
		return iter(self._children)

	def __getitem__(self, name: str) -> NBT:
		return self._children[name]

	def __setitem__(self, name: str, tag: NBT):
		tag.name = name
		self._children[name] = tag

	def __delitem__(self, name: str):
		del self._children[name]

	def __contains__(self, obj: str | NBT) -> bool:
		if isinstance(obj, NBT):
			return obj in self._children.values()
		return obj in self._children

	def as_str(self, *, indent: int = 0) -> str:
		ind = '  ' * indent
		s = super().as_str(indent=indent) + ': ' + \
			('1 entry' if len(self) == 1 else '{} entries\n'.format(len(self))) + \
			ind + '{\n'
		indent += 1
		for e in sorted(self.values(), key=lambda v: v.name):
			s += e.as_str(indent=indent) + '\n'
		s += ind + '}'
		return s
