# Generate from <https://wiki.vg/index.php?title=Protocol&oldid=>

import abc
import uuid
from abc import abstractmethod
from typing import final, Type, Self, Any, Callable

from loginproxy import PacketBuffer, PacketReader, BitSet, ConnStatus

from ..packet import Packet, PacketRepo, PacketStatusMap, PacketIdMap
from ..nbt import NBT, Compound

SIGNATURE_LENGTH = 256

__all__ = [
	'HandshakingHandshakeC2S',
	'HandshakingLegacyServerListPingC2S',
	'StatusResponseS2C',
	'StatusPingResponseS2C',
	'StatusRequestC2S',
	'StatusPingRequestC2S',
	'LoginDisconnect(login)S2C',
	'LoginEncryptionRequestS2C',
	'LoginSuccessS2C',
	'LoginSetCompressionS2C',
	'LoginPluginRequestS2C',
	'LoginStartC2S',
	'LoginEncryptionResponseC2S',
	'LoginPluginResponseC2S',
	'PlaySpawnEntityS2C',
	'PlaySpawnExperienceOrbS2C',
	'PlaySpawnPlayerS2C',
	'PlayEntityAnimationS2C',
	'PlayAwardStatisticsS2C',
	'PlayAcknowledgeBlockChangeS2C',
	'PlaySetBlockDestroyStageS2C',
	'PlayBlockEntityDataS2C',
	'PlayBlockActionS2C',
	'PlayBlockUpdateS2C',
	'PlayBossBarS2C',
	'PlayChangeDifficultyS2C',
	'PlayClearTitlesS2C',
	'PlayCommandSuggestionsResponseS2C',
	'PlayCommandsS2C',
	'PlayCloseContainerS2C',
	'PlaySetContainerContentS2C',
	'PlaySetContainerPropertyS2C',
	'PlaySetContainerSlotS2C',
	'PlaySetCooldownS2C',
	'PlayChatSuggestionsS2C',
	'PlayPluginMessageS2C',
	'PlayDeleteMessageS2C',
	'PlayDisconnect(play)S2C',
	'PlayDisguisedChatMessageS2C',
	'PlayEntityEventS2C',
	'PlayExplosionS2C',
	'PlayUnloadChunkS2C',
	'PlayGameEventS2C',
	'PlayOpenHorseScreenS2C',
	'PlayInitializeWorldBorderS2C',
	'PlayKeepAliveS2C',
	'PlayChunkDataandUpdateLightS2C',
	'PlayWorldEventS2C',
	'PlayParticleS2C',
	'PlayUpdateLightS2C',
	'PlayLogin(play)S2C',
	'PlayMapDataS2C',
	'PlayMerchantOffersS2C',
	'PlayUpdateEntityPositionS2C',
	'PlayUpdateEntityPositionandRotationS2C',
	'PlayUpdateEntityRotationS2C',
	'PlayMoveVehicleS2C',
	'PlayOpenBookS2C',
	'PlayOpenScreenS2C',
	'PlayOpenSignEditorS2C',
	'PlayPing(play)S2C',
	'PlayPlaceGhostRecipeS2C',
	'PlayerAbilitiesS2C',
	'PlayEndCombatS2C',
	'PlayEnterCombatS2C',
	'PlayCombatDeathS2C',
	'PlayerInfoRemoveS2C',
	'PlayerInfoUpdateS2C',
	'PlayLookAtS2C',
	'PlaySynchronizePlayerPositionS2C',
	'PlayUpdateRecipeBookS2C',
	'PlayRemoveEntitiesS2C',
	'PlayRemoveEntityEffectS2C',
	'PlayResourcePackS2C',
	'PlayRespawnS2C',
	'PlaySetHeadRotationS2C',
	'PlayUpdateSectionBlocksS2C',
	'PlaySelectAdvancementsTabS2C',
	'PlayServerDataS2C',
	'PlaySetActionBarTextS2C',
	'PlaySetBorderCenterS2C',
	'PlaySetBorderLerpSizeS2C',
	'PlaySetBorderSizeS2C',
	'PlaySetBorderWarningDelayS2C',
	'PlaySetBorderWarningDistanceS2C',
	'PlaySetCameraS2C',
	'PlaySetHeldItemS2C',
	'PlaySetCenterChunkS2C',
	'PlaySetRenderDistanceS2C',
	'PlaySetDefaultSpawnPositionS2C',
	'PlayDisplayObjectiveS2C',
	'PlaySetEntityMetadataS2C',
	'PlayLinkEntitiesS2C',
	'PlaySetEntityVelocityS2C',
	'PlaySetEquipmentS2C',
	'PlaySetExperienceS2C',
	'PlaySetHealthS2C',
	'PlayUpdateObjectivesS2C',
	'PlaySetPassengersS2C',
	'PlayUpdateTeamsS2C',
	'PlayUpdateScoreS2C',
	'PlaySetSimulationDistanceS2C',
	'PlaySetSubtitleTextS2C',
	'PlayUpdateTimeS2C',
	'PlaySetTitleTextS2C',
	'PlaySetTitleAnimationTimesS2C',
	'PlayEntitySoundEffectS2C',
	'PlaySoundEffectS2C',
	'PlayStopSoundS2C',
	'PlaySystemChatMessageS2C',
	'PlaySetTabListHeaderAndFooterS2C',
	'PlayTagQueryResponseS2C',
	'PlayPickupItemS2C',
	'PlayTeleportEntityS2C',
	'PlayUpdateAdvancementsS2C',
	'PlayUpdateAttributesS2C',
	'PlayFeatureFlagsS2C',
	'PlayEntityEffectS2C',
	'PlayUpdateRecipesS2C',
	'PlayUpdateTagsS2C',
	'PlayConfirmTeleportationC2S',
	'PlayQueryBlockEntityTagC2S',
	'PlayChangeDifficultyC2S',
	'PlayMessageAcknowledgmentC2S',
	'PlayChatCommandC2S',
	'PlayChatMessageC2S',
	'PlayClientCommandC2S',
	'PlayClientInformationC2S',
	'PlayCommandSuggestionsRequestC2S',
	'PlayClickContainerButtonC2S',
	'PlayClickContainerC2S',
	'PlayCloseContainerC2S',
	'PlayPluginMessageC2S',
	'PlayEditBookC2S',
	'PlayQueryEntityTagC2S',
	'PlayInteractC2S',
	'PlayJigsawGenerateC2S',
	'PlayKeepAliveC2S',
	'PlayLockDifficultyC2S',
	'PlaySetPlayerPositionC2S',
	'PlaySetPlayerPositionandRotationC2S',
	'PlaySetPlayerRotationC2S',
	'PlaySetPlayerOnGroundC2S',
	'PlayMoveVehicleC2S',
	'PlayPaddleBoatC2S',
	'PlayPickItemC2S',
	'PlayPlaceRecipeC2S',
	'PlayerAbilitiesC2S',
	'PlayerActionC2S',
	'PlayerCommandC2S',
	'PlayerInputC2S',
	'PlayPong(play)C2S',
	'PlayerSessionC2S',
	'PlayChangeRecipeBookSettingsC2S',
	'PlaySetSeenRecipeC2S',
	'PlayRenameItemC2S',
	'PlayResourcePackC2S',
	'PlaySeenAdvancementsC2S',
	'PlaySelectTradeC2S',
	'PlaySetBeaconEffectC2S',
	'PlaySetHeldItemC2S',
	'PlayProgramCommandBlockC2S',
	'PlayProgramCommandBlockMinecartC2S',
	'PlaySetCreativeModeSlotC2S',
	'PlayProgramJigsawBlockC2S',
	'PlayProgramStructureBlockC2S',
	'PlayUpdateSignC2S',
	'PlaySwingArmC2S',
	'PlayTeleportToEntityC2S',
	'PlayUseItemOnC2S',
	'PlayUseItemC2S',
]

######## BEGIN STRUCTS ########

@final
class Slot:
	def __init__(self,
		present: bool, # Boolean
		item_id: int | None, # Optional VarInt
		item_count: int | None, # Optional Byte
		nbt: NBT | None, # Optional NBT
	):
		self.present = present
		self.item_id = item_id
		self.item_count = item_count
		self.nbt = nbt

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_bool(self.present)
		if self.present:
			assert self.item_id is not None
			assert self.item_count is not None
			assert self.nbt is not None
			b.write_varint(self.item_id)
			b.write_byte(self.item_count)
			self.nbt.to_bytes(b)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		present = r.read_bool()
		if present:
			item_id = r.read_varint()
			item_count = r.read_byte()
			nbt = NBT.parse_from(r)
		else:
			item_id = None
			item_count = None
			nbt = None
		return cls(present, item_id, item_count, nbt)

@final
class PlayerProperty(Packet, id=0x02):
	def __init__(self,
		name: str, # String (32767)
		value: str, # String (32767)
		signed: bool, # Boolean
		signature: str | None, # Optional String (32767)
	):
		self.name = name
		self.value = value
		self.signed = signed
		self.signature = signature # Only if Is Signed is true.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_string(self.name)
		b.write_string(self.value)
		b.write_bool(self.signed)
		if self.signed:
			assert self.signature is not None
			b.write_string(self.signature)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		name = r.read_string()
		value = r.read_string()
		signed = r.read_bool()
		signature = r.read_string() if signed else None
		return cls(name, value, signed, signature)


# # # # BEGIN PARTICLE # # # #

class ParticleData(abc.ABC):
	__type_map: dict[int, Type['ParticleData']] = {}
	__name2id_map: dict[str, int] = {}

	NAME: str
	ID: int

	def __init_subclass__(cls, name: str | None = None, id: int | None = None):
		if name is None or id is None:
			assert name is None and id is None
			return
		cls.NAME = name
		cls.ID = id
		assert id not in ParticleData.__type_map
		assert name not in ParticleData.__name2id_map
		ParticleData.__type_map[id] = cls
		ParticleData.__name2id_map[name] = id

	@abstractmethod
	def to_bytes(self, b: PacketBuffer) -> None:
		raise NotImplementedError()

	@abstractmethod
	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		raise NotImplementedError()

	@staticmethod
	def parse_by_id(id: int, r: PacketReader) -> 'ParticleData':
		typ = ParticleData.__type_map[id]
		return typ.parse_from(r)

	@staticmethod
	def parse_by_name(name: str, r: PacketReader) -> 'ParticleData':
		id = ParticleData.__name2id_map[name]
		return ParticleData.parse_by_id(id, r)

class EmptyParticleData(ParticleData):
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
		return cls()

# # # # END PARTICLE # # # #

@final
class EntityMetadata:
	def __init__(self,
		index: int, # Unsigned Byte
		type: int | None, # Optional VarInt Enum
		value: Any | None, # Optional value of Type
	):
		"""
		Value of Type field	Type of Value field	Notes
		0   Byte
		1   VarInt
		2   VarLong
		3   Float
		4   String
		5   Chat
		6   OptChat (Boolean + Optional Chat)	Chat is present if the Boolean is set to true
		7   Slot
		8   Boolean
		9   Rotation	3 floats: rotation on x, rotation on y, rotation on z
		10  Position
		11  OptPosition (Boolean + Optional Position)	Position is present if the Boolean is set to true
		12  Direction (VarInt)	(Down = 0, Up = 1, North = 2, South = 3, West = 4, East = 5)
		13  OptUUID (Boolean + Optional UUID)	UUID is present if the Boolean is set to true
		14  BlockID (VarInt)
		15  OptBlockID (VarInt)	0 for absent (implies air); otherwise, a block state ID as per the global palette
		16  NBT
		17  Particle
		18  Villager Data	3 VarInts: villager type, villager profession, level
		19  OptVarInt	0 for absent; 1 + actual value otherwise. Used for entity IDs.
		20  Pose	A VarInt enum: 0: STANDING, 1: FALL_FLYING, 2: SLEEPING, 3: SWIMMING, 4: SPIN_ATTACK, 5: SNEAKING, 6: LONG_JUMPING, 7: DYING, 8: CROAKING, 9: USING_TONGUE, 10: SITTING, 11: ROARING, 12: SNIFFING, 13: EMERGING, 14: DIGGING
		21  Cat Variant	A VarInt that points towards the CAT_VARIANT registry.
		22  Frog Variant	A VarInt that points towards the FROG_VARIANT registry.
		23  OptGlobalPos (Boolean + Optional GlobalPos)	GlobalPos consists of a dimension identifier and Position.
		24  Painting Variant	A VarInt that points towards the PAINTING_VARIANT registry.
		25  Sniffer State	A VarInt enum: IDLING = 0, FEELING_HAPPY = 1, SCENTING = 2, SNIFFING = 3, SEARCHING = 4, DIGGING = 5, RISING = 6
		26  Vector3	3 floats: x, y, z
		27  Quaternion	4 floats: x, y, z, w
		"""
		self.index = index # Unique index key determining the meaning of the following value, see the table below. If this is 0xff then the it is the end of the Entity Metadata array and no more is read.
		self.type = type # Only if Index is not 0xff; the type of the index, see the table below
		self.value = value # Only if Index is not 0xff: the value of the metadata field

	def to_bytes(self, b: PacketBuffer):
		b.write_ubyte(self.index)
		if self.index != 0xff:
			assert self.type is not None
			b.write_varint(self.type)
			self.__class__.write_type(self.type, self.value, b)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		index = r.read_ubyte()
		if index != 0xff:
			type = r.read_varint()
			value = cls.read_type(type, r)
		else:
			type = None
			value = None
		return cls(index, type, value)

	@staticmethod
	def write_type(type: int, value: Any, b: PacketBuffer):
		if type == 0:
			assert isinstance(value, int)
			b.write_byte(value)
		elif type == 1:
			assert isinstance(value, int)
			b.write_varint(value)
		elif type == 2:
			assert isinstance(value, int)
			b.write_varlong(value)
		elif type == 3:
			assert isinstance(value, float)
			b.write_float(value)
		elif type == 4:
			assert isinstance(value, str)
			b.write_string(value)
		elif type == 5:
			assert isinstance(value, dict)
			b.write_json(value)
		elif type == 6:
			if value is None:
				b.write_bool(False)
			else:
				assert isinstance(value, dict)
				b.write_bool(True)
				b.write_json(value)
		elif type == 7:
			assert isinstance(value, Slot)
			value.to_bytes(b)
		elif type == 8:
			assert isinstance(value, bool)
			b.write_bool(value)
		elif type == 9:
			assert isinstance(value, tuple)
			assert len(value) == 3
			x, y, z = value
			assert isinstance(x, float)
			assert isinstance(y, float)
			assert isinstance(z, float)
			b.write_float(x)
			b.write_float(y)
			b.write_float(z)
		elif type == 10:
			assert isinstance(value, tuple)
			assert len(value) == 3
			x, y, z = value
			assert isinstance(x, int)
			assert isinstance(y, int)
			assert isinstance(z, int)
			b.write_pos_1_14((x, y, z))
		elif type == 11:
			if value is None:
				b.write_bool(False)
			else:
				assert isinstance(value, tuple)
				assert len(value) == 3
				x, y, z = value
				b.write_bool(True)
				assert isinstance(x, int)
				assert isinstance(y, int)
				assert isinstance(z, int)
				b.write_pos_1_14((x, y, z))
		elif type == 12:
			assert isinstance(value, int)
			b.write_varint(value)
		elif type == 13:
			if value is None:
				b.write_bool(False)
			else:
				assert isinstance(value, uuid.UUID)
				b.write_bool(True)
				b.write_uuid(value)
		elif type == 14:
			assert isinstance(value, int)
			b.write_varint(value)
		elif type == 15:
			assert isinstance(value, int)
			b.write_varint(value)
		elif type == 16:
			assert isinstance(value, NBT)
			value.to_bytes(b)
		elif type == 17:
			assert isinstance(value, ParticleData)
			value.to_bytes(b)
		elif type == 18:
			assert isinstance(value, tuple)
			assert len(value) == 3
			villager_type, villager_profession, level = value
			b.write_varint(villager_type)
			b.write_varint(villager_profession)
			b.write_varint(level)
		elif type == 19:
			if value is None:
				b.write_varint(0)
			else:
				assert isinstance(value, int)
				b.write_varint(value + 1)
		elif type == 20:
			assert isinstance(value, int)
			b.write_varint(value)
		elif type == 21:
			assert isinstance(value, int)
			b.write_varint(value)
		elif type == 22:
			assert isinstance(value, int)
			b.write_varint(value)
		elif type == 23:
			if value is None:
				b.write_bool(False)
			else:
				assert isinstance(value, tuple) # tuple[str, tuple[int, int, int]]
				assert len(value) == 2
				dimension_name, position = value
				assert isinstance(dimension_name, str)
				b.write_bool(True)
				b.write_string(dimension_name)
				b.write_pos_1_14(position)
		elif type == 24:
			assert isinstance(value, int)
			b.write_varint(value)
		elif type == 25:
			assert isinstance(value, int)
			b.write_varint(value)
		elif type == 26:
			assert isinstance(value, tuple)
			assert len(value) == 3
			x, y, z = value
			assert isinstance(x, float)
			assert isinstance(y, float)
			assert isinstance(z, float)
			b.write_float(x)
			b.write_float(y)
			b.write_float(z)
		elif type == 27:
			assert isinstance(value, tuple)
			assert len(value) == 4
			x, y, z, w = value
			assert isinstance(x, float)
			assert isinstance(y, float)
			assert isinstance(z, float)
			assert isinstance(w, float)
			b.write_float(x)
			b.write_float(y)
			b.write_float(z)
			b.write_float(w)


	@staticmethod
	def read_type(type: int, r: PacketReader) -> Any:
		if type == 0:
			return r.read_byte()
		elif type == 1:
			return r.read_varint()
		elif type == 2:
			return r.read_varlong()
		elif type == 3:
			return r.read_float()
		elif type == 4:
			return r.read_string()
		elif type == 5:
			return r.read_json()
		elif type == 6:
			if not r.read_bool():
				return None
			return r.read_json()
		elif type == 7:
			return Slot.parse_from(r)
		elif type == 8:
			return r.read_bool()
		elif type == 9:
			x = r.read_float()
			y = r.read_float()
			z = r.read_float()
			return x, y, z
		elif type == 10:
			return r.read_pos_1_14()
		elif type == 11:
			if not r.read_bool():
				return None
			return r.read_pos_1_14()
		elif type == 12:
			return r.read_varint()
		elif type == 13:
			if not r.read_bool():
				return None
			return r.read_uuid()
		elif type == 14:
			return r.read_varint()
		elif type == 15:
			return r.read_varint()
		elif type == 16:
			return NBT.parse_from(r)
		elif type == 17:
			return ParticleData.parse_from(r)
		elif type == 18:
			villager_type = r.read_varint()
			villager_profession = r.read_varint()
			level = r.read_varint()
			return (villager_type, villager_profession, level)
		elif type == 19:
			value = r.read_varint()
			if value == 0:
				return None
			return value - 1
		elif type == 20:
			return r.read_varint()
		elif type == 21:
			return r.read_varint()
		elif type == 22:
			return r.read_varint()
		elif type == 23:
			if not r.read_bool():
				return None
			dimension_name = r.read_string()
			position = r.read_pos_1_14()
			return (dimension_name, position)
		elif type == 24:
			return r.read_varint()
		elif type == 25:
			return r.read_varint()
		elif type == 26:
			x = r.read_float()
			y = r.read_float()
			z = r.read_float()
			return (x, y, z)
		elif type == 27:
			x = r.read_float()
			y = r.read_float()
			z = r.read_float()
			w = r.read_float()
			return (x, y, z, w)

