from word_search import word_search

def test_0():
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"

    assert(word_search(board,word) == True)

def test_1():
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "SEE"
    
    assert(word_search(board,word) == True)

def test_2():
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCB"

    assert(word_search(board,word) == False)