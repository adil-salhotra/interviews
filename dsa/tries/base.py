class Trie:
    class TrieNode:
        def __init__(self, value='*', children=list(), is_end_of_word=False):
            self.value = value
            self.children = children
            self.is_end_of_word = is_end_of_word

        def __eq__(self, other):
            return self.value == other.value


    def __init__(self):
        self.root = self.TrieNode()
        self._collection = set()
    
    @property
    def collection(self):
        return self._collection

    def add_word(self, word):
        curr_node = self.root
        for index,char in enumerate(word):
            # If the root has no children, the trie is empty
            child_node = self.TrieNode(value=char, children=list())
            if child_node in curr_node.children:
                curr_node = curr_node.children[curr_node.children.index(child_node)]
                if index == len(word) - 1:
                    curr_node.is_end_of_word = True
                    self._collection.add(word)
            else:
                new_node = self.TrieNode(value=char, children=list())
                curr_node.children.append(new_node)
                curr_node = curr_node.children[curr_node.children.index(new_node)]

                if index == len(word) - 1:
                    curr_node.is_end_of_word = True
                    self._collection.add(word)

    def check_word_in_trie(self, word) -> bool:
        curr_node = self.root
        for index,char in enumerate(word):
            child_node = self.TrieNode(value=char, children=list())
            if child_node in curr_node.children:
                curr_node = curr_node.children[curr_node.children.index(child_node)]
            else:
                return False
            if index == len(word) - 1:
                return curr_node.is_end_of_word

#TODO: 
# trie.countWordsEqualTo("apple");    // There are two instances of "apple" so return 2.
# trie.countWordsStartingWith("app"); // "app" is a prefix of "apple" so return 2.
# trie.erase("apple");    




    


