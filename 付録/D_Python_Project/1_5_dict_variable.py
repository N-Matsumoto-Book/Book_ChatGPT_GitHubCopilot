my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
print(my_dict['key1'])  # value1

# print(my_dict['key4'])  # KeyError: 'key4'(エラーが発生)
print(my_dict.get('key4', 'default_value'))  # 'default_value'(エラーは発生しない)

my_dict = {'key1': 'value1', 'key2': 'value2'}
# my_dictには、key1の値がすでに格納されているため、new_value1で更新される
my_dict['key1'] = 'new_value1'
my_dict['key3'] = 'value3'  # my_dictには、key3は格納されていないため、新たに値value3として格納される
print(my_dict)  # {'key1': 'new_value1', 'key2': 'value2', 'key3': 'value3'}

my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
keys = my_dict.keys()  # dict_keys(['key1', 'key2', 'key3'])
values = my_dict.values()  # dict_values(['value1', 'value2', 'value3'])

my_dict1 = {'key1': 'value1', 'key2': 'value2'}
my_dict2 = {'key2': 'new_value2', 'key3': 'value3'}
my_dict1.update(my_dict2)  # key2をnew_value2で更新、key3: value3を追加。
print(my_dict1)  # {'key1': 'value1', 'key2': 'new_value2', 'key3': 'value3'}
