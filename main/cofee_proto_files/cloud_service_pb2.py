# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cloud_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='cloud_service.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x13\x63loud_service.proto\"\x1a\n\tfog_label\x12\r\n\x05label\x18\x01 \x01(\x05\":\n\x0c\x66og_metadata\x12\x0e\n\x06\x66og_ip\x18\x01 \x01(\t\x12\x1a\n\x06labels\x18\x02 \x03(\x0b\x32\n.fog_label\"(\n\nfog_labels\x12\x1a\n\x06labels\x18\x01 \x03(\x0b\x32\n.fog_label\"&\n\x14\x66og_spatial_locality\x12\x0e\n\x06\x66og_ip\x18\x01 \x01(\t\"Z\n\x1e\x66og_info_spatial_locality_list\x12\x38\n\x19\x66og_info_spatial_locality\x18\x01 \x03(\x0b\x32\x15.fog_spatial_locality\"\xe4\x01\n\x0bopen_filter\x12\r\n\x05nwlat\x18\x01 \x01(\x02\x12\x0e\n\x06nwlong\x18\x02 \x01(\x02\x12\r\n\x05selat\x18\x03 \x01(\x02\x12\x0e\n\x06selong\x18\x04 \x01(\x02\x12\x11\n\tstartTime\x18\x05 \x01(\x05\x12\x0f\n\x07\x65ndTime\x18\x06 \x01(\x05\x12;\n\x10namevalue_filter\x18\x07 \x03(\x0b\x32!.open_filter.NamevalueFilterEntry\x1a\x36\n\x14NamevalueFilterEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"e\n\x19\x64\x61g_filter_deadline_input\x12\x18\n\x10JSON_PATH_TO_DAG\x18\x01 \x01(\t\x12\x10\n\x08\x64\x65\x61\x64line\x18\x02 \x01(\x05\x12\x1c\n\x06\x66ilter\x18\x03 \x01(\x0b\x32\x0c.open_filter\"^\n\nfree_slots\x12#\n\x04slot\x18\x01 \x03(\x0b\x32\x15.free_slots.SlotEntry\x1a+\n\tSlotEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\"\x9f\x01\n\x17\x66og_sequence_free_slots\x12\x42\n\x0e\x66ree_slot_list\x18\x01 \x03(\x0b\x32*.fog_sequence_free_slots.FreeSlotListEntry\x1a@\n\x11\x46reeSlotListEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\x1a\n\x05value\x18\x02 \x01(\x0b\x32\x0b.free_slots:\x02\x38\x01\"X\n\x1b\x66og_sequence_free_slot_list\x12\x39\n\x17\x66og_sequence_free_slots\x18\x01 \x03(\x0b\x32\x18.fog_sequence_free_slots\"\x14\n\x05\x45mpty\x12\x0b\n\x03\x61\x63k\x18\x01 \x01(\x05\"F\n\x0ctask_details\x12\x11\n\ttask_name\x18\x01 \x01(\t\x12\x0f\n\x07task_id\x18\x02 \x01(\x05\x12\x12\n\nslack_time\x18\x03 \x01(\x05\"f\n\x1ctask_and_open_filter_details\x12!\n\x0bopen_filter\x18\x01 \x01(\x0b\x32\x0c.open_filter\x12#\n\x0ctask_details\x18\x02 \x01(\x0b\x32\r.task_details\"@\n\x0c\x62id_metadata\x12\x0b\n\x03\x62id\x18\x01 \x01(\x05\x12\x0c\n\x04\x63ost\x18\x02 \x01(\x05\x12\x15\n\rmicrobatch_id\x18\x03 \x01(\x05\"\x1d\n\x06result\x12\x13\n\x0b\x62ool_status\x18\x01 \x01(\x05\x32\xc8\x02\n\x05\x63loud\x12%\n\x0cregister_fog\x12\r.fog_metadata\x1a\x06.Empty\x12.\n\x10request_fog_list\x12\x0b.fog_labels\x1a\r.fog_metadata\x12/\n\tdag_input\x12\x1a.dag_filter_deadline_input\x1a\x06.Empty\x12\x33\n\x0bheap_update\x12\x1c.fog_sequence_free_slot_list\x1a\x06.Empty\x12\"\n\ttask_done\x12\r.task_details\x1a\x06.Empty\x12$\n\x0btask_undone\x12\r.task_details\x1a\x06.Empty\x12\x38\n\x1e\x62id_for_task_on_new_microbatch\x12\r.bid_metadata\x1a\x07.resultb\x06proto3')
)




