#!/usr/bin/env python3

import os
import requests
from bs4 import BeautifulSoup

targetURL = 'https://wiki.vg/index.php?title=Protocol&oldid={id}'

_wiki_type_map = {
	'BOOLEAN': 'bool',
	'BYTE': 'int',
	'UNSIGNED BYTE': 'int',
	'SHORT': 'int',
	'UNSIGNED SHORT': 'int',
	'INT': 'int',
	'LONG': 'int',
	'FLOAT': 'float',
	'DOUBLE': 'float',
	'STRING': 'str',
	'CHAT': 'dict',
	'IDENTIFIER': 'str',
	'VARINT': 'int',
	'VARLONG': 'int',
	'ENTITY METADATA': 'EntityMetadata',
	'SLOT': 'Slot',
	'NBT': 'NBT',
	'NBT TAG': 'NBT',
	'POSITION': 'tuple[int, int, int]',
	'ANGLE': 'int',
	'UUID': 'uuid.UUID',
	'BYTE ARRAY': 'bytes',
	'CHUNK': 'Chunk',
	'METADATA': 'Metadata',
	'BITSET': 'BitSet',
	'STRINGS': 'list[str]',
	'NBT TAG COMPOUND': 'Compound',
	'NODE': 'Node',

	'2048 BYTES': 'bytes[2048]',
}

_wiki_writter_map = {
	'BOOLEAN': '{w}.write_bool({e})',
	'BYTE': '{w}.write_byte({e})',
	'UNSIGNED BYTE': '{w}.write_ubyte({e})',
	'SHORT': '{w}.write_short({e})',
	'UNSIGNED SHORT': '{w}.write_ushort({e})',
	'INT': '{w}.write_int({e})',
	'LONG': '{w}.write_long({e})',
	'FLOAT': '{w}.write_float({e})',
	'DOUBLE': '{w}.write_double({e})',
	'STRING': '{w}.write_string({e})',
	'CHAT': '{w}.write_json({e})',
	'IDENTIFIER': '{w}.write_string({e})',
	'VARINT': '{w}.write_varint({e})',
	'VARLONG': '{w}.write_varlong({e})',
	'ENTITY METADATA': '{e}.to_bytes({w})',
	'SLOT': '{e}.to_bytes({w})',
	'NBT': '{e}.to_bytes({w})',
	'NBT TAG': '{e}.to_bytes({w})',
	'POSITION': '{w}.write_pos({e})',
	'ANGLE': '{w}.write_byte({e})',
	'UUID': '{w}.write_uuid({e})',
	'BYTE ARRAY': '{w}.write({e})',
	'CHUNK': '{e}.to_bytes({w})',
	'METADATA': '{e}.to_bytes({w})',
	'BITSET': '{e}.to_bytes({w})',
	'STRINGS': '{w}.write_todo_strings({e})',
	'NBT TAG COMPOUND': '{e}.to_bytes({w})',
	'NODE': '{e}.to_bytes({w})',

	'2048 BYTES': 'w.write({e})',
}
_wiki_reader_map = {
	'BOOLEAN': '{}.read_bool()',
	'BYTE': '{}.read_byte()',
	'UNSIGNED BYTE': '{}.read_ubyte()',
	'SHORT': '{}.read_short()',
	'UNSIGNED SHORT': '{}.read_ushort()',
	'INT': '{}.read_int()',
	'LONG': '{}.read_long()',
	'FLOAT': '{}.read_float()',
	'DOUBLE': '{}.read_double()',
	'STRING': '{}.read_string()',
	'CHAT': '{}.read_json()',
	'IDENTIFIER': '{}.read_string()',
	'VARINT': '{}.read_varint()',
	'VARLONG': '{}.read_varlong()',
	'ENTITY METADATA': 'EntityMetadata.parse_from({})',
	'SLOT': 'Slot.parse_from({})',
	'NBT': 'NBT.parse({})',
	'NBT TAG': 'NBT.parse({})',
	'POSITION': '{}.read_pos()',
	'ANGLE': '{}.read_byte()',
	'UUID': '{}.read_uuid()',
	'BYTE ARRAY': '{}.read_todo_byte_array()',
	'CHUNK': 'Chunk.parse_from({})',
	'METADATA': 'Metadata.{}',
	'BITSET': 'BitSet.parse_from({})',
	'STRINGS': '{}.read_todo_strings()',
	'NBT TAG COMPOUND': 'Compound.parse_from({}); assert isinstance(, Compound)',
	'NODE': 'Node.parse_from({})',

	'2048 BYTES': '{}.read(2048)',
}

