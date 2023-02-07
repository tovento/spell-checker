class CheckSpelling:
    """Check the spelling of a given word."""
    def __init__(self, trie: object):
        """
        Constructor.

        Args:
            trie: Object. Data structure containing all of the acceptable strings.
        """
        self.trie = trie

    def check_word(self, word: str):
        """Check the spelling.

        Args:
            word: String. A word input by the user.

        Returns: Boolean.
        """
        return self.trie.find(word)
