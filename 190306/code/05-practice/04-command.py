#!/usr/bin/env python3
class Turn:
    def do_turn(field):
        pass

    def undo_turn(field):
        pass


class DestoryTurn:  # Не сделать функциями: нужно состояние
    def do_turn(field):
        self.destroyed = field[0]
        field[0] = None

    def undo_turn(field):
        field[0] = self.destroyed
