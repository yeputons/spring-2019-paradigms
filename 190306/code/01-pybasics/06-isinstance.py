#!/usr/bin/env python3

# Не надо так писать, демонстрация isinstance, лучше
# просто x.lower(), тогда автоматически вызовется нужный
# bounded-метод


def generic_lower(x):
    if isinstance(x, str):
        return str.lower(x)
    elif isinstance(x, bytes):
        return bytes.lower(x)
    else:
        assert False


print(generic_lower('Hello'))
print(generic_lower(b'Hello'))
print(type('Hello'))
print(type(b'Hello'))

print(isinstance(5, int))
print(isinstance(5.0, int))
print(isinstance(5.0, float))
