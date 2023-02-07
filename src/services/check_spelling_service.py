class CheckSpelling:
    def __init__(self, trie: object):
        self.trie = trie

    def check_word(self, word):
        return self.trie.find(word)
