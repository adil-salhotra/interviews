from how_sum import how_sum, how_sum_memo, how_sum_tab

def test_0():
    assert sorted(how_sum(7, [2,3])) == [2,2,3]
    assert sorted(how_sum(10, [3,5])) == [5,5]
    assert how_sum(7, [2,3]) == how_sum_memo(7, [2,3], dict())
    assert how_sum(10, [3,5]) == how_sum_memo(10, [3,5], dict())

def test_1():
    assert not how_sum_memo(300, [7,14], dict())

def test_2():
    assert sorted(how_sum_tab(7, [2,3])) == [2,2,3]
    assert sorted(how_sum_tab(10, [3,5])) == [5,5]
    assert how_sum(7, [2,3]) == how_sum_tab(7, [2,3])
    assert how_sum(10, [3,5]) == how_sum_tab(10, [3,5])

def test_3():
    assert not how_sum_tab(300, [7,14])