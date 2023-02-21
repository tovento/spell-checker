import unittest
from services.suggest_spelling_service import SuggestSpelling
from tests.services.mock_damerau_levenshtein import MockDamerauLevenshtein

class TestSuggestSpelling(unittest.TestCase):
    """Test that SuggestSpelling service works as expected."""
    def test_ss_returns_closest_word(self):
        word = "misspelled word"
        test_dict = {'insignificant word': 5,
                           'correct word': 2,
                           'random word': 3}
        suggestion_service = self.initialize_suggestion_service(test_dict)

        result = suggestion_service.suggest_spelling(word)

        self.assertEqual(result[0], 'correct word')

    def test_original_word_is_returned_if_correct(self):
        word = "cat"
        test_dict = {'rat': 1, 'hat': 1, 'cat': 0, 'mat': 1}
        suggestion_service = self.initialize_suggestion_service(test_dict)

        result = suggestion_service.suggest_spelling(word)

        self.assertEqual(result[0], 'cat')

    def test_suggestions_are_in_right_order(self):
        word = "kumble"
        test_dict = {'bumble': 1, 'rumble': 1 , 'mumble': 1, 'humble': 1}
        suggestion_service = self.initialize_suggestion_service(test_dict)

        result = suggestion_service.suggest_spelling(word)

        self.assertEqual(result, ['bumble', 'rumble', 'mumble'])

    def test_bigger_distances_will_not_be_in_list(self):
        word = "testing"
        test_dict = {'resting': 1, 'wrestling': 3}
        suggestion_service = self.initialize_suggestion_service(test_dict)

        result = suggestion_service.suggest_spelling(word)

        self.assertEqual(result, ['resting'])

    def initialize_suggestion_service(self, test_dictionary):
        mock_dl = MockDamerauLevenshtein(test_dictionary)
        suggestion_service = SuggestSpelling(list(test_dictionary.keys()))
        suggestion_service.damlev = mock_dl
        return suggestion_service
