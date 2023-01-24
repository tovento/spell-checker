import unittest
from data_structures.trie.trie import Trie

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()

    def test_empty_trie(self):
        result1 = self.trie.find("kissa")
        result2 = self.trie.find(" ")
        result3 = self.trie.find("a")

        self.assertFalse(result1)
        self.assertFalse(result2)
        self.assertFalse(result3)

    def test_adding_words_into_trie(self):
        self.trie.add_word("kissa")
        result1 = self.trie.find("kissa")

        self.assertTrue(result1)
        
        self.trie.add_word("koirankoppi")
        result2 = self.trie.find("koira")
        result3 = self.trie.find("koirankoppi")

        self.assertFalse(result2)
        self.assertTrue(result3)
