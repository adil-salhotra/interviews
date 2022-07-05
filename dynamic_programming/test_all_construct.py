from all_construct import all_construct, all_construct_memo
def test_0():
    assert(all_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']) == 
            [['purp', 'le'], 
            ['p', 'ur', 'p', 'le']])
def test_1():
    assert(all_construct('abcdef', ['ab','abc','cd','def','abcd','ef','c']) == 
            [['ab','cd','ef'],
            ['ab','c','def'],
            ['abc','def'],
            ['abcd','ef']])
def test_2():
    assert(all_construct('abcdef', ['ab','abc','cd','def','abcd','ef','c']) == 
    all_construct_memo('abcdef', ['ab','abc','cd','def','abcd','ef','c']))