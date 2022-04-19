import unittest
import sys

from config.overwriteable_config import OverwriteableConfig
from config.overwriteable_config import is_scientific


def test_merge():
    a = OverwriteableConfig()
    a.a = 0

    b = OverwriteableConfig()
    b.b = 1

    c = OverwriteableConfig(a, b)

    c_ = OverwriteableConfig()
    c_.a = 0
    c_.b = 1

    assert c_ == c

def test_merge_overwrite():
    a = OverwriteableConfig()
    a.a = 0

    b = OverwriteableConfig()
    b.a = 2
    b.b = 1

    c = OverwriteableConfig(a, b)

    c_ = OverwriteableConfig()
    c_.a = 2
    c_.b = 1

    assert c_ == c

def test_overwrite_leaf2node():
    a = OverwriteableConfig()
    a.a = 0
    a.b = 1

    b = OverwriteableConfig()
    b.b = OverwriteableConfig()
    b.b.a = 1
    b.b.b = 2

    c = OverwriteableConfig(a, b)
    
    c_ = OverwriteableConfig()
    c_.a = 0
    c_.b = OverwriteableConfig()
    c_.b.a = 1
    c_.b.b = 2

    assert c_ == c

def test_overwrite_node2leaf():
    a = OverwriteableConfig()
    a.a = 0
    a.b = 1

    b = OverwriteableConfig()
    b.b = OverwriteableConfig()
    b.b.a = 1
    b.b.b = 2

    c = OverwriteableConfig(b, a)
    
    c_ = OverwriteableConfig()
    c_.a = 0
    c_.b = 1

    assert c_ == c

def test_scientific():
    assert is_scientific('1e1') == True
    assert is_scientific('1E1') == True
    assert is_scientific('+1e-1') == True
    assert is_scientific('24e34') == True

    assert is_scientific('1e1e1') == False
    assert is_scientific('e') == False
    assert is_scientific('1e1e') == False
    assert is_scientific('1e') == False
    assert is_scientific('e1') == False
    assert is_scientific('5e1.2') == False
    assert is_scientific('5.6e1') == False


if __name__ == '__main__':
    test_merge()
    test_merge_overwrite()

    test_scientific()

    test_overwrite_leaf2node()
    test_overwrite_node2leaf()

