#!/usr/bin/env python3
import random
import pytest
import sys
from unittest.mock import MagicMock
 

class Printer:
    def output(self, value):
        print("Printing!!! {}".format(random.randrange(10)))
        print(value)
        print("Done printing!!!")
        return 10

class Terminal:
    def __init__(self, printer):
        self.printer = printer

    def received_answer(self, answer):
        assert answer.startswith('ANS:')
        assert self.printer.output(answer[4:]) == 10


def test_terminal():
    p = MagicMock()
    t = Terminal(p)
    p.output.return_value = 10
    t.received_answer('ANS:hello')
    p.output.assert_called_with('hello')

if __name__ == "__main__":
    pytest.main(sys.argv)
