from all_construct import all_construct, all_construct_memo, all_construct_tab
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

def test_3():
    print(all_construct_tab('abcdef', ['ab','abc','cd','def','abcd','ef','c']), all_construct('abcdef', ['ab','abc','cd','def','abcd','ef','c']))
    assert(sorted(all_construct_tab('abcdef', ['ab','abc','cd','def','abcd','ef','c'])) == 
    sorted(all_construct_memo('abcdef', ['ab','abc','cd','def','abcd','ef','c'])))