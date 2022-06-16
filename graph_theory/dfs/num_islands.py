"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the 
number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.
"""

def num_islands(grid):
    ROWS = len(grid)
    COLS = len(grid[0])
    visited = set()

    island_count = 0
    def dfs(row, col):
        if (row >= ROWS or col >= COLS or row < 0 or col < 0 
        or (row,col) in visited or grid[row][col] == '0'):
            return 

        visited.add((row,col))
        dfs(row+1,col)
        dfs(row-1,col)
        dfs(row,col+1)
        dfs(row,col-1)

    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] == '1' and (row,col) not in visited:
                island_count += 1
                dfs(row,col)
    
    return island_count


