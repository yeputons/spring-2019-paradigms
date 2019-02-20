#!/usr/bin/env python3
import pytest


def test_print(capsys):  # parameter name is important!
    print('Hello')
    out, err = capsys.readouterr()
    assert out == 'Hello\n'
    assert err == ''

    print('Hello-2')
    print('Hello-3')
    out, err = capsys.readouterr()
    assert out == 'Hello-2\nHello-3\n'
    assert err == ''
    

if __name__ == '__main__':
    pytest.main([__file__])
