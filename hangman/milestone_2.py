import random as rd
word_list = ['Apple','Banana','Orange','Pear','Grape']
word = rd.choice(word_list)
guess = input('Guess a Letter:')
guess = strip(guess)
while len(guess) != 1:
    guess = input('Oops! That is not a valid input! Please guess a single letter:')
print('Good Guess!')