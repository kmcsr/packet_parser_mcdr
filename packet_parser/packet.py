
import abc
from abc import abstractmethod, abstractclassmethod
from typing import TypeAlias, TypeVar, Self, Type

from loginproxy import ConnStatus, PacketReader, PacketBuffer

__all__ = [
	'PacketIdMap', 'PacketStatusMap', 'PacketRepo', 'Packet',
]

PacketSelf = TypeVar('PacketSelf', bound='Packet')
PacketType: TypeAlias = Type[PacketSelf]

class PacketIdMap:
	def __init__(self) -> None:
		self._value: dict[int, PacketType] = {}

	@property
	def value(self) -> dict[int, PacketType]:
		return self._value

	def add(self, typ: PacketType, id: int) -> Self:
		assert int not in self.value, f'Packet id {int} already exists'
		self.value[id] = typ
		return self

	def get(self, id: int) -> PacketType | None:
		return self.value.get(id, None)

	def __setitem__(self, key: int, value: PacketType):
		self.value[key] = value

	def __getitem__(self, key: int) -> PacketType:
		return self.value[key]

class PacketStatusMap:
	def __init__(self) -> None:
		self._value: dict[ConnStatus, PacketIdMap] = {}

	@property
	def value(self) -> dict[ConnStatus, PacketIdMap]:
		return self._value

	def add(self, status: ConnStatus, typ: PacketIdMap) -> Self:
		assert status not in self.value, f'Status {status} already exists'
		self.value[status] = typ
		return self

	def get(self, status: ConnStatus, id: int) -> PacketType | None:
		m = self.value.get(status, None)
		if m is None:
			return None
		return m.get(id)

	def __setitem__(self, key: ConnStatus, value: PacketIdMap):
		self.value[key] = value

	def __getitem__(self, key: ConnStatus) -> PacketIdMap:
		return self.value[key]

class PacketRepo:
	def __init__(self, protocol: int, c2s: PacketStatusMap, s2c: PacketStatusMap):
		self._protocol = protocol
		self._c2s = c2s
		self._s2c = s2c

	@property
	def protocol(self):
		return self._protocol
	
	@property
	def c2s(self):
		return self._c2s

	@property
	def s2c(self):
		return self._s2c

def _search_repo(lst: list[PacketRepo], protocol: int) -> int:
		l, r = 0, len(lst) - 1
		m: int = 0
		while l <= r:
			m = (l + r) // 2
			o = lst[m].protocol
			if o == protocol:
				return m
			if o < protocol:
				l = m + 1
			else:
				r = m - 1
		return m


class Packet(abc.ABC):
	_packet_types: list[PacketRepo] = []

	@staticmethod
	def register(repo: PacketRepo):
		if len(Packet._packet_types) == 0:
			Packet._packet_types.append(repo)
			return
		i = _search_repo(Packet._packet_types, repo.protocol)
		rp = Packet._packet_types[i].protocol
		assert rp != repo.protocol, f'Protocol {repo.protocol} is already exists'
		if rp > repo.protocol:
			i += 1
		Packet._packet_types.insert(i, repo)

	@staticmethod
	def get_packet_cls(protocol: int, c2s: bool, status: ConnStatus, id: int) -> PacketType | None:
		if len(Packet._packet_types) == 0:
			return None
		i = _search_repo(Packet._packet_types, protocol)
		while i >= 0:
			repo = Packet._packet_types[i]
			t = (repo.c2s if c2s else repo.s2c).get(status, id)
			if t is not None:
				return t
			i -= 1
		return None

	@staticmethod
	def parse(r: PacketReader, protocol: int, c2s: bool, status: ConnStatus) -> PacketSelf | None:
		typ = Packet.get_packet_cls(protocol, c2s, status, r.id)
		if typ is None:
			return None
		pkt = typ.parse_from(r)
		remain = r.remain
		if remain != 0:
			raise RuntimeError('Parser did not parsed all data, remain {} bytes'.format(remain))
		return pkt

	@abstractmethod
	def to_bytes(self, b: PacketBuffer):
		raise NotImplementedError()

	@classmethod
	@abstractmethod
	def parse_from(cls, r: PacketReader) -> Self:
		raise NotImplementedError()
