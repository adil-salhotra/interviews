"""
Say that you are a traveler on a 2D M x N grid. You begin in the
top-left corner and your goal is to travel to the bottom-right
corner. You may only move down or right. How many ways can you
travel to the bottom right?
"""


def grid_traveler(m, n):
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    return grid_traveler(m-1, n) + grid_traveler(m, n-1)

def grid_traveler_memo(m, n, memo):
    key = str(m) + ',' + str(n)
    if key in memo:
        return memo[key]
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    memo[key] = grid_traveler(m-1, n) + grid_traveler(m, n-1)
    return memo[key]

