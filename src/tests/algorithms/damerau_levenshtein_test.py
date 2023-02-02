import unittest
from algorithms.damerau_levenshtein import DamerauLevenshtein

class TestDamerauLevenshtein(unittest.TestCase):
    def setUp(self):
        self.dl = DamerauLevenshtein()

    def test_addition(self):
        word1 = "cat"
        word2 = "catnip"
        distance = self.dl.calculate_distance(word1, word2)

        self.assertEqual(distance, 3)

    def test_deletion(self):
        word1 = "doghill"
        word2 = "dghll"
        distance = self.dl.calculate_distance(word1, word2)

        self.assertEqual(distance, 2)

    def test_substitution(self):
        word1 = "moon"
        word2 = "noon"
        distance = self.dl.calculate_distance(word1, word2)

        self.assertEqual(distance, 1)

    def test_transposition(self):
        word1 = "algorithm"
        word2 = "lagorithm"
        distance = self.dl.calculate_distance(word1, word2)

        self.assertEqual(distance, 1)

    def test_transposition_with_addition(self):
        word1 = "abcd"
        word2 = "acxbd"
        distance = self.dl.calculate_distance(word1, word2)

        self.assertEqual(distance, 2)
