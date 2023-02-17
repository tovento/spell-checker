class MockDamerauLevenshtein:
    """
    A class to mock the Damerau-Levenshtein algorithm for testing purposes.
    Does not calculate actual Damerau-Levenshtein distances.
    """
    def __init__(self, test_dictionary: dict):
        self.test_dictionary = test_dictionary

    def calculate_distance(self, word1, word2):
        return self.test_dictionary[word2]
