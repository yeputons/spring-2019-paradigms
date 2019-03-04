print('lib_b loading...')
import lib_a  # lib_a прямо сейчас загружается, цикла нет
print('lib_b loaded')


# lib_a.foo()  # lib_a может сейчас загружаться, поэтому foo() ещё не было объявлено


def bar():
    print('bar')
    lib_a.foo()  # Тут окей, все библиотеки уже подгрузились
