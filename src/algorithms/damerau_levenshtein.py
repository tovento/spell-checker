class DamerauLevenshtein():
    def __init__(self):
        pass

    def calculate_distance(self, word1: str, word2: str):
        """
        Calculate the Damerau-Levenshtein distance between two
        words.

        Args:
            word1: String. First word used for calculation.
            word2: String. Second word used for calculation.

        Returns: Integer. The Damerau-Levenshtein distance between word1 and word2.
        """
        len1 = len(word1)
        len2 = len(word2)

        matrix = self.create_matrix(len1, len2)

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
                                            self.calculate_substitution(
                                                matrix, row, column,
                                                substitution_cost),
                                            self.calculate_addition(
                                                matrix, row, column),
                                            self.calculate_deletion(
                                                matrix, row, column),
                                            self.calculate_transposition(
                                                matrix, row, column,
                                                last_matching_row,
                                                last_matching_column))

                if substitution_cost == 0:
                    last_matching_column = column

            last_row_with_letter[word1_char] = row

        return matrix[-1][-1]

    def create_matrix(self, len1, len2):
        """Create a matrix the size of (len1 + 2) * (len2 + 2)."""
        maxdist = len1 + len2

        matrix = [[maxdist for _ in range(len2+2)]]
        matrix += [[maxdist] + list(range(len2 + 1))]
        matrix += [[maxdist, x] + [0] * len2 for x in range(1, len1 + 1)]

        return matrix

    def calculate_substitution(self, matrix: list, row: int, column: int, substitution_cost: int):
        """Calculate the cost of substitution."""
        return matrix[row][column] + substitution_cost

    def calculate_addition(self, matrix: list, row: int, column: int):
        """Calculate the cost of addition. """
        return matrix[row+1][column] + 1

    def calculate_deletion(self, matrix: list, row: int, column: int):
        """Calculate the cost of deletion."""
        return matrix[row][column+1] + 1

    def calculate_transposition(self, matrix: list, row: int,
                                column: int, last_matching_row: int,
                                last_matching_column: int):
        """Calculate the cost of transposition."""
        return (matrix[last_matching_row][last_matching_column]
                + (row - last_matching_row - 1) + 1
                + (column - last_matching_column -1))
