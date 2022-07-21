"""
Write a function allConstruct(target, wordbank) that accepts
a target string and an array of strings. 

The function should return a 2D array containing all of the ways
that the target can be constructed by concatenating elements to
the wordbank array.

Complexity:
m = len(target)
n = len(wordbank)
We will have a tree with n possible branches at each subtree with 
a length of m. Therefore the time complexity will be O(n^m).

Just like the other problems in this category of word bank/target word input,
we have len(wordbank) possible branches and a tree with a height of m. 
O(n^m)

"""

def all_construct(target, word_bank):
    if target == '': 
        return [[]]

    output = list()
    for word in word_bank:
        if target.find(word) == 0:
            suffix = target[len(word):]
            suffix_ways = all_construct(suffix, word_bank)
            target_ways = list(map(lambda l: [word] + l, suffix_ways))
            output.extend(target_ways)
    return output

"""
Memoizing all construct doesn't do anything to the runtime. Just for practice.

"""
def all_construct_memo(target, word_bank, memo=dict()):
    if target in memo:
        return memo[target]
    if target == '': 
        return [[]]

    output = list()
    for word in word_bank:
        if target.find(word) == 0:
            suffix = target[len(word):]
            suffix_ways = all_construct(suffix, word_bank)
            target_ways = list(map(lambda l: [word] + l, suffix_ways))
            output.extend(target_ways)
    
    memo[target] = output
    return output

def all_construct_tab(target, word_bank):
    length = len(target)
    table = [[] for _ in range(length + 1)]
    table[0] = [[]]

    for index in range(length+1):
        if table[index] is not None:
            for word in word_bank:
                offset = len(word)
                if word == target[index:index+offset]:
                    ways = [[*way,word] for way in table[index]]
                    table[index+len(word)].extend(ways)
                    # table[index+offset] = table[index][:] + [word]
    
    return table[-1]