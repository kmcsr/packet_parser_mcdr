
from typing import final, Self, Any, Callable

from loginproxy import Protocol, PacketBuffer, PacketReader

from .props import *
from .ranges import *

__all__ = [
	'Node',
]

ID_MAPS: list[tuple[int, list[str]]] = []

ID_MAPS.append((Protocol.V1_21, [
	'brigadier:bool',
	'brigadier:float',
	'brigadier:double',
	'brigadier:integer',
	'brigadier:long',
	'brigadier:string',
	'minecraft:entity',
	'minecraft:game_profile',
	'minecraft:block_pos',
	'minecraft:column_pos',
	'minecraft:vec3',
	'minecraft:vec2',
	'minecraft:block_state',
	'minecraft:block_predicate',
	'minecraft:item_stack',
	'minecraft:item_predicate',
	'minecraft:color',
	'minecraft:component',
	'minecraft:style',
	'minecraft:message',
	'minecraft:nbt',
	'minecraft:nbt_tag',
	'minecraft:nbt_path',
	'minecraft:objective',
	'minecraft:objective_criteria',
	'minecraft:operation',
	'minecraft:particle',
	'minecraft:angle',
	'minecraft:rotation',
	'minecraft:scoreboard_slot',
	'minecraft:score_holder',
	'minecraft:swizzle',
	'minecraft:team',
	'minecraft:item_slot',
	'minecraft:item_slots',
	'minecraft:resource_location',
	'minecraft:function',
	'minecraft:entity_anchor',
	'minecraft:int_range',
	'minecraft:float_range',
	'minecraft:dimension',
	'minecraft:gamemode',
	'minecraft:time',
	'minecraft:resource_or_tag',
	'minecraft:resource_or_tag_key',
	'minecraft:resource',
	'minecraft:resource_key',
	'minecraft:template_mirror',
	'minecraft:template_rotation',
	'minecraft:heightmap',
	'minecraft:loot_table',
	'minecraft:loot_predicate',
	'minecraft:loot_modifier',
	'minecraft:uuid',
]))

ID_MAPS.append((Protocol.V1_20_3, [
	'brigadier:bool',
	'brigadier:float',
	'brigadier:double',
	'brigadier:integer',
	'brigadier:long',
	'brigadier:string',
	'minecraft:entity',
	'minecraft:game_profile',
	'minecraft:block_pos',
	'minecraft:column_pos',
	'minecraft:vec3',
	'minecraft:vec2',
	'minecraft:block_state',
	'minecraft:block_predicate',
	'minecraft:item_stack',
	'minecraft:item_predicate',
	'minecraft:color',
	'minecraft:component',
	'minecraft:style',
	'minecraft:message',
	'minecraft:nbt',
	'minecraft:nbt_tag',
	'minecraft:nbt_path',
	'minecraft:objective',
	'minecraft:objective_criteria',
	'minecraft:operation',
	'minecraft:particle',
	'minecraft:angle',
	'minecraft:rotation',
	'minecraft:scoreboard_slot',
	'minecraft:score_holder',
	'minecraft:swizzle',
	'minecraft:team',
	'minecraft:item_slot',
	'minecraft:resource_location',
	'minecraft:function',
	'minecraft:entity_anchor',
	'minecraft:int_range',
	'minecraft:float_range',
	'minecraft:dimension',
	'minecraft:gamemode',
	'minecraft:time',
	'minecraft:resource_or_tag',
	'minecraft:resource_or_tag_key',
	'minecraft:resource',
	'minecraft:resource_key',
	'minecraft:template_mirror',
	'minecraft:template_rotation',
	'minecraft:heightmap',
	'minecraft:uuid',
]))

ID_MAPS.append((Protocol.V1_19_4, [
	'brigadier:bool',
	'brigadier:float',
	'brigadier:double',
	'brigadier:integer',
	'brigadier:long',
	'brigadier:string',
	'minecraft:entity',
	'minecraft:game_profile',
	'minecraft:block_pos',
	'minecraft:column_pos',
	'minecraft:vec3',
	'minecraft:vec2',
	'minecraft:block_state',
	'minecraft:block_predicate',
	'minecraft:item_stack',
	'minecraft:item_predicate',
	'minecraft:color',
	'minecraft:component',
	'minecraft:message',
	'minecraft:nbt',
	'minecraft:nbt_tag',
	'minecraft:nbt_path',
	'minecraft:objective',
	'minecraft:objective_criteria',
	'minecraft:operation',
	'minecraft:particle',
	'minecraft:angle',
	'minecraft:rotation',
	'minecraft:scoreboard_slot',
	'minecraft:score_holder',
	'minecraft:swizzle',
	'minecraft:team',
	'minecraft:item_slot',
	'minecraft:resource_location',
	'minecraft:function',
	'minecraft:entity_anchor',
	'minecraft:int_range',
	'minecraft:float_range',
	'minecraft:dimension',
	'minecraft:gamemode',
	'minecraft:time',
	'minecraft:resource_or_tag',
	'minecraft:resource_or_tag_key',
	'minecraft:resource',
	'minecraft:resource_key',
	'minecraft:template_mirror',
	'minecraft:template_rotation',
	'minecraft:heightmap',
	'minecraft:uuid',
]))

