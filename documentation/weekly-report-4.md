# Weekly report 4

Things I did this week:
- some cleaning and refactoring of the DL algorithm
- wrote a simple user interface -> now the application can be executed and tested
  manually
- wrote [a service](../src/services/check_spelling_service.py) that checks if the spelling of a word is acceptable
- wrote [a service](../src/services/suggest_spelling_service.py) that suggests a corrected spelling
- initially the application was **very slow** in suggesting correctly spelled
  words. I made some changes and now the user experience is better with a much faster
  response.
- updated the [tests for the trie
  structure](../src/tests/data_structures/trie/trie_test.py) a little bit
- documentation

Things I will do next:
- testing is lagging behind, with test coverage going down from 100 % to 54 %
  this week:
    - tests for the services are missing and need to be written
    - the existing tests need to be examined and made more complete
- the application should return better suggestions. At the moment it suggests a
  word with a small DL distance - which is good - but it can be made better. It
  could e.g. take into account the proximity of letters on the keyboard.
- more documentation
- at the moment the application checks only individual words. Later on, the application could check the spelling of sentences or other longer strings

Things I am unsure about:
- nothing urgent at the moment

This week I have spent 5 + 4 + 2 + 4 + 4 = 19 hours on the project.
