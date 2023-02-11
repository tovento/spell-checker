import os
import unittest
from data_structures.trie.trie import Trie

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()

    def test_empty_trie(self):
        cat = self.trie.find("cat")
        space = self.trie.find(" ")
        a = self.trie.find("a")

        self.assertFalse(cat)
        self.assertFalse(space)
        self.assertFalse(a)

    def test_adding_words_into_trie(self):
        self.trie.add_word("dog")
        dog = self.trie.find("dog")

        self.assertTrue(dog)
        
        self.trie.add_word("catnip")
        cat = self.trie.find("cat")
        catnip = self.trie.find("catnip")

        self.assertFalse(cat)
        self.assertTrue(catnip)

    def test_read_file(self):
        path = os.path.join("src","tests", "data", "test_file.txt")
        self.trie.read_file(path)

        apple = self.trie.find("apple")
        banana = self.trie.find("banana")
        bananarama = self.trie.find("bananarama")
        grape = self.trie.find("grape")
        grapefruit = self.trie.find("grapefruit")
        lemon = self.trie.find("lemon")
        mango = self.trie.find("mango")
        mangosteen = self.trie.find("mangosteen")
        papaya = self.trie.find("papaya")
        pitaya = self.trie.find("pitaya")
        raspberry = self.trie.find("raspberry")
        strawberry = self.trie.find("strawberry")
        tangerine = self.trie.find("tangerine")
        orange = self.trie.find("orange")

        self.assertTrue(apple)
        self.assertTrue(banana)
        self.assertTrue(bananarama)
        self.assertTrue(grape)
        self.assertTrue(grapefruit)
        self.assertTrue(lemon)
        self.assertTrue(mango)
        self.assertTrue(mangosteen)
        self.assertTrue(papaya)
        self.assertTrue(pitaya)
        self.assertTrue(raspberry)
        self.assertTrue(strawberry)
        self.assertTrue(tangerine)
        self.assertFalse(orange)

    def test_list_items(self):
        path = os.path.join("src","tests", "data", "test_file.txt")
        self.trie.read_file(path)

        self.trie.list_items(self.trie.root, "")

        expected_list = ['apple', 'banana', 'bananarama', 'grape',
                         'grapefruit', 'lemon', 'mango', 'mangosteen',
                         'papaya', 'pitaya', 'raspberry', 'strawberry',
                         'tangerine']

        self.assertEqual(self.trie.list, expected_list)
