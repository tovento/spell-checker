import os
import click
from ui.ui import UI
from data_structures.trie.trie import Trie

class Main:
    """Start up the application."""
    def __init__(self):
        click.echo("Initializing...")
        self.trie = Trie()
        path = os.path.join("data", "english-words.txt")
        self.trie.read_file(path)

        self.frequency_list = self.read_frequency_file()

        self.start_ui()

    def read_frequency_file(self):
        frequency_list = []
        path = os.path.join("data", "wiktionary-40k.txt")
        with open(path, encoding="utf-8") as file:
            for word in file.readlines():
                frequency_list.append(word.strip())
        return frequency_list

    def start_ui(self):
        user_interface = UI(self.trie, self.frequency_list)
        user_interface.start()

if __name__ == "__main__":
    Main()
