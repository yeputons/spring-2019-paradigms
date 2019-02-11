#!/usr/bin/env python3
def remove_all_max(a):
    """
    >>> a = [1, 3, 2, 2]
    >>> remove_all_max(a)
    [1, 2, 2]
    >>> remove_all_max(a)  # Не проверить отдельно работу с повторами
    [1]
    >>> remove_all_max(a)
    []
    """
    a.remove(max(a))  # Неверное решение
    return a  # Обязательно для тестов, нельзя проверить значение переменной??!


if __name__ == "__main__":
    import doctest
    doctest.testmod()
