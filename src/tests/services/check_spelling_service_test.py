import unittest
from services.check_spelling_service import CheckSpelling
from tests.services.mock_trie import MockTrie

class TestCheckSpelling(unittest.TestCase):
    """Test that CheckSpelling service works as expected."""
    def test_check_spelling_with_misspelled_word(self):
        trie = MockTrie(False)
        word = "badly misspelled word"
        result = trie.find(word)

        self.assertFalse(result)
        self.assertEqual(word, trie.parameter_word)

    def test_check_spelling_with_accepted_word(self):
        trie = MockTrie(True)
        word = "problem"
        result = trie.find(word)

        self.assertTrue(result)
        self.assertEqual(word, trie.parameter_word)
