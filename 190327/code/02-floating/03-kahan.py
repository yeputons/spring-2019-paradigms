from random import shuffle

def kahan_sum(xs):
    # Copied verbatim from https://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html
    # Is it good? I have no idea :(
    s = 0
    c = 0
    for x in xs:
        y = x - c
        t = s + y
        c = (t - s) - y
        s = t
    return s


a=[123456 * 2 ** x for x in range(0, 200)]
print(format(sum(a), ".20e")) # Точный результат
print()
a = list(map(float, a))
for _ in range(10):
    shuffle(a)
    print(format(sum(a), ".20e"))
print()
for _ in range(10):
    shuffle(a)
    print(format(kahan_sum(a), ".20e"))
