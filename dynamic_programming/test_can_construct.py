from can_construct import can_construct, can_construct_memo

def test_0():
    assert(can_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']) == True)
    assert(can_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']) == can_construct_memo('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'], dict()))

def test_1():
    assert(can_construct("skateboard", ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']) == False)   

def test_2():
    assert not can_construct_memo(
        target = 'eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',
        word_bank = ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee'],
        memo = dict()
    )