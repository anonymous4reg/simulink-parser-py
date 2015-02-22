# simulink-parser-py

This module is based on [PyParsing](https://pypi.python.org/pypi/pyparsing) and exposes two classes, two methods, and two options.

## Classes

1. `simulink_model`: A simulink model object that has three fields:
  + `name`(`string`)
  + `block_defaults`(`dict`)
  + `system`(`simulink_system`)

2. `simulink_system`: A simulink system object that has three fields:
  + `name`(`string`)
  + `blocks`(`list`)
  + `lines`(`list`)

## Methods

1. `read_mdl_lib_as_dict`: reads an mdl file as a library and returns a `dict` object.
2. `read_mdl_model`: reads an mdl file as a system and returns a `simulink_system` object.

## Options

1. `use_white_list`: a boolean value indicates if the whitelist should be used for propertiy filtering. Default = True.
2. `property_list`: a `string` list containing all the property names that should be parsed.
  Default value:

```python
property_list = [
  'BlockType',
  'SourceBlock',
  'System',
  'Block',
  'Ports',
  'Port',
  'PortNumber',
  'SampleTime',
  'SignalType',
  'SamplingMode',
  'Inputs',
  'Operator',
  'OutDataTypeStr',
  'Name',
  'SID',
  'SrcBlock',
  'SrcPort',
  'DstBlock',
  'DstPort']
```

## Usage example

```python
import mdl_reader

mdl_reader.use_white_list = True
# use the white list (property_list)

mdl_reader.property_list += ['ZOrder']
# add 'ZOrder' as one property to be parsed

print mdl_reader.read_mdl_lib_as_dict('testlib.mdl')
# read one simulink library as a dict object

print mdl_reader.read_mdl_model('testmodel.mdl')
# read one simulink model as a simulink_system object
```
