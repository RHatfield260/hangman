import random as rd
word_list = ['Apple','Banana','Orange','Pear','Grape']
word = rd.choice(word_list)
def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print('Good Guess!',guess, 'is in the word!') 
    else:
        print('Bad luck!',guess,"isn't in the word")   

def ask_for_input():
    while True:
        guess = input('Guess a letter:').strip()
        if guess.isalpha() == True and len(guess) == 1:
            break
        else:
            print('That was an invalid guess!')
    check_guess(guess)
ask_for_input()