#!/usr/bin/env python3
s = "hello good world"
cnt = 0
total_len = 0
in_word = False
for c in s + " ":
    if c == " ":
        if in_word:
            cnt += 1
        in_word = False
    else:
        total_len += 1
        in_word = True
print(total_len / cnt)
