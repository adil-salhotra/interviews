"""
Write a function

howSum(targetSum, numbers)

that takes in a targetSum and an array of numbers as arguments.
The function should return an arrav containing anv combination of
elements that add up to exactlv the targetSum. If there is no
combination that adds up to the targetSum, then return null.
"""

def how_sum(target_sum, numbers):
    if target_sum == 0:
        return list()
    if target_sum < 0:
        return None
    
    for number in numbers:
        remainder = target_sum - number
        remainder_result = how_sum(remainder, numbers)
        if remainder_result is not None:
            remainder_result.append(number)
            return remainder_result

def how_sum_memo(target_sum, numbers, memo):
    if memo is None:
        return dict()
    if target_sum in memo: 
        return memo[target_sum]
    if target_sum == 0:
        return list()
    if target_sum < 0:
        return None
    
    for number in numbers:
        remainder = target_sum - number
        remainder_result = how_sum_memo(remainder, numbers, memo) 
        if remainder_result is not None:
            remainder_result.append(number)
            memo[target_sum] = remainder_result
            return memo[target_sum]

    memo[target_sum] = None
    return 
    