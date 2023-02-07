class TrieNode:
    """Represent one node in a trie data structure."""
    def __init__(self, char: str):
        self.char = char
        self.end_of_word = False
        self.children = {}
