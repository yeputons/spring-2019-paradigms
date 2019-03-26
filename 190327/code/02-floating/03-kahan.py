from random import shuffle

def kahan_sum(xs):
    # Copied verbatim from https://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html
    # Is it good? I have no idea :(
    # See https://ru.wikipedia.org/wiki/%D0%90%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC_%D0%9A%D1%8D%D1%85%D1%8D%D0%BD%D0%B0
    # See https://en.wikipedia.org/wiki/Kahan_summation_algorithm
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