def wiki_type_to_python(typ: str) -> str:
	typ = typ.upper()
	optional = typ.startswith('OPTIONAL ')
	if optional:
		typ = typ[len('OPTIONAL '):]
	array_of = typ.startswith('ARRAY OF ')
	if array_of:
		typ = typ[len('ARRAY OF '):]
	if typ.endswith(' ENUM'):
		typ = typ[:-len(' ENUM')]
	if typ.endswith(')'):
		typ = typ[:typ.index('(') - 1]
	t = _wiki_type_map.get(typ, None)
	if t is None:
		raise RuntimeError(f'Unknown wiki type {repr(typ)}')
	if array_of:
		t = 'list[{}]'.format(t)
	if optional:
		t += ' | None'
	return t

def wiki_type_to_writter(typ: str, w: str, e: str) -> str:
	typ = typ.upper()
	optional = typ.startswith('OPTIONAL ')
	if optional:
		typ = typ[len('OPTIONAL '):]
	array_of = typ.startswith('ARRAY OF ')
	if array_of:
		typ = typ[len('ARRAY OF '):]
	if typ.endswith(' ENUM'):
		typ = typ[:-len(' ENUM')]
	if typ.endswith(')'):
		typ = typ[:typ.index('(') - 1]
	t = _wiki_writter_map.get(typ, None)
	if t is None:
		raise RuntimeError(f'Unknown wiki type {repr(typ)}')
	if array_of:
		t += '_todo_arr'
	if optional:
		t += '_todo_opt'
	t = t.format(w=w, e=e)
	return t

def wiki_type_to_reader(typ: str, r: str) -> str:
	typ = typ.upper()
	optional = typ.startswith('OPTIONAL ')
	if optional:
		typ = typ[len('OPTIONAL '):]
	array_of = typ.startswith('ARRAY OF ')
	if array_of:
		typ = typ[len('ARRAY OF '):]
	if typ.endswith(' ENUM'):
		typ = typ[:-len(' ENUM')]
	if typ.endswith(')'):
		typ = typ[:typ.index('(') - 1]
	t = _wiki_reader_map.get(typ, None)
	if t is None:
		raise RuntimeError(f'Unknown wiki type {repr(typ)}')
	if array_of:
		t += '_todo_arr'
	if optional:
		t += '_todo_opt'
	t = t.format(r)
	return t

