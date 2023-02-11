from .trie_node import TrieNode

class Trie():
    """Represent a trie data structure."""
    def __init__(self):
        self.root = TrieNode("")
        self.list = []

    def add_word(self, word: str):
        """Add a new word into the trie."""
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
        """Search for a word in the trie."""
        node = self.root
        length = len(word)
        for i in range(length):
            letter = word[i]
            if letter not in node.children:
                return False
            node = node.children[letter]
        return node.end_of_word

    def read_file(self, file_path: str):
        """Read a file and adds its contents to the trie."""
        with open(file_path, encoding="utf-8") as file:
            for word in file.readlines():
                self.add_word(word.strip())

    def list_items(self, node: object, string: str):
        for child in node.children:
            newstring = string + node.children[child].char
            if node.children[child].end_of_word:
                self.list.append(newstring)
            self.list_items(node.children[child], newstring)
