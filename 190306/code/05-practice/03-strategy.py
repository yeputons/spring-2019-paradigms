#!/usr/bin/env python3

# Можно даже писать моды, мод - один класс. Потом при загрузке
# записываем мод в переменную strategy, а основной игровой цикл не меняем.


class RandomStrategy:
    def get_next_turn(self):
        pass


class BalancedStrategy:
    def __init__(self):
        self.random_moves = 0

    def get_next_turn(field):
        pass


stategy = RandomStrategy()

while True:
    go(strategy.get_next_turn(field))
