from algorithms.damerau_levenshtein import DamerauLevenshtein

class SuggestSpelling:
    """
    Suggest correct spellings for a word that was not among the accepted
    words.
    """
    def __init__(self, frequency_list: list):
        self.damlev = DamerauLevenshtein()
        self.frequency_list = frequency_list

    def suggest_spelling(self, word):
        """
        Suggest correctly spelled words.

        Args:
            word: String. The misspelled word input by the user.

        Returns: List of strings. Three correctly spelled words that are close
                 to the original word in Damerau-Levenshtein distance.
        """
        mindist = 1000
        candidates = []
        for accepted_word in self.frequency_list:
            distance = self.damlev.calculate_distance(
                                            word,
                                            accepted_word.lower())
            if distance < mindist:
                mindist = distance
                if len(candidates) == 3:
                    candidates.pop()
                candidates.insert(0, (accepted_word, distance))
            elif distance == mindist:
                if len(candidates) == 3:
                    if candidates[-1][1] <= distance:
                        continue
                    candidates.pop()
                    if candidates[-1][1] == mindist:
                        candidates.append((accepted_word, distance))
                    else:
                        candidates.insert(1, (accepted_word, distance))
                else:
                    candidates.append((accepted_word, distance))

        return [candidate[0] for candidate in candidates]
