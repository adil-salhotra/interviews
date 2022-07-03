def n_queens(n):
    """
    The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
    Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.
    Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and 
    an empty space, respectively.
    """
    
    neg_diag = set()
    cols = set()
    pos_diag = set()

    res = list()
    board = [['.'] * n for _ in range(n)]

    def backtrack(row):
        if row == n:
            copy = [''.join(row) for row in board]
            res.append(copy)
            return res

        for col in range(n):
            if ((row - col) in neg_diag or (row + col) in pos_diag or 
            col in cols):
                continue

            cols.add(col)
            pos_diag.add(row+col)
            neg_diag.add(row-col)
            board[row][col] = 'Q'
            
            backtrack(row+1)

            cols.remove(col)
            pos_diag.remove(row+col)
            neg_diag.remove(row-col)
            board[row][col] = '.'

    backtrack(0)
    return res