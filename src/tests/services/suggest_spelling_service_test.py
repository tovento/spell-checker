import unittest
from services.suggest_spelling_service import SuggestSpelling
from tests.services.mock_damerau_levenshtein import MockDamerauLevenshtein

class TestSuggestSpelling(unittest.TestCase):
    """Test that SuggestSpelling service works as expected."""
    def test_suggest_spelling(self):
        word = "misspelled word"
        test_dictionary = {'insignificant word': 5,
                           'correct word': 2,
                           'random word': 3}
        mock_dl = MockDamerauLevenshtein(test_dictionary)
        suggestion_service = SuggestSpelling(['insignificant word',
                                              'correct word',
                                              'random word'])
        suggestion_service.damlev = mock_dl
        result = suggestion_service.suggest_spelling(word)

        self.assertEqual(result, 'correct word')
