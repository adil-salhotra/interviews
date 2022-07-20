import pytest 
from can_sum import can_sum, can_sum_memo, can_sum_tab
 
def test_0():
    assert can_sum(7, [2,3]) == can_sum_memo(7, [2,3], dict())

def test_1():
    assert can_sum_memo(300, [2, 1], dict())

def test_2():
    assert can_sum_tab(300, [2, 1])

def test_3():
    assert not can_sum_memo(30, [7,14]) and not can_sum_tab(30, [7,14])

def test_4():
    assert can_sum(7, [5,3,4]) == can_sum_tab(7, [5,3,4])
    assert can_sum(7, [2,3]) == can_sum_tab(7, [2,3])
    assert can_sum(1, [2,4]) == can_sum_tab(1, [2,4])