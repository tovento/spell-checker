# Weekly report 3

Things I did this week:
- Added another dataset of English words, this time ordered by frequency
- Wrote an algorithm that calculates the Damerau-Levenshtein distance between
  two words
- Wrote unit tests testing the algorithm, the algorithm seems to work
- Started to write the [test documentation](./test-docs.md)

Next I will look into the following issues:
- Clean up the code of the algorithm a little bit
- Write an application that uses the algorithm. The application should 
    - use a dataset of English words to check if a word is among them and acceptable
    - if the word is not among the accepted English words, the app will
      calculate the DL distances between the word and the acceptable words
    - the app will then suggest one or more acceptable English words that have
      the smallest DL distance with the original word
- Write a user interface
- Write more tests as the project grows

Things I am unsure about:
- Nothing urgent at the moment, but I'm looking forward to receiving general feedback
  about my progress.

This week I have spent 4 + 2 + 7 + 2 + 3 + 1 = 19 hours on the project.
