
from abc import abstractmethod
from typing import final, Type, Self

from loginproxy import ConnStatus, PacketReader, PacketBuffer

from .packet import *

######## BEGIN HANDSHAKING ########

@final
class HandshakeC2S(Packet, id=0x00):
	def __init__(self, protocol: int, address: str, port: int, next_state: int):
		self.protocol = protocol
		self.address = address
		self.port = port
		self.next_state = next_state

	def to_bytes(self, b: PacketBuffer):
		b.\
			write_varint(self.protocol).\
			write_string(self.address).\
			write_short(self.port).\
			write_varint(self.next_state)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		protocol = r.read_varint()
		address = r.read_string()
		port = r.read_short()
		next_state = r.read_varint()
		return cls(protocol, address, port, next_state)

######## END HANDSHAKING ########

######## BEGIN STATUS ########

@final
class StatusResponseS2C(Packet, id=0x00):
	def __init__(self, status: dict):
		self.status = status

	def to_bytes(self, b: PacketBuffer):
		b.\
			write_json(self.status)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		status = r.read_json()
		return cls(status)

@final
class StatusPongS2C(Packet, id=0x01):
	def __init__(self, payload: int):
		self.payload = payload

	def to_bytes(self, b: PacketBuffer):
		b.\
			write_long(self.payload)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		payload = r.read_long()
		return cls(payload)

@final
class StatusRequestC2S(Packet):
	_INSTANCE = None
	def __new__(cls):
		if cls._INSTANCE is None:
			cls._INSTANCE = super().__new__(cls)
		return cls._INSTANCE

	def __init__(self):
		pass

	def to_bytes(self, b: PacketBuffer):
		pass

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		return StatusRequestC2S()


@final
class StatusPingC2S(Packet):
	def __init__(self, payload: int):
		self.payload = payload

	def to_bytes(self, b: PacketBuffer):
		b.\
			write_long(self.payload)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		payload = r.read_long()
		return cls(payload)

######## END STATUS ########

######## BEGIN LOGIN ########

@final
class LoginDisconnectS2C(Packet):


######## END LOGIN ########
