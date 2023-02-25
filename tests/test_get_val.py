
# файл dicts.py

from utils.dicts import get_val

coll = {'a': 1, 'b':2, 'c':3}

def test_get_val1():
    assert get_val(coll, 'b') == 2

def test_get_val2():
    assert get_val(coll, 'd') == "git"

def test_get_val3():
    assert get_val({}, 'a', "default") == "default"

