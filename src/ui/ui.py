import click
from services.check_spelling_service import CheckSpelling

class UI:
    def __init__(self, trie: object):
        self.trie = trie
        self.check_spelling = CheckSpelling(self.trie)

    def start(self):
        """Starts the user interface."""
        click.echo("Write 'q' to quit.")
        click.echo("Write a word for spellchecker.")

        while True:
            word = click.prompt("word")

            if word == "q":
                break
            else:
                correct = self.check_spelling.check_word(word.lower())
                if correct:
                    click.echo("great!")
                else:
                    click.echo("too bad :(")
