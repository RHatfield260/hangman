import random as rd
import numpy as np
word_list = ['Apple','Banana','Orange','Pear','Grape']   
word = rd.choice(word_list).lower()
word_guessed = ['_']  * len(word)
num_letters = len(dict.fromkeys(word))
num_lives = 5
        
list_of_guesses = []

class Hangman:
    
    def __init__(self,word_list,num_lives):
        
        self.num_lives = num_lives
        self.word_list = word_list
    
    def check_guess(guess):
        global num_letters, num_lives
        guess = guess.lower()
        if guess in word:
            print('Good Guess!',guess, 'is in the word!')
            for i in range (len(word)+1):
                if guess == word[i-1]:
                    word_guessed[i-1] = guess
            num_letters -= 1
        else:
            num_lives -= 1
            print('Sorry ',guess," isn't in the word!")
            print('You have ',num_lives,' lives remaining.')
    
    def ask_for_input(): 
        while True:
            guess = input('Guess a letter:').strip()
            if guess.isalpha() == False or len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in list_of_guesses:
                print("You already tried that letter!")
            else:
                Hangman.check_guess(guess)
                list_of_guesses.append(guess)
Hangman.ask_for_input()

