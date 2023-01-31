class DamerauLevenshtein():
    def __init__(self):
        pass

    def calculate_distance(self, word1, word2):
        len1 = len(word1)
        len2 = len(word2)

        maxdist = len1 + len2

        matrix = [[maxdist for _ in range(len2+2)]]
        matrix += [[maxdist] + list(range(len2 + 1))]
        matrix += [[maxdist, x] + [0] * len2 for x in range(1, len1 + 1)]