_FOG_LABEL = _descriptor.Descriptor(
  name='fog_label',
  full_name='fog_label',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='label', full_name='fog_label.label', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=23,
  serialized_end=49,
)


_FOG_METADATA = _descriptor.Descriptor(
  name='fog_metadata',
  full_name='fog_metadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fog_ip', full_name='fog_metadata.fog_ip', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='labels', full_name='fog_metadata.labels', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=51,
  serialized_end=109,
)


_FOG_LABELS = _descriptor.Descriptor(
  name='fog_labels',
  full_name='fog_labels',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='labels', full_name='fog_labels.labels', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=111,
  serialized_end=151,
)


_FOG_SPATIAL_LOCALITY = _descriptor.Descriptor(
  name='fog_spatial_locality',
  full_name='fog_spatial_locality',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fog_ip', full_name='fog_spatial_locality.fog_ip', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=153,
  serialized_end=191,
)


_FOG_INFO_SPATIAL_LOCALITY_LIST = _descriptor.Descriptor(
  name='fog_info_spatial_locality_list',
  full_name='fog_info_spatial_locality_list',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fog_info_spatial_locality', full_name='fog_info_spatial_locality_list.fog_info_spatial_locality', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=193,
  serialized_end=283,
)


_OPEN_FILTER_NAMEVALUEFILTERENTRY = _descriptor.Descriptor(
  name='NamevalueFilterEntry',
  full_name='open_filter.NamevalueFilterEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='open_filter.NamevalueFilterEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='open_filter.NamevalueFilterEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=460,
  serialized_end=514,
)

_OPEN_FILTER = _descriptor.Descriptor(
  name='open_filter',
  full_name='open_filter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nwlat', full_name='open_filter.nwlat', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nwlong', full_name='open_filter.nwlong', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='selat', full_name='open_filter.selat', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='selong', full_name='open_filter.selong', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='startTime', full_name='open_filter.startTime', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='endTime', full_name='open_filter.endTime', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='namevalue_filter', full_name='open_filter.namevalue_filter', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_OPEN_FILTER_NAMEVALUEFILTERENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=286,
  serialized_end=514,
)


_DAG_FILTER_DEADLINE_INPUT = _descriptor.Descriptor(
  name='dag_filter_deadline_input',
  full_name='dag_filter_deadline_input',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='JSON_PATH_TO_DAG', full_name='dag_filter_deadline_input.JSON_PATH_TO_DAG', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deadline', full_name='dag_filter_deadline_input.deadline', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filter', full_name='dag_filter_deadline_input.filter', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=516,
  serialized_end=617,
)


_FREE_SLOTS_SLOTENTRY = _descriptor.Descriptor(
  name='SlotEntry',
  full_name='free_slots.SlotEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='free_slots.SlotEntry.key', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='free_slots.SlotEntry.value', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=670,
  serialized_end=713,
)

_FREE_SLOTS = _descriptor.Descriptor(
  name='free_slots',
  full_name='free_slots',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='slot', full_name='free_slots.slot', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_FREE_SLOTS_SLOTENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=619,
  serialized_end=713,
)


_FOG_SEQUENCE_FREE_SLOTS_FREESLOTLISTENTRY = _descriptor.Descriptor(
  name='FreeSlotListEntry',
  full_name='fog_sequence_free_slots.FreeSlotListEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='fog_sequence_free_slots.FreeSlotListEntry.key', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='fog_sequence_free_slots.FreeSlotListEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=811,
  serialized_end=875,
)

_FOG_SEQUENCE_FREE_SLOTS = _descriptor.Descriptor(
  name='fog_sequence_free_slots',
  full_name='fog_sequence_free_slots',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='free_slot_list', full_name='fog_sequence_free_slots.free_slot_list', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_FOG_SEQUENCE_FREE_SLOTS_FREESLOTLISTENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=716,
  serialized_end=875,
)


_FOG_SEQUENCE_FREE_SLOT_LIST = _descriptor.Descriptor(
  name='fog_sequence_free_slot_list',
  full_name='fog_sequence_free_slot_list',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fog_sequence_free_slots', full_name='fog_sequence_free_slot_list.fog_sequence_free_slots', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=877,
  serialized_end=965,
)


_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ack', full_name='Empty.ack', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=967,
  serialized_end=987,
)


