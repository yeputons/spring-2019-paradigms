#!/usr/bin/env python3
a = {}

try:
    x = a[10]
except KeyError as err:
    print('not found', err)
finally:
    print('finally')

print('done')
