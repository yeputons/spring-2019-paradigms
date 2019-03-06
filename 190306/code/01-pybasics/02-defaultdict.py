#!/usr/bin/env python3


# Напишем свой класс:


class defaultdict:
    # d = {} # Это статическая переменная: одна на все экземпляры

    def get(self, key):  # Метод; первый аргумент - this, принято называть self
        # Можно проверить, есть ли у нашего экземпляра класса (объекта) поле
        if not hasattr(self, 'd'):
            self.d = {}
        if key not in self.d:
            self.d[key] = []
        return self.d[key]

# class defaultdict: - это синтаксический сахар над примерно этим:
#   defaultdict.d = {}
#   defaultdict.get = lambda self, key: ...


a = defaultdict()  # Вызываем конструктор
defaultdict.get(a, 'key').append(10)  # unbounded-метод (явный self)
a.get('key').append(20)  # bounded-метод (self уже привязан к a)
assert a.get('key') == [10, 20]
assert a.get('not_found') == []

b = defaultdict()
print(b.get('key'))