_TASK_DETAILS = _descriptor.Descriptor(
  name='task_details',
  full_name='task_details',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='task_name', full_name='task_details.task_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='task_id', full_name='task_details.task_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='slack_time', full_name='task_details.slack_time', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=989,
  serialized_end=1059,
)


_TASK_AND_OPEN_FILTER_DETAILS = _descriptor.Descriptor(
  name='task_and_open_filter_details',
  full_name='task_and_open_filter_details',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='open_filter', full_name='task_and_open_filter_details.open_filter', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='task_details', full_name='task_and_open_filter_details.task_details', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1061,
  serialized_end=1163,
)


_BID_METADATA = _descriptor.Descriptor(
  name='bid_metadata',
  full_name='bid_metadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bid', full_name='bid_metadata.bid', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cost', full_name='bid_metadata.cost', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='microbatch_id', full_name='bid_metadata.microbatch_id', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1165,
  serialized_end=1229,
)


_RESULT = _descriptor.Descriptor(
  name='result',
  full_name='result',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bool_status', full_name='result.bool_status', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1231,
  serialized_end=1260,
)

_FOG_METADATA.fields_by_name['labels'].message_type = _FOG_LABEL
_FOG_LABELS.fields_by_name['labels'].message_type = _FOG_LABEL
_FOG_INFO_SPATIAL_LOCALITY_LIST.fields_by_name['fog_info_spatial_locality'].message_type = _FOG_SPATIAL_LOCALITY
_OPEN_FILTER_NAMEVALUEFILTERENTRY.containing_type = _OPEN_FILTER
_OPEN_FILTER.fields_by_name['namevalue_filter'].message_type = _OPEN_FILTER_NAMEVALUEFILTERENTRY
_DAG_FILTER_DEADLINE_INPUT.fields_by_name['filter'].message_type = _OPEN_FILTER
_FREE_SLOTS_SLOTENTRY.containing_type = _FREE_SLOTS
_FREE_SLOTS.fields_by_name['slot'].message_type = _FREE_SLOTS_SLOTENTRY
_FOG_SEQUENCE_FREE_SLOTS_FREESLOTLISTENTRY.fields_by_name['value'].message_type = _FREE_SLOTS
_FOG_SEQUENCE_FREE_SLOTS_FREESLOTLISTENTRY.containing_type = _FOG_SEQUENCE_FREE_SLOTS
_FOG_SEQUENCE_FREE_SLOTS.fields_by_name['free_slot_list'].message_type = _FOG_SEQUENCE_FREE_SLOTS_FREESLOTLISTENTRY
_FOG_SEQUENCE_FREE_SLOT_LIST.fields_by_name['fog_sequence_free_slots'].message_type = _FOG_SEQUENCE_FREE_SLOTS
_TASK_AND_OPEN_FILTER_DETAILS.fields_by_name['open_filter'].message_type = _OPEN_FILTER
_TASK_AND_OPEN_FILTER_DETAILS.fields_by_name['task_details'].message_type = _TASK_DETAILS
DESCRIPTOR.message_types_by_name['fog_label'] = _FOG_LABEL
DESCRIPTOR.message_types_by_name['fog_metadata'] = _FOG_METADATA
DESCRIPTOR.message_types_by_name['fog_labels'] = _FOG_LABELS
DESCRIPTOR.message_types_by_name['fog_spatial_locality'] = _FOG_SPATIAL_LOCALITY
DESCRIPTOR.message_types_by_name['fog_info_spatial_locality_list'] = _FOG_INFO_SPATIAL_LOCALITY_LIST
DESCRIPTOR.message_types_by_name['open_filter'] = _OPEN_FILTER
DESCRIPTOR.message_types_by_name['dag_filter_deadline_input'] = _DAG_FILTER_DEADLINE_INPUT
DESCRIPTOR.message_types_by_name['free_slots'] = _FREE_SLOTS
DESCRIPTOR.message_types_by_name['fog_sequence_free_slots'] = _FOG_SEQUENCE_FREE_SLOTS
DESCRIPTOR.message_types_by_name['fog_sequence_free_slot_list'] = _FOG_SEQUENCE_FREE_SLOT_LIST
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['task_details'] = _TASK_DETAILS
DESCRIPTOR.message_types_by_name['task_and_open_filter_details'] = _TASK_AND_OPEN_FILTER_DETAILS
DESCRIPTOR.message_types_by_name['bid_metadata'] = _BID_METADATA
DESCRIPTOR.message_types_by_name['result'] = _RESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

