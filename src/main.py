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

        self.start_ui()

    def start_ui(self):
        user_interface = UI(self.trie)
        user_interface.start()

if __name__ == "__main__":
    Main()
