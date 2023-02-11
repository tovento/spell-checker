import click
from services.check_spelling_service import CheckSpelling
from services.suggest_spelling_service import SuggestSpelling

class UI:
    def __init__(self, trie: object):
        self.trie = trie
        self.check_spelling = CheckSpelling(self.trie)
        self.suggest_spelling = SuggestSpelling(self.trie)

    def start(self):
        """Start the user interface."""
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
                    suggestion = self.suggest_spelling.suggest_spelling(word.lower())
                    click.echo(f"Did you mean {suggestion}?")