fog_label = _reflection.GeneratedProtocolMessageType('fog_label', (_message.Message,), dict(
  DESCRIPTOR = _FOG_LABEL,
  __module__ = 'cloud_service_pb2'
  # @@protoc_insertion_point(class_scope:fog_label)
  ))
_sym_db.RegisterMessage(fog_label)

fog_metadata = _reflection.GeneratedProtocolMessageType('fog_metadata', (_message.Message,), dict(
  DESCRIPTOR = _FOG_METADATA,
  __module__ = 'cloud_service_pb2'
  # @@protoc_insertion_point(class_scope:fog_metadata)
  ))
_sym_db.RegisterMessage(fog_metadata)

fog_labels = _reflection.GeneratedProtocolMessageType('fog_labels', (_message.Message,), dict(
  DESCRIPTOR = _FOG_LABELS,
  __module__ = 'cloud_service_pb2'
  # @@protoc_insertion_point(class_scope:fog_labels)
  ))
_sym_db.RegisterMessage(fog_labels)

fog_spatial_locality = _reflection.GeneratedProtocolMessageType('fog_spatial_locality', (_message.Message,), dict(
  DESCRIPTOR = _FOG_SPATIAL_LOCALITY,
  __module__ = 'cloud_service_pb2'
  # @@protoc_insertion_point(class_scope:fog_spatial_locality)
  ))
_sym_db.RegisterMessage(fog_spatial_locality)

fog_info_spatial_locality_list = _reflection.GeneratedProtocolMessageType('fog_info_spatial_locality_list', (_message.Message,), dict(
  DESCRIPTOR = _FOG_INFO_SPATIAL_LOCALITY_LIST,
  __module__ = 'cloud_service_pb2'
  # @@protoc_insertion_point(class_scope:fog_info_spatial_locality_list)
  ))
_sym_db.RegisterMessage(fog_info_spatial_locality_list)

open_filter = _reflection.GeneratedProtocolMessageType('open_filter', (_message.Message,), dict(

  NamevalueFilterEntry = _reflection.GeneratedProtocolMessageType('NamevalueFilterEntry', (_message.Message,), dict(
    DESCRIPTOR = _OPEN_FILTER_NAMEVALUEFILTERENTRY,
    __module__ = 'cloud_service_pb2'
    # @@protoc_insertion_point(class_scope:open_filter.NamevalueFilterEntry)
    ))
  ,
  DESCRIPTOR = _OPEN_FILTER,
  __module__ = 'cloud_service_pb2'
  # @@protoc_insertion_point(class_scope:open_filter)
  ))
_sym_db.RegisterMessage(open_filter)
_sym_db.RegisterMessage(open_filter.NamevalueFilterEntry)

dag_filter_deadline_input = _reflection.GeneratedProtocolMessageType('dag_filter_deadline_input', (_message.Message,), dict(
  DESCRIPTOR = _DAG_FILTER_DEADLINE_INPUT,
  __module__ = 'cloud_service_pb2'
  # @@protoc_insertion_point(class_scope:dag_filter_deadline_input)
  ))
_sym_db.RegisterMessage(dag_filter_deadline_input)

free_slots = _reflection.GeneratedProtocolMessageType('free_slots', (_message.Message,), dict(

  SlotEntry = _reflection.GeneratedProtocolMessageType('SlotEntry', (_message.Message,), dict(
    DESCRIPTOR = _FREE_SLOTS_SLOTENTRY,
    __module__ = 'cloud_service_pb2'
    # @@protoc_insertion_point(class_scope:free_slots.SlotEntry)
    ))
  ,
  DESCRIPTOR = _FREE_SLOTS,
  __module__ = 'cloud_service_pb2'
  # @@protoc_insertion_point(class_scope:free_slots)
  ))
_sym_db.RegisterMessage(free_slots)
_sym_db.RegisterMessage(free_slots.SlotEntry)

fog_sequence_free_slots = _reflection.GeneratedProtocolMessageType('fog_sequence_free_slots', (_message.Message,), dict(

  FreeSlotListEntry = _reflection.GeneratedProtocolMessageType('FreeSlotListEntry', (_message.Message,), dict(
    DESCRIPTOR = _FOG_SEQUENCE_FREE_SLOTS_FREESLOTLISTENTRY,
    __module__ = 'cloud_service_pb2'
    # @@protoc_insertion_point(class_scope:fog_sequence_free_slots.FreeSlotListEntry)
    ))
  ,
  DESCRIPTOR = _FOG_SEQUENCE_FREE_SLOTS,
  __module__ = 'cloud_service_pb2'
  # @@protoc_insertion_point(class_scope:fog_sequence_free_slots)
  ))
