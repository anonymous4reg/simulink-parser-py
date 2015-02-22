import mdl_reader

mdl_reader.use_white_list = True
# use the white list (property_list)

mdl_reader.property_list += ['ZOrder']
# add 'ZOrder' as one property to be parsed

print mdl_reader.read_mdl_lib_as_dict('testlib.mdl')
# read one simulink library as a dict object

print mdl_reader.read_mdl_model('testmodel.mdl')
# read one simulink model as a simulink_system object
