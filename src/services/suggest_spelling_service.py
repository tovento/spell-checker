from algorithms.damerau_levenshtein import DamerauLevenshtein

class SuggestSpelling:
    def __init__(self, trie: object):
        self.trie = trie
        self.damlev = DamerauLevenshtein()

    def suggest_spelling(self, word):
        mindist = 1000
        candidate = ""
        self.trie.list_items(self.trie.root, "")
        for accepted_word in self.trie.list:
            distance = self.damlev.calculate_distance(word, accepted_word)
            if distance < mindist:
                mindist = distance
                candidate = accepted_word
                if distance == 1:
                    return candidate
        return candidate