_sym_db.RegisterMessage(fog_sequence_free_slots)
_sym_db.RegisterMessage(fog_sequence_free_slots.FreeSlotListEntry)

fog_sequence_free_slot_list = _reflection.GeneratedProtocolMessageType('fog_sequence_free_slot_list', (_message.Message,), dict(
  DESCRIPTOR = _FOG_SEQUENCE_FREE_SLOT_LIST,
  __module__ = 'cloud_service_pb2'
  # @@protoc_insertion_point(class_scope:fog_sequence_free_slot_list)
  ))
_sym_db.RegisterMessage(fog_sequence_free_slot_list)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), dict(
  DESCRIPTOR = _EMPTY,
  __module__ = 'cloud_service_pb2'
  # @@protoc_insertion_point(class_scope:Empty)
  ))
_sym_db.RegisterMessage(Empty)

task_details = _reflection.GeneratedProtocolMessageType('task_details', (_message.Message,), dict(
  DESCRIPTOR = _TASK_DETAILS,
  __module__ = 'cloud_service_pb2'
  # @@protoc_insertion_point(class_scope:task_details)
  ))
_sym_db.RegisterMessage(task_details)

task_and_open_filter_details = _reflection.GeneratedProtocolMessageType('task_and_open_filter_details', (_message.Message,), dict(
  DESCRIPTOR = _TASK_AND_OPEN_FILTER_DETAILS,
  __module__ = 'cloud_service_pb2'
  # @@protoc_insertion_point(class_scope:task_and_open_filter_details)
  ))
_sym_db.RegisterMessage(task_and_open_filter_details)

bid_metadata = _reflection.GeneratedProtocolMessageType('bid_metadata', (_message.Message,), dict(
  DESCRIPTOR = _BID_METADATA,
  __module__ = 'cloud_service_pb2'
  # @@protoc_insertion_point(class_scope:bid_metadata)
  ))
_sym_db.RegisterMessage(bid_metadata)

result = _reflection.GeneratedProtocolMessageType('result', (_message.Message,), dict(
  DESCRIPTOR = _RESULT,
  __module__ = 'cloud_service_pb2'
  # @@protoc_insertion_point(class_scope:result)
  ))
_sym_db.RegisterMessage(result)


_OPEN_FILTER_NAMEVALUEFILTERENTRY.has_options = True
_OPEN_FILTER_NAMEVALUEFILTERENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_FREE_SLOTS_SLOTENTRY.has_options = True
_FREE_SLOTS_SLOTENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_FOG_SEQUENCE_FREE_SLOTS_FREESLOTLISTENTRY.has_options = True
_FOG_SEQUENCE_FREE_SLOTS_FREESLOTLISTENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))

_CLOUD = _descriptor.ServiceDescriptor(
  name='cloud',
  full_name='cloud',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=1263,
  serialized_end=1591,
  methods=[
  _descriptor.MethodDescriptor(
    name='register_fog',
    full_name='cloud.register_fog',
    index=0,
    containing_service=None,
    input_type=_FOG_METADATA,
    output_type=_EMPTY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='request_fog_list',
    full_name='cloud.request_fog_list',
    index=1,
    containing_service=None,
    input_type=_FOG_LABELS,
    output_type=_FOG_METADATA,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='dag_input',
    full_name='cloud.dag_input',
    index=2,
    containing_service=None,
    input_type=_DAG_FILTER_DEADLINE_INPUT,
    output_type=_EMPTY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='heap_update',
    full_name='cloud.heap_update',
    index=3,
    containing_service=None,
    input_type=_FOG_SEQUENCE_FREE_SLOT_LIST,
    output_type=_EMPTY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='task_done',
    full_name='cloud.task_done',
    index=4,
    containing_service=None,
    input_type=_TASK_DETAILS,
    output_type=_EMPTY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='task_undone',
    full_name='cloud.task_undone',
    index=5,
    containing_service=None,
    input_type=_TASK_DETAILS,
    output_type=_EMPTY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='bid_for_task_on_new_microbatch',
    full_name='cloud.bid_for_task_on_new_microbatch',
    index=6,
    containing_service=None,
    input_type=_BID_METADATA,
    output_type=_RESULT,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CLOUD)

DESCRIPTOR.services_by_name['cloud'] = _CLOUD

# @@protoc_insertion_point(module_scope)