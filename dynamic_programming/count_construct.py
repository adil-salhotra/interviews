"""
Write a function countConstruct(target, word_bank)
that accepts a target string and an array of strings.

The function should return the number of ways that the target 
can be constructed by concatenating elements of the word_bank
array. 

You may reuse the elements of word_bank as many times as needed.
"""
def count_construct(target, word_bank):
    """
    m = len(target)
    n = len(word_bank)
    Operation 1: for loop for all the words in word bank
    """
    count = 0
    if target == '':
        return 1
    
    for word in word_bank:
        if word in target:
            if target.find(word) == 0:
                new_target = target[len(word):]
                num_ways = count_construct(new_target, word_bank)
                count += num_ways
    return count

def count_construct_memo(target, word_bank, memo=dict()):
    count = 0

    if target in memo:
        return memo[target]
    if target == '':
        return 1
    
    for word in word_bank:
        if word in target:
            if target.find(word) == 0:
                new_target = target[len(word):]
                count += count_construct_memo(new_target, word_bank, memo)
                memo[target] = count
    return memo[target] if target in memo else count
