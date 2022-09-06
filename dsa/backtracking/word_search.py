def word_search(board, word):
    """
    :type board: List[List[str]]
    :type word: str
    :rtype: bool

    Given an m x n grid of characters board and a string word, return true if word exists in the grid.
    The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are 
    horizontally or vertically neighboring. The same letter cell may not be used more than once.
    """
    ROWS = len(board)
    COLS = len(board[0])
    visited = set()
    
    def dfs(row, col, visited, index):
        if (row >= ROWS or col >= COLS or row < 0 or col < 0 
        or (row,col) in visited or word[index] != board[row][col]):
            return False
        
        if index == len(word) - 1:
            return True

        
        visited.add((row,col))
        
        ret = (dfs(row+1, col, visited, index+1) 
        or dfs(row-1, col, visited, index+1) 
        or dfs(row, col+1, visited, index+1) 
        or dfs(row, col-1, visited, index+1))
            
        visited.remove((row,col))
        return ret
    
    for row in range(ROWS):
        for col in range(COLS):
            if dfs(row, col, visited, 0):
                return True
    
    return False