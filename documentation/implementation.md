# Implementation

## Architecture

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
