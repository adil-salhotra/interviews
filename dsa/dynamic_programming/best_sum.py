"""
Write a function
bestSum(targetSum, numbers)
that takes in a number targetSum and an array of numbers as arguments.

The function should return an array containing the shortest
combination of numbers that add up to exactly the targetSum.
If there is a tie for the shortest combination, you may return any
one of the shortest.
"""

def best_sum(target_sum, numbers):
    """
    n = len(numbers)
    m = target_sum
    Total Run Time complexity: O(n^m * m)
    """
    if target_sum == 0:
        return list()
    if target_sum < 0:
        return

    shortest_combo = None
    # We branch for every choice of number. Therefore the branching factor
    # is the length of the numbers array.
    for number in numbers:
        remainder = target_sum - number
        combo = best_sum(remainder, numbers)
        if combo is not None:
            combo.append(number)
            if not shortest_combo or len(combo) < len(shortest_combo):
                shortest_combo = combo
    
    return shortest_combo

def best_sum_memo(target_sum, numbers, memo=dict()):
    """
    n = len(numbers)
    m = target_sum
    O(m * n * m) = O(m^2 * n)
    """
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return list()
    if target_sum < 0:
        return

    shortest_combo = None

    for number in numbers:
        remainder = target_sum - number
        remainder_combo = best_sum_memo(remainder, numbers, memo)
        if remainder_combo is not None:
            combo = remainder_combo + [number]
            if not shortest_combo or len(combo) < len(shortest_combo):
                shortest_combo = combo
    
    memo[target_sum] = shortest_combo
    
    return shortest_combo

def best_sum_tab(target_sum, numbers):
    table = [None] * (target_sum + 1)
    table[0] = []
    for index in range(target_sum + 1):
        if table[index] != None:
            for number in numbers:
                combo = table[index][:] + [number]
                if index + number < target_sum + 1:
                    if not table[index+number] or len(table[index + number]) > len(combo):
                        table[index + number] = combo
    
    return table[target_sum]