def generate(target: str, id, fd):
	target = target.format(id=id)
	fd.write(f'# Generate from <{target}>\n\n')
	chpt = f'.cache/wiki_{id}.html'
	content: bytes
	if os.path.exists(chpt):
		print('-> Cached', chpt)
		with open(chpt, 'rb') as ch:
			content = ch.read()
	else:
		print('-> Getting', target)
		res = requests.get(target)
		content = res.content
		with open(chpt, 'wb') as ch:
			ch.write(content)
	bs = BeautifulSoup(content, features="html5lib")
	tables = bs.select('.mw-parser-output>table.wikitable')

	classnames = []
	states_s2c = {}
	states_c2s = {}

	for tb in tables:
		trs = tb.select('tr')
		thead = [th.get_text().strip().upper() for th in trs[0].find_all('th')]
		if len(thead) < 6:
			continue
		hasSector = thead[3] == 'SECTOR'
		if hasSector:
			thead.pop(3)
		if thead != ['PACKET ID', 'STATE', 'BOUND TO', 'FIELD NAME', 'FIELD TYPE', 'NOTES']:
			continue
		pktname: str | None = None
		ps = tb.previous_sibling
		while ps is not None:
			if pktname is None and ps.name == 'h4' :
				pktname = ps.get_text().strip().replace(' ', '')
				break
			ps = ps.previous_sibling
		if ps is None:
			continue

		try:
			hd = [td.get_text().strip() for td in trs[1].find_all('td')]
			if hasSector:
				hd.pop(3)
			pid, state, bound = hd[0:3]
			classname = pktname + ("S2C" if bound.upper() == "CLIENT" else "C2S")
			if not classname.startswith(state):
				classname = state + classname
			classnames.append(classname)

			if bound.upper() == "CLIENT":
				if state in states_s2c:
					states_s2c[state].append((classname, pid))
				else:
					states_s2c[state] = [(classname, pid)]
			else:
				if state in states_c2s:
					states_c2s[state].append((classname, pid))
				else:
					states_c2s[state] = [(classname, pid)]
			fd.write('@final\n')
			fd.write(f'class {classname}(Packet):\n')

			if hasSector:
				raise RuntimeError('TODO: Has sector')

			fields = []
			if len(hd) > 3:
				name, typ, note = hd[3:]
				fields.append((name.replace(' ', '_').replace('-', '_').lower(), typ, note))
			for tr in trs[2:]:
				tds = [td.get_text().strip() for td in tr.find_all('td')]
				if len(tds) == 0:
					continue
				elif len(tds) == 2:
					name, typ = tds
					note = ''
				elif len(tds) == 3:
					name, typ, note = tds
				elif len(tds) == 4:
					name1, name2, typ, note = tds
					name = name1 + ':' + name2
				else:
					name1, name2, typ1, typ2, note = tds
					name = name1 + ':' + name2
					typ = typ1 + ' OF ' + typ2
				fields.append((name.replace(' ', '_').replace('-', '_').lower(), typ, note))
			fd.write('\tdef __init__(self,\n')
			for name, typ, note in fields:
				fd.write(f'\t\t{name}: {wiki_type_to_python(typ)}, # {typ}\n')
			fd.write('\t):\n')
			for name, typ, note in fields:
				fd.write(f'\t\tself.{name} = {name} # {note}\n')
			fd.write('\n')
			fd.write('\tdef to_bytes(self, b: PacketBuffer) -> None:\n')
			for name, typ, _ in fields:
				fd.write(f'\t\t{wiki_type_to_writter(typ, "b", f"self.{name}")}\n')
			fd.write('\n')
			fd.write('\t@classmethod\n')
			fd.write('\tdef parse_from(cls, r: PacketReader) -> Self:\n')
			for name, typ, _ in fields:
				fd.write(f'\t\t{name} = {wiki_type_to_reader(typ, "r")}\n')
			fd.write('\t\treturn cls(' + ', '.join(name for name, _, _ in fields) + ')\n')
		except Exception as e:
			fd.write('\t# ' + '=' * 16 + 'ERROR' + '=' * 16 + '\n')
			fd.write('\t# ' + str(e) + '\n')
			fd.write('\t# ' + str(tb)
				.replace('<table class="wikitable">', '')
				.replace('</table>', '')
				.replace('<tbody>', '')
				.replace('</tbody>', '')
				.replace('<tr>', '')
				.replace('</tr>', '\n')
				.replace('\n<td>', ' ')
				.replace('\n<td', '<td')
				.replace('\n</td>', ' ;')
				.replace('\n<th>', ' ')
				.replace('\n</th>', ' |')
				.replace('\n', '\n\t# ')
			)
			fd.write('\n')
		fd.write('\n')
	fd.write('\n')
	fd.write('__all__ = [\n')
	for classname in classnames:
		fd.write(f"\t'{classname}',\n")
	fd.write(']\n\n')
	fd.write('Packet.register(PacketRepo($TODO_protocol,\n')
	fd.write('\tPacketStatusMap()\n')
	for state, pkts in states_c2s.items():
		fd.write(f'\t.add(ConnStatus.{state.upper()}, PacketIdMap()\n')
		for p, d in pkts:
			fd.write(f'\t\t.add({p}, {d})\n')
		fd.write('\t)\n')
	fd.write('\t, PacketStatusMap()\n')
	for state, pkts in states_s2c.items():
		fd.write(f'\t.add(ConnStatus.{state.upper()}, PacketIdMap()\n')
		for p, d in pkts:
			fd.write(f'\t\t.add({p}, {d})\n')
		fd.write('\t)\n')
	fd.write('))\n')

def main():
	versions: list = [
		# ('1_8', 7368),
		# ('1_9', 7959),
		# ('1_10', 8235),
		# ('1_11', 8543),
		# ('1_12', 14204),
		# ('1_13', 14889),
		# ('1_14', 15346),
		# ('1_15', 16067),
		# ('1_16', 16681),
		# ('1_17', 16918),
		('1_18', 17499),
		('1_19', ''),
	]
	if not os.path.exists('.cache'):
		os.mkdir('.cache')
	if not os.path.exists('.generated'):
		os.mkdir('.generated')
	for v, p in versions:
		with open(f'./.generated/packet_{v}.py', 'w') as fd:
			generate(targetURL, p, fd)

if __name__ == '__main__':
	main()

