# Requirements specification

## Description

With the spell checker, it will be possible to check the spelling of English
texts. The application will find incorrectly spelled words and
provide suggestions for the misspellings.

It will use an algorithm that calculates the Damerau-Levenshtein distance
between words.

The input will be text provided by the user of the spell checker. Each word
will be compared to a dataset of correctly spelled English words. If a word
provided by the user cannot be found in the dataset, the spell checker will
assume it was misspelled and try to provide a corrected spelling.

The spell checker will scan the words one by one. In-depth analysis of
the context or the meaning of the words will be beyond the scope of this
project.

## Time and space complexities

- I will use a trie data structure to search for words in the dataset. This can be done in a
O(n) time complexity. N stands for the length of the input word. [1]

- Calculating the Damerau-Levenshtein distance between two words/strings can be done
in between O(n³) and O(n * m) time complexities, where n and m are string
lengths. I will aim at an efficient algorithm with a total time complexity of O(n * m). [2]

The space complexity that I aim at is O(n * m). The trie data structure demands
this much space. N and m stand for the size and number of the strings stored in
the trie. [1]

## Languages

The programming language will be Python.

The documentation and the code of the project will be written in English. The
project belongs in the curriculum of the Finnish degree tietojenkäsittelytieteen kandidaatti
(TKT).

## Sources

[1] https://www.geeksforgeeks.org/introduction-to-trie-data-structure-and-algorithm-tutorials/

[2] https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance
