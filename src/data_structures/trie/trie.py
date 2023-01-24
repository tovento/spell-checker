from .trie_node import TrieNode

class Trie():
    """Represents a trie data structure."""
    def __init__(self):
        self.root = TrieNode("")

    def add_word(self, word: str):
        """Adds a new word into the trie."""
        node = self.root

        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = node.children[char]

        node.end_of_word = True

    def find(self, word: str):
        """Searches for a word in the trie."""
        node = self.root
        length = len(word)
        for i in range(length):
            letter = word[i]
            if letter not in node.children:
                return False
            node = node.children[letter]
        return node.end_of_word

    def read_file(self, file_path: str):
        """Reads a file and adds its contents to the trie."""
        with open(file_path) as file:
            contents = file.readlines()

        for word in contents:
            self.add_word(word.strip())
