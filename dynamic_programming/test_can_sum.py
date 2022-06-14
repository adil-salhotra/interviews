import pytest 
from can_sum import can_sum, can_sum_memo
 
def test_0():
    assert can_sum(7, [2,3]) == can_sum_memo(7, [2,3], dict())

def test_1():
    assert can_sum_memo(300, [2, 1], dict())