ID_MAPS.append((Protocol.V1_19_3, [
	'brigadier:bool',
	'brigadier:float',
	'brigadier:double',
	'brigadier:integer',
	'brigadier:long',
	'brigadier:string',
	'minecraft:entity',
	'minecraft:game_profile',
	'minecraft:block_pos',
	'minecraft:column_pos',
	'minecraft:vec3',
	'minecraft:vec2',
	'minecraft:block_state',
	'minecraft:block_predicate',
	'minecraft:item_stack',
	'minecraft:item_predicate',
	'minecraft:color',
	'minecraft:component',
	'minecraft:message',
	'minecraft:nbt',
	'minecraft:nbt_tag',
	'minecraft:nbt_path',
	'minecraft:objective',
	'minecraft:objective_criteria',
	'minecraft:operation',
	'minecraft:particle',
	'minecraft:angle',
	'minecraft:rotation',
	'minecraft:scoreboard_slot',
	'minecraft:score_holder',
	'minecraft:swizzle',
	'minecraft:team',
	'minecraft:item_slot',
	'minecraft:resource_location',
	'minecraft:function',
	'minecraft:entity_anchor',
	'minecraft:int_range',
	'minecraft:float_range',
	'minecraft:dimension',
	'minecraft:gamemode',
	'minecraft:time',
	'minecraft:resource_or_tag',
	'minecraft:resource_or_tag_key',
	'minecraft:resource',
	'minecraft:resource_key',
	'minecraft:template_mirror',
	'minecraft:template_rotation',
	'minecraft:uuid',
]))

ID_MAPS.append((Protocol.V1_19_2, [
	'brigadier:bool',
	'brigadier:float',
	'brigadier:double',
	'brigadier:integer',
	'brigadier:long',
	'brigadier:string',
	'minecraft:entity',
	'minecraft:game_profile',
	'minecraft:block_pos',
	'minecraft:column_pos',
	'minecraft:vec3',
	'minecraft:vec2',
	'minecraft:block_state',
	'minecraft:block_predicate',
	'minecraft:item_stack',
	'minecraft:item_predicate',
	'minecraft:color',
	'minecraft:component',
	'minecraft:message',
	'minecraft:nbt',
	'minecraft:nbt_tag',
	'minecraft:nbt_path',
	'minecraft:objective',
	'minecraft:objective_criteria',
	'minecraft:operation',
	'minecraft:particle',
	'minecraft:angle',
	'minecraft:rotation',
	'minecraft:scoreboard_slot',
	'minecraft:score_holder',
	'minecraft:swizzle',
	'minecraft:team',
	'minecraft:item_slot',
	'minecraft:resource_location',
	'minecraft:mob_effect',
	'minecraft:function',
	'minecraft:entity_anchor',
	'minecraft:int_range',
	'minecraft:float_range',
	'minecraft:item_enchantment',
	'minecraft:entity_summon',
	'minecraft:dimension',
	'minecraft:time',
	'minecraft:resource_or_tag',
	'minecraft:resource',
	'minecraft:template_mirror',
	'minecraft:template_rotation',
	'minecraft:uuid',
]))

def get_id_map(protocol: int) -> list[str]:
	for p, m in ID_MAPS:
		if protocol >= p:
			return m
	raise ValueError(f'Unsupported protocol {protocol}')

