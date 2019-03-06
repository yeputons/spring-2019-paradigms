#!/usr/bin/env python
import pytest
import sys
from io import StringIO


def read_number():
    return int(input())


def test_read_number(monkeypatch):
    monkeypatch.setattr(sys, 'stdin', StringIO('12'))
    # requests.get
    assert read_number() == 12


if __name__ == "__main__":
    pytest.main(sys.argv)
