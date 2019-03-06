#!/usr/bin/env python3

strs = ['Hello', 'World']
print([x.lower() for x in strs])
print(list(map(lambda x: x.lower(), strs)))
# Аккуратно: тут важно, что в strs только типы 'str'
print(list(map(str.lower, strs)))

some_list = ['Hello', b'World']
print([x.lower() for x in some_list])
print(list(map(lambda x: x.lower(), some_list)))
print(list(map(str.lower, some_list)))
