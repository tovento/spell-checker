# Spell checker

## About

The spell checker is a project work for the course Datastructures and Algorithms
Lab of Helsinki University. The development will take place from January to
March 2023.

With the spell checker, a user can check the correct spelling of English words.
It is a command-line application with a text-based user interface.

## Requirements

The application has been developed and tested using Python 3.10.6. It may not work as
intended if used with an older version of Python.

To use the application, one should have [Poetry](https://python-poetry.org/)
installed first.

## Command line instructions

### Starting the application

```
poetry run invoke start
```

### Running a pylint check

```
poetry run invoke pylint
```

### Running the tests

```
poetry run invoke test
```

### Creating a test coverage report

```
poetry run invoke coverage-report
```
## Data

[The dataset of English words](./data/english-words.txt) is taken from
https://github.com/dwyl/english-words. Copyright belongs to Infochimps: [https://www.infochimps.com/datasets/word-list-350000-simple-english-words-excel-readable](https://web.archive.org/web/20131118073324/https://www.infochimps.com/datasets/word-list-350000-simple-english-words-excel-readable) (archived).

[Another dataset of English words listed by
frequency](./data/wiktionary-40k.txt) is taken from
[Wiktionary](https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists#Project_Gutenberg) and includes a bit less than 40 000 of the most common words from [Project Gutenberg](https://en.wikipedia.org/wiki/Project_Gutenberg).

## Documentation

[Requirements specification](./documentation/requirements-specification.md)

[Test documentation](./documentation/test-docs.md)

### Weekly reports

[Week 1](./documentation/weekly-report-1.md)

[Week 2](./documentation/weekly-report-2.md)

[Week 3](./documentation/weekly-report-3.md)

[Week 4](./documentation/weekly-report-4.md)
