import pytest
from base import Trie

def test_add_word():
    trie = Trie()
    word = 'poop'
    trie.add_word('poop')
    assert trie.check_word_in_trie(word)

def test_dictionary_in_trie():
    collection = ['many', 'men', 'by', 'twenty', 'one', 'savage']
    trie = Trie()
    for word in collection:
        trie.add_word(word)
        assert trie.check_word_in_trie(word)
        assert word in trie.collection

def test_add_words_with_same_prefix():
    collection = ['me', 'mean']
    trie = Trie()
    for word in collection:
        trie.add_word(word)
        assert trie.check_word_in_trie(word)
        assert word in trie.collection