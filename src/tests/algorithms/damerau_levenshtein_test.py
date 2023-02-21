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

    def test_multiple_distances(self):
        original_word = "distance"
        variation1 = "sistance"
        variation2 = "disstanc"
        variation3 = "idstanec"
        variation4 = "idtsnaec"
        variation5 = "suarabxw"

        distance1 = self.dl.calculate_distance(original_word, variation1)
        distance2 = self.dl.calculate_distance(original_word, variation2)
        distance3 = self.dl.calculate_distance(original_word, variation3)
        distance4 = self.dl.calculate_distance(original_word, variation4)
        distance5 = self.dl.calculate_distance(original_word, variation5)

        self.assertEqual(distance1, 1)
        self.assertEqual(distance2, 2)
        self.assertEqual(distance3, 2)
        self.assertEqual(distance4, 4)
        self.assertEqual(distance5, 7)
