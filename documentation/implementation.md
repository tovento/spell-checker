# Implementation

## Architecture

The application has the following packages:

![](./pictures/package-diagram.png)

- The package _ui_ is responsible for the user interface.
- The package _services_ is responsible for the logic of the application.
    - CheckSpelling checks if the input from the user is correctly
      spelled or not
    - SuggestSpelling suggests correctly spelled words for the
      misspelled ones
- The package _data_structures_ contains the data structures that were coded for
  this project
    - TrieNode represents one node in the trie structure
    - Trie represents a trie data structure
- The package _algorithms_ contains the algorithms needed for the project
    - DamerauLevenshtein is an algorithm that calculates the Damerau-Levenshtein distance between two strings

## Process interactions

![](./pictures/sequence-diagram.png)

After startup and initialization, the UI of the application asks the user to write a word
for a spell check.

The UI will pass the word onto the 'CheckSpelling' service. The service will
use a trie data structure consisting of 350 000 correctly spelled words to check if the original
word is among them.

If the word is spelled in an acceptable way, the user gets a quick feedback
(the text "great", at the moment).

If the word seems to be misspelled, the UI will then call the 'SuggestSpelling'
service. This service will use a list of 40 000 correctly spelled words that is sorted by their frequency. It will calculate the Damerau-Levenshtein(DL) distance between the original word and the words on the list. It returns a candidate from the list with as small DL distance as possible.

Finally, the UI will suggest this candidate to the user.

## Time and space complexities

A trie data structure is used to search for words in the dataset. This is done in a O(n) time complexity. N stands for the length of the input word.

The Damerau-Levenshtein algorithm that is used for the application has O(n * m) time
complexity, where n and m mean the lengths of the two strings compared.

The space complexity of the application is O(n * m). The trie data structure demands this much space. N and m stand for the size and number of the strings stored in the trie.

## Data

The application uses two lists of English words:
- [The dataset of English words](../data/english-words.txt) is taken from
https://github.com/dwyl/english-words. Copyright belongs to Infochimps: [https://www.infochimps.com/datasets/word-list-350000-simple-english-words-excel-readable](https://web.archive.org/web/20131118073324/https://www.infochimps.com/datasets/word-list-350000-simple-english-words-excel-readable) (archived).
    - This list has approximately 350 000 words
    - Used to check whether the original word is spelled correctly or not

- [Another dataset of English words listed by
frequency](../data/wiktionary-40k.txt) is taken from
[Wiktionary](https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists#Project_Gutenberg) and includes a bit less than 40 000 of the most common words from [Project Gutenberg](https://en.wikipedia.org/wiki/Project_Gutenberg).
    - This list has approximately 40 000 words
    - The list has the most commonly used words and is sorted by frequency
    - Used to recommend correct spellings

### Inconsistencies

Due to the data it uses, there may be times the spell checker works against the
expectations of the user. There are more than 300 000 words that are accepted (=found in the
first list) but will never be recommended to the user (=not included in the
sorted list). This is a known issue resulting from the following:
- the first list has to be as large as possible to avoid miscategorizing correctly spelled words
- the second list has to be sorted to give the most relevant suggestions
- a sorted list as extensive as the first list was not readily available

It is also possible that some words are included in both lists but are spelled
in a slightly different way. In this case the spell checker may judge a word
misspelled but then suggest the exact same spelling to the user. Some
example of this are the spellings "am" vs. "a.m." and "pm" vs. "p.m.". The bigger
list includes the spellings "am" and "pm" whereas the smaller list has "a.m." and
"p.m.". In this case, if the user inputs "a.m." the spell checker will not
accept it as correctly spelled but will then suggest the same spelling ("a.m.")
back to the user.

## Sources

- Au Yeung, Albert 2020: [Implementing Trie in
  Python](https://albertauyeung.github.io/2020/06/15/python-trie.html/). Web
article. Retrieved 23 Jan 2023.

- [Damerau-Levenshtein
  distance](https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance). Wikipedia article. Retrieved 2 March 2023.

- Jensen II, James M. 2018: [Damerau-Levenshtein Edit Distance
  Explained](https://www.lemoda.net/text-fuzzy/damerau-levenshtein/). Web
article. Retrieved 2 Feb 2023.

- [Trie](https://en.wikipedia.org/wiki/Trie). Wikipedia article. Retrieved 23
  Jan 2023.

- [Trie | (Insert and
  Search)](https://www.geeksforgeeks.org/trie-insert-and-search/). Web
article. Retrieved 23 Jan 2023.
