# Weekly report 4

Things I did this week:
- some cleaning and refactoring of the DL algorithm
- wrote a simple user interface -> now the application can be executed and tested
  manually
- wrote [a service](../src/services/check_spelling_service.py) that checks if the spelling of a word is acceptable
- wrote [a service](../src/services/suggest_spelling_service.py) that suggests a corrected spelling
- documentation

Things I will do next:
- tests for the services are missing and need to be written
- the existing tests need to be examined and made more complete
- the application is slow: it doesn't take long to check if the given word is
  acceptable, but suggesting a correct spelling seems to take **a lot of time**.
  This is problematic and needs attention.
- the trie data structure needs a little debugging regarding attribute 'list'
- more documentation

This week I have spent 5 + 4 + 2 + 4  = X hours on the project.
