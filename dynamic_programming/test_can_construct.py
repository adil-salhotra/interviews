from can_construct import can_construct, can_construct_memo, can_construct_tab

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
def test_3():
    assert(can_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']) == True)
    assert(can_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']) == can_construct_tab('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))

def test_4():
    assert(can_construct_tab("skateboard", ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']) == False)   

def test_5():
    assert not can_construct_tab(
        target = 'eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',
        word_bank = ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee'],
    )