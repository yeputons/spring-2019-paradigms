#!/usr/bin/env python3
# 'Reverse integer'

x = 1234567890123
print(int("".join(reversed(str(x)))))

digits = str(x)
need_str = "".join(reversed(digits))  # list() can be omitted sometimes
print(int(need_str))
