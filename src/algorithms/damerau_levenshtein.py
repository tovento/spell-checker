class DamerauLevenshtein():
    def __init__(self):
        pass

    def calculate_distance(self, word1: str, word2: str):
        """
        A function to calculate the Damerau-Levenshtein distance between two
        words.

        Args:
            word1: String. First word used for calculation.
            word2: String. Second word used for calculation.

        Returns: Integer. The Damerau-Levenshtein distance between word1 and word2.
        """
        len1 = len(word1)
        len2 = len(word2)

        maxdist = len1 + len2

        matrix = [[maxdist for _ in range(len2+2)]]
        matrix += [[maxdist] + list(range(len2 + 1))]
        matrix += [[maxdist, x] + [0] * len2 for x in range(1, len1 + 1)]

        last_row_with_letter = {}

        for row in range(1, len1+1):
            word1_char = word1[row-1]

            last_matching_column = 0

            for column in range(1, len2+1):
                word2_char = word2[column-1]

                if word2_char not in last_row_with_letter:
                    last_matching_row = 0
                else:
                    last_matching_row = last_row_with_letter[word2_char]

                if word1_char == word2_char:
                    substitution_cost = 0
                else:
                    substitution_cost = 1

                matrix[row+1][column+1] = min(
                        matrix[row][column] + substitution_cost,
                        matrix[row+1][column] + 1,
                        matrix[row][column+1] + 1,
                        matrix[last_matching_row][last_matching_column]
                            + (row - last_matching_row - 1) + 1
                            + (column - last_matching_column - 1))

                if substitution_cost == 0:
                    last_matching_column = column

            last_row_with_letter[word1_char] = row

        return matrix[-1][-1]
