def n_queens(n):
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