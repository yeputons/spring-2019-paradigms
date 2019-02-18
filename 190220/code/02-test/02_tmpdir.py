#!/usr/bin/env python3
import pytest


def test_file_read(tmp_path):  # parameter name is important!
    tmp_f = tmp_path / 'hello.txt'
    tmp_f.write_text('Hello World!\n')  # https://docs.python.org/3/library/pathlib.html

    with open(tmp_f, 'r') as f:
        assert f.read() == 'Hello World!\n'
    # print(str(tmp_f))
    # assert False  # To show captured stdout


def test_file_write(tmp_path):  # parameter name is important!
    tmp_f = tmp_path / 'hello.txt'
    #with open(tmp_f, 'w') as f:
    f = open(tmp_f, 'w')
    f.write('Hello World!\n')
    f.close()
    assert tmp_f.read_text() == 'Hello World!\n'
    

if __name__ == '__main__':
    pytest.main([__file__])
