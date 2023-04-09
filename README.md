# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

Milestone 2:
This milestone involves creation of the core variable for the hangman game. The created variables are:
word_list: a list containing 5 words
word: a random single entry from the word_list list that is generated using the random module method random.choice()
guess: a simple user input that asks for a single letter. After it is selected, the answer is stripped of whitespace using .strip()
The while loop after the variables is designed to check that the input is a single character. The task asked for this to be done using an if else statement but I prefer this option as it is simpler as well as allows the user to easily give a new input if the original guess was not valid
