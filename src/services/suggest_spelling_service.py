from algorithms.damerau_levenshtein import DamerauLevenshtein

class SuggestSpelling:
    """
    Suggest a correct spelling for a word that was not among the accepted
    words.
    """
    def __init__(self, trie: object, frequency_list: list):
        self.trie = trie
        self.damlev = DamerauLevenshtein()
        self.frequency_list = frequency_list

    def suggest_spelling(self, word):
        """
        Suggest a correctly spelled word.

        Args:
            word: String. The misspelled word input by the user.

        Returns: String. A correctly spelled word that is close to the original word in
                 Damerau-Levenshtein distance.
        """
        mindist = 1000
        candidate = ""
        for accepted_word in self.frequency_list:
            distance = self.damlev.calculate_distance(
                                            word,
                                            accepted_word.lower())
            if distance < mindist:
                mindist = distance
                candidate = accepted_word
                if distance == 1:
                    return candidate
        return candidate