@final
class Node:
	def __init__(self,
		protocol: int,
		flags: int, # Byte
		children: list[int], # Array of VarInt
		redirect_node: int | None, # Optional VarInt
		name: str | None, # Optional String (32767)
		parser_id: int | None, # Optional Varint
		properties: Any | None, # Optional Varies
		suggestions_type: str | None, # Optional Identifier
	):
		"""
		Flags:
			| Bit mask | Field Name           | Notes
			| 0x03     | Node type            | 0: root, 1: literal, 2: argument. 3 is not used.
			| 0x04     | Is executable        | Set if the node stack to this point constitutes a valid command.
			| 0x08     | Has redirect         | Set if the node redirects to another node.
			| 0x10     | Has suggestions type | Only present for argument nodes.
		"""
		self.protocol = protocol
		self.id_map = get_id_map(self.protocol)
		self.flags = flags
		self.children = children # Array of indices of child nodes.
		self.redirect_node = redirect_node # Only if flags & 0x08. Index of redirect node.
		self.name = name # Only for argument and literal nodes.
		self.parser_id = parser_id # Only for argument nodes.
		self.properties = properties # Only for argument nodes. Varies by parser.
		self.suggestions_type = suggestions_type # Only if flags & 0x10.

	def __str__(self) -> str:
		return f"<Node flags={bin(self.flags)} children={self.children} {f'name=' + self.name if self.name else ''} parser={self.parser_sid} {f'suggestions_type=' + self.suggestions_type if self.suggestions_type else ''}>"

	__repr__ = __str__

	@property
	def parser_sid(self) -> str | None:
		if self.parser_id is None:
			return None
		return self.id_map[self.parser_id]

	def write_to(self, b: PacketBuffer) -> None:
		b.write_varint(self.flags)
		b.write_varint(len(self.children))
		for child in self.children:
			b.write_varint(child)
		if self.flags & 0x08:
			assert self.redirect_node is not None
			b.write_varint(self.redirect_node)
		if self.flags & 0x03 in (1, 2):
			assert self.name is not None
			b.write_string(self.name)
		if self.flags & 0x03 == 2:
			assert self.parser_id is not None
			b.write_varint(self.parser_id)
			self.__class__.encode_properties(self.protocol, self.parser_id, self.properties, b)
		if self.flags & 0x10:
			assert self.suggestions_type is not None
			b.write_string(self.suggestions_type)

	@classmethod
	def parse_from(cls, protocol: int, r: PacketReader) -> Self:
		flags = r.read_ubyte()
		children = []
		for _ in range(r.read_varint()):
			child = r.read_varint()
			children.append(child)
		redirect_node = r.read_varint() if flags & 0x08 else None
		assert flags & 0x03 != 3
		name = r.read_string() if flags & 0x03 in (1, 2) else None
		if flags & 0x03 == 2:
			parser_id = r.read_varint()
			properties = cls.parse_properties(protocol, parser_id, r)
		else:
			parser_id = None
			properties = None
		suggestions_type = r.read_string() if flags & 0x10 else None
		return cls(protocol, flags, children, redirect_node, name, parser_id, properties, suggestions_type)

	@classmethod
	def encode_properties(cls, protocol: int, parser_id: int, properties: Any, b: PacketBuffer) -> None:
		id_map = get_id_map(protocol)
		sid = id_map[parser_id]
		if sid in cls.properties_encoder:
			encoder, _ = cls.properties_encoder[sid]
			encoder(properties, b)

	@classmethod
	def parse_properties(cls, protocol: int, parser_id: int, r: PacketReader) -> Any:
		id_map = get_id_map(protocol)
		sid = id_map[parser_id]
		if sid in cls.properties_encoder:
			_, parser = cls.properties_encoder[sid]
			return parser(r)
		return None

	properties_encoder: dict[str, tuple[Callable[[Any, PacketBuffer], None], Callable[[PacketReader], Any]]] = {
		'brigadier:double': (DoubleRange.write_to, DoubleRange.parse_from),
		'brigadier:float': (FloatRange.write_to, FloatRange.parse_from),
		'brigadier:integer': (IntRange.write_to, IntRange.parse_from),
		'brigadier:long': (LongRange.write_to, LongRange.parse_from),
		'brigadier:string': (NodeStringProp.write_to, NodeStringProp.parse_from),
		'minecraft:entity': (NodeEntityProp.write_to, NodeEntityProp.parse_from),
		'minecraft:score_holder': (NodeScoreHolderProp.write_to, NodeScoreHolderProp.parse_from),
		'minecraft:time': (TimeRange.write_to, TimeRange.parse_from),
		'minecraft:resource_or_tag': (ResourceOrTagProp.write_to, ResourceOrTagProp.parse_from),
		'minecraft:resource_or_tag_key': (ResourceOrTagKeyProp.write_to, ResourceOrTagKeyProp.parse_from),
		'minecraft:resource': (ResourceProp.write_to, ResourceProp.parse_from),
		'minecraft:resource_key': (ResourceKeyProp.write_to, ResourceKeyProp.parse_from),
	}
