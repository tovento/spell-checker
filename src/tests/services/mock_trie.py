class MockTrie:
    """
    A class to mock the Trie data structure for testing purposes. Does not have
    the structure or functions or a real trie.
    """
    def __init__(self, return_value: bool):
        self.return_value = return_value

    def find(self, parameter_word: str):
        self.parameter_word = parameter_word
        return self.return_value
