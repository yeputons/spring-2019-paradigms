#!/usr/bin/env python3
import pytest


def test_print(capsys):  # parameter name is important!
    print('Hello')
    out, err = capsys.readouterr()
    assert out == 'Hello\n'
    assert err == ''
    

if __name__ == '__main__':
    pytest.main([__file__])
