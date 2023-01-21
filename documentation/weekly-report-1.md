# Weekly report 1

This week I have chosen the topic for my project. I will work on a spell
checker. I chose the topic because it interested me the most. I have studied
some linguistics in the past and languages have always fascinated me.

This far the project has been initialized, but I haven't written any code yet. I
have written the documentation on requirements specificaton, thought about how
to get the project started and searched information about the relevant data
structures and algorithms.

I have a vague idea on how to get going:
- I need to find a dataset of English words.
- I need to study the trie data structure.
- I need to save the dataset in a trie structure.
- I need to study and understand the Damerau-Levenshtein distance algorithm and
  utilize it in the project.

Things I am unsure about or interested in getting feedback on:
- I would like general feedback on the chosen topic and how I have described
  my project in the [requirements specification](./requirements-specification.md) document.
- The time and space complexities of the project. In the [requirements
  specification](./requirements-specification.md) document I have estimated the complexities that I am aiming at. Since I am still unfamiliar with both the trie data structure and the Damerau-Lenvenshtein distance algorithm I would appreciate feedback on whether my estimations are on the right track or not.
- I will be able to calculate the Damerau-Levenshtein distance for two words. However, the English dataset will have a large amount of words, and it is not realistic to calculate the distance to all of them for every word that the user inputs. I will need to pick words that are somewhat close to the input, but I'm not sure how to do that. Should I first calculate the Damerau-Levenshtein distances between *all* the words in the dataset and store them in another data structure?

This week I have spent 2 + 3 + 5 = 10 hours on the project.
