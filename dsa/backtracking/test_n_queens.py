from n_queens import n_queens

def test_0():
    assert n_queens(4) == [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]

def test_1():
    assert n_queens(1) == [["Q"]]