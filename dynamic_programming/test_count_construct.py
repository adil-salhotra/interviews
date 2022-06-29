from count_construct import count_construct, count_construct_memo

def test_0():
    assert(count_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']) == 1)

def test_1():
    assert(count_construct('purple', ['purp', 'p', 'ur', 'le', ]) == 2)

def test_2():
    assert(
        count_construct_memo(
            target = 'eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',
            word_bank = ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee'],
            memo = dict()
        ) == 0
    )

def test_3():
    assert(
        count_construct(
            'enterapotentpot', 
            ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']
        ) == 4
    )
    assert(
        count_construct(
            'enterapotentpot', 
            ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']
        ) == 
        count_construct_memo(
            'enterapotentpot', 
            ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'],
            dict()
        )

    )