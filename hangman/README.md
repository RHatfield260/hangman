# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

### Milestone 2:
This milestone involves creation of the core variable for the hangman game. The created variables are:
`word_list`: a list containing 5 words
`word`: a random single entry from the word_list list that is generated using the random module method random.choice()
`guess`: a simple user input that asks for a single letter. After it is selected, the answer is stripped of whitespace using .strip()
The `while` loop after the variables is designed to check that the input is a single character. The task asked for this to be done using an `if` then `else` statement but I prefer this option as it is simpler as well as allows the user to easily give a new input if the original guess was not valid.

### Milestone 3:
This milestone involves creation of the basic functions necessary for the hangman game. The first function `check_guess` takes a use input then converts to lower case. Following this the user input which is stored in the variable `guess` and checks if it is held in the `word` variable. Provided this condition is met, we `print` a simple message confirming this. The opposite is done if the conditions are not met.
The next function is the `ask_for_input` function. This function is what gets the user input that will be stored in the `guess` variable that we used earlier. We take the input and strip any whitespace and then check that the input is an alphabetic character and only a single character.A message confirming if this is correct or not (similar to the above function) is then printed. This is all held within an `while` loop that will repeat until the condition is met at which point we break from the loop.

### Milestone 4:
Milestone 4 begins creating a `class` to store the main building blocks of the game. The class `Hangman` contains the methods for the game which are extended versions of the `check_guess` and `ask_for_input` functions in milestone 3. It also creates 2 class perameters as well as several new global variables.The parameters are `word_list` that is the list of words defined previously and `num_lives` which stores the number of attempts the user has left to guess the word. The new global variables are `word_guessed` which stores an list of underscores equal to the length of the word, `num_letters` which stores the length of the word the user has to guess, and `list_of_guesses` which is an empty list that adds every guessed letter to it to prevent the user repeating guesses.  

### Milestone 5:
The final milestone for this project was creating the final function `play game` that allows the user to actually play the game. It defines the number of lives the user has and stores it in `num_lives`. It then allows the user to guess letters until either they have no lives left or they guess all the letters in the word. 