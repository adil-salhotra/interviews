"""
Write a function canConstruct(target, word_bank)
that accepts a target string and an array of strings.

The function should return a boolean indicating whether or not 
the target can be constructed by concatenating elements of
the wordbank array.

You may reuse elements of wordbank as many times as needed.

"""

def can_construct(target, word_bank):
    """
    n = len(word_bank)
    m = len(target)

    Operation 1: Recursion Factor inside For Loop
    Run Time complexity: O(n^m)
    You have a n branches on a tree with height of m. 
    So we multiply n decisions by itself m times to get 
    the number of decisions being made. Hence, n^m run time.

    Operation 2: str.replace()
    Run Time complexity: O(m)
    Worst case you have to replace all of the characters in 
    the string, which has time complexity of the size of the
    string.

    Total Run Time complexity: O(n^m * m)


    Space complexity: 

    """

    if target == '':
        return True
    
    for word in word_bank:
        if target.find(word) == 0:
                new_target = target[len(word):]
                if can_construct(new_target, word_bank):
                    return True

    return False

def can_construct_memo(target, word_bank, memo=dict()):
    """
    n = len(word_bank)
    m = len(target)
    Run Time complexity: O(n * m)

    """

    if target in memo:
        return memo[target]
    if target == '':
        return True

    for word in word_bank:
        if target.find(word) == 0:
             # using list comprehensions, ie. new_target = target[len(word):], causes the code to hang.
            new_target = target.replace(word, '')
            memo[target] = can_construct(new_target, word_bank)
            if memo[target]:
                return True

    return False

    
    



            