@final
class Node:
	def __init__(self,
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
		self.flags = flags
		self.children = children # Array of indices of child nodes.
		self.redirect_node = redirect_node # Only if flags & 0x08. Index of redirect node.
		self.name = name # Only for argument and literal nodes.
		self.parser_id = parser_id # Only for argument nodes.
		self.properties = properties # Only for argument nodes. Varies by parser.
		self.suggestions_type = suggestions_type # Only if flags & 0x10.

	def to_bytes(self, b: PacketBuffer) -> None:
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
			self.__class__.encode_properties(self.parser_id, self.properties, b)
		if self.flags & 0x10:
			assert self.suggestions_type is not None
			b.write_string(self.suggestions_type)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		flags = r.read_varint()
		children = []
		for _ in range(r.read_varint()):
			child = r.read_varint()
			children.append(child)
		redirect_node = r.read_varint() if flags & 0x08 else None
		name = r.read_string() if flags & 0x03 in (1, 2) else None
		if flags & 0x03 == 2 :
			parser_id = r.read_varint()
			properties = cls.parse_properties(parser_id, r)
		else:
			parser_id = None
			properties = None
		suggestions_type = r.read_string() if flags & 0x10 else None
		return cls(flags, children, redirect_node, name, parser_id, properties, suggestions_type)

	@classmethod
	def encode_properties(cls, parser_id: int, properties: Any, b: PacketBuffer) -> None:
		raise NotImplementedError()

	@classmethod
	def parse_properties(cls, parser_id: int, r: PacketReader) -> Any:
		raise NotImplementedError()

@final
class CriterionProgress:
	def __init__(self,
		achieved: bool, # Boolean
		date_of_achieving: int | None, # Optional Long
	):
		self.achieved = achieved # If true, next field is present.
		self.date_of_achieving = date_of_achieving # As returned by Date.getTime.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_bool(self.achieved)
		if self.achieved:
			assert self.date_of_achieving is not None
			b.write_long(self.date_of_achieving)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		achieved = r.read_bool()
		date_of_achieving = r.read_long() if achieved else None
		return cls(achieved, date_of_achieving)

@final
class AdvancementProgress:
	def __init__(self,
		criterias: list[
			tuple[
				str, # Criterion identifier; Identifier; The identifier of the criterion.
				CriterionProgress, # Criterion progress; Criterion progress;
			]
		]
	):
		self.criterias = criterias

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_varint(len(self.criterias))
		for identifier, progress in self.criterias:
			b.write_string(identifier)
			progress.to_bytes(b)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		criterias = []
		for _ in range(r.read_varint()):
			identifier = r.read_string()
			progress = CriterionProgress.parse_from(r)
			criterias.append((identifier, progress))
		return cls(criterias)

@final
class AdvancementDisplay:
	def __init__(self,
		title: dict, # Chat
		description: dict, # Chat
		icon: Slot, # Slot
		frame_type: int, # VarInt Enum
		flags: int, # Int
		background_texture: str | None, # Optional Identifier
		x_coord: float, # Float
		y_coord: float, # Float
	):
		self.title = title #
		self.description = description #
		self.icon = icon #
		self.frame_type = frame_type # 0 = task, 1 = challenge, 2 = goal.
		self.flags = flags # 0x01: has background texture; 0x02: show_toast; 0x04: hidden.
		self.background_texture = background_texture # Background texture location. Only if flags indicates it.
		self.x_coord = x_coord #
		self.y_coord = y_coord #

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_json(self.title)
		b.write_json(self.description)
		self.icon.to_bytes(b)
		b.write_varint(self.frame_type)
		b.write_int(self.flags)
		if self.flags & 0x01:
			assert self.background_texture is not None
			b.write_string(self.background_texture)
		b.write_float(self.x_coord)
		b.write_float(self.y_coord)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		title = r.read_json()
		description = r.read_json()
		icon = Slot.parse_from(r)
		frame_type = r.read_varint()
		flags = r.read_int()
		background_texture = r.read_string() if flags & 0x01 else None
		x_coord = r.read_float()
		y_coord = r.read_float()
		return cls(title, description, icon, frame_type, flags, background_texture, x_coord, y_coord)

@final
class Advancement:
	def __init__(self,
		has_parent: bool, # Boolean
		parent_id: str | None, # Optional Identifier
		has_display: bool, # Boolean
		display_data: AdvancementDisplay | None, # Optional advancement display
		criterias: dict[
			str, # Key; Identifier; The identifier of the criterion.
			None, # Value; Void; There is no content written here. Perhaps this will be expanded in the future?
		],
		requirements: list[
			list[str] # Array of required criteria.
		],
	):
		self.has_parent = has_parent # Indicates whether the next field exists.
		self.parent_id = parent_id # The identifier of the parent advancement.
		self.has_display = has_display # Indicates whether the next field exists.
		self.display_data = display_data #
		self.criterias = criterias # See above
		self.requirements = requirements # See above

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_bool(self.has_parent)
		if self.has_parent:
			assert self.parent_id is not None
			b.write_string(self.parent_id)
		b.write_bool(self.has_display)
		if self.has_display:
			assert self.display_data is not None
			self.display_data.to_bytes(b)
		b.write_varint(len(self.criterias))
		for key, value in self.criterias.items():
			b.write_string(key)
		b.write_varint(len(self.requirements))
		for requirement in self.requirements:
			b.write_varint(len(requirement))
			for req in requirement:
				b.write_string(req)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		has_parent = r.read_bool()
		parent_id = r.read_string() if has_parent else None
		has_display = r.read_bool()
		display_data = AdvancementDisplay.parse_from(r) if has_display else None
		criterias: dict[str, None] = {}
		for _ in range(r.read_varint()):
			key = r.read_string()
			criterias[key] = None
		requirements = []
		for _ in range(r.read_varint()):
			requirement = []
			for _ in range(r.read_varint()):
				req = r.read_string()
				requirement.append(req)
			requirements.append(requirement)
		return cls(has_parent, parent_id, has_display, display_data, criterias, requirements)

@final
class Modifier:
	def __init__(self,
		uuid: uuid.UUID, # UUID
		amount: float, # Double
		operation: int, # Byte
	):
		self.uuid = uuid
		self.amount = amount # May be positive or negative.
		"""
		The operation controls how the base value of the modifier is changed.
		- 0: Add/subtract amount
		- 1: Add/subtract amount percent of the current value
		- 2: Multiply by amount percent
		All of the 0's are applied first, and then the 1's, and then the 2's.
		"""
		self.operation = operation

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_uuid(self.uuid)
		b.write_double(self.amount)
		b.write_byte(self.operation)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		uuid = r.read_uuid()
		amount = r.read_double()
		operation = r.read_byte()
		return cls(uuid, amount, operation)

@final
class Ingredient:
	def __init__(self,
		count: int, # VarInt
		items: list[Slot], # Array of Slot
	):
		self.count = count # Number of elements in the following array.
		self.items = items # Any item in this array may be used for the recipe. The count of each item should be 1.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_varint(self.count)
		b.write_varint(len(self.items))
		for item in self.items:
			item.to_bytes(b)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		count = r.read_varint()
		items: list[Slot] = []
		for _ in range(r.read_varint()):
			item = Slot.parse_from(r)
			items.append(item)
		return cls(count, items)

@final
class Recipe:
	def __init__(self,
		type: str, # Identifier
		recipe_id: str, # Identifier
		data: dict, # Varies
	):
		self.type = type # The recipe type, see below.
		self.recipe_id = recipe_id
		self.data = data

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_string(self.type)
		b.write_string(self.recipe_id)
		if type in self.__class__.ENCODERS:
			self.__class__.ENCODERS[self.type][0](self.data, b)
		elif '_' in self.data:
			b.write(self.data['_'])

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		type = r.read_string()
		recipe_id = r.read_string()
		data = cls.ENCODERS[type][1](r) if type in cls.ENCODERS else {'_': r.read()}

		return cls(type, recipe_id, data)

	@staticmethod
	def crafting_shapeless_encoder(data: dict, b: PacketBuffer) -> None:
		b.write_string(data['group']) # String; Used to group similar recipes together in the recipe book. Tag is present in recipe JSON.
		b.write_varint(data['category']) # VarInt Enum; Building = 0, Redstone = 1, Equipment = 2, Misc = 3
		ingredients: list[Ingredient] = data['ingredients'] # Array of Ingredient.
		b.write_varint(len(ingredients))
		for ingredient in ingredients:
			ingredient.to_bytes(b)
		result = data['result'] # Slot
		assert isinstance(result, Slot)
		result.to_bytes(b)

	@staticmethod
	def crafting_shapeless_decoder(r: PacketReader) -> dict:
		data: dict = {}
		data['group'] = r.read_string()
		data['category'] = r.read_varint()
		ingredients: list[Ingredient] = []
		for _ in range(r.read_varint()):
			ingredient = Ingredient.parse_from(r)
			ingredients.append(ingredient)
		data['ingredients'] = ingredients
		data['result'] = Slot.parse_from(r)
		return data

	@staticmethod
	def crafting_shaped_encoder(data: dict, b: PacketBuffer) -> None:
		b.write_varint(data['width']) # VarInt
		b.write_varint(data['height']) # VarInt
		b.write_string(data['group']) # String; Used to group similar recipes together in the recipe book. Tag is present in recipe JSON.
		b.write_varint(data['category']) # VarInt Enum; Building = 0, Redstone = 1, Equipment = 2, Misc = 3
		ingredients: list[Ingredient] = data['ingredients'] # Array of Ingredient.
		for ingredient in ingredients:
			ingredient.to_bytes(b)
		result = data['result'] # Slot
		assert isinstance(result, Slot)
		result.to_bytes(b)

	@staticmethod
	def crafting_shaped_decoder(r: PacketReader) -> dict:
		data: dict = {}
		width = r.read_varint()
		data['width'] = width
		height = r.read_varint()
		data['height'] = height
		data['group'] = r.read_string()
		data['category'] = r.read_varint()
		ingredients: list[Ingredient] = []
		for _ in range(width * height):
			ingredient = Ingredient.parse_from(r)
			ingredients.append(ingredient)
		data['ingredients'] = ingredients
		data['result'] = Slot.parse_from(r)
		return data

	@staticmethod
	def crafting_special_encoder(data: dict, b: PacketBuffer) -> None:
		b.write_varint(data['category']) # VarInt Enum; Building = 0, Redstone = 1, Equipment = 2, Misc = 3

	@staticmethod
	def crafting_special_decoder(r: PacketReader) -> dict:
		data: dict = {}
		data['category'] = r.read_varint()
		return data

	@staticmethod
	def crafting_smelting_encoder(data: dict, b: PacketBuffer) -> None:
		b.write_string(data['group']) # String; Used to group similar recipes together in the recipe book.
		b.write_varint(data['category']) # VarInt Enum; Food = 0, Blocks = 1, Misc = 2
		ingredient = data['ingredient'] # Ingredient
		assert isinstance(ingredient, Ingredient)
		ingredient.to_bytes(b)
		result = data['result'] # Slot
		assert isinstance(result, Slot)
		result.to_bytes(b)
		b.write_float(data['experience']) # Float
		b.write_varint(data['cooking_time']) # VarInt

	@staticmethod
	def crafting_smelting_decoder(r: PacketReader) -> dict:
		data: dict = {}
		data['group'] = r.read_string()
		data['category'] = r.read_varint()
		data['ingredient'] = Ingredient.parse_from(r)
		data['result'] = Slot.parse_from(r)
		data['experience'] = r.read_float()
		data['cooking_time'] = r.read_varint()
		return data

	@staticmethod
	def crafting_stonecutting_encoder(data: dict, b: PacketBuffer) -> None:
		b.write_string(data['group']) # String; Used to group similar recipes together in the recipe book. Tag is present in recipe JSON.
		ingredient = data['ingredient'] # Ingredient
		assert isinstance(ingredient, Ingredient)
		ingredient.to_bytes(b)
		result = data['result'] # Slot
		assert isinstance(result, Slot)
		result.to_bytes(b)

	@staticmethod
	def crafting_stonecutting_decoder(r: PacketReader) -> dict:
		data: dict = {}
		data['group'] = r.read_string()
		data['ingredient'] = Ingredient.parse_from(r)
		data['result'] = Slot.parse_from(r)
		return data

	@staticmethod
	def crafting_smithing_encoder(data: dict, b: PacketBuffer) -> None:
		base = data['base'] # Ingredient; First item.
		assert isinstance(base, Ingredient)
		base.to_bytes(b)
		addition = data['addition'] # Ingredient; Second item.
		assert isinstance(addition, Ingredient)
		addition.to_bytes(b)
		result = data['result'] # Slot
		assert isinstance(result, Slot)
		result.to_bytes(b)

	@staticmethod
	def crafting_smithing_decoder(r: PacketReader) -> dict:
		data: dict = {}
		data['base'] = Ingredient.parse_from(r)
		data['addition'] = Ingredient.parse_from(r)
		data['result'] = Slot.parse_from(r)
		return data

	ENCODERS: dict[str, tuple[Callable[[dict, PacketBuffer], None], Callable[[PacketReader], dict]]] = {
		'minecraft:crafting_shapeless': (crafting_shapeless_encoder, crafting_shapeless_decoder),
		'minecraft:crafting_shaped': (crafting_shaped_encoder, crafting_shaped_decoder),
		'minecraft:crafting_special_armordye': (crafting_special_encoder, crafting_special_decoder),
		'minecraft:crafting_special_bookcloning': (crafting_special_encoder, crafting_special_decoder),
		'minecraft:crafting_special_mapcloning': (crafting_special_encoder, crafting_special_decoder),
		'minecraft:crafting_special_mapextending': (crafting_special_encoder, crafting_special_decoder),
		'minecraft:crafting_special_firework_rocket': (crafting_special_encoder, crafting_special_decoder),
		'minecraft:crafting_special_firework_star': (crafting_special_encoder, crafting_special_decoder),
		'minecraft:crafting_special_firework_star_fade': (crafting_special_encoder, crafting_special_decoder),
		'minecraft:crafting_special_repairitem': (crafting_special_encoder, crafting_special_decoder),
		'minecraft:crafting_special_tippedarrow': (crafting_special_encoder, crafting_special_decoder),
		'minecraft:crafting_special_bannerduplicate': (crafting_special_encoder, crafting_special_decoder),
		'minecraft:crafting_special_shielddecoration': (crafting_special_encoder, crafting_special_decoder),
		'minecraft:crafting_special_shulkerboxcoloring': (crafting_special_encoder, crafting_special_decoder),
		'minecraft:crafting_special_suspiciousstew': (crafting_special_encoder, crafting_special_decoder),
		'minecraft:smelting': (crafting_smelting_encoder, crafting_smelting_decoder),
		'minecraft:blasting': (crafting_smelting_encoder, crafting_smelting_decoder),
		'minecraft:smoking': (crafting_smelting_encoder, crafting_smelting_decoder),
		'minecraft:campfire_cooking': (crafting_smelting_encoder, crafting_smelting_decoder),
		'minecraft:stonecutting': (crafting_stonecutting_encoder, crafting_stonecutting_decoder),
		'minecraft:smithing': (crafting_smithing_encoder, crafting_smithing_decoder),
	}

@final
class Tag:
	def __init__(self,
		name: str, # Identifier
		entries: list[int], # Array of VarInt
	):
		self.name = name
		self.entries = entries # Numeric ID of the given type (block, item, etc.).

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_string(self.name)
		b.write_varint(len(self.entries))
		for entry in self.entries:
			b.write_varint(entry)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		name = r.read_string()
		entries = []
		for _ in range(r.read_varint()):
			entry = r.read_varint()
			entries.append(entry)
		return cls(name, entries)

@final
class Action:
	def __init__(self,
		uuid: uuid.UUID, # UUID
		name: str | None, # String (16)
		properties: list[PlayerProperty] | None, # Array Of Property
		has_signature_data: bool | None, # Boolean
		chat_session_id: uuid.UUID | None, # UUID
		public_key_expiry_time: int | None, # Long
		encoded_public_key: bytes | None, # Byte Array
		public_key_signature: bytes | None, # Byte Array
		gamemode: int | None, # VarInt
		listed: bool | None, # Boolean
		ping: int | None, # VarInt
		has_display_name: bool | None, # Boolean
		display_name: dict | None, # Optional Chat
	):
		self.uuid = uuid # The player UUID
		# Action bit 0
		self.name = name
		self.properties = properties
		# Action bit 1
		self.has_signature_data = has_signature_data # 
		self.chat_session_id = chat_session_id # Only send if Has Signature Data is true.
		self.public_key_expiry_time = public_key_expiry_time # Key expiry time, as a UNIX timestamp in milliseconds. Only send if Has Signature Data is true.
		self.encoded_public_key = encoded_public_key # The player's public key, in bytes. Only send if Has Signature Data is true.
		self.public_key_signature = public_key_signature # The public key's digital signature. Only send if Has Signature Data is true.
		# Action bit 2
		self.gamemode = gamemode # 
		# Action bit 3
		self.listed = listed # Whether the player should be listed on the player list.
		# Action bit 4
		self.ping = ping # Measured in milliseconds.
		# Action bit 5
		self.has_display_name = has_display_name # 
		self.display_name = display_name # Only send if Has Display Name is true.

	def to_bytes(self, actions: int, b: PacketBuffer) -> None:
		b.write_uuid(self.uuid)
		if actions & 1:
			assert self.name is not None
			assert self.properties is not None
			b.write_string(self.name)
			b.write_varint(len(self.properties))
			for property in self.properties:
				property.to_bytes(b)
		if actions & (1 << 1):
			assert self.has_signature_data is not None
			assert self.public_key_expiry_time is not None
			assert self.encoded_public_key is not None
			assert self.public_key_signature is not None
			b.write_bool(self.has_signature_data)
			if self.has_signature_data:
				assert self.chat_session_id is not None
				b.write_uuid(self.chat_session_id)
			b.write_long(self.public_key_expiry_time)
			b.write_varint(len(self.encoded_public_key))
			b.write(self.encoded_public_key)
			b.write_varint(len(self.public_key_signature))
			b.write(self.public_key_signature)
		if actions & (1 << 2):
			assert self.gamemode is not None
			b.write_varint(self.gamemode)
		if actions & (1 << 3):
			assert self.listed is not None
			b.write_bool(self.listed)
		if actions & (1 << 4):
			assert self.ping is not None
			b.write_varint(self.ping)
		if actions & (1 << 5):
			assert self.has_display_name is not None
			b.write_bool(self.has_display_name)
			if self.has_display_name:
				assert self.display_name is not None
				b.write_json(self.display_name)

	@classmethod
	def parse_from(cls, actions: int, r: PacketReader) -> Self:
		uuid = r.read_uuid()
		if actions & 1:
			name = r.read_string()
			properties = []
			for _ in range(r.read_varint()):
				property = PlayerProperty.parse_from(r)
				properties.append(property)
		else:
			name = None
			properties = None
		if actions & (1 << 1):
			has_signature_data = r.read_bool()
			chat_session_id = r.read_uuid() if has_signature_data else None
			public_key_expiry_time = r.read_long()
			encoded_public_key = r.read(r.read_varint())
			public_key_signature = r.read(r.read_varint())
		else:
			has_signature_data = None
			chat_session_id = None
			public_key_expiry_time = None
			encoded_public_key = None
			public_key_signature = None
		gamemode = r.read_varint() if actions & (1 << 2) else None
		listed = r.read_bool() if actions & (1 << 3) else None
		ping = r.read_varint() if actions & (1 << 4) else None
		if actions & (1 << 5):
			has_display_name = r.read_bool()
			display_name = r.read_json() if has_display_name else None
		else:
			has_display_name = None
			display_name = None
		return cls(uuid, name, properties, has_signature_data, chat_session_id, public_key_expiry_time, encoded_public_key, public_key_signature, gamemode, listed, ping, has_display_name, display_name)


######## END STRUCTS ########

@final
class HandshakingHandshakeC2S(Packet, id=0x00):
	def __init__(self,
		protocol_version: int, # VarInt
		server_address: str, # String (255)
		server_port: int, # Unsigned Short
		next_state: int, # VarInt Enum
	):
		self.protocol_version = protocol_version # See protocol version numbers (currently 761 in Minecraft 1.19.3).
		self.server_address = server_address # Hostname or IP, e.g. localhost or 127.0.0.1, that was used to connect. The Notchian server does not use this information. Note that SRV records are a simple redirect, e.g. if _minecraft._tcp.example.com points to mc.example.org, users connecting to example.com will provide example.org as server address in addition to connecting to it.
		self.server_port = server_port # Default is 25565. The Notchian server does not use this information.
		self.next_state = next_state # 1 for Status, 2 for Login.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_varint(self.protocol_version)
		b.write_string(self.server_address)
		b.write_ushort(self.server_port)
		b.write_varint(self.next_state)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		protocol_version = r.read_varint()
		server_address = r.read_string()
		server_port = r.read_ushort()
		next_state = r.read_varint()
		return cls(protocol_version, server_address, server_port, next_state)

@final
class StatusResponseS2C(Packet, id=0x00):
	def __init__(self,
		json_response: dict, # String (32767)
	):
		self.json_response = json_response # See Server List Ping#Response; as with all strings this is prefixed by its length as a VarInt.

	def to_bytes(self, b: PacketBuffer):
		b.write_json(self.json_response)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		json_response = r.read_json()
		return cls(json_response)

@final
class StatusPingResponseS2C(Packet, id=0x01):
	def __init__(self,
		payload: int, # Long
	):
		self.payload = payload # Should be the same as sent by the client.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_long(self.payload)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		payload = r.read_long()
		return cls(payload)

@final
class StatusRequestC2S(Packet, id=0x00):
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
		return cls()

@final
class StatusPingRequestC2S(Packet, id=0x01):
	def __init__(self,
		payload: int, # Long
	):
		self.payload = payload # May be any number. Notchian clients use a system-dependent time value which is counted in milliseconds.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_long(self.payload)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		payload = r.read_long()
		return cls(payload)

@final
class LoginDisconnectS2C(Packet, id=0x00):
	def __init__(self,
		reason: dict, # Chat
	):
		self.reason = reason # The reason why the player was disconnected.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_json(self.reason)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		reason = r.read_json()
		return cls(reason)

@final
class LoginEncryptionRequestS2C(Packet, id=0x01):
	def __init__(self,
		server_id: str, # String (20)
		public_key: bytes, # Byte Array
		verify_token: bytes, # Byte Array
	):
		self.server_id = server_id # Appears to be empty.
		self.public_key = public_key # The server's public key, in bytes.
		self.verify_token = verify_token # A sequence of random bytes generated by the server.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_string(self.server_id)
		b.write_varint(len(self.public_key))
		b.write(self.public_key)
		b.write_varint(len(self.verify_token))
		b.write(self.verify_token)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		server_id = r.read_string()
		public_key = r.read(r.read_varint())
		verify_token = r.read(r.read_varint())
		return cls(server_id, public_key, verify_token)

@final
class LoginSuccessS2C(Packet, id=0x02):
	def __init__(self,
		uuid: uuid.UUID, # UUID
		username: str, # String (16)
		properties: list[PlayerProperty],
	):
		self.uuid = uuid
		self.username = username
		self.properties = properties

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_uuid(self.uuid)
		b.write_string(self.username)
		b.write_varint(len(self.properties))
		for property in self.properties:
			property.to_bytes(b)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		uuid = r.read_uuid()
		username = r.read_string()
		properties = []
		for _ in range(r.read_varint()):
			property = PlayerProperty.parse_from(r)
			properties.append(property)
		return cls(uuid, username, properties)

@final
class LoginSetCompressionS2C(Packet, id=0x03):
	def __init__(self,
		threshold: int, # VarInt
	):
		self.threshold = threshold # Maximum size of a packet before it is compressed.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_varint(self.threshold)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		threshold = r.read_varint()
		return cls(threshold)

@final
class LoginPluginRequestS2C(Packet, id=0x04):
	def __init__(self,
		message_id: int, # VarInt
		channel: str, # Identifier
		data: bytes, # Byte Array (1048576)
	):
		self.message_id = message_id # Generated by the server - should be unique to the connection.
		self.channel = channel # Name of the plugin channel used to send the data.
		self.data = data # Any data, depending on the channel. The length of this array must be inferred from the packet length.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_varint(self.message_id)
		b.write_string(self.channel)
		b.write(self.data)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		message_id = r.read_varint()
		channel = r.read_string()
		data = r.read()
		return cls(message_id, channel, data)

@final
class LoginStartC2S(Packet, id=0x00):
	def __init__(self,
		name: str, # String (16)
		has_player_uuid: bool, # Boolean
		player_uuid: uuid.UUID | None, # Optional UUID
	):
		self.name = name # Player's Username.
		self.has_player_uuid = has_player_uuid # Whether or not the next field should be sent.
		self.player_uuid = player_uuid # The UUID of the player logging in. Only sent if Has Player UUID is true.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_string(self.name)
		b.write_bool(self.has_player_uuid)
		if self.has_player_uuid:
			assert self.player_uuid is not None
			b.write_uuid(self.player_uuid)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		name = r.read_string()
		has_player_uuid = r.read_bool()
		player_uuid = r.read_uuid() if has_player_uuid else None
		return cls(name, has_player_uuid, player_uuid)

@final
class LoginEncryptionResponseC2S(Packet, id=0x01):
	def __init__(self,
		shared_secret: bytes, # Byte Array
		verify_token: bytes, # Byte Array
	):
		self.shared_secret = shared_secret # Shared Secret value, encrypted with the server's public key.
		self.verify_token = verify_token # Verify Token value, encrypted with the same public key as the shared secret.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_varint(len(self.shared_secret))
		b.write(self.shared_secret)
		b.write_varint(len(self.verify_token))
		b.write(self.verify_token)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		shared_secret = r.read(r.read_varint())
		verify_token = r.read(r.read_varint())
		return cls(shared_secret, verify_token)

@final
class LoginPluginResponseC2S(Packet, id=0x02):
	def __init__(self,
		message_id: int, # VarInt
		successful: bool, # Boolean
		data: bytes | None, # Optional Byte Array (1048576)
	):
		self.message_id = message_id # Should match ID from server.
		self.successful = successful # true if the client understood the request, false otherwise. When false, no payload follows.
		self.data = data # Any data, depending on the channel. The length of this array must be inferred from the packet length.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_varint(self.message_id)
		b.write_bool(self.successful)
		if self.successful:
			assert self.data is not None
			b.write(self.data)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		message_id = r.read_varint()
		successful = r.read_bool()
		data = r.read() if successful else None
		return cls(message_id, successful, data)

@final
class PlaySpawnEntityS2C(Packet, id=0x00):
	def __init__(self,
		entity_id: int, # VarInt
		entity_uuid: uuid.UUID, # UUID
		type: int, # VarInt
		x: float, # Double
		y: float, # Double
		z: float, # Double
		pitch: int, # Angle
		yaw: int, # Angle
		head_yaw: int, # Angle
		data: int, # VarInt
		velocity_x: int, # Short
		velocity_y: int, # Short
		velocity_z: int, # Short
	):
		self.entity_id = entity_id # A unique integer ID mostly used in the protocol to identify the entity.
		self.entity_uuid = entity_uuid # A unique identifier that is mostly used in persistence and places where the uniqueness matters more.
		self.type = type # The type of the entity (see "type" field of the list of Mob types).
		self.x = x # 
		self.y = y # 
		self.z = z # 
		self.pitch = pitch # To get the real pitch, you must divide this by (256.0F / 360.0F)
		self.yaw = yaw # To get the real yaw, you must divide this by (256.0F / 360.0F)
		self.head_yaw = head_yaw # Only used by living entities, where the head of the entity may differ from the general body rotation.
		self.data = data # Meaning dependent on the value of the Type field, see Object Data for details.
		self.velocity_x = velocity_x # Same units as Set Entity Velocity.
		self.velocity_y = velocity_y # Same units as Set Entity Velocity.
		self.velocity_z = velocity_z # Same units as Set Entity Velocity.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_varint(self.entity_id)
		b.write_uuid(self.entity_uuid)
		b.write_varint(self.type)
		b.write_double(self.x)
		b.write_double(self.y)
		b.write_double(self.z)
		b.write_byte(self.pitch)
		b.write_byte(self.yaw)
		b.write_byte(self.head_yaw)
		b.write_varint(self.data)
		b.write_short(self.velocity_x)
		b.write_short(self.velocity_y)
		b.write_short(self.velocity_z)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		entity_id = r.read_varint()
		entity_uuid = r.read_uuid()
		type = r.read_varint()
		x = r.read_double()
		y = r.read_double()
		z = r.read_double()
		pitch = r.read_byte()
		yaw = r.read_byte()
		head_yaw = r.read_byte()
		data = r.read_varint()
		velocity_x = r.read_short()
		velocity_y = r.read_short()
		velocity_z = r.read_short()
		return cls(entity_id, entity_uuid, type, x, y, z, pitch, yaw, head_yaw, data, velocity_x, velocity_y, velocity_z)

@final
class PlaySpawnExperienceOrbS2C(Packet, id=0x01):
	def __init__(self,
		entity_id: int, # VarInt
		x: float, # Double
		y: float, # Double
		z: float, # Double
		count: int, # Short
	):
		self.entity_id = entity_id # 
		self.x = x # 
		self.y = y # 
		self.z = z # 
		self.count = count # The amount of experience this orb will reward once collected.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_varint(self.entity_id)
		b.write_double(self.x)
		b.write_double(self.y)
		b.write_double(self.z)
		b.write_short(self.count)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		entity_id = r.read_varint()
		x = r.read_double()
		y = r.read_double()
		z = r.read_double()
		count = r.read_short()
		return cls(entity_id, x, y, z, count)

@final
class PlaySpawnPlayerS2C(Packet, id=0x02):
	def __init__(self,
		entity_id: int, # VarInt
		player_uuid: uuid.UUID, # UUID
		x: float, # Double
		y: float, # Double
		z: float, # Double
		yaw: int, # Angle
		pitch: int, # Angle
	):
		self.entity_id = entity_id # A unique integer ID mostly used in the protocol to identify the player.
		self.player_uuid = player_uuid # See below for notes on offline mode and NPCs.
		self.x = x # 
		self.y = y # 
		self.z = z # 
		self.yaw = yaw # 
		self.pitch = pitch # 

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_varint(self.entity_id)
		b.write_uuid(self.player_uuid)
		b.write_double(self.x)
		b.write_double(self.y)
		b.write_double(self.z)
		b.write_byte(self.yaw)
		b.write_byte(self.pitch)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		entity_id = r.read_varint()
		player_uuid = r.read_uuid()
		x = r.read_double()
		y = r.read_double()
		z = r.read_double()
		yaw = r.read_byte()
		pitch = r.read_byte()
		return cls(entity_id, player_uuid, x, y, z, yaw, pitch)

@final
class PlayEntityAnimationS2C(Packet, id=0x03):
	def __init__(self,
		entity_id: int, # VarInt
		animation: int, # Unsigned Byte
	):
		self.entity_id = entity_id # Player ID.
		self.animation = animation # Animation ID (see below).

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_varint(self.entity_id)
		b.write_ubyte(self.animation)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		entity_id = r.read_varint()
		animation = r.read_ubyte()
		return cls(entity_id, animation)

@final
class PlayAwardStatisticsS2C(Packet, id=0x04):
	def __init__(self,
		statistics: list[
			tuple[
				int, # Category ID; VarInt; See below.
				int, # Statistic ID; VarInt; See below.
				int, # Value; VarInt; The amount to set it to.
			]
		],
	):
		self.statistics = statistics

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_varint(len(self.statistics))
		for category, statistic, value in self.statistics:
			b.write_varint(category)
			b.write_varint(statistic)
			b.write_varint(value)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		statistics = []
		for _ in range(r.read_varint()):
			category = r.read_varint()
			statistic = r.read_varint()
			value = r.read_varint()
			statistics.append((category, statistic, value))
		return cls(statistics)

@final
class PlayAcknowledgeBlockChangeS2C(Packet, id=0x05):
	def __init__(self,
		sequence_id: int, # VarInt
	):
		self.sequence_id = sequence_id # Represents the sequence to acknowledge, this is used for properly syncing block changes to the client after interactions.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_varint(self.sequence_id)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		sequence_id = r.read_varint()
		return cls(sequence_id)

@final
class PlaySetBlockDestroyStageS2C(Packet, id=0x06):
	def __init__(self,
		entity_id: int, # VarInt
		location: tuple[int, int, int], # Position
		destroy_stage: int, # Byte
	):
		self.entity_id = entity_id # The ID of the entity breaking the block.
		self.location = location # Block Position.
		self.destroy_stage = destroy_stage # 0–9 to set it, any other value to remove it.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_varint(self.entity_id)
		b.write_pos_1_14(self.location)
		b.write_byte(self.destroy_stage)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		entity_id = r.read_varint()
		location = r.read_pos_1_14()
		destroy_stage = r.read_byte()
		return cls(entity_id, location, destroy_stage)

@final
class PlayBlockEntityDataS2C(Packet, id=0x07):
	def __init__(self,
		location: tuple[int, int, int], # Position
		type: int, # VarInt
		nbt_data: NBT, # NBT Tag
	):
		self.location = location # 
		self.type = type # The type of the block entity
		self.nbt_data = nbt_data # Data to set.  May be a TAG_END (0), in which case the block entity at the given location is removed (though this is not required since the client will remove the block entity automatically on chunk unload or block removal).

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_pos_1_14(self.location)
		b.write_varint(self.type)
		self.nbt_data.to_bytes(b)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		location = r.read_pos_1_14()
		type = r.read_varint()
		nbt_data = NBT.parse_from(r)
		return cls(location, type, nbt_data)

@final
class PlayBlockActionS2C(Packet, id=0x08):
	def __init__(self,
		location: tuple[int, int, int], # Position
		action_id: int, # Unsigned Byte
		action_parameter: int, # Unsigned Byte
		block_type: int, # VarInt
	):
		self.location = location # Block coordinates.
		self.action_id = action_id # Varies depending on block — see Block Actions.
		self.action_parameter = action_parameter # Varies depending on block — see Block Actions.
		self.block_type = block_type # The block type ID for the block.  This must match the block at the given coordinates.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_pos_1_14(self.location)
		b.write_ubyte(self.action_id)
		b.write_ubyte(self.action_parameter)
		b.write_varint(self.block_type)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		location = r.read_pos_1_14()
		action_id = r.read_ubyte()
		action_parameter = r.read_ubyte()
		block_type = r.read_varint()
		return cls(location, action_id, action_parameter, block_type)

@final
class PlayBlockUpdateS2C(Packet, id=0x09):
	def __init__(self,
		location: tuple[int, int, int], # Position
		block_id: int, # VarInt
	):
		self.location = location # Block Coordinates.
		self.block_id = block_id # The new block state ID for the block as given in the global palette. See that section for more information.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_pos_1_14(self.location)
		b.write_varint(self.block_id)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		location = r.read_pos_1_14()
		block_id = r.read_varint()
		return cls(location, block_id)

@final
class PlayBossBarS2C(Packet, id=0x0A):
	def __init__(self,
		uuid: uuid.UUID, # UUID
		action: int, # VarInt Enum
		title: str | None, # Chat
		health: float | None, # Float
		color: int | None, # VarInt Enum
		division: int | None, # VarInt Enum
		flags: int | None, # Unsigned Byte
	):
		self.uuid = uuid # Unique ID for this bar.
		self.action = action # Determines the layout of the remaining packet.
		self.title = title # 
		self.health = health # From 0 to 1. Values greater than 1 do not crash a Notchian client, and start rendering part of a second health bar at around 1.5.
		self.color = color # Color ID (see below).
		self.division = division # Type of division (see below).
		self.flags = flags # Bit mask. 0x1: should darken sky, 0x2: is dragon bar (used to play end music), 0x04: create fog (previously was also controlled by 0x02).

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_uuid(self.uuid)
		b.write_varint(self.action)
		if self.action in (0, 3):
			assert self.title is not None
			b.write_string(self.title)
		if self.action in (0, 2):
			assert self.health is not None
			b.write_float(self.health)
		if self.action in (0, 4):
			assert self.color is not None
			assert self.division is not None
			b.write_varint(self.color)
			b.write_varint(self.division)
		if self.action in (0, 5):
			assert self.flags is not None
			b.write_ubyte(self.flags)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		uuid = r.read_uuid()
		action = r.read_varint()
		title = r.read_string() if action in (0, 3) else None
		health = r.read_float() if action in (0, 2) else None
		if action in (0, 4):
			color = r.read_varint()
			division = r.read_varint()
		else:
			color = None
			division = None
		flags = r.read_ubyte() if action in (0, 5) else None
		return cls(uuid, action, title, health, color, division, flags)

@final
class PlayChangeDifficultyS2C(Packet, id=0x0B):
	def __init__(self,
		difficulty: int, # Unsigned Byte
		difficulty_locked: bool, # Boolean
	):
		self.difficulty = difficulty # 0: peaceful, 1: easy, 2: normal, 3: hard.
		self.difficulty_locked = difficulty_locked # 

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_ubyte(self.difficulty)
		b.write_bool(self.difficulty_locked)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		difficulty = r.read_ubyte()
		difficulty_locked = r.read_bool()
		return cls(difficulty, difficulty_locked)

@final
class PlayClearTitlesS2C(Packet, id=0x0C):
	def __init__(self,
		reset: bool, # Boolean
	):
		self.reset = reset # 

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_bool(self.reset)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		reset = r.read_bool()
		return cls(reset)

@final
class PlayCommandSuggestionsResponseS2C(Packet, id=0x0D):
	def __init__(self,
		id: int, # VarInt
		start: int, # VarInt
		length: int, # VarInt
		matches: list[
			tuple[
				str, # String (32767)
				bool, # Boolean
				dict | None, # Optional Chat
			]
		],
	):
		self.id = id # Transaction ID.
		self.start = start # Start of the text to replace.
		self.length = length # Length of the text to replace.
		self.matches = matches

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_varint(self.id)
		b.write_varint(self.start)
		b.write_varint(self.length)
		b.write_varint(len(self.matches))
		for match, has_tooltip, tooltip in self.matches:
			b.write_string(match)
			b.write_bool(has_tooltip)
			if has_tooltip:
				assert tooltip is not None
				b.write_json(tooltip)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		id = r.read_varint()
		start = r.read_varint()
		length = r.read_varint()
		matches = []
		for _ in range(r.read_varint()):
			match = r.read_string()
			has_tooltip = r.read_bool()
			tooltip = r.read_json() if has_tooltip else None
			matches.append((match, has_tooltip, tooltip))
		return cls(id, start, length, matches)

@final
class PlayCommandsS2C(Packet, id=0x0E):
	def __init__(self,
		nodes: list[Node], # Array of Node
		root_index: int, # VarInt
	):
		self.nodes = nodes # An array of nodes.
		self.root_index = root_index # 	Index of the root node in the previous array.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_varint(len(self.nodes))
		for n in self.nodes:
			n.to_bytes(b)
		b.write_varint(self.root_index)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		nodes: list[Node] = []
		for _ in range(r.read_varint()):
			node = Node.parse_from(r)
			nodes.append(node)
		root_index = r.read_varint()
		return cls(nodes, root_index)

@final
class PlayCloseContainerS2C(Packet, id=0x0F):
	def __init__(self,
		window_id: int, # Unsigned Byte
	):
		self.window_id = window_id # This is the ID of the window that was closed. 0 for inventory.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_ubyte(self.window_id)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		window_id = r.read_ubyte()
		return cls(window_id)

@final
class PlaySetContainerContentS2C(Packet, id=0x10):
	def __init__(self,
		window_id: int, # Unsigned Byte
		state_id: int, # VarInt
		slot_data: list[Slot], # Array of Slot
		carried_item: Slot, # Slot
	):
		self.window_id = window_id # The ID of window which items are being sent for. 0 for player inventory.
		self.state_id = state_id # The last received State ID from either a Set Container Slot or a Set Container Content packet
		self.slot_data = slot_data # Number of elements in the following array.
		self.carried_item = carried_item # Item held by player.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_ubyte(self.window_id)
		b.write_varint(self.state_id)
		b.write_varint(len(self.slot_data))
		for slot in self.slot_data:
			slot.to_bytes(b)
		self.carried_item.to_bytes(b)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		window_id = r.read_ubyte()
		state_id = r.read_varint()
		slot_data = [Slot.parse_from(r) for _ in range(r.read_varint())]
		carried_item = Slot.parse_from(r)
		return cls(window_id, state_id, slot_data, carried_item)

@final
class PlaySetContainerPropertyS2C(Packet, id=0x11):
	def __init__(self,
		window_id: int, # Unsigned Byte
		property: int, # Short
		value: int, # Short
	):
		self.window_id = window_id # 
		self.property = property # The property to be updated, see below.
		self.value = value # The new value for the property, see below.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_ubyte(self.window_id)
		b.write_short(self.property)
		b.write_short(self.value)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		window_id = r.read_ubyte()
		property = r.read_short()
		value = r.read_short()
		return cls(window_id, property, value)

@final
class PlaySetContainerSlotS2C(Packet, id=0x12):
	def __init__(self,
		window_id: int, # Byte
		state_id: int, # VarInt
		slot: int, # Short
		slot_data: Slot, # Slot
	):
		self.window_id = window_id # The window which is being updated. 0 for player inventory. Note that all known window types include the player inventory. This packet will only be sent for the currently opened window while the player is performing actions, even if it affects the player inventory. After the window is closed, a number of these packets are sent to update the player's inventory window (0).
		self.state_id = state_id # The last received State ID from either a Set Container Slot or a Set Container Content packet
		self.slot = slot # The slot that should be updated.
		self.slot_data = slot_data # 

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_byte(self.window_id)
		b.write_varint(self.state_id)
		b.write_short(self.slot)
		self.slot_data.to_bytes(b)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		window_id = r.read_byte()
		state_id = r.read_varint()
		slot = r.read_short()
		slot_data = Slot.parse_from(r)
		return cls(window_id, state_id, slot, slot_data)

@final
class PlaySetCooldownS2C(Packet, id=0x13):
	def __init__(self,
		item_id: int, # VarInt
		cooldown_ticks: int, # VarInt
	):
		self.item_id = item_id # Numeric ID of the item to apply a cooldown to.
		self.cooldown_ticks = cooldown_ticks # Number of ticks to apply a cooldown for, or 0 to clear the cooldown.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_varint(self.item_id)
		b.write_varint(self.cooldown_ticks)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		item_id = r.read_varint()
		cooldown_ticks = r.read_varint()
		return cls(item_id, cooldown_ticks)

@final
class PlayChatSuggestionsS2C(Packet, id=0x14):
	def __init__(self,
		action: int, # VarInt Enum
		entries: list[str], # Array of String
	):
		self.action = action # 0: Add, 1: Remove, 2: Set
		self.entries = entries # 

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_varint(self.action)
		b.write_varint(len(self.entries))
		for i in self.entries:
			b.write_string(i)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		action = r.read_varint()
		entries = [r.read_string() for _ in range(r.read_varint())]
		return cls(action, entries)

@final
class PlayPluginMessageS2C(Packet, id=0x15):
	def __init__(self,
		channel: str, # Identifier
		data: bytes, # Byte Array (1048576)
	):
		self.channel = channel # Name of the plugin channel used to send the data.
		self.data = data # Any data. The length of this array must be inferred from the packet length.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_string(self.channel)
		b.write(self.data)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		channel = r.read_string()
		data = r.read()
		return cls(channel, data)

@final
class PlayDeleteMessageS2C(Packet, id=0x16):
	def __init__(self,
		signature: bytes, # Byte Array
	):
		self.signature = signature # Bytes of the signature.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_varint(len(self.signature))
		b.write(self.signature)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		signature = r.read(r.read_varint())
		return cls(signature)

@final
class PlayDisconnectS2C(Packet, id=0x17):
	def __init__(self,
		reason: dict, # Chat
	):
		self.reason = reason # Displayed to the client when the connection terminates.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_json(self.reason)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		reason = r.read_json()
		return cls(reason)

@final
class PlayDisguisedChatMessageS2C(Packet, id=0x18):
	def __init__(self,
		message: dict, # Chat
		chat_type: int, # VarInt
		chat_type_name: dict, # Chat
		has_target_name: bool, # Boolean
		target_name: dict | None, # Chat
	):
		self.message = message # 
		self.chat_type = chat_type # The chat message type.
		self.chat_type_name = chat_type_name # The name associated with the chat type. Usually the message sender's display name.
		self.has_target_name = has_target_name # True if target name is present.
		self.target_name = target_name # The target name associated with the chat type. Usually the message target's display name. Only present if previous boolean is true.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_json(self.message)
		b.write_varint(self.chat_type)
		b.write_json(self.chat_type_name)
		b.write_bool(self.has_target_name)
		if self.has_target_name:
			assert self.target_name is not None
			b.write_json(self.target_name)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		message = r.read_json()
		chat_type = r.read_varint()
		chat_type_name = r.read_json()
		has_target_name = r.read_bool()
		target_name = r.read_json() if has_target_name else None
		return cls(message, chat_type, chat_type_name, has_target_name, target_name)

@final
class PlayEntityEventS2C(Packet, id=0x19):
	def __init__(self,
		entity_id: int, # Int
		entity_status: int, # Byte Enum
	):
		self.entity_id = entity_id # 
		self.entity_status = entity_status # See Entity statuses for a list of which statuses are valid for each type of entity.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_int(self.entity_id)
		b.write_byte(self.entity_status)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		entity_id = r.read_int()
		entity_status = r.read_byte()
		return cls(entity_id, entity_status)

@final
class PlayExplosionS2C(Packet, id=0x1A):
	def __init__(self,
		x: float, # Double
		y: float, # Double
		z: float, # Double
		strength: float, # Float
		records: list[
			tuple[int, int, int] # (Byte, Byte, Byte)
		],
		player_motion_x: float, # Float
		player_motion_y: float, # Float
		player_motion_z: float, # Float
	):
		self.x = x
		self.y = y
		self.z = z
		self.strength = strength # A strength greater than or equal to 2.0 spawns a minecraft:explosion_emitter particle, while a lesser strength spawns a minecraft:explosion particle.
		self.records = records # Each record is 3 signed bytes long; the 3 bytes are the XYZ (respectively) signed offsets of affected blocks.
		self.player_motion_x = player_motion_x # X velocity of the player being pushed by the explosion.
		self.player_motion_y = player_motion_y # Y velocity of the player being pushed by the explosion.
		self.player_motion_z = player_motion_z # Z velocity of the player being pushed by the explosion.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_double(self.x)
		b.write_double(self.y)
		b.write_double(self.z)
		b.write_float(self.strength)
		b.write_varint(len(self.records))
		for rx, ry, rz in self.records:
			b.write_byte(rx)
			b.write_byte(ry)
			b.write_byte(rz)
		b.write_float(self.player_motion_x)
		b.write_float(self.player_motion_y)
		b.write_float(self.player_motion_z)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		x = r.read_double()
		y = r.read_double()
		z = r.read_double()
		strength = r.read_float()
		records = []
		for _ in range(r.read_varint()):
			rx = r.read_byte()
			ry = r.read_byte()
			rz = r.read_byte()
			records.append((rx, ry, rz))
		player_motion_x = r.read_float()
		player_motion_y = r.read_float()
		player_motion_z = r.read_float()
		return cls(x, y, z, strength, records, player_motion_x, player_motion_y, player_motion_z)

@final
class PlayUnloadChunkS2C(Packet, id=0x1B):
	def __init__(self,
		chunk_x: int, # Int
		chunk_z: int, # Int
	):
		self.chunk_x = chunk_x # Block coordinate divided by 16, rounded down.
		self.chunk_z = chunk_z # Block coordinate divided by 16, rounded down.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_int(self.chunk_x)
		b.write_int(self.chunk_z)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		chunk_x = r.read_int()
		chunk_z = r.read_int()
		return cls(chunk_x, chunk_z)

@final
class PlayGameEventS2C(Packet, id=0x1C):
	def __init__(self,
		event: int, # Unsigned Byte
		value: float, # Float
	):
		self.event = event # See below.
		self.value = value # Depends on Event.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_ubyte(self.event)
		b.write_float(self.value)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		event = r.read_ubyte()
		value = r.read_float()
		return cls(event, value)

@final
class PlayOpenHorseScreenS2C(Packet, id=0x1D):
	def __init__(self,
		window_id: int, # Unsigned Byte
		slot_count: int, # VarInt
		entity_id: int, # Int
	):
		self.window_id = window_id # 
		self.slot_count = slot_count # 
		self.entity_id = entity_id # 

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_ubyte(self.window_id)
		b.write_varint(self.slot_count)
		b.write_int(self.entity_id)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		window_id = r.read_ubyte()
		slot_count = r.read_varint()
		entity_id = r.read_int()
		return cls(window_id, slot_count, entity_id)

@final
class PlayInitializeWorldBorderS2C(Packet, id=0x1E):
	def __init__(self,
		x: float, # Double
		z: float, # Double
		old_diameter: float, # Double
		new_diameter: float, # Double
		speed: int, # VarLong
		portal_teleport_boundary: int, # VarInt
		warning_blocks: int, # VarInt
		warning_time: int, # VarInt
	):
		self.x = x # 
		self.z = z # 
		self.old_diameter = old_diameter # Current length of a single side of the world border, in meters.
		self.new_diameter = new_diameter # Target length of a single side of the world border, in meters.
		self.speed = speed # Number of real-time milliseconds until New Diameter is reached. It appears that Notchian server does not sync world border speed to game ticks, so it gets out of sync with server lag. If the world border is not moving, this is set to 0.
		self.portal_teleport_boundary = portal_teleport_boundary # Resulting coordinates from a portal teleport are limited to ±value. Usually 29999984.
		self.warning_blocks = warning_blocks # In meters.
		self.warning_time = warning_time # In seconds as set by /worldborder warning time.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_double(self.x)
		b.write_double(self.z)
		b.write_double(self.old_diameter)
		b.write_double(self.new_diameter)
		b.write_varlong(self.speed)
		b.write_varint(self.portal_teleport_boundary)
		b.write_varint(self.warning_blocks)
		b.write_varint(self.warning_time)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		x = r.read_double()
		z = r.read_double()
		old_diameter = r.read_double()
		new_diameter = r.read_double()
		speed = r.read_varlong()
		portal_teleport_boundary = r.read_varint()
		warning_blocks = r.read_varint()
		warning_time = r.read_varint()
		return cls(x, z, old_diameter, new_diameter, speed, portal_teleport_boundary, warning_blocks, warning_time)

@final
class PlayKeepAliveS2C(Packet, id=0x1F):
	def __init__(self,
		keep_alive_id: int, # Long
	):
		self.keep_alive_id = keep_alive_id # 

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_long(self.keep_alive_id)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		keep_alive_id = r.read_long()
		return cls(keep_alive_id)

@final
class PlayChunkDataandUpdateLightS2C(Packet, id=0x20):
	def __init__(self,
		chunk_x: int, # Int
		chunk_z: int, # Int
		heightmaps: NBT, # NBT
		data: bytes, # Byte array
		block_entities: list[
			tuple[
				int, # Packed XZ; Byte
				int, # Y; Short
				int, # Type; VarInt
				NBT, # Data; NBT
			]
		],
		trust_edges: bool, # Boolean
		sky_light_mask: BitSet, # BitSet
		block_light_mask: BitSet, # BitSet
		empty_sky_light_mask: BitSet, # BitSet
		empty_block_light_mask: BitSet, # BitSet
		sky_light_arrays: list[list[bytes]], # Array of Array of 2048 bytes
		block_light_arrays: list[list[bytes]], # Array of Array of 2048 bytes
	):
		self.chunk_x = chunk_x # Chunk coordinate (block coordinate divided by 16, rounded down)
		self.chunk_z = chunk_z # Chunk coordinate (block coordinate divided by 16, rounded down)
		self.heightmaps = heightmaps # Compound containing one long array named MOTION_BLOCKING, which is a heightmap for the highest solid block at each position in the chunk (as a compacted long array with 256 entries, with the number of bits per entry varying depending on the world's height, defined by the formula ceil(log2(height + 1))). The Notchian server also adds a WORLD_SURFACE long array, the purpose of which is unknown, but it's not required for the chunk to be accepted.
		self.data = data # See data structure in Chunk Format
		self.block_entities = block_entities #
		self.trust_edges = trust_edges # If edges should be trusted for light updates.
		self.sky_light_mask = sky_light_mask # BitSet containing bits for each section in the world + 2.  Each set bit indicates that the corresponding 16×16×16 chunk section has data in the Sky Light array below.  The least significant bit is for blocks 16 blocks to 1 block below the min world height (one section below the world), while the most significant bit covers blocks 1 to 16 blocks above the max world height (one section above the world).
		self.block_light_mask = block_light_mask # BitSet containing bits for each section in the world + 2.  Each set bit indicates that the corresponding 16×16×16 chunk section has data in the Block Light array below.  The order of bits is the same as in Sky Light Mask.
		self.empty_sky_light_mask = empty_sky_light_mask # BitSet containing bits for each section in the world + 2.  Each set bit indicates that the corresponding 16×16×16 chunk section has all zeros for its Sky Light data.  The order of bits is the same as in Sky Light Mask.
		self.empty_block_light_mask = empty_block_light_mask # BitSet containing bits for each section in the world + 2.  Each set bit indicates that the corresponding 16×16×16 chunk section has all zeros for its Block Light data.  The order of bits is the same as in Sky Light Mask.
		self.sky_light_arrays = sky_light_arrays #
		self.block_light_arrays = block_light_arrays #

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_int(self.chunk_x)
		b.write_int(self.chunk_z)
		self.heightmaps.to_bytes(b)
		b.write_varint(len(self.data))
		b.write(self.data)
		b.write_varint(len(self.block_entities))
		for packed_xz, y, type, data in self.block_entities:
			b.write_byte(packed_xz)
			b.write_short(y)
			b.write_varint(type)
			data.to_bytes(b)
		b.write_bool(self.trust_edges)
		self.sky_light_mask.to_bytes(b)
		self.block_light_mask.to_bytes(b)
		self.empty_sky_light_mask.to_bytes(b)
		self.empty_block_light_mask.to_bytes(b)
		b.write_varint(len(self.sky_light_arrays))
		for sky_light_array in self.sky_light_arrays:
			b.write_varint(len(sky_light_array))
			for sky_light in sky_light_array:
				assert len(sky_light) == 2048
				b.write(sky_light)
		b.write_varint(len(self.block_light_arrays))
		for block_light_array in self.block_light_arrays:
			b.write_varint(len(block_light_array))
			for block_light in block_light_array:
				assert len(block_light) == 2048
				b.write(block_light)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		chunk_x = r.read_int()
		chunk_z = r.read_int()
		heightmaps = NBT.parse_from(r)
		data = r.read(r.read_varint())
		block_entities = []
		for _ in range(r.read_varint()):
			packed_xz = r.read_byte()
			y = r.read_short()
			type = r.read_varint()
			dta = NBT.parse_from(r)
			block_entities.append((packed_xz, y, type, dta))
		trust_edges = r.read_bool()
		sky_light_mask = BitSet.parse_from(r)
		block_light_mask = BitSet.parse_from(r)
		empty_sky_light_mask = BitSet.parse_from(r)
		empty_block_light_mask = BitSet.parse_from(r)
		sky_light_arrays = []
		for _ in range(r.read_varint()):
			sky_light_array = []
			for _ in range(r.read_varint()):
				sky_light = r.read(2048)
				sky_light_array.append(sky_light)
			sky_light_arrays.append(sky_light_array)
		block_light_arrays = []
		for _ in range(r.read_varint()):
			block_light_array = []
			for _ in range(r.read_varint()):
				block_light = r.read(2048)
				block_light_array.append(block_light)
			block_light_arrays.append(block_light_array)
		return cls(chunk_x, chunk_z, heightmaps, data, block_entities, trust_edges, sky_light_mask, block_light_mask, empty_sky_light_mask, empty_block_light_mask, sky_light_arrays, block_light_arrays)

@final
class PlayWorldEventS2C(Packet, id=0x21):
	def __init__(self,
		event: int, # Int
		location: tuple[int, int, int], # Position
		data: int, # Int
		disable_relative_volume: bool, # Boolean
	):
		self.event = event # The event, see below.
		self.location = location # The location of the event.
		self.data = data # Extra data for certain events, see below.
		self.disable_relative_volume = disable_relative_volume # See above.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_int(self.event)
		b.write_pos_1_14(self.location)
		b.write_int(self.data)
		b.write_bool(self.disable_relative_volume)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		event = r.read_int()
		location = r.read_pos_1_14()
		data = r.read_int()
		disable_relative_volume = r.read_bool()
		return cls(event, location, data, disable_relative_volume)

@final
class PlayParticleS2C(Packet, id=0x22):
	def __init__(self,
		particle_id: int, # VarInt
		long_distance: bool, # Boolean
		x: float, # Double
		y: float, # Double
		z: float, # Double
		offset_x: float, # Float
		offset_y: float, # Float
		offset_z: float, # Float
		max_speed: float, # Float
		particles: list[ParticleData], # The variable data listed in the particle data type.
	):
		self.particle_id = particle_id
		self.long_distance = long_distance
		self.x = x
		self.y = y
		self.z = z
		self.offset_x = offset_x
		self.offset_y = offset_y
		self.offset_z = offset_z
		self.max_speed = max_speed
		self.particles = particles

@final
class PlayUpdateLightS2C(Packet, id=0x23):
	def __init__(self,
		chunk_x: int, # VarInt
		chunk_z: int, # VarInt
		trust_edges: bool, # Boolean
		sky_light_mask: BitSet, # BitSet
		block_light_mask: BitSet, # BitSet
		empty_sky_light_mask: BitSet, # BitSet
		empty_block_light_mask: BitSet, # BitSet
		sky_light_arrays: list[list[bytes]], # Array of Array of 2048 bytes
		block_light_arrays: list[list[bytes]], # Array of Array of 2048 bytes
	):
		self.chunk_x = chunk_x # Chunk coordinate (block coordinate divided by 16, rounded down)
		self.chunk_z = chunk_z # Chunk coordinate (block coordinate divided by 16, rounded down)
		self.trust_edges = trust_edges # If edges should be trusted for light updates.
		self.sky_light_mask = sky_light_mask # BitSet containing bits for each section in the world + 2.  Each set bit indicates that the corresponding 16×16×16 chunk section has data in the Sky Light array below.  The least significant bit is for blocks 16 blocks to 1 block below the min world height (one section below the world), while the most significant bit covers blocks 1 to 16 blocks above the max world height (one section above the world).
		self.block_light_mask = block_light_mask # BitSet containing bits for each section in the world + 2.  Each set bit indicates that the corresponding 16×16×16 chunk section has data in the Block Light array below.  The order of bits is the same as in Sky Light Mask.
		self.empty_sky_light_mask = empty_sky_light_mask # BitSet containing bits for each section in the world + 2.  Each set bit indicates that the corresponding 16×16×16 chunk section has all zeros for its Sky Light data.  The order of bits is the same as in Sky Light Mask.
		self.empty_block_light_mask = empty_block_light_mask # BitSet containing bits for each section in the world + 2.  Each set bit indicates that the corresponding 16×16×16 chunk section has all zeros for its Block Light data.  The order of bits is the same as in Sky Light Mask.
		self.sky_light_arrays = sky_light_arrays #
		self.block_light_arrays = block_light_arrays #

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_varint(self.chunk_x)
		b.write_varint(self.chunk_z)
		b.write_bool(self.trust_edges)
		self.sky_light_mask.to_bytes(b)
		self.block_light_mask.to_bytes(b)
		self.empty_sky_light_mask.to_bytes(b)
		self.empty_block_light_mask.to_bytes(b)
		b.write_varint(len(self.sky_light_arrays))
		for sky_light_array in self.sky_light_arrays:
			b.write_varint(len(sky_light_array))
			for sky_light in sky_light_array:
				assert len(sky_light) == 2048
				b.write(sky_light)
		b.write_varint(len(self.block_light_arrays))
		for block_light_array in self.block_light_arrays:
			b.write_varint(len(block_light_array))
			for block_light in block_light_array:
				assert len(block_light) == 2048
				b.write(block_light)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		chunk_x = r.read_varint()
		chunk_z = r.read_varint()
		trust_edges = r.read_bool()
		sky_light_mask = BitSet.parse_from(r)
		block_light_mask = BitSet.parse_from(r)
		empty_sky_light_mask = BitSet.parse_from(r)
		empty_block_light_mask = BitSet.parse_from(r)
		sky_light_arrays = []
		for _ in range(r.read_varint()):
			sky_light_array = []
			for _ in range(r.read_varint()):
				sky_light = r.read(2048)
				sky_light_array.append(sky_light)
			sky_light_arrays.append(sky_light_array)
		block_light_arrays = []
		for _ in range(r.read_varint()):
			block_light_array = []
			for _ in range(r.read_varint()):
				block_light = r.read(2048)
				block_light_array.append(block_light)
			block_light_arrays.append(block_light_array)
		return cls(chunk_x, chunk_z, trust_edges, sky_light_mask, block_light_mask, empty_sky_light_mask, empty_block_light_mask, sky_light_arrays, block_light_arrays)

@final
class PlayLoginS2C(Packet, id=0x24):
	def __init__(self,
		entity_id: int, # Int
		is_hardcore: bool, # Boolean
		gamemode: int, # Unsigned Byte
		previous_gamemode: int, # Byte
		dimension_names: list[str], # Array of Identifier
		registry_codec: Compound, # NBT Tag Compound
		dimension_type: str, # Identifier
		dimension_name: str, # Identifier
		hashed_seed: int, # Long
		max_players: int, # VarInt
		view_distance: int, # VarInt
		simulation_distance: int, # VarInt
		reduced_debug_info: bool, # Boolean
		enable_respawn_screen: bool, # Boolean
		is_debug: bool, # Boolean
		is_flat: bool, # Boolean
		has_death_location: bool, # Boolean
		death_dimension_name: str | None, # Optional Identifier
		death_location: tuple[int, int, int] | None, # Optional Position
	):
		self.entity_id = entity_id # The player's Entity ID (EID).
		self.is_hardcore = is_hardcore # 
		self.gamemode = gamemode # 0: Survival, 1: Creative, 2: Adventure, 3: Spectator.
		self.previous_gamemode = previous_gamemode # -1: Undefined (null), 0: Survival, 1: Creative, 2: Adventure, 3: Spectator. The previous gamemode. Vanilla client uses this for the debug (F3 + N & F3 + F4) gamemode switch. (More information needed)
		self.dimension_names = dimension_names # Identifiers for all dimensions on the server.
		self.registry_codec = registry_codec # Represents certain registries that are sent from the server and are applied on the client.
		self.dimension_type = dimension_type # Name of the dimension type being spawned into.
		self.dimension_name = dimension_name # Name of the dimension being spawned into.
		self.hashed_seed = hashed_seed # First 8 bytes of the SHA-256 hash of the world's seed. Used client side for biome noise
		self.max_players = max_players # Was once used by the client to draw the player list, but now is ignored.
		self.view_distance = view_distance # Render distance (2-32).
		self.simulation_distance = simulation_distance # The distance that the client will process specific things, such as entities.
		self.reduced_debug_info = reduced_debug_info # If true, a Notchian client shows reduced information on the debug screen.  For servers in development, this should almost always be false.
		self.enable_respawn_screen = enable_respawn_screen # Set to false when the doImmediateRespawn gamerule is true.
		self.is_debug = is_debug # True if the world is a debug mode world; debug mode worlds cannot be modified and have predefined blocks.
		self.is_flat = is_flat # True if the world is a superflat world; flat worlds have different void fog and a horizon at y=0 instead of y=63.
		self.has_death_location = has_death_location # If true, then the next two fields are present.
		self.death_dimension_name = death_dimension_name # Name of the dimension the player died in.
		self.death_location = death_location # The location that the player died at.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_int(self.entity_id)
		b.write_bool(self.is_hardcore)
		b.write_ubyte(self.gamemode)
		b.write_byte(self.previous_gamemode)
		b.write_varint(len(self.dimension_names))
		for dimension_name in self.dimension_names:
			b.write_string(dimension_name)
		self.registry_codec.to_bytes(b)
		b.write_string(self.dimension_type)
		b.write_string(self.dimension_name)
		b.write_long(self.hashed_seed)
		b.write_varint(self.max_players)
		b.write_varint(self.view_distance)
		b.write_varint(self.simulation_distance)
		b.write_bool(self.reduced_debug_info)
		b.write_bool(self.enable_respawn_screen)
		b.write_bool(self.is_debug)
		b.write_bool(self.is_flat)
		b.write_bool(self.has_death_location)
		if self.has_death_location:
			assert self.death_dimension_name is not None
			assert self.death_location is not None
			b.write_string(self.death_dimension_name)
			b.write_pos_1_14(self.death_location)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		entity_id = r.read_int()
		is_hardcore = r.read_bool()
		gamemode = r.read_ubyte()
		previous_gamemode = r.read_byte()
		dimension_names = []
		for _ in range(r.read_varint()):
			dimension_name = r.read_string()
			dimension_names.append(dimension_name)
		registry_codec = Compound.parse_from(r)
		dimension_type = r.read_string()
		dimension_name = r.read_string()
		hashed_seed = r.read_long()
		max_players = r.read_varint()
		view_distance = r.read_varint()
		simulation_distance = r.read_varint()
		reduced_debug_info = r.read_bool()
		enable_respawn_screen = r.read_bool()
		is_debug = r.read_bool()
		is_flat = r.read_bool()
		has_death_location = r.read_bool()
		if has_death_location:
			death_dimension_name = r.read_string()
			death_location = r.read_pos_1_14()
		else:
			death_dimension_name = None
			death_location = None
		return cls(entity_id, is_hardcore, gamemode, previous_gamemode, dimension_names, registry_codec, dimension_type, dimension_name, hashed_seed, max_players, view_distance, simulation_distance, reduced_debug_info, enable_respawn_screen, is_debug, is_flat, has_death_location, death_dimension_name, death_location)

@final
class PlayMapDataS2C(Packet, id=0x25):
	def __init__(self,
		map_id: int, # VarInt
		scale: int, # Byte
		locked: bool, # Boolean
		has_icons: bool, # Boolean
		icons: list[
			tuple[
				int, # Type; VarInt Enum
				int, # X; Byte; Map coordinates: -128 for furthest left, +127 for furthest right
				int, # Z; Byte; Map coordinates: -128 for highest, +127 for lowest
				int, # Direction; Byte; 0-15
				bool, # Has Display Name; Boolean
				dict | None, # Display Name; Optional Chat; Only present if previous Boolean is true
			]
		] | None, # Optional Array
		columns: int, # Unsigned Byte
		rows: int | None, # Optional Unsigned Byte
		x: int | None, # Optional Byte
		z: int | None, # Optional Byte
		length: int | None, # Optional VarInt
		data: list[int] | None, # Optional Array of Unsigned Byte
	):
		self.map_id = map_id # Map ID of the map being modified
		self.scale = scale # From 0 for a fully zoomed-in map (1 block per pixel) to 4 for a fully zoomed-out map (16 blocks per pixel)
		self.locked = locked # True if the map has been locked in a cartography table
		self.has_icons = has_icons # 
		self.icons = icons #
		self.columns = columns # Number of columns updated
		self.rows = rows # Only if Columns is more than 0; number of rows updated
		self.x = x # Only if Columns is more than 0; x offset of the westernmost column
		self.z = z # Only if Columns is more than 0; z offset of the northernmost row
		self.length = length # Only if Columns is more than 0; length of the following array
		self.data = data # Only if Columns is more than 0; see Map item format

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_varint(self.map_id)
		b.write_byte(self.scale)
		b.write_bool(self.locked)
		b.write_bool(self.has_icons)
		if self.has_icons:
			assert self.icons is not None
			b.write_varint(len(self.icons))
			for type, x, z, direction, has_display_name, display_name in self.icons:
				b.write_varint(type)
				b.write_byte(x)
				b.write_byte(z)
				b.write_byte(direction)
				b.write_bool(has_display_name)
				if has_display_name:
					assert display_name is not None
					b.write_json(display_name)
		b.write_ubyte(self.columns)
		if self.columns > 0:
			assert self.rows is not None
			assert self.x is not None
			assert self.z is not None
			assert self.length is not None
			assert self.data is not None
			b.write_ubyte(self.rows)
			b.write_byte(self.x)
			b.write_byte(self.z)
			b.write_varint(self.length)
			b.write_varint(len(self.data))
			for d in self.data:
				b.write_ubyte(d)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		map_id = r.read_varint()
		scale = r.read_byte()
		locked = r.read_bool()
		has_icons = r.read_bool()
		if has_icons:
			icons = []
			for _ in range(r.read_varint()):
				type = r.read_varint()
				x0 = r.read_byte()
				z0 = r.read_byte()
				direction = r.read_byte()
				has_display_name = r.read_bool()
				display_name = r.read_json() if has_display_name else None
				icons.append((type, x0, z0, direction, has_display_name, display_name))
		else:
			icons = None
		columns = r.read_ubyte()
		if columns > 0:
			rows = r.read_ubyte()
			x = r.read_byte()
			z = r.read_byte()
			length = r.read_varint()
			data = []
			for _ in range(r.read_varint()):
				d = r.read_ubyte()
				data.append(d)
		else:
			rows = None
			x = None
			z = None
			length = None
			data = None
		return cls(map_id, scale, locked, has_icons, icons, columns, rows, x, z, length, data)

@final
class PlayMerchantOffersS2C(Packet, id=0x26):
	def __init__(self,
		window_id: int, # VarInt
		trades: list[
			tuple[
				Slot, # input_item_1; Slot; The first item the player has to supply for this villager trade. The count of the item stack is the default "price" of this trade.
				Slot, # output_item; Slot; The ID of the window that is open; this is an int rather than a byte.
				Slot, # input_item_2; Slot; The number of trades in the following array.
				bool, # trade_disabled; Boolean; True if the trade is disabled; false if the trade is enabled.
				int, # number_of_trade_uses; Int; Number of times the trade has been used so far. If equal to the maximum number of trades, the client will display a red X.
				int, # maximum_number_of_trade_uses; Int; Number of times this trade can be used before it's exhausted.
				int, # xp; Int; Amount of XP the villager will earn each time the trade is used.
				int, # special_price; Int; Can be zero or negative. The number is added to the price when an item is discounted due to player reputation or other effects.
				float, # price_multiplier; Float; Can be low (0.05) or high (0.2). Determines how much demand, player reputation, and temporary effects will adjust the price.
				int, # demand; Int; If positive, causes the price to increase. Negative values seem to be treated the same as zero.
			]
		],
		villager_level: int, # VarInt
		experience: int, # VarInt
		is_regular_villager: bool, # Boolean
		can_restock: bool, # Boolean
	):
		self.window_id = window_id # The ID of the window that is open; this is an int rather than a byte.
		self.trades = trades #
		self.villager_level = villager_level # Appears on the trade GUI; meaning comes from the translation key merchant.level. + level. 1: Novice, 2: Apprentice, 3: Journeyman, 4: Expert, 5: Master.
		self.experience = experience # Total experience for this villager (always 0 for the wandering trader).
		self.is_regular_villager = is_regular_villager # True if this is a regular villager; false for the wandering trader.  When false, hides the villager level and some other GUI elements.
		self.can_restock = can_restock # True for regular villagers and false for the wandering trader. If true, the "Villagers restock up to two times per day." message is displayed when hovering over disabled trades.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_varint(self.window_id)
		b.write_varint(len(self.trades))
		for input_item_1, output_item, input_item_2, trade_disabled, number_of_trade_uses, maximum_number_of_trade_uses, xp, special_price, price_multiplier, demand in self.trades:
			input_item_1.to_bytes(b)
			output_item.to_bytes(b)
			input_item_2.to_bytes(b)
			b.write_bool(trade_disabled)
			b.write_int(number_of_trade_uses)
			b.write_int(maximum_number_of_trade_uses)
			b.write_int(xp)
			b.write_int(special_price)
			b.write_float(price_multiplier)
			b.write_int(demand)
		b.write_varint(self.villager_level)
		b.write_varint(self.experience)
		b.write_bool(self.is_regular_villager)
		b.write_bool(self.can_restock)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		window_id = r.read_varint()
		trades = []
		for _ in range(r.read_varint()):
			input_item_1 = Slot.parse_from(r)
			output_item = Slot.parse_from(r)
			input_item_2 = Slot.parse_from(r)
			trade_disabled = r.read_bool()
			number_of_trade_uses = r.read_int()
			maximum_number_of_trade_uses = r.read_int()
			xp = r.read_int()
			special_price = r.read_int()
			price_multiplier = r.read_float()
			demand = r.read_int()
			trades.append((input_item_1, output_item, input_item_2, trade_disabled, number_of_trade_uses, maximum_number_of_trade_uses, xp, special_price, price_multiplier, demand))
		villager_level = r.read_varint()
		experience = r.read_varint()
		is_regular_villager = r.read_bool()
		can_restock = r.read_bool()
		return cls(window_id, trades, villager_level, experience, is_regular_villager, can_restock)

@final
class PlayUpdateEntityPositionS2C(Packet, id=0x27):
	def __init__(self,
		entity_id: int, # VarInt
		delta_x: int, # Short
		delta_y: int, # Short
		delta_z: int, # Short
		on_ground: bool, # Boolean
	):
		self.entity_id = entity_id # 
		self.delta_x = delta_x # Change in X position as (currentX * 32 - prevX * 32) * 128.
		self.delta_y = delta_y # Change in Y position as (currentY * 32 - prevY * 32) * 128.
		self.delta_z = delta_z # Change in Z position as (currentZ * 32 - prevZ * 32) * 128.
		self.on_ground = on_ground # 

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_varint(self.entity_id)
		b.write_short(self.delta_x)
		b.write_short(self.delta_y)
		b.write_short(self.delta_z)
		b.write_bool(self.on_ground)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		entity_id = r.read_varint()
		delta_x = r.read_short()
		delta_y = r.read_short()
		delta_z = r.read_short()
		on_ground = r.read_bool()
		return cls(entity_id, delta_x, delta_y, delta_z, on_ground)

@final
class PlayUpdateEntityPositionandRotationS2C(Packet, id=0x28):
	def __init__(self,
		entity_id: int, # VarInt
		delta_x: int, # Short
		delta_y: int, # Short
		delta_z: int, # Short
		yaw: int, # Angle
		pitch: int, # Angle
		on_ground: bool, # Boolean
	):
		self.entity_id = entity_id # 
		self.delta_x = delta_x # Change in X position as (currentX * 32 - prevX * 32) * 128.
		self.delta_y = delta_y # Change in Y position as (currentY * 32 - prevY * 32) * 128.
		self.delta_z = delta_z # Change in Z position as (currentZ * 32 - prevZ * 32) * 128.
		self.yaw = yaw # New angle, not a delta.
		self.pitch = pitch # New angle, not a delta.
		self.on_ground = on_ground # 

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_varint(self.entity_id)
		b.write_short(self.delta_x)
		b.write_short(self.delta_y)
		b.write_short(self.delta_z)
		b.write_byte(self.yaw)
		b.write_byte(self.pitch)
		b.write_bool(self.on_ground)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		entity_id = r.read_varint()
		delta_x = r.read_short()
		delta_y = r.read_short()
		delta_z = r.read_short()
		yaw = r.read_byte()
		pitch = r.read_byte()
		on_ground = r.read_bool()
		return cls(entity_id, delta_x, delta_y, delta_z, yaw, pitch, on_ground)

@final
class PlayUpdateEntityRotationS2C(Packet, id=0x29):
	def __init__(self,
		entity_id: int, # VarInt
		yaw: int, # Angle
		pitch: int, # Angle
		on_ground: bool, # Boolean
	):
		self.entity_id = entity_id # 
		self.yaw = yaw # New angle, not a delta.
		self.pitch = pitch # New angle, not a delta.
		self.on_ground = on_ground # 

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_varint(self.entity_id)
		b.write_byte(self.yaw)
		b.write_byte(self.pitch)
		b.write_bool(self.on_ground)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		entity_id = r.read_varint()
		yaw = r.read_byte()
		pitch = r.read_byte()
		on_ground = r.read_bool()
		return cls(entity_id, yaw, pitch, on_ground)

@final
class PlayMoveVehicleS2C(Packet, id=0x2A):
	def __init__(self,
		x: float, # Double
		y: float, # Double
		z: float, # Double
		yaw: float, # Float
		pitch: float, # Float
	):
		self.x = x # Absolute position (X coordinate).
		self.y = y # Absolute position (Y coordinate).
		self.z = z # Absolute position (Z coordinate).
		self.yaw = yaw # Absolute rotation on the vertical axis, in degrees.
		self.pitch = pitch # Absolute rotation on the horizontal axis, in degrees.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_double(self.x)
		b.write_double(self.y)
		b.write_double(self.z)
		b.write_float(self.yaw)
		b.write_float(self.pitch)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		x = r.read_double()
		y = r.read_double()
		z = r.read_double()
		yaw = r.read_float()
		pitch = r.read_float()
		return cls(x, y, z, yaw, pitch)

@final
class PlayOpenBookS2C(Packet, id=0x2B):
	def __init__(self,
		hand: int, # VarInt Enum
	):
		self.hand = hand # 0: Main hand, 1: Off hand .

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_varint(self.hand)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		hand = r.read_varint()
		return cls(hand)

@final
class PlayOpenScreenS2C(Packet, id=0x2C):
	def __init__(self,
		window_id: int, # VarInt
		window_type: int, # VarInt
		window_title: dict, # Chat
	):
		self.window_id = window_id # A unique id number for the window to be displayed. Notchian server implementation is a counter, starting at 1.
		self.window_type = window_type # The window type to use for display. Contained in the minecraft:menu registry; see Inventory for the different values.
		self.window_title = window_title # The title of the window.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_varint(self.window_id)
		b.write_varint(self.window_type)
		b.write_json(self.window_title)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		window_id = r.read_varint()
		window_type = r.read_varint()
		window_title = r.read_json()
		return cls(window_id, window_type, window_title)

@final
class PlayOpenSignEditorS2C(Packet, id=0x2D):
	def __init__(self,
		location: tuple[int, int, int], # Position
	):
		self.location = location # 

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_pos_1_14(self.location)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		location = r.read_pos_1_14()
		return cls(location)

@final
class PlayPingS2C(Packet, id=0x2E):
	def __init__(self,
		id: int, # Int
	):
		self.id = id # 

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_int(self.id)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		id = r.read_int()
		return cls(id)

@final
class PlayPlaceGhostRecipeS2C(Packet, id=0x2F):
	def __init__(self,
		window_id: int, # Byte
		recipe: str, # Identifier
	):
		self.window_id = window_id # 
		self.recipe = recipe # A recipe ID.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_byte(self.window_id)
		b.write_string(self.recipe)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		window_id = r.read_byte()
		recipe = r.read_string()
		return cls(window_id, recipe)

@final
class PlayerAbilitiesS2C(Packet, id=0x30):
	def __init__(self,
		flags: int, # Byte
		flying_speed: float, # Float
		field_of_view_modifier: float, # Float
	):
		self.flags = flags # Bit field, see below.
		self.flying_speed = flying_speed # 0.05 by default.
		self.field_of_view_modifier = field_of_view_modifier # Modifies the field of view, like a speed potion. A Notchian server will use the same value as the movement speed sent in the Update Attributes packet, which defaults to 0.1 for players.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_byte(self.flags)
		b.write_float(self.flying_speed)
		b.write_float(self.field_of_view_modifier)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		flags = r.read_byte()
		flying_speed = r.read_float()
		field_of_view_modifier = r.read_float()
		return cls(flags, flying_speed, field_of_view_modifier)

@final
class PlayEndCombatS2C(Packet, id=0x32):
	def __init__(self,
		duration: int, # VarInt
		entity_id: int, # Int
	):
		self.duration = duration # Length of the combat in ticks.
		self.entity_id = entity_id # ID of the primary opponent of the ended combat, or -1 if there is no obvious primary opponent.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_varint(self.duration)
		b.write_int(self.entity_id)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		duration = r.read_varint()
		entity_id = r.read_int()
		return cls(duration, entity_id)

@final
class PlayEnterCombatS2C(Packet, id=0x33):
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
		return cls()

@final
class PlayCombatDeathS2C(Packet, id=0x34):
	def __init__(self,
		player_id: int, # VarInt
		entity_id: int, # Int
		message: dict, # Chat
	):
		self.player_id = player_id # Entity ID of the player that died (should match the client's entity ID).
		self.entity_id = entity_id # The killer entity's ID, or -1 if there is no obvious killer.
		self.message = message # The death message.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_varint(self.player_id)
		b.write_int(self.entity_id)
		b.write_json(self.message)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		player_id = r.read_varint()
		entity_id = r.read_int()
		message = r.read_json()
		return cls(player_id, entity_id, message)

@final
class PlayerInfoRemoveS2C(Packet, id=0x35):
	def __init__(self,
		players: list[uuid.UUID], # Array of UUID
	):
		self.players = players # UUIDs of players to remove.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_varint(len(self.players))
		for player_id in self.players:
			b.write_uuid(player_id)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		players = []
		for _ in range(r.read_varint()):
			player_id = r.read_uuid()
			players.append(player_id)
		return cls(players)

@final
class PlayerInfoUpdateS2C(Packet, id=0x36):
	def __init__(self,
		actions: int, # Byte
		action_array: list[Action], # Array Of Action
	):
		self.actions = actions # Bit Mask. The actions to process. This must have a bit set for every action below, whether it's true or false.
		self.action_array = action_array

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_byte(self.actions)
		b.write_varint(len(self.action_array))
		for action in self.action_array:
			action.to_bytes(self.actions, b)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		actions = r.read_byte()
		action_array = []
		for _ in range(r.read_varint()):
			action = Action.parse_from(actions, r)
			action_array.append(action)
		return cls(actions, action_array)

@final
class PlayLookAtS2C(Packet, id=0x37):
	def __init__(self,
		feet_eyes: int, # VarInt Enum
		target_x: float, # Double
		target_y: float, # Double
		target_z: float, # Double
		is_entity: bool, # Boolean
		entity_id: int | None, # Optional VarInt
		entity_feet_eyes: int | None, # Optional VarInt Enum
	):
		self.feet_eyes = feet_eyes # Values are feet=0, eyes=1.  If set to eyes, aims using the head position; otherwise aims using the feet position.
		self.target_x = target_x # x coordinate of the point to face towards.
		self.target_y = target_y # y coordinate of the point to face towards.
		self.target_z = target_z # z coordinate of the point to face towards.
		self.is_entity = is_entity # If true, additional information about an entity is provided.
		self.entity_id = entity_id # Only if is entity is true — the entity to face towards.
		self.entity_feet_eyes = entity_feet_eyes # Whether to look at the entity's eyes or feet.  Same values and meanings as before, just for the entity's head/feet.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_varint(self.feet_eyes)
		b.write_double(self.target_x)
		b.write_double(self.target_y)
		b.write_double(self.target_z)
		b.write_bool(self.is_entity)
		if self.is_entity:
			assert self.entity_id is not None
			assert self.entity_feet_eyes is not None
			b.write_varint(self.entity_id)
			b.write_varint(self.entity_feet_eyes)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		feet_eyes = r.read_varint()
		target_x = r.read_double()
		target_y = r.read_double()
		target_z = r.read_double()
		is_entity = r.read_bool()
		if is_entity:
			entity_id = r.read_varint()
			entity_feet_eyes = r.read_varint()
		else:
			entity_id = None
			entity_feet_eyes = None
		return cls(feet_eyes, target_x, target_y, target_z, is_entity, entity_id, entity_feet_eyes)

@final
class PlaySynchronizePlayerPositionS2C(Packet, id=0x38):
	def __init__(self,
		x: float, # Double
		y: float, # Double
		z: float, # Double
		yaw: float, # Float
		pitch: float, # Float
		flags: int, # Byte
		teleport_id: int, # VarInt
		dismount_vehicle: bool, # Boolean
	):
		self.x = x # Absolute or relative position, depending on Flags.
		self.y = y # Absolute or relative position, depending on Flags.
		self.z = z # Absolute or relative position, depending on Flags.
		self.yaw = yaw # Absolute or relative rotation on the X axis, in degrees.
		self.pitch = pitch # Absolute or relative rotation on the Y axis, in degrees.
		self.flags = flags # Bit field, see below.
		self.teleport_id = teleport_id # Client should confirm this packet with Confirm Teleportation containing the same Teleport ID.
		self.dismount_vehicle = dismount_vehicle # True if the player should dismount their vehicle.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_double(self.x)
		b.write_double(self.y)
		b.write_double(self.z)
		b.write_float(self.yaw)
		b.write_float(self.pitch)
		b.write_byte(self.flags)
		b.write_varint(self.teleport_id)
		b.write_bool(self.dismount_vehicle)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		x = r.read_double()
		y = r.read_double()
		z = r.read_double()
		yaw = r.read_float()
		pitch = r.read_float()
		flags = r.read_byte()
		teleport_id = r.read_varint()
		dismount_vehicle = r.read_bool()
		return cls(x, y, z, yaw, pitch, flags, teleport_id, dismount_vehicle)

@final
class PlayUpdateRecipeBookS2C(Packet, id=0x39):
	def __init__(self,
		action: int, # VarInt
		crafting_recipe_book_open: bool, # Boolean
		crafting_recipe_book_filter_active: bool, # Boolean
		smelting_recipe_book_open: bool, # Boolean
		smelting_recipe_book_filter_active: bool, # Boolean
		blast_furnace_recipe_book_open: bool, # Boolean
		blast_furnace_recipe_book_filter_active: bool, # Boolean
		smoker_recipe_book_open: bool, # Boolean
		smoker_recipe_book_filter_active: bool, # Boolean
		recipe_ids: list[str], # Array of Identifier
		recipe_ids_2: list[str] | None, # Optional Array of Identifier
	):
		self.action = action # 0: init, 1: add, 2: remove.
		self.crafting_recipe_book_open = crafting_recipe_book_open # If true, then the crafting recipe book will be open when the player opens its inventory.
		self.crafting_recipe_book_filter_active = crafting_recipe_book_filter_active # If true, then the filtering option is active when the players opens its inventory.
		self.smelting_recipe_book_open = smelting_recipe_book_open # If true, then the smelting recipe book will be open when the player opens its inventory.
		self.smelting_recipe_book_filter_active = smelting_recipe_book_filter_active # If true, then the filtering option is active when the players opens its inventory.
		self.blast_furnace_recipe_book_open = blast_furnace_recipe_book_open # If true, then the blast furnace recipe book will be open when the player opens its inventory.
		self.blast_furnace_recipe_book_filter_active = blast_furnace_recipe_book_filter_active # If true, then the filtering option is active when the players opens its inventory.
		self.smoker_recipe_book_open = smoker_recipe_book_open # If true, then the smoker recipe book will be open when the player opens its inventory.
		self.smoker_recipe_book_filter_active = smoker_recipe_book_filter_active # If true, then the filtering option is active when the players opens its inventory.
		self.recipe_ids = recipe_ids # 
		self.recipe_ids_2 = recipe_ids_2 # Only present if mode is 0 (init)

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_varint(self.action)
		b.write_bool(self.crafting_recipe_book_open)
		b.write_bool(self.crafting_recipe_book_filter_active)
		b.write_bool(self.smelting_recipe_book_open)
		b.write_bool(self.smelting_recipe_book_filter_active)
		b.write_bool(self.blast_furnace_recipe_book_open)
		b.write_bool(self.blast_furnace_recipe_book_filter_active)
		b.write_bool(self.smoker_recipe_book_open)
		b.write_bool(self.smoker_recipe_book_filter_active)
		b.write_varint(len(self.recipe_ids))
		for recipe_id in self.recipe_ids:
			b.write_string(recipe_id)
		if self.action:
			assert self.recipe_ids_2 is not None
			b.write_varint(len(self.recipe_ids_2))
			for recipe_id in self.recipe_ids_2:
				b.write_string(recipe_id)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		action = r.read_varint()
		crafting_recipe_book_open = r.read_bool()
		crafting_recipe_book_filter_active = r.read_bool()
		smelting_recipe_book_open = r.read_bool()
		smelting_recipe_book_filter_active = r.read_bool()
		blast_furnace_recipe_book_open = r.read_bool()
		blast_furnace_recipe_book_filter_active = r.read_bool()
		smoker_recipe_book_open = r.read_bool()
		smoker_recipe_book_filter_active = r.read_bool()
		recipe_ids = []
		for _ in range(r.read_varint()):
			recipe_id = r.read_string()
			recipe_ids.append(recipe_id)
		if action == 0:
			recipe_ids_2 = []
			for _ in range(r.read_varint()):
				recipe_id = r.read_string()
				recipe_ids_2.append(recipe_id)
		else:
			recipe_ids_2 = None
		return cls(action, crafting_recipe_book_open, crafting_recipe_book_filter_active, smelting_recipe_book_open, smelting_recipe_book_filter_active, blast_furnace_recipe_book_open, blast_furnace_recipe_book_filter_active, smoker_recipe_book_open, smoker_recipe_book_filter_active, recipe_ids, recipe_ids_2)

@final
class PlayRemoveEntitiesS2C(Packet, id=0x3A):
	def __init__(self,
		entity_ids: list[int], # Array of VarInt
	):
		self.entity_ids = entity_ids # The list of entities to destroy.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_varint(len(self.entity_ids))
		for i in self.entity_ids:
			b.write_varint(i)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		entity_ids = [r.read_varint() for _ in range(r.read_varint())]
		return cls(entity_ids)

@final
class PlayRemoveEntityEffectS2C(Packet, id=0x3B):
	def __init__(self,
		entity_id: int, # VarInt
		effect_id: int, # VarInt
	):
		self.entity_id = entity_id # 
		self.effect_id = effect_id # See this table.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_varint(self.entity_id)
		b.write_varint(self.effect_id)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		entity_id = r.read_varint()
		effect_id = r.read_varint()
		return cls(entity_id, effect_id)

@final
class PlayResourcePackS2C(Packet, id=0x3C):
	def __init__(self,
		url: str, # String (32767)
		hash: str, # String (40)
		forced: bool, # Boolean
		has_prompt_message: bool, # Boolean
		prompt_message: dict | None, # Optional Chat
	):
		self.url = url # The URL to the resource pack.
		self.hash = hash # A 40 character hexadecimal and lowercase SHA-1 hash of the resource pack file.If it's not a 40 character hexadecimal string, the client will not use it for hash verification and likely waste bandwidth — but it will still treat it as a unique id
		self.forced = forced # The notchian client will be forced to use the resource pack from the server. If they decline they will be kicked from the server.
		self.has_prompt_message = has_prompt_message # true If the next field will be sent false otherwise. When false, this is the end of the packet
		self.prompt_message = prompt_message # This is shown in the prompt making the client accept or decline the resource pack.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_string(self.url)
		b.write_string(self.hash)
		b.write_bool(self.forced)
		b.write_bool(self.has_prompt_message)
		if self.has_prompt_message:
			assert self.prompt_message is not None
			b.write_json(self.prompt_message)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		url = r.read_string()
		hash = r.read_string()
		forced = r.read_bool()
		has_prompt_message = r.read_bool()
		prompt_message = r.read_json() if has_prompt_message else None
		return cls(url, hash, forced, has_prompt_message, prompt_message)

@final
class PlayRespawnS2C(Packet, id=0x3D):
	def __init__(self,
		dimension_type: str, # Identifier
		dimension_name: str, # Identifier
		hashed_seed: int, # Long
		gamemode: int, # Unsigned Byte
		previous_gamemode: int, # Byte
		is_debug: bool, # Boolean
		is_flat: bool, # Boolean
		copy_metadata: bool, # Boolean
		has_death_location: bool, # Boolean
		death_dimension_name: str | None, # Optional Identifier
		death_location: tuple[int, int, int] | None, # Optional Position
	):
		self.dimension_type = dimension_type # Valid dimensions are defined per dimension registry sent in Login (play)
		self.dimension_name = dimension_name # Name of the dimension being spawned into.
		self.hashed_seed = hashed_seed # First 8 bytes of the SHA-256 hash of the world's seed. Used client side for biome noise
		self.gamemode = gamemode # 0: Survival, 1: Creative, 2: Adventure, 3: Spectator.
		self.previous_gamemode = previous_gamemode # -1: Undefined (null), 0: Survival, 1: Creative, 2: Adventure, 3: Spectator. The previous gamemode. Vanilla client uses this for the debug (F3 + N & F3 + F4) gamemode switch. (More information needed)
		self.is_debug = is_debug # True if the world is a debug mode world; debug mode worlds cannot be modified and have predefined blocks.
		self.is_flat = is_flat # True if the world is a superflat world; flat worlds have different void fog and a horizon at y=0 instead of y=63.
		self.copy_metadata = copy_metadata # If false, metadata is reset on the respawned player entity.  Set to true for dimension changes (including the dimension change triggered by sending client status perform respawn to exit the end poem/credits), and false for normal respawns.
		self.has_death_location = has_death_location # If true, then the next two fields are present.
		self.death_dimension_name = death_dimension_name # Name of the dimension the player died in.
		self.death_location = death_location # The location that the player died at.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_string(self.dimension_type)
		b.write_string(self.dimension_name)
		b.write_long(self.hashed_seed)
		b.write_ubyte(self.gamemode)
		b.write_byte(self.previous_gamemode)
		b.write_bool(self.is_debug)
		b.write_bool(self.is_flat)
		b.write_bool(self.copy_metadata)
		b.write_bool(self.has_death_location)
		if self.has_death_location:
			assert self.death_dimension_name is not None
			assert self.death_location is not None
			b.write_string(self.death_dimension_name)
			b.write_pos_1_14(self.death_location)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		dimension_type = r.read_string()
		dimension_name = r.read_string()
		hashed_seed = r.read_long()
		gamemode = r.read_ubyte()
		previous_gamemode = r.read_byte()
		is_debug = r.read_bool()
		is_flat = r.read_bool()
		copy_metadata = r.read_bool()
		has_death_location = r.read_bool()
		if has_death_location:
			death_dimension_name = r.read_string()
			death_location = r.read_pos_1_14()
		else:
			death_dimension_name = None
			death_location = None
		return cls(dimension_type, dimension_name, hashed_seed, gamemode, previous_gamemode, is_debug, is_flat, copy_metadata, has_death_location, death_dimension_name, death_location)

@final
class PlaySetHeadRotationS2C(Packet, id=0x3E):
	def __init__(self,
		entity_id: int, # VarInt
		head_yaw: int, # Angle
	):
		self.entity_id = entity_id # 
		self.head_yaw = head_yaw # New angle, not a delta.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_varint(self.entity_id)
		b.write_byte(self.head_yaw)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		entity_id = r.read_varint()
		head_yaw = r.read_byte()
		return cls(entity_id, head_yaw)

@final
class PlayUpdateSectionBlocksS2C(Packet, id=0x3F):
	def __init__(self,
		chunk_section_position: int, # Long
		suppress_light_updates: bool, # Boolean
		blocks: list[int], # Array of VarLong
	):
		self.chunk_section_position = chunk_section_position # Chunk section coordinate (encoded chunk x and z with each 22 bits, and section y with 20 bits, from left to right).
		self.suppress_light_updates = suppress_light_updates # Whether to ignore light updates caused by the contained changes. Always inverse the preceding Update Light packet's "Trust Edges" bool
		self.blocks = blocks # Each entry is composed of the block state id, shifted left by 12, and the relative block position in the chunk section (4 bits for x, z, and y, from left to right).

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_long(self.chunk_section_position)
		b.write_bool(self.suppress_light_updates)
		b.write_varint(len(self.blocks))
		for i in self.blocks:
			b.write_varlong(i)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		chunk_section_position = r.read_long()
		suppress_light_updates = r.read_bool()
		blocks = [r.read_varlong() for _ in range(r.read_varint())]
		return cls(chunk_section_position, suppress_light_updates, blocks)

@final
class PlaySelectAdvancementsTabS2C(Packet, id=0x40):
	def __init__(self,
		has_id: bool, # Boolean
		optional_identifier: str, # Identifier
	):
		self.has_id = has_id # Indicates if the next field is present.
		self.optional_identifier = optional_identifier # See below.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_bool(self.has_id)
		b.write_string(self.optional_identifier)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		has_id = r.read_bool()
		optional_identifier = r.read_string()
		return cls(has_id, optional_identifier)

@final
class PlayServerDataS2C(Packet, id=0x41):
	def __init__(self,
		has_motd: bool, # Boolean
		motd: dict | None, # Optional Chat
		has_icon: bool, # Boolean
		icon: str | None, # Optional String (32767)
		enforces_secure_chat: bool, # Boolean
	):
		self.has_motd = has_motd # 
		self.motd = motd # 
		self.has_icon = has_icon # 
		self.icon = icon # Icon PNG base64 String
		self.enforces_secure_chat = enforces_secure_chat # 

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_bool(self.has_motd)
		if self.has_motd:
			assert self.motd is not None
			b.write_json(self.motd)
		b.write_bool(self.has_icon)
		if self.has_icon:
			assert self.icon is not None
			b.write_string(self.icon)
		b.write_bool(self.enforces_secure_chat)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		has_motd = r.read_bool()
		motd = r.read_json() if has_motd else None
		has_icon = r.read_bool()
		icon = r.read_string() if has_icon else None
		enforces_secure_chat = r.read_bool()
		return cls(has_motd, motd, has_icon, icon, enforces_secure_chat)

@final
class PlaySetActionBarTextS2C(Packet, id=0x42):
	def __init__(self,
		action_bar_text: dict, # Chat
	):
		self.action_bar_text = action_bar_text # Displays a message above the hotbar (the same as position 2 in Player Chat Message.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_json(self.action_bar_text)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		action_bar_text = r.read_json()
		return cls(action_bar_text)

@final
class PlaySetBorderCenterS2C(Packet, id=0x43):
	def __init__(self,
		x: float, # Double
		z: float, # Double
	):
		self.x = x # 
		self.z = z # 

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_double(self.x)
		b.write_double(self.z)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		x = r.read_double()
		z = r.read_double()
		return cls(x, z)

@final
class PlaySetBorderLerpSizeS2C(Packet, id=0x44):
	def __init__(self,
		old_diameter: float, # Double
		new_diameter: float, # Double
		speed: int, # VarLong
	):
		self.old_diameter = old_diameter # Current length of a single side of the world border, in meters.
		self.new_diameter = new_diameter # Target length of a single side of the world border, in meters.
		self.speed = speed # Number of real-time milliseconds until New Diameter is reached. It appears that Notchian server does not sync world border speed to game ticks, so it gets out of sync with server lag. If the world border is not moving, this is set to 0.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_double(self.old_diameter)
		b.write_double(self.new_diameter)
		b.write_varlong(self.speed)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		old_diameter = r.read_double()
		new_diameter = r.read_double()
		speed = r.read_varlong()
		return cls(old_diameter, new_diameter, speed)

@final
class PlaySetBorderSizeS2C(Packet, id=0x45):
	def __init__(self,
		diameter: float, # Double
	):
		self.diameter = diameter # Length of a single side of the world border, in meters.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_double(self.diameter)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		diameter = r.read_double()
		return cls(diameter)

@final
class PlaySetBorderWarningDelayS2C(Packet, id=0x46):
	def __init__(self,
		warning_time: int, # VarInt
	):
		self.warning_time = warning_time # In seconds as set by /worldborder warning time.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_varint(self.warning_time)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		warning_time = r.read_varint()
		return cls(warning_time)

@final
class PlaySetBorderWarningDistanceS2C(Packet, id=0x47):
	def __init__(self,
		warning_blocks: int, # VarInt
	):
		self.warning_blocks = warning_blocks # In meters.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_varint(self.warning_blocks)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		warning_blocks = r.read_varint()
		return cls(warning_blocks)

@final
class PlaySetCameraS2C(Packet, id=0x48):
	def __init__(self,
		camera_id: int, # VarInt
	):
		self.camera_id = camera_id # ID of the entity to set the client's camera to.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_varint(self.camera_id)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		camera_id = r.read_varint()
		return cls(camera_id)

@final
class PlaySetHeldItemS2C(Packet, id=0x49):
	def __init__(self,
		slot: int, # Byte
	):
		self.slot = slot # The slot which the player has selected (0–8).

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_byte(self.slot)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		slot = r.read_byte()
		return cls(slot)

@final
class PlaySetCenterChunkS2C(Packet, id=0x4A):
	def __init__(self,
		chunk_x: int, # VarInt
		chunk_z: int, # VarInt
	):
		self.chunk_x = chunk_x # Chunk X coordinate of the player's position.
		self.chunk_z = chunk_z # Chunk Z coordinate of the player's position.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_varint(self.chunk_x)
		b.write_varint(self.chunk_z)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		chunk_x = r.read_varint()
		chunk_z = r.read_varint()
		return cls(chunk_x, chunk_z)

@final
class PlaySetRenderDistanceS2C(Packet, id=0x4B):
	def __init__(self,
		view_distance: int, # VarInt
	):
		self.view_distance = view_distance # Render distance (2-32).

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_varint(self.view_distance)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		view_distance = r.read_varint()
		return cls(view_distance)

@final
class PlaySetDefaultSpawnPositionS2C(Packet, id=0x4C):
	def __init__(self,
		location: tuple[int, int, int], # Position
		angle: float, # Float
	):
		self.location = location # Spawn location.
		self.angle = angle # The angle at which to respawn at.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_pos_1_14(self.location)
		b.write_float(self.angle)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		location = r.read_pos_1_14()
		angle = r.read_float()
		return cls(location, angle)

@final
class PlayDisplayObjectiveS2C(Packet, id=0x4D):
	def __init__(self,
		position: int, # Byte
		score_name: str, # String (16)
	):
		self.position = position # The position of the scoreboard. 0: list, 1: sidebar, 2: below name, 3 - 18: team specific sidebar, indexed as 3 + team color.
		self.score_name = score_name # The unique name for the scoreboard to be displayed.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_byte(self.position)
		b.write_string(self.score_name)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		position = r.read_byte()
		score_name = r.read_string()
		return cls(position, score_name)

@final
class PlaySetEntityMetadataS2C(Packet, id=0x4E):
	def __init__(self,
		entity_id: int, # VarInt
		metadata: EntityMetadata, # Entity Metadata
	):
		self.entity_id = entity_id # 
		self.metadata = metadata # 

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_varint(self.entity_id)
		self.metadata.to_bytes(b)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		entity_id = r.read_varint()
		metadata = EntityMetadata.parse_from(r)
		return cls(entity_id, metadata)

@final
class PlayLinkEntitiesS2C(Packet, id=0x4F):
	def __init__(self,
		attached_entity_id: int, # Int
		holding_entity_id: int, # Int
	):
		self.attached_entity_id = attached_entity_id # Attached entity's EID.
		self.holding_entity_id = holding_entity_id # ID of the entity holding the lead. Set to -1 to detach.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_int(self.attached_entity_id)
		b.write_int(self.holding_entity_id)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		attached_entity_id = r.read_int()
		holding_entity_id = r.read_int()
		return cls(attached_entity_id, holding_entity_id)

@final
class PlaySetEntityVelocityS2C(Packet, id=0x50):
	def __init__(self,
		entity_id: int, # VarInt
		velocity_x: int, # Short
		velocity_y: int, # Short
		velocity_z: int, # Short
	):
		self.entity_id = entity_id # 
		self.velocity_x = velocity_x # Velocity on the X axis.
		self.velocity_y = velocity_y # Velocity on the Y axis.
		self.velocity_z = velocity_z # Velocity on the Z axis.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_varint(self.entity_id)
		b.write_short(self.velocity_x)
		b.write_short(self.velocity_y)
		b.write_short(self.velocity_z)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		entity_id = r.read_varint()
		velocity_x = r.read_short()
		velocity_y = r.read_short()
		velocity_z = r.read_short()
		return cls(entity_id, velocity_x, velocity_y, velocity_z)

@final
class PlaySetEquipmentS2C(Packet, id=0x51):
	def __init__(self,
		entity_id: int, # VarInt
		equipments: list[
			tuple[
				int, # Slot; Byte Enum; Equipment slot. 0: main hand, 1: off hand, 2–5: armor slot (2: boots, 3: leggings, 4: chestplate, 5: helmet). Also has the top bit set if another entry follows, and otherwise unset if this is the last item in the array.
				Slot, # Item; Slot;
			]
		]
	):
		self.entity_id = entity_id
		self.equipments = equipments

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_varint(self.entity_id)
		for slot, item in self.equipments:
			b.write_byte(slot)
			item.to_bytes(b)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		entity_id = r.read_varint()
		equipments = []
		while r.remain > 0:
			slot = r.read_byte()
			item = Slot.parse_from(r)
			equipments.append((slot, item))
		return cls(entity_id, equipments)

@final
class PlaySetExperienceS2C(Packet, id=0x52):
	def __init__(self,
		experience_bar: float, # Float
		total_experience: int, # VarInt
		level: int, # VarInt
	):
		self.experience_bar = experience_bar # Between 0 and 1.
		self.total_experience = total_experience # See Experience#Leveling up on the Minecraft Wiki for Total Experience to Level conversion.
		self.level = level # 

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_float(self.experience_bar)
		b.write_varint(self.total_experience)
		b.write_varint(self.level)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		experience_bar = r.read_float()
		total_experience = r.read_varint()
		level = r.read_varint()
		return cls(experience_bar, total_experience, level)

@final
class PlaySetHealthS2C(Packet, id=0x53):
	def __init__(self,
		health: float, # Float
		food: int, # VarInt
		food_saturation: float, # Float
	):
		self.health = health # 0 or less = dead, 20 = full HP.
		self.food = food # 0–20.
		self.food_saturation = food_saturation # Seems to vary from 0.0 to 5.0 in integer increments.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_float(self.health)
		b.write_varint(self.food)
		b.write_float(self.food_saturation)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		health = r.read_float()
		food = r.read_varint()
		food_saturation = r.read_float()
		return cls(health, food, food_saturation)

@final
class PlayUpdateObjectivesS2C(Packet, id=0x54):
	def __init__(self,
		objective_name: str, # String (16)
		mode: int, # Byte
		objective_value: dict | None, # Optional Chat
		type: int | None, # Optional VarInt Enum
	):
		self.objective_name = objective_name # A unique name for the objective.
		self.mode = mode # 0 to create the scoreboard. 1 to remove the scoreboard. 2 to update the display text.
		self.objective_value = objective_value # Only if mode is 0 or 2. The text to be displayed for the score.
		self.type = type # Only if mode is 0 or 2. 0 = "integer", 1 = "hearts".

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_string(self.objective_name)
		b.write_byte(self.mode)
		if self.mode in (0, 2):
			assert self.objective_value is not None
			assert self.type is not None
			b.write_json(self.objective_value)
			b.write_varint(self.type)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		objective_name = r.read_string()
		mode = r.read_byte()
		if mode in (0, 2):
			objective_value = r.read_json()
			type = r.read_varint()
		else:
			objective_value = None
			type = None
		return cls(objective_name, mode, objective_value, type)

@final
class PlaySetPassengersS2C(Packet, id=0x55):
	def __init__(self,
		entity_id: int, # VarInt
		passengers: list[int], # Array of VarInt
	):
		self.entity_id = entity_id # Vehicle's EID.
		self.passengers = passengers # EIDs of entity's passengers.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_varint(self.entity_id)
		b.write_varint(len(self.passengers))
		for passenger in self.passengers:
			b.write_varint(passenger)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		entity_id = r.read_varint()
		passengers = []
		for _ in range(r.read_varint()):
			passenger = r.read_varint()
			passengers.append(passenger)
		return cls(entity_id, passengers)

@final
class PlayUpdateTeamsS2C(Packet, id=0x56):
	def __init__(self,
		team_name: str, # String (16)
		mode: int, # Byte
		team_display_name: dict | None, # Chat
		friendly_flags: int | None, # Byte
		name_tag_visibility: str | None, # String Enum (32)
		collision_rule: str | None, # String Enum (32)
		team_color: int | None, # VarInt Enum
		team_prefix: dict | None, # Chat
		team_suffix: dict | None, # Chat
		entities: list[str] | None, # Array of String (40)
	):
		self.team_name = team_name # A unique name for the team. (Shared with scoreboard).
		self.mode = mode # Determines the layout of the remaining packet.
		self.team_display_name = team_display_name #
		self.friendly_flags = friendly_flags # Bit mask. 0x01: Allow friendly fire, 0x02: can see invisible players on same team.
		self.name_tag_visibility = name_tag_visibility # always, hideForOtherTeams, hideForOwnTeam, never.
		self.collision_rule = collision_rule # always, pushOtherTeams, pushOwnTeam, never.
		self.team_color = team_color # Used to color the name of players on the team; see below.
		self.team_prefix = team_prefix # Displayed before the names of players that are part of this team.
		self.team_suffix = team_suffix # Displayed after the names of players that are part of this team.
		self.entities = entities # Identifiers for the entities in this team. For players, this is their username; for other entities, it is their UUID.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_string(self.team_name)
		b.write_byte(self.mode)
		if self.mode in (0, 2):
			assert self.team_display_name is not None
			assert self.friendly_flags is not None
			assert self.name_tag_visibility is not None
			assert self.collision_rule is not None
			assert self.team_color is not None
			assert self.team_prefix is not None
			assert self.team_suffix is not None
			b.write_json(self.team_display_name)
			b.write_byte(self.friendly_flags)
			b.write_string(self.name_tag_visibility)
			b.write_string(self.collision_rule)
			b.write_varint(self.team_color)
			b.write_json(self.team_prefix)
			b.write_json(self.team_suffix)
		if self.mode in (0, 3, 4):
			assert self.entities is not None
			b.write_varint(len(self.entities))
			for entity in self.entities:
				b.write_string(entity)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		team_name = r.read_string()
		mode = r.read_byte()
		if mode in (0, 2):
			team_display_name = r.read_json()
			friendly_flags = r.read_byte()
			name_tag_visibility = r.read_string()
			collision_rule = r.read_string()
			team_color = r.read_varint()
			team_prefix = r.read_json()
			team_suffix = r.read_json()
		else:
			team_display_name = None
			friendly_flags = None
			name_tag_visibility = None
			collision_rule = None
			team_color = None
			team_prefix = None
			team_suffix = None
		if mode in (0, 3, 4):
			entities = []
			for _ in range(r.read_varint()):
				entity = r.read_string()
				entities.append(entity)
		else:
			entities = None
		return cls(team_name, mode, team_display_name, friendly_flags, name_tag_visibility, collision_rule, team_color, team_prefix, team_suffix, entities)

@final
class PlayUpdateScoreS2C(Packet, id=0x57):
	def __init__(self,
		entity_name: str, # String (40)
		action: int, # VarInt Enum
		objective_name: str, # String (16)
		value: int | None, # Optional VarInt
	):
		self.entity_name = entity_name # The entity whose score this is.  For players, this is their username; for other entities, it is their UUID.
		self.action = action # 0 to create/update an item. 1 to remove an item.
		self.objective_name = objective_name # The name of the objective the score belongs to.
		self.value = value # The score to be displayed next to the entry. Only sent when Action does not equal 1.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_string(self.entity_name)
		b.write_varint(self.action)
		b.write_string(self.objective_name)
		if self.action != 1:
			assert self.value is not None
			b.write_varint(self.value)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		entity_name = r.read_string()
		action = r.read_varint()
		objective_name = r.read_string()
		value = r.read_varint() if action != 1 else None
		return cls(entity_name, action, objective_name, value)

@final
class PlaySetSimulationDistanceS2C(Packet, id=0x58):
	def __init__(self,
		simulation_distance: int, # VarInt
	):
		self.simulation_distance = simulation_distance # The distance that the client will process specific things, such as entities.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_varint(self.simulation_distance)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		simulation_distance = r.read_varint()
		return cls(simulation_distance)

@final
class PlaySetSubtitleTextS2C(Packet, id=0x59):
	def __init__(self,
		subtitle_text: dict, # Chat
	):
		self.subtitle_text = subtitle_text # 

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_json(self.subtitle_text)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		subtitle_text = r.read_json()
		return cls(subtitle_text)

@final
class PlayUpdateTimeS2C(Packet, id=0x5A):
	def __init__(self,
		world_age: int, # Long
		time_of_day: int, # Long
	):
		self.world_age = world_age # In ticks; not changed by server commands.
		self.time_of_day = time_of_day # The world (or region) time, in ticks. If negative the sun will stop moving at the Math.abs of the time.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_long(self.world_age)
		b.write_long(self.time_of_day)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		world_age = r.read_long()
		time_of_day = r.read_long()
		return cls(world_age, time_of_day)

@final
class PlaySetTitleTextS2C(Packet, id=0x5B):
	def __init__(self,
		title_text: dict, # Chat
	):
		self.title_text = title_text # 

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_json(self.title_text)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		title_text = r.read_json()
		return cls(title_text)

@final
class PlaySetTitleAnimationTimesS2C(Packet, id=0x5C):
	def __init__(self,
		fade_in: int, # Int
		stay: int, # Int
		fade_out: int, # Int
	):
		self.fade_in = fade_in # Ticks to spend fading in.
		self.stay = stay # Ticks to keep the title displayed.
		self.fade_out = fade_out # Ticks to spend fading out, not when to start fading out.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_int(self.fade_in)
		b.write_int(self.stay)
		b.write_int(self.fade_out)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		fade_in = r.read_int()
		stay = r.read_int()
		fade_out = r.read_int()
		return cls(fade_in, stay, fade_out)

@final
class PlayEntitySoundEffectS2C(Packet, id=0x5D):
	def __init__(self,
		sound_id: int, # VarInt
		sound_name: str | None, # Optional Identifier
		has_fixed_range: bool | None, # Optional Boolean
		range: float | None, # Optional Float
		sound_category: int, # VarInt Enum
		entity_id: int, # VarInt
		volume: float, # Float
		pitch: float, # Float
		seed: int, # Long
	):
		self.sound_id = sound_id # Represents the Sound ID + 1. If the value is 0, the packet contains a sound specified by Identifier.
		self.sound_name = sound_name # Only present if Sound ID is 0
		self.has_fixed_range = has_fixed_range # Only present if Sound ID is 0.
		self.range = range # The fixed range of the sound. Only present if previous boolean is true and Sound ID is 0.
		self.sound_category = sound_category # The category that this sound will be played from (current categories).
		self.entity_id = entity_id # 
		self.volume = volume # 1.0 is 100%, capped between 0.0 and 1.0 by Notchian clients.
		self.pitch = pitch # Float between 0.5 and 2.0 by Notchian clients.
		self.seed = seed # Seed used to pick sound variant.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_varint(self.sound_id)
		if self.sound_id == 0:
			assert self.sound_name is not None
			assert self.has_fixed_range is not None
			b.write_string(self.sound_name)
			b.write_bool(self.has_fixed_range)
			if self.has_fixed_range:
				assert self.range is not None
				b.write_float(self.range)
		b.write_varint(self.sound_category)
		b.write_varint(self.entity_id)
		b.write_float(self.volume)
		b.write_float(self.pitch)
		b.write_long(self.seed)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		sound_id = r.read_varint()
		if sound_id == 0:
			sound_name = r.read_string()
			has_fixed_range = r.read_bool()
			if has_fixed_range:
				range = r.read_float()
			else:
				range = None
		else:
			sound_name = None
			has_fixed_range = None
			range = None
		sound_category = r.read_varint()
		entity_id = r.read_varint()
		volume = r.read_float()
		pitch = r.read_float()
		seed = r.read_long()
		return cls(sound_id, sound_name, has_fixed_range, range, sound_category, entity_id, volume, pitch, seed)

@final
class PlaySoundEffectS2C(Packet, id=0x5E):
	def __init__(self,
		sound_id: int, # VarInt
		sound_name: str | None, # Optional Identifier
		has_fixed_range: bool | None, # Optional Boolean
		range: float | None, # Optional Float
		sound_category: int, # VarInt Enum
		effect_position_x: int, # Int
		effect_position_y: int, # Int
		effect_position_z: int, # Int
		volume: float, # Float
		pitch: float, # Float
		seed: int, # Long
	):
		self.sound_id = sound_id # Represents the Sound ID + 1. If the value is 0, the packet contains a sound specified by Identifier.
		self.sound_name = sound_name # Only present if Sound ID is 0
		self.has_fixed_range = has_fixed_range # Only present if Sound ID is 0.
		self.range = range # The fixed range of the sound. Only present if previous boolean is true and Sound ID is 0.
		self.sound_category = sound_category # The category that this sound will be played from (current categories).
		self.effect_position_x = effect_position_x # Effect X multiplied by 8 (fixed-point number with only 3 bits dedicated to the fractional part).
		self.effect_position_y = effect_position_y # Effect Y multiplied by 8 (fixed-point number with only 3 bits dedicated to the fractional part).
		self.effect_position_z = effect_position_z # Effect Z multiplied by 8 (fixed-point number with only 3 bits dedicated to the fractional part).
		self.volume = volume # 1.0 is 100%, capped between 0.0 and 1.0 by Notchian clients.
		self.pitch = pitch # Float between 0.5 and 2.0 by Notchian clients.
		self.seed = seed # Seed used to pick sound variant.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_varint(self.sound_id)
		if self.sound_id == 0:
			assert self.sound_name is not None
			assert self.has_fixed_range is not None
			b.write_string(self.sound_name)
			b.write_bool(self.has_fixed_range)
			if self.has_fixed_range:
				assert self.range is not None
				b.write_float(self.range)
		b.write_varint(self.sound_category)
		b.write_int(self.effect_position_x)
		b.write_int(self.effect_position_y)
		b.write_int(self.effect_position_z)
		b.write_float(self.volume)
		b.write_float(self.pitch)
		b.write_long(self.seed)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		sound_id = r.read_varint()
		if sound_id == 0:
			sound_name = r.read_string()
			has_fixed_range = r.read_bool()
			if has_fixed_range:
				range = r.read_float()
			else:
				range = None
		else:
			sound_name = None
			has_fixed_range = None
			range = None
		sound_category = r.read_varint()
		effect_position_x = r.read_int()
		effect_position_y = r.read_int()
		effect_position_z = r.read_int()
		volume = r.read_float()
		pitch = r.read_float()
		seed = r.read_long()
		return cls(sound_id, sound_name, has_fixed_range, range, sound_category, effect_position_x, effect_position_y, effect_position_z, volume, pitch, seed)

@final
class PlayStopSoundS2C(Packet, id=0x5F):
	def __init__(self,
		flags: int, # Byte
		source: int | None, # Optional VarInt Enum
		sound: str | None, # Optional Identifier
	):
		self.flags = flags # Controls which fields are present.
		self.source = source # Only if flags is 3 or 1 (bit mask 0x1). See below. If not present, then sounds from all sources are cleared.
		self.sound = sound # Only if flags is 2 or 3 (bit mask 0x2).  A sound effect name, see Custom Sound Effect. If not present, then all sounds are cleared.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_byte(self.flags)
		if self.flags & 0x1:
			assert self.source is not None
			b.write_varint(self.source)
		if self.flags & 0x2:
			assert self.sound is not None
			b.write_string(self.sound)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		flags = r.read_byte()
		source = r.read_varint() if flags & 0x1 else None
		sound = r.read_string() if flags & 0x2 else None
		return cls(flags, source, sound)

@final
class PlaySystemChatMessageS2C(Packet, id=0x60):
	def __init__(self,
		content: dict, # Chat
		overlay: bool, # Boolean
	):
		self.content = content # Limited to 262144 bytes.
		self.overlay = overlay # Whether the message is an actionbar or chat message.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_json(self.content)
		b.write_bool(self.overlay)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		content = r.read_json()
		overlay = r.read_bool()
		return cls(content, overlay)

@final
class PlaySetTabListHeaderAndFooterS2C(Packet, id=0x61):
	def __init__(self,
		header: dict, # Chat
		footer: dict, # Chat
	):
		self.header = header # To remove the header, send a empty text component: {"text":""}.
		self.footer = footer # To remove the footer, send a empty text component: {"text":""}.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_json(self.header)
		b.write_json(self.footer)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		header = r.read_json()
		footer = r.read_json()
		return cls(header, footer)

@final
class PlayTagQueryResponseS2C(Packet, id=0x62):
	def __init__(self,
		transaction_id: int, # VarInt
		nbt: NBT, # NBT Tag
	):
		self.transaction_id = transaction_id # Can be compared to the one sent in the original query packet.
		self.nbt = nbt # The NBT of the block or entity.  May be a TAG_END (0) in which case no NBT is present.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_varint(self.transaction_id)
		self.nbt.to_bytes(b)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		transaction_id = r.read_varint()
		nbt = NBT.parse_from(r)
		return cls(transaction_id, nbt)

@final
class PlayPickupItemS2C(Packet, id=0x63):
	def __init__(self,
		collected_entity_id: int, # VarInt
		collector_entity_id: int, # VarInt
		pickup_item_count: int, # VarInt
	):
		self.collected_entity_id = collected_entity_id # 
		self.collector_entity_id = collector_entity_id # 
		self.pickup_item_count = pickup_item_count # Seems to be 1 for XP orbs, otherwise the number of items in the stack.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_varint(self.collected_entity_id)
		b.write_varint(self.collector_entity_id)
		b.write_varint(self.pickup_item_count)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		collected_entity_id = r.read_varint()
		collector_entity_id = r.read_varint()
		pickup_item_count = r.read_varint()
		return cls(collected_entity_id, collector_entity_id, pickup_item_count)

@final
class PlayTeleportEntityS2C(Packet, id=0x64):
	def __init__(self,
		entity_id: int, # VarInt
		x: float, # Double
		y: float, # Double
		z: float, # Double
		yaw: int, # Angle
		pitch: int, # Angle
		on_ground: bool, # Boolean
	):
		self.entity_id = entity_id # 
		self.x = x # 
		self.y = y # 
		self.z = z # 
		self.yaw = yaw # (Y Rot)New angle, not a delta.
		self.pitch = pitch # (X Rot)New angle, not a delta.
		self.on_ground = on_ground # 

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_varint(self.entity_id)
		b.write_double(self.x)
		b.write_double(self.y)
		b.write_double(self.z)
		b.write_byte(self.yaw)
		b.write_byte(self.pitch)
		b.write_bool(self.on_ground)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		entity_id = r.read_varint()
		x = r.read_double()
		y = r.read_double()
		z = r.read_double()
		yaw = r.read_byte()
		pitch = r.read_byte()
		on_ground = r.read_bool()
		return cls(entity_id, x, y, z, yaw, pitch, on_ground)

@final
class PlayUpdateAdvancementsS2C(Packet, id=0x65):
	def __init__(self,
		reset_clear: bool, # Boolean
		advancement_mapping: dict[
			str, # Key; Identifier; The identifier of the advancement
			Advancement, # Value; Advancement;
		],
		identifiers: list[str], # Array of Identifier
		progress_mapping: dict[
			str, # Key; Identifier; The identifier of the advancement.
			AdvancementProgress, # Value; Advancement progress;
		]
	):
		self.reset_clear = reset_clear # Whether to reset/clear the current advancements.
		self.advancement_mapping = advancement_mapping # See above
		self.identifiers = identifiers # The identifiers of the advancements that should be removed.
		self.progress_mapping = progress_mapping # See above

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_bool(self.reset_clear)
		b.write_varint(len(self.advancement_mapping))
		for key, value in self.advancement_mapping.items():
			b.write_string(key)
			value.to_bytes(b)
		b.write_varint(len(self.identifiers))
		for identifier in self.identifiers:
			b.write_string(identifier)
		b.write_varint(len(self.progress_mapping))
		for key, progress in self.progress_mapping.items():
			b.write_string(key)
			progress.to_bytes(b)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		reset_clear = r.read_bool()
		advancement_mapping = {}
		for _ in range(r.read_varint()):
			key = r.read_string()
			value = Advancement.parse_from(r)
			advancement_mapping[key] = value
		identifiers = []
		for _ in range(r.read_varint()):
			identifier = r.read_string()
			identifiers.append(identifier)
		progress_mapping = {}
		for _ in range(r.read_varint()):
			key = r.read_string()
			progress = AdvancementProgress.parse_from(r)
			progress_mapping[key] = progress
		return cls(reset_clear, advancement_mapping, identifiers, progress_mapping)

@final
class PlayUpdateAttributesS2C(Packet, id=0x66):
	def __init__(self,
		entity_id: int, # VarInt
		properties: list[
			tuple[
				str, # Key; Identifier;
				float, # Value; Double;
				Modifier, # Modifiers; Array of Modifier Data; See Attribute#Modifiers. Modifier Data defined below.
			]
		]
	):
	 self.entity_id = entity_id
	 self.properties = properties

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_varint(self.entity_id)
		b.write_varint(len(self.properties))
		for key, value, modifier in self.properties:
			b.write_string(key)
			b.write_double(value)
			modifier.to_bytes(b)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		entity_id = r.read_varint()
		properties = []
		for _ in range(r.read_varint()):
			key = r.read_string()
			value = r.read_double()
			modifier = Modifier.parse_from(r)
			properties.append((key, value, modifier))
		return cls(entity_id, properties)

@final
class PlayFeatureFlagsS2C(Packet, id=0x67):
	def __init__(self,
		total_features: int, # VarInt
		feature_flags: list[str], # Identifier Array
	):
		self.total_features = total_features # Number of features that appear in the array below.
		self.feature_flags = feature_flags #

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_varint(self.total_features)
		b.write_varint(len(self.feature_flags))
		for feature_flag in self.feature_flags:
			b.write_string(feature_flag)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		total_features = r.read_varint()
		feature_flags = []
		for _ in range(r.read_varint()):
			feature_flag = r.read_string()
			feature_flags.append(feature_flag)
		return cls(total_features, feature_flags)

@final
class PlayEntityEffectS2C(Packet, id=0x68):
	def __init__(self,
		entity_id: int, # VarInt
		effect_id: int, # VarInt
		amplifier: int, # Byte
		duration: int, # VarInt
		flags: int, # Byte
		has_factor_data: bool, # Boolean
		factor_codec: NBT, # NBT Tag
	):
		self.entity_id = entity_id # 
		self.effect_id = effect_id # See this table.
		self.amplifier = amplifier # Notchian client displays effect level as Amplifier + 1.
		self.duration = duration # Duration in ticks.
		self.flags = flags # Bit field, see below.
		self.has_factor_data = has_factor_data # Used in DARKNESS effect
		self.factor_codec = factor_codec # See below

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_varint(self.entity_id)
		b.write_varint(self.effect_id)
		b.write_byte(self.amplifier)
		b.write_varint(self.duration)
		b.write_byte(self.flags)
		b.write_bool(self.has_factor_data)
		self.factor_codec.to_bytes(b)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		entity_id = r.read_varint()
		effect_id = r.read_varint()
		amplifier = r.read_byte()
		duration = r.read_varint()
		flags = r.read_byte()
		has_factor_data = r.read_bool()
		factor_codec = NBT.parse_from(r)
		return cls(entity_id, effect_id, amplifier, duration, flags, has_factor_data, factor_codec)

@final
class PlayUpdateRecipesS2C(Packet, id=0x69):
	def __init__(self,
		recipes: list[Recipe], # Array of Recipe
	):
		self.recipes = recipes

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_varint(len(self.recipes))
		for recipe in self.recipes:
			recipe.to_bytes(b)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		recipes = []
		for _ in range(r.read_varint()):
			recipe = Recipe.parse_from(r)
			recipes.append(recipe)
		return cls(recipes)

@final
class PlayUpdateTagsS2C(Packet, id=0x6A):
	def __init__(self,
		array_of_tags: list[
			tuple[
				str, # Tag type; Identifier; Tag identifier (Vanilla required tags are minecraft:block, minecraft:item, minecraft:fluid, minecraft:entity_type, and minecraft:game_event)
				list[Tag], # Array of Tag;
			]
		],
	):
		self.array_of_tags = array_of_tags

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_varint(len(self.array_of_tags))
		for tag_type, tags in self.array_of_tags:
			b.write_string(tag_type)
			b.write_varint(len(tags))
			for tag in tags:
				tag.to_bytes(b)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		array_of_tags = []
		for _ in range(r.read_varint()):
			tag_type = r.read_string()
			tags = []
			for _ in range(r.read_varint()):
				tag = Tag.parse_from(r)
				tags.append(tag)
			array_of_tags.append((tag_type, tags))
		return cls(array_of_tags)

@final
class PlayConfirmTeleportationC2S(Packet, id=0x00):
	def __init__(self,
		teleport_id: int, # VarInt
	):
		self.teleport_id = teleport_id # The ID given by the Synchronize Player Position packet.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_varint(self.teleport_id)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		teleport_id = r.read_varint()
		return cls(teleport_id)

@final
class PlayQueryBlockEntityTagC2S(Packet, id=0x01):
	def __init__(self,
		transaction_id: int, # VarInt
		location: tuple[int, int, int], # Position
	):
		self.transaction_id = transaction_id # An incremental ID so that the client can verify that the response matches.
		self.location = location # The location of the block to check.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_varint(self.transaction_id)
		b.write_pos_1_14(self.location)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		transaction_id = r.read_varint()
		location = r.read_pos_1_14()
		return cls(transaction_id, location)

@final
class PlayChangeDifficultyC2S(Packet, id=0x02):
	def __init__(self,
		new_difficulty: int, # Byte
	):
		self.new_difficulty = new_difficulty # 0: peaceful, 1: easy, 2: normal, 3: hard .

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_byte(self.new_difficulty)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		new_difficulty = r.read_byte()
		return cls(new_difficulty)

@final
class PlayMessageAcknowledgmentC2S(Packet, id=0x03):
	def __init__(self,
		message_count: int, # VarInt
	):
		self.message_count = message_count # 

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_varint(self.message_count)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		message_count = r.read_varint()
		return cls(message_count)

@final
class PlayChatCommandC2S(Packet, id=0x04):
	def __init__(self,
		command: str, # String (256)
		timestamp: int, # Long
		salt: int, # Long
		array_of_argument_signatures: list[
			tuple[
				str, # Argument name; String; The name of the argument that is signed by the following signature.
				bytes, # Signature; Byte Array; The signature that verifies the argument.
			]
		],
		message_count: int, # VarInt
		acknowledged: BitSet, # BitSet (20)
	):
		self.command = command # The command typed by the client.
		self.timestamp = timestamp # The timestamp that the command was executed.
		self.salt = salt # The salt for the following argument signatures.
		self.array_of_argument_signatures = array_of_argument_signatures #
		self.message_count = message_count # 
		self.acknowledged = acknowledged # 

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_string(self.command)
		b.write_long(self.timestamp)
		b.write_long(self.salt)
		b.write_varint(len(self.array_of_argument_signatures))
		for argument_name, signature in self.array_of_argument_signatures:
			assert len(signature) == 256
			b.write_string(argument_name)
			b.write(signature)
		b.write_varint(self.message_count)
		self.acknowledged.to_bytes(b)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		command = r.read_string()
		timestamp = r.read_long()
		salt = r.read_long()
		array_of_argument_signatures = []
		for _ in range(r.read_varint()):
			argument_name = r.read_string()
			signature = r.read(SIGNATURE_LENGTH)
			array_of_argument_signatures.append((argument_name, signature))
		message_count = r.read_varint()
		acknowledged = BitSet.parse_from(r)
		return cls(command, timestamp, salt, array_of_argument_signatures, message_count, acknowledged)

@final
class PlayChatMessageC2S(Packet, id=0x05):
	def __init__(self,
		message: str, # String (256 chars)
		timestamp: int, # Long
		salt: int, # Long
		has_signature: bool, # Boolean
		signature: bytes | None, # Optional Byte Array
		message_count: int, # VarInt
		acknowledged: BitSet, # BitSet (20)
	):
		self.message = message # 
		self.timestamp = timestamp # 
		self.salt = salt # The salt used to verify the signature hash.
		self.has_signature = has_signature # Whether the next field is present.
		self.signature = signature # The signature used to verify the chat message's authentication.
		self.message_count = message_count # 
		self.acknowledged = acknowledged # 

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_string(self.message)
		b.write_long(self.timestamp)
		b.write_long(self.salt)
		b.write_bool(self.has_signature)
		if self.has_signature:
			assert self.signature is not None
			assert len(self.signature) == 256
			b.write(self.signature)
		b.write_varint(self.message_count)
		self.acknowledged.to_bytes(b)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		message = r.read_string()
		timestamp = r.read_long()
		salt = r.read_long()
		has_signature = r.read_bool()
		signature = r.read(SIGNATURE_LENGTH) if has_signature else None
		message_count = r.read_varint()
		acknowledged = BitSet.parse_from(r)
		return cls(message, timestamp, salt, has_signature, signature, message_count, acknowledged)

@final
class PlayClientCommandC2S(Packet, id=0x06):
	def __init__(self,
		action_id: int, # VarInt Enum
	):
		self.action_id = action_id # See below

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_varint(self.action_id)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		action_id = r.read_varint()
		return cls(action_id)

@final
class PlayClientInformationC2S(Packet, id=0x07):
	def __init__(self,
		locale: str, # String (16)
		view_distance: int, # Byte
		chat_mode: int, # VarInt Enum
		chat_colors: bool, # Boolean
		displayed_skin_parts: int, # Unsigned Byte
		main_hand: int, # VarInt Enum
		enable_text_filtering: bool, # Boolean
		allow_server_listings: bool, # Boolean
	):
		self.locale = locale # e.g. en_GB.
		self.view_distance = view_distance # Client-side render distance, in chunks.
		self.chat_mode = chat_mode # 0: enabled, 1: commands only, 2: hidden.  See processing chat for more information.
		self.chat_colors = chat_colors # “Colors” multiplayer setting. Can the chat be colored?
		self.displayed_skin_parts = displayed_skin_parts # Bit mask, see below.
		self.main_hand = main_hand # 0: Left, 1: Right.
		self.enable_text_filtering = enable_text_filtering # Enables filtering of text on signs and written book titles. Currently always false (i.e. the filtering is disabled)
		self.allow_server_listings = allow_server_listings # Servers usually list online players, this option should let you not show up in that list.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_string(self.locale)
		b.write_byte(self.view_distance)
		b.write_varint(self.chat_mode)
		b.write_bool(self.chat_colors)
		b.write_ubyte(self.displayed_skin_parts)
		b.write_varint(self.main_hand)
		b.write_bool(self.enable_text_filtering)
		b.write_bool(self.allow_server_listings)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		locale = r.read_string()
		view_distance = r.read_byte()
		chat_mode = r.read_varint()
		chat_colors = r.read_bool()
		displayed_skin_parts = r.read_ubyte()
		main_hand = r.read_varint()
		enable_text_filtering = r.read_bool()
		allow_server_listings = r.read_bool()
		return cls(locale, view_distance, chat_mode, chat_colors, displayed_skin_parts, main_hand, enable_text_filtering, allow_server_listings)

@final
class PlayCommandSuggestionsRequestC2S(Packet, id=0x08):
	def __init__(self,
		transaction_id: int, # VarInt
		text: str, # String (32500)
	):
		self.transaction_id = transaction_id # The id of the transaction that the server will send back to the client in the response of this packet. Client generates this and increments it each time it sends another tab completion that doesn't get a response.
		self.text = text # All text behind the cursor without the / (e.g. to the left of the cursor in left-to-right languages like English).

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_varint(self.transaction_id)
		b.write_string(self.text)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		transaction_id = r.read_varint()
		text = r.read_string()
		return cls(transaction_id, text)

@final
class PlayClickContainerButtonC2S(Packet, id=0x09):
	def __init__(self,
		window_id: int, # Byte
		button_id: int, # Byte
	):
		self.window_id = window_id # The ID of the window sent by Open Screen.
		self.button_id = button_id # Meaning depends on window type; see below.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_byte(self.window_id)
		b.write_byte(self.button_id)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		window_id = r.read_byte()
		button_id = r.read_byte()
		return cls(window_id, button_id)

@final
class PlayClickContainerC2S(Packet, id=0x0A):
	def __init__(self,
		window_id: int, # Unsigned Byte
		state_id: int, # VarInt
		slot: int, # Short
		button: int, # Byte
		mode: int, # VarInt Enum
		array_of_slots: list[
			tuple[
				int, #  Slot Number; Short;
				Slot, # Slot Data; Slot;  New data for this slot
			]
		],
		carried_item: Slot, # Slot
	):
		self.window_id = window_id # The ID of the window which was clicked. 0 for player inventory.
		self.state_id = state_id # The last recieved State ID from either a Set Container Slot or a Set Container Content packet
		self.slot = slot # The clicked slot number, see below.
		self.button = button # The button used in the click, see below.
		self.mode = mode # Inventory operation mode, see below.
		self.array_of_slots = array_of_slots # 
		self.carried_item = carried_item # Item carried by the cursor. Has to be empty (item ID = -1) for drop mode, otherwise nothing will happen.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_ubyte(self.window_id)
		b.write_varint(self.state_id)
		b.write_short(self.slot)
		b.write_byte(self.button)
		b.write_varint(self.mode)
		b.write_varint(len(self.array_of_slots))
		for slot_number, slot_data in self.array_of_slots:
			b.write_short(slot_number)
			slot_data.to_bytes(b)
		self.carried_item.to_bytes(b)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		window_id = r.read_ubyte()
		state_id = r.read_varint()
		slot = r.read_short()
		button = r.read_byte()
		mode = r.read_varint()
		array_of_slots = []
		for _ in range(r.read_varint()):
			slot_number = r.read_short()
			slot_data = Slot.parse_from(r)
			array_of_slots.append((slot_number, slot_data))
		carried_item = Slot.parse_from(r)
		return cls(window_id, state_id, slot, button, mode, array_of_slots, carried_item)

@final
class PlayCloseContainerC2S(Packet, id=0x0B):
	def __init__(self,
		window_id: int, # Unsigned Byte
	):
		self.window_id = window_id # This is the ID of the window that was closed. 0 for player inventory.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_ubyte(self.window_id)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		window_id = r.read_ubyte()
		return cls(window_id)

@final
class PlayPluginMessageC2S(Packet, id=0x0C):
	def __init__(self,
		channel: str, # Identifier
		data: bytes, # Byte Array (32767)
	):
		self.channel = channel # Name of the plugin channel used to send the data.
		self.data = data # Any data, depending on the channel. minecraft: channels are documented here. The length of this array must be inferred from the packet length.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_string(self.channel)
		b.write(self.data)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		channel = r.read_string()
		data = r.read()
		return cls(channel, data)

@final
class PlayEditBookC2S(Packet, id=0x0D):
	def __init__(self,
		slot: int, # VarInt
		entries: list[list[str]], # Array of Strings (8192 chars)
		has_title: bool, # Boolean
		title: str | None, # Optional String (128 chars)
	):
		self.slot = slot # The hotbar slot where the written book is located
		self.entries = entries # Text from each page.
		self.has_title = has_title # If true, the next field is present.
		self.title = title # Title of book.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_varint(self.slot)
		b.write_varint(len(self.entries))
		for entry in self.entries:
			b.write_varint(len(entry))
			for e in entry:
				b.write_string(e)
		b.write_bool(self.has_title)
		if self.has_title:
			assert self.title is not None
			b.write_string(self.title)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		slot = r.read_varint()
		entries = []
		for _ in range(r.read_varint()):
			entry = []
			for _ in range(r.read_varint()):
				e = r.read_string()
				entry.append(e)
			entries.append(entry)
		has_title = r.read_bool()
		title = r.read_string() if has_title else None
		return cls(slot, entries, has_title, title)

@final
class PlayQueryEntityTagC2S(Packet, id=0x0E):
	def __init__(self,
		transaction_id: int, # VarInt
		entity_id: int, # VarInt
	):
		self.transaction_id = transaction_id # An incremental ID so that the client can verify that the response matches.
		self.entity_id = entity_id # The ID of the entity to query.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_varint(self.transaction_id)
		b.write_varint(self.entity_id)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		transaction_id = r.read_varint()
		entity_id = r.read_varint()
		return cls(transaction_id, entity_id)

@final
class PlayInteractC2S(Packet, id=0x0F):
	def __init__(self,
		entity_id: int, # VarInt
		type: int, # VarInt Enum
		target_x: float | None, # Optional Float
		target_y: float | None, # Optional Float
		target_z: float | None, # Optional Float
		hand: int | None, # Optional VarInt Enum
		sneaking: bool, # Boolean
	):
		self.entity_id = entity_id # The ID of the entity to interact.
		self.type = type # 0: interact, 1: attack, 2: interact at.
		self.target_x = target_x # Only if Type is interact at.
		self.target_y = target_y # Only if Type is interact at.
		self.target_z = target_z # Only if Type is interact at.
		self.hand = hand # Only if Type is interact or interact at; 0: main hand, 1: off hand.
		self.sneaking = sneaking # If the client is sneaking.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_varint(self.entity_id)
		b.write_varint(self.type)
		if self.type == 2:
			assert self.target_x is not None
			assert self.target_y is not None
			assert self.target_z is not None
			b.write_float(self.target_x)
			b.write_float(self.target_y)
			b.write_float(self.target_z)
		if self.type in (0, 2):
			assert self.hand is not None
			b.write_varint(self.hand)
		b.write_bool(self.sneaking)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		entity_id = r.read_varint()
		type = r.read_varint()
		if type == 2:
			target_x = r.read_float()
			target_y = r.read_float()
			target_z = r.read_float()
		else:
			target_x = None
			target_y = None
			target_z = None
		hand = r.read_varint() if type in (0, 2) else None
		sneaking = r.read_bool()
		return cls(entity_id, type, target_x, target_y, target_z, hand, sneaking)

@final
class PlayJigsawGenerateC2S(Packet, id=0x10):
	def __init__(self,
		location: tuple[int, int, int], # Position
		levels: int, # VarInt
		keep_jigsaws: bool, # Boolean
	):
		self.location = location # Block entity location.
		self.levels = levels # Value of the levels slider/max depth to generate.
		self.keep_jigsaws = keep_jigsaws # 

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_pos_1_14(self.location)
		b.write_varint(self.levels)
		b.write_bool(self.keep_jigsaws)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		location = r.read_pos_1_14()
		levels = r.read_varint()
		keep_jigsaws = r.read_bool()
		return cls(location, levels, keep_jigsaws)

@final
class PlayKeepAliveC2S(Packet, id=0x11):
	def __init__(self,
		keep_alive_id: int, # Long
	):
		self.keep_alive_id = keep_alive_id # 

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_long(self.keep_alive_id)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		keep_alive_id = r.read_long()
		return cls(keep_alive_id)

@final
class PlayLockDifficultyC2S(Packet, id=0x12):
	def __init__(self,
		locked: bool, # Boolean
	):
		self.locked = locked # 

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_bool(self.locked)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		locked = r.read_bool()
		return cls(locked)

@final
class PlaySetPlayerPositionC2S(Packet, id=0x13):
	def __init__(self,
		x: float, # Double
		feet_y: float, # Double
		z: float, # Double
		on_ground: bool, # Boolean
	):
		self.x = x # Absolute position.
		self.feet_y = feet_y # Absolute feet position, normally Head Y - 1.62.
		self.z = z # Absolute position.
		self.on_ground = on_ground # True if the client is on the ground, false otherwise.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_double(self.x)
		b.write_double(self.feet_y)
		b.write_double(self.z)
		b.write_bool(self.on_ground)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		x = r.read_double()
		feet_y = r.read_double()
		z = r.read_double()
		on_ground = r.read_bool()
		return cls(x, feet_y, z, on_ground)

@final
class PlaySetPlayerPositionandRotationC2S(Packet, id=0x14):
	def __init__(self,
		x: float, # Double
		feet_y: float, # Double
		z: float, # Double
		yaw: float, # Float
		pitch: float, # Float
		on_ground: bool, # Boolean
	):
		self.x = x # Absolute position.
		self.feet_y = feet_y # Absolute feet position, normally Head Y - 1.62.
		self.z = z # Absolute position.
		self.yaw = yaw # Absolute rotation on the X Axis, in degrees.
		self.pitch = pitch # Absolute rotation on the Y Axis, in degrees.
		self.on_ground = on_ground # True if the client is on the ground, false otherwise.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_double(self.x)
		b.write_double(self.feet_y)
		b.write_double(self.z)
		b.write_float(self.yaw)
		b.write_float(self.pitch)
		b.write_bool(self.on_ground)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		x = r.read_double()
		feet_y = r.read_double()
		z = r.read_double()
		yaw = r.read_float()
		pitch = r.read_float()
		on_ground = r.read_bool()
		return cls(x, feet_y, z, yaw, pitch, on_ground)

@final
class PlaySetPlayerRotationC2S(Packet, id=0x15):
	def __init__(self,
		yaw: float, # Float
		pitch: float, # Float
		on_ground: bool, # Boolean
	):
		self.yaw = yaw # Absolute rotation on the X Axis, in degrees.
		self.pitch = pitch # Absolute rotation on the Y Axis, in degrees.
		self.on_ground = on_ground # True if the client is on the ground, false otherwise.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_float(self.yaw)
		b.write_float(self.pitch)
		b.write_bool(self.on_ground)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		yaw = r.read_float()
		pitch = r.read_float()
		on_ground = r.read_bool()
		return cls(yaw, pitch, on_ground)

@final
class PlaySetPlayerOnGroundC2S(Packet, id=0x16):
	def __init__(self,
		on_ground: bool, # Boolean
	):
		self.on_ground = on_ground # True if the client is on the ground, false otherwise.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_bool(self.on_ground)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		on_ground = r.read_bool()
		return cls(on_ground)

@final
class PlayMoveVehicleC2S(Packet, id=0x17):
	def __init__(self,
		x: float, # Double
		y: float, # Double
		z: float, # Double
		yaw: float, # Float
		pitch: float, # Float
	):
		self.x = x # Absolute position (X coordinate).
		self.y = y # Absolute position (Y coordinate).
		self.z = z # Absolute position (Z coordinate).
		self.yaw = yaw # Absolute rotation on the vertical axis, in degrees.
		self.pitch = pitch # Absolute rotation on the horizontal axis, in degrees.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_double(self.x)
		b.write_double(self.y)
		b.write_double(self.z)
		b.write_float(self.yaw)
		b.write_float(self.pitch)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		x = r.read_double()
		y = r.read_double()
		z = r.read_double()
		yaw = r.read_float()
		pitch = r.read_float()
		return cls(x, y, z, yaw, pitch)

@final
class PlayPaddleBoatC2S(Packet, id=0x18):
	def __init__(self,
		left_paddle_turning: bool, # Boolean
		right_paddle_turning: bool, # Boolean
	):
		self.left_paddle_turning = left_paddle_turning # 
		self.right_paddle_turning = right_paddle_turning # 

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_bool(self.left_paddle_turning)
		b.write_bool(self.right_paddle_turning)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		left_paddle_turning = r.read_bool()
		right_paddle_turning = r.read_bool()
		return cls(left_paddle_turning, right_paddle_turning)

@final
class PlayPickItemC2S(Packet, id=0x19):
	def __init__(self,
		slot_to_use: int, # VarInt
	):
		self.slot_to_use = slot_to_use # See Inventory.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_varint(self.slot_to_use)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		slot_to_use = r.read_varint()
		return cls(slot_to_use)

@final
class PlayPlaceRecipeC2S(Packet, id=0x1A):
	def __init__(self,
		window_id: int, # Byte
		recipe: str, # Identifier
		make_all: bool, # Boolean
	):
		self.window_id = window_id # 
		self.recipe = recipe # A recipe ID.
		self.make_all = make_all # Affects the amount of items processed; true if shift is down when clicked.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_byte(self.window_id)
		b.write_string(self.recipe)
		b.write_bool(self.make_all)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		window_id = r.read_byte()
		recipe = r.read_string()
		make_all = r.read_bool()
		return cls(window_id, recipe, make_all)

@final
class PlayerAbilitiesC2S(Packet, id=0x1B):
	def __init__(self,
		flags: int, # Byte
	):
		self.flags = flags # Bit mask. 0x02: is flying.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_byte(self.flags)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		flags = r.read_byte()
		return cls(flags)

@final
class PlayerActionC2S(Packet, id=0x1C):
	def __init__(self,
		status: int, # VarInt Enum
		location: tuple[int, int, int], # Position
		face: int, # Byte Enum
		sequence: int, # VarInt
	):
		self.status = status # The action the player is taking against the block (see below).
		self.location = location # Block position.
		self.face = face # The face being hit (see below).
		self.sequence = sequence # 

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_varint(self.status)
		b.write_pos_1_14(self.location)
		b.write_byte(self.face)
		b.write_varint(self.sequence)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		status = r.read_varint()
		location = r.read_pos_1_14()
		face = r.read_byte()
		sequence = r.read_varint()
		return cls(status, location, face, sequence)

@final
class PlayerCommandC2S(Packet, id=0x1D):
	def __init__(self,
		entity_id: int, # VarInt
		action_id: int, # VarInt Enum
		jump_boost: int, # VarInt
	):
		self.entity_id = entity_id # Player ID
		self.action_id = action_id # The ID of the action, see below.
		self.jump_boost = jump_boost # Only used by the “start jump with horse” action, in which case it ranges from 0 to 100. In all other cases it is 0.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_varint(self.entity_id)
		b.write_varint(self.action_id)
		b.write_varint(self.jump_boost)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		entity_id = r.read_varint()
		action_id = r.read_varint()
		jump_boost = r.read_varint()
		return cls(entity_id, action_id, jump_boost)

@final
class PlayerInputC2S(Packet, id=0x1E):
	def __init__(self,
		sideways: float, # Float
		forward: float, # Float
		flags: int, # Unsigned Byte
	):
		self.sideways = sideways # Positive to the left of the player.
		self.forward = forward # Positive forward.
		self.flags = flags # Bit mask. 0x1: jump, 0x2: unmount.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_float(self.sideways)
		b.write_float(self.forward)
		b.write_ubyte(self.flags)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		sideways = r.read_float()
		forward = r.read_float()
		flags = r.read_ubyte()
		return cls(sideways, forward, flags)

@final
class PlayPongC2S(Packet, id=0x1F):
	def __init__(self,
		id: int, # Int
	):
		self.id = id # id is the same as the ping packet

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_int(self.id)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		id = r.read_int()
		return cls(id)

@final
class PlayerSessionC2S(Packet, id=0x20):
	def __init__(self,
		session_id: uuid.UUID, # UUID
		expires_at: int, # Long
		public_key: bytes, # Byte Array
		key_signature: bytes, # Byte Array
	):
		self.session_id = session_id # 
		self.expires_at = expires_at # The time the play session key expires in epoch milliseconds.
		self.public_key = public_key # A byte array of an X.509-encoded public key.
		self.key_signature = key_signature # The signature consists of the player UUID, the key expiration timestamp, and the public key data. These values are hashed using SHA-1 and signed using Mojang's private RSA key.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_uuid(self.session_id)
		b.write_long(self.expires_at)
		b.write_varint(len(self.public_key))
		b.write(self.public_key)
		b.write_varint(len(self.key_signature))
		b.write(self.key_signature)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		session_id = r.read_uuid()
		expires_at = r.read_long()
		public_key = r.read(r.read_varint())
		key_signature = r.read(r.read_varint())
		return cls(session_id, expires_at, public_key, key_signature)

@final
class PlayChangeRecipeBookSettingsC2S(Packet, id=0x21):
	def __init__(self,
		book_id: int, # VarInt Enum
		book_open: bool, # Boolean
		filter_active: bool, # Boolean
	):
		self.book_id = book_id # 0: crafting, 1: furnace, 2: blast furnace, 3: smoker.
		self.book_open = book_open # 
		self.filter_active = filter_active # 

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_varint(self.book_id)
		b.write_bool(self.book_open)
		b.write_bool(self.filter_active)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		book_id = r.read_varint()
		book_open = r.read_bool()
		filter_active = r.read_bool()
		return cls(book_id, book_open, filter_active)

@final
class PlaySetSeenRecipeC2S(Packet, id=0x22):
	def __init__(self,
		recipe_id: str, # Identifier
	):
		self.recipe_id = recipe_id # 

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_string(self.recipe_id)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		recipe_id = r.read_string()
		return cls(recipe_id)

@final
class PlayRenameItemC2S(Packet, id=0x23):
	def __init__(self,
		item_name: str, # String (32767)
	):
		self.item_name = item_name # The new name of the item.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_string(self.item_name)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		item_name = r.read_string()
		return cls(item_name)

@final
class PlayResourcePackC2S(Packet, id=0x24):
	def __init__(self,
		result: int, # VarInt Enum
	):
		self.result = result # 0: successfully loaded, 1: declined, 2: failed download, 3: accepted.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_varint(self.result)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		result = r.read_varint()
		return cls(result)

@final
class PlaySeenAdvancementsC2S(Packet, id=0x25):
	def __init__(self,
		action: int, # VarInt Enum
		tab_id: str | None, # Optional identifier
	):
		self.action = action # 0: Opened tab, 1: Closed screen.
		self.tab_id = tab_id # Only present if action is Opened tab.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_varint(self.action)
		if self.action == 0:
			assert self.tab_id is not None
			b.write_string(self.tab_id)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		action = r.read_varint()
		tab_id = r.read_string() if action == 0 else None
		return cls(action, tab_id)

@final
class PlaySelectTradeC2S(Packet, id=0x26):
	def __init__(self,
		selected_slot: int, # VarInt
	):
		self.selected_slot = selected_slot # The selected slot in the players current (trading) inventory. (Was a full Integer for the plugin message).

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_varint(self.selected_slot)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		selected_slot = r.read_varint()
		return cls(selected_slot)

@final
class PlaySetBeaconEffectC2S(Packet, id=0x27):
	def __init__(self,
		has_primary_effect: bool, # Boolean
		primary_effect: int, # VarInt
		has_secondary_effect: bool, # Boolean
		secondary_effect: int, # VarInt
	):
		self.has_primary_effect = has_primary_effect # The selected slot in the players current (trading) inventory. (Was a full Integer for the plugin message).
		self.primary_effect = primary_effect # A Potion ID. (Was a full Integer for the plugin message).
		self.has_secondary_effect = has_secondary_effect # 
		self.secondary_effect = secondary_effect # A Potion ID. (Was a full Integer for the plugin message).

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_bool(self.has_primary_effect)
		b.write_varint(self.primary_effect)
		b.write_bool(self.has_secondary_effect)
		b.write_varint(self.secondary_effect)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		has_primary_effect = r.read_bool()
		primary_effect = r.read_varint()
		has_secondary_effect = r.read_bool()
		secondary_effect = r.read_varint()
		return cls(has_primary_effect, primary_effect, has_secondary_effect, secondary_effect)

@final
class PlaySetHeldItemC2S(Packet, id=0x28):
	def __init__(self,
		slot: int, # Short
	):
		self.slot = slot # The slot which the player has selected (0–8).

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_short(self.slot)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		slot = r.read_short()
		return cls(slot)

@final
class PlayProgramCommandBlockC2S(Packet, id=0x29):
	def __init__(self,
		location: tuple[int, int, int], # Position
		command: str, # String (32767)
		mode: int, # VarInt Enum
		flags: int, # Byte
	):
		self.location = location # 
		self.command = command # 
		self.mode = mode # One of SEQUENCE (0), AUTO (1), or REDSTONE (2).
		self.flags = flags # 0x01: Track Output (if false, the output of the previous command will not be stored within the command block); 0x02: Is conditional; 0x04: Automatic.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_pos_1_14(self.location)
		b.write_string(self.command)
		b.write_varint(self.mode)
		b.write_byte(self.flags)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		location = r.read_pos_1_14()
		command = r.read_string()
		mode = r.read_varint()
		flags = r.read_byte()
		return cls(location, command, mode, flags)

@final
class PlayProgramCommandBlockMinecartC2S(Packet, id=0x2A):
	def __init__(self,
		entity_id: int, # VarInt
		command: str, # String (32767)
		track_output: bool, # Boolean
	):
		self.entity_id = entity_id # 
		self.command = command # 
		self.track_output = track_output # If false, the output of the previous command will not be stored within the command block.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_varint(self.entity_id)
		b.write_string(self.command)
		b.write_bool(self.track_output)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		entity_id = r.read_varint()
		command = r.read_string()
		track_output = r.read_bool()
		return cls(entity_id, command, track_output)

@final
class PlaySetCreativeModeSlotC2S(Packet, id=0x2B):
	def __init__(self,
		slot: int, # Short
		clicked_item: Slot, # Slot
	):
		self.slot = slot # Inventory slot.
		self.clicked_item = clicked_item # 

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_short(self.slot)
		self.clicked_item.to_bytes(b)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		slot = r.read_short()
		clicked_item = Slot.parse_from(r)
		return cls(slot, clicked_item)

@final
class PlayProgramJigsawBlockC2S(Packet, id=0x2C):
	def __init__(self,
		location: tuple[int, int, int], # Position
		name: str, # Identifier
		target: str, # Identifier
		pool: str, # Identifier
		final_state: str, # String (32767)
		joint_type: str, # String
	):
		self.location = location # Block entity location
		self.name = name # 
		self.target = target # 
		self.pool = pool # 
		self.final_state = final_state # "Turns into" on the GUI, final_state in NBT.
		self.joint_type = joint_type # rollable if the attached piece can be rotated, else aligned.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_pos_1_14(self.location)
		b.write_string(self.name)
		b.write_string(self.target)
		b.write_string(self.pool)
		b.write_string(self.final_state)
		b.write_string(self.joint_type)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		location = r.read_pos_1_14()
		name = r.read_string()
		target = r.read_string()
		pool = r.read_string()
		final_state = r.read_string()
		joint_type = r.read_string()
		return cls(location, name, target, pool, final_state, joint_type)

@final
class PlayProgramStructureBlockC2S(Packet, id=0x2D):
	def __init__(self,
		location: tuple[int, int, int], # Position
		action: int, # VarInt Enum
		mode: int, # VarInt Enum
		name: str, # String (32767)
		offset_x: int, # Byte
		offset_y: int, # Byte
		offset_z: int, # Byte
		size_x: int, # Byte
		size_y: int, # Byte
		size_z: int, # Byte
		mirror: int, # VarInt Enum
		rotation: int, # VarInt Enum
		metadata: str, # String (128)
		integrity: float, # Float
		seed: int, # VarLong
		flags: int, # Byte
	):
		self.location = location # Block entity location.
		self.action = action # An additional action to perform beyond simply saving the given data; see below.
		self.mode = mode # One of SAVE (0), LOAD (1), CORNER (2), DATA (3).
		self.name = name # 
		self.offset_x = offset_x # Between -32 and 32.
		self.offset_y = offset_y # Between -32 and 32.
		self.offset_z = offset_z # Between -32 and 32.
		self.size_x = size_x # Between 0 and 32.
		self.size_y = size_y # Between 0 and 32.
		self.size_z = size_z # Between 0 and 32.
		self.mirror = mirror # One of NONE (0), LEFT_RIGHT (1), FRONT_BACK (2).
		self.rotation = rotation # One of NONE (0), CLOCKWISE_90 (1), CLOCKWISE_180 (2), COUNTERCLOCKWISE_90 (3).
		self.metadata = metadata # 
		self.integrity = integrity # Between 0 and 1.
		self.seed = seed # 
		self.flags = flags # 0x01: Ignore entities; 0x02: Show air; 0x04: Show bounding box.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_pos_1_14(self.location)
		b.write_varint(self.action)
		b.write_varint(self.mode)
		b.write_string(self.name)
		b.write_byte(self.offset_x)
		b.write_byte(self.offset_y)
		b.write_byte(self.offset_z)
		b.write_byte(self.size_x)
		b.write_byte(self.size_y)
		b.write_byte(self.size_z)
		b.write_varint(self.mirror)
		b.write_varint(self.rotation)
		b.write_string(self.metadata)
		b.write_float(self.integrity)
		b.write_varlong(self.seed)
		b.write_byte(self.flags)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		location = r.read_pos_1_14()
		action = r.read_varint()
		mode = r.read_varint()
		name = r.read_string()
		offset_x = r.read_byte()
		offset_y = r.read_byte()
		offset_z = r.read_byte()
		size_x = r.read_byte()
		size_y = r.read_byte()
		size_z = r.read_byte()
		mirror = r.read_varint()
		rotation = r.read_varint()
		metadata = r.read_string()
		integrity = r.read_float()
		seed = r.read_varlong()
		flags = r.read_byte()
		return cls(location, action, mode, name, offset_x, offset_y, offset_z, size_x, size_y, size_z, mirror, rotation, metadata, integrity, seed, flags)

@final
class PlayUpdateSignC2S(Packet, id=0x2E):
	def __init__(self,
		location: tuple[int, int, int], # Position
		line_1: str, # String (384)
		line_2: str, # String (384)
		line_3: str, # String (384)
		line_4: str, # String (384)
	):
		self.location = location # Block Coordinates.
		self.line_1 = line_1 # First line of text in the sign.
		self.line_2 = line_2 # Second line of text in the sign.
		self.line_3 = line_3 # Third line of text in the sign.
		self.line_4 = line_4 # Fourth line of text in the sign.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_pos_1_14(self.location)
		b.write_string(self.line_1)
		b.write_string(self.line_2)
		b.write_string(self.line_3)
		b.write_string(self.line_4)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		location = r.read_pos_1_14()
		line_1 = r.read_string()
		line_2 = r.read_string()
		line_3 = r.read_string()
		line_4 = r.read_string()
		return cls(location, line_1, line_2, line_3, line_4)

@final
class PlaySwingArmC2S(Packet, id=0x2F):
	def __init__(self,
		hand: int, # VarInt Enum
	):
		self.hand = hand # Hand used for the animation. 0: main hand, 1: off hand.

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_varint(self.hand)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		hand = r.read_varint()
		return cls(hand)

@final
class PlayTeleportToEntityC2S(Packet, id=0x30):
	def __init__(self,
		target_player: uuid.UUID, # UUID
	):
		self.target_player = target_player # UUID of the player to teleport to (can also be an entity UUID).

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_uuid(self.target_player)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		target_player = r.read_uuid()
		return cls(target_player)

@final
class PlayUseItemOnC2S(Packet, id=0x31):
	def __init__(self,
		hand: int, # VarInt Enum
		location: tuple[int, int, int], # Position
		face: int, # VarInt Enum
		cursor_position_x: float, # Float
		cursor_position_y: float, # Float
		cursor_position_z: float, # Float
		inside_block: bool, # Boolean
		sequence: int, # VarInt
	):
		self.hand = hand # The hand from which the block is placed; 0: main hand, 1: off hand.
		self.location = location # Block position.
		self.face = face # The face on which the block is placed (as documented at Player Action).
		self.cursor_position_x = cursor_position_x # The position of the crosshair on the block, from 0 to 1 increasing from west to east.
		self.cursor_position_y = cursor_position_y # The position of the crosshair on the block, from 0 to 1 increasing from bottom to top.
		self.cursor_position_z = cursor_position_z # The position of the crosshair on the block, from 0 to 1 increasing from north to south.
		self.inside_block = inside_block # True when the player's head is inside of a block.
		self.sequence = sequence # 

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_varint(self.hand)
		b.write_pos_1_14(self.location)
		b.write_varint(self.face)
		b.write_float(self.cursor_position_x)
		b.write_float(self.cursor_position_y)
		b.write_float(self.cursor_position_z)
		b.write_bool(self.inside_block)
		b.write_varint(self.sequence)

@final
class PlayUseItemC2S(Packet, id=0x32):
	def __init__(self,
		hand: int, # VarInt Enum
		sequence: int, # VarInt
	):
		self.hand = hand # Hand used for the animation. 0: main hand, 1: off hand.
		self.sequence = sequence # 

	def to_bytes(self, b: PacketBuffer) -> None:
		b.write_varint(self.hand)
		b.write_varint(self.sequence)

	@classmethod
	def parse_from(cls, r: PacketReader) -> Self:
		hand = r.read_varint()
		sequence = r.read_varint()
		return cls(hand, sequence)

Packet.register(PacketRepo(762, # 1.19.4
	PacketStatusMap()
	.add(ConnStatus.HANDSHAKING, PacketIdMap()
		.add(HandshakingHandshakeC2S)
	)
	.add(ConnStatus.STATUS, PacketIdMap()
		.add(StatusRequestC2S)
		.add(StatusPingRequestC2S)
	)
	.add(ConnStatus.LOGIN, PacketIdMap()
		.add(LoginStartC2S)
		.add(LoginEncryptionResponseC2S)
		.add(LoginPluginResponseC2S)
	)
	.add(ConnStatus.PLAY, PacketIdMap()
		.add(PlayConfirmTeleportationC2S)
		.add(PlayQueryBlockEntityTagC2S)
		.add(PlayChangeDifficultyC2S)
		.add(PlayMessageAcknowledgmentC2S)
		.add(PlayChatCommandC2S)
		.add(PlayChatMessageC2S)
		.add(PlayClientCommandC2S)
		.add(PlayClientInformationC2S)
		.add(PlayCommandSuggestionsRequestC2S)
		.add(PlayClickContainerButtonC2S)
		.add(PlayClickContainerC2S)
		.add(PlayCloseContainerC2S)
		.add(PlayPluginMessageC2S)
		.add(PlayEditBookC2S)
		.add(PlayQueryEntityTagC2S)
		.add(PlayInteractC2S)
		.add(PlayJigsawGenerateC2S)
		.add(PlayKeepAliveC2S)
		.add(PlayLockDifficultyC2S)
		.add(PlaySetPlayerPositionC2S)
		.add(PlaySetPlayerPositionandRotationC2S)
		.add(PlaySetPlayerRotationC2S)
		.add(PlaySetPlayerOnGroundC2S)
		.add(PlayMoveVehicleC2S)
		.add(PlayPaddleBoatC2S)
		.add(PlayPickItemC2S)
		.add(PlayPlaceRecipeC2S)
		.add(PlayerAbilitiesC2S)
		.add(PlayerActionC2S)
		.add(PlayerCommandC2S)
		.add(PlayerInputC2S)
		.add(PlayPongC2S)
		.add(PlayerSessionC2S)
		.add(PlayChangeRecipeBookSettingsC2S)
		.add(PlaySetSeenRecipeC2S)
		.add(PlayRenameItemC2S)
		.add(PlayResourcePackC2S)
		.add(PlaySeenAdvancementsC2S)
		.add(PlaySelectTradeC2S)
		.add(PlaySetBeaconEffectC2S)
		.add(PlaySetHeldItemC2S)
		.add(PlayProgramCommandBlockC2S)
		.add(PlayProgramCommandBlockMinecartC2S)
		.add(PlaySetCreativeModeSlotC2S)
		.add(PlayProgramJigsawBlockC2S)
		.add(PlayProgramStructureBlockC2S)
		.add(PlayUpdateSignC2S)
		.add(PlaySwingArmC2S)
		.add(PlayTeleportToEntityC2S)
		.add(PlayUseItemOnC2S)
		.add(PlayUseItemC2S)
	)
	, PacketStatusMap()
	.add(ConnStatus.STATUS, PacketIdMap()
		.add(StatusResponseS2C)
		.add(StatusPingResponseS2C)
	)
	.add(ConnStatus.LOGIN, PacketIdMap()
		.add(LoginDisconnectS2C)
		.add(LoginEncryptionRequestS2C)
		.add(LoginSuccessS2C)
		.add(LoginSetCompressionS2C)
		.add(LoginPluginRequestS2C)
	)
	.add(ConnStatus.PLAY, PacketIdMap()
		.add(PlaySpawnEntityS2C)
		.add(PlaySpawnExperienceOrbS2C)
		.add(PlaySpawnPlayerS2C)
		.add(PlayEntityAnimationS2C)
		.add(PlayAwardStatisticsS2C)
		.add(PlayAcknowledgeBlockChangeS2C)
		.add(PlaySetBlockDestroyStageS2C)
		.add(PlayBlockEntityDataS2C)
		.add(PlayBlockActionS2C)
		.add(PlayBlockUpdateS2C)
		.add(PlayBossBarS2C)
		.add(PlayChangeDifficultyS2C)
		.add(PlayClearTitlesS2C)
		.add(PlayCommandSuggestionsResponseS2C)
		.add(PlayCommandsS2C)
		.add(PlayCloseContainerS2C)
		.add(PlaySetContainerContentS2C)
		.add(PlaySetContainerPropertyS2C)
		.add(PlaySetContainerSlotS2C)
		.add(PlaySetCooldownS2C)
		.add(PlayChatSuggestionsS2C)
		.add(PlayPluginMessageS2C)
		.add(PlayDeleteMessageS2C)
		.add(PlayDisconnectS2C)
		.add(PlayDisguisedChatMessageS2C)
		.add(PlayEntityEventS2C)
		.add(PlayExplosionS2C)
		.add(PlayUnloadChunkS2C)
		.add(PlayGameEventS2C)
		.add(PlayOpenHorseScreenS2C)
		.add(PlayInitializeWorldBorderS2C)
		.add(PlayKeepAliveS2C)
		.add(PlayChunkDataandUpdateLightS2C)
		.add(PlayWorldEventS2C)
		.add(PlayParticleS2C)
		.add(PlayUpdateLightS2C)
		.add(PlayLoginS2C)
		.add(PlayMapDataS2C)
		.add(PlayMerchantOffersS2C)
		.add(PlayUpdateEntityPositionS2C)
		.add(PlayUpdateEntityPositionandRotationS2C)
		.add(PlayUpdateEntityRotationS2C)
		.add(PlayMoveVehicleS2C)
		.add(PlayOpenBookS2C)
		.add(PlayOpenScreenS2C)
		.add(PlayOpenSignEditorS2C)
		.add(PlayPingS2C)
		.add(PlayPlaceGhostRecipeS2C)
		.add(PlayerAbilitiesS2C)
		.add(PlayEndCombatS2C)
		.add(PlayEnterCombatS2C)
		.add(PlayCombatDeathS2C)
		.add(PlayerInfoRemoveS2C)
		.add(PlayerInfoUpdateS2C)
		.add(PlayLookAtS2C)
		.add(PlaySynchronizePlayerPositionS2C)
		.add(PlayUpdateRecipeBookS2C)
		.add(PlayRemoveEntitiesS2C)
		.add(PlayRemoveEntityEffectS2C)
		.add(PlayResourcePackS2C)
		.add(PlayRespawnS2C)
		.add(PlaySetHeadRotationS2C)
		.add(PlayUpdateSectionBlocksS2C)
		.add(PlaySelectAdvancementsTabS2C)
		.add(PlayServerDataS2C)
		.add(PlaySetActionBarTextS2C)
		.add(PlaySetBorderCenterS2C)
		.add(PlaySetBorderLerpSizeS2C)
		.add(PlaySetBorderSizeS2C)
		.add(PlaySetBorderWarningDelayS2C)
		.add(PlaySetBorderWarningDistanceS2C)
		.add(PlaySetCameraS2C)
		.add(PlaySetHeldItemS2C)
		.add(PlaySetCenterChunkS2C)
		.add(PlaySetRenderDistanceS2C)
		.add(PlaySetDefaultSpawnPositionS2C)
		.add(PlayDisplayObjectiveS2C)
		.add(PlaySetEntityMetadataS2C)
		.add(PlayLinkEntitiesS2C)
		.add(PlaySetEntityVelocityS2C)
		.add(PlaySetEquipmentS2C)
		.add(PlaySetExperienceS2C)
		.add(PlaySetHealthS2C)
		.add(PlayUpdateObjectivesS2C)
		.add(PlaySetPassengersS2C)
		.add(PlayUpdateTeamsS2C)
		.add(PlayUpdateScoreS2C)
		.add(PlaySetSimulationDistanceS2C)
		.add(PlaySetSubtitleTextS2C)
		.add(PlayUpdateTimeS2C)
		.add(PlaySetTitleTextS2C)
		.add(PlaySetTitleAnimationTimesS2C)
		.add(PlayEntitySoundEffectS2C)
		.add(PlaySoundEffectS2C)
		.add(PlayStopSoundS2C)
		.add(PlaySystemChatMessageS2C)
		.add(PlaySetTabListHeaderAndFooterS2C)
		.add(PlayTagQueryResponseS2C)
		.add(PlayPickupItemS2C)
		.add(PlayTeleportEntityS2C)
		.add(PlayUpdateAdvancementsS2C)
		.add(PlayUpdateAttributesS2C)
		.add(PlayFeatureFlagsS2C)
		.add(PlayEntityEffectS2C)
		.add(PlayUpdateRecipesS2C)
		.add(PlayUpdateTagsS2C)
	)
))
