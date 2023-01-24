import os
import unittest
from data_structures.trie.trie import Trie

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()

    def test_empty_trie(self):
        result1 = self.trie.find("cat")
        result2 = self.trie.find(" ")
        result3 = self.trie.find("a")

        self.assertFalse(result1)
        self.assertFalse(result2)
        self.assertFalse(result3)

    def test_adding_words_into_trie(self):
        self.trie.add_word("dog")
        result1 = self.trie.find("dog")

        self.assertTrue(result1)
        
        self.trie.add_word("catnip")
        result2 = self.trie.find("cat")
        result3 = self.trie.find("catnip")

        self.assertFalse(result2)
        self.assertTrue(result3)

    def test_read_file(self):
        path = os.path.join("src","tests", "data", "test_file.txt")
        self.trie.read_file(path)

        result1 = self.trie.find("apple")
        result2 = self.trie.find("tangerine")
        result3 = self.trie.find("orange")

        self.assertTrue(result1)
        self.assertTrue(result2)
        self.assertFalse(result3)
