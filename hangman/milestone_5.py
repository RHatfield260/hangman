import random as rd
word_list = ['Apple','Banana','Orange','Pear','Grape']   
word = rd.choice(word_list).lower()
word_guessed = ['_']  * len(word)
num_letters = len(dict.fromkeys(word))
list_of_guesses = []

def play_game(word_list):
    global num_lives
    num_lives = 5
    game = Hangman(word_list,num_lives)
    print('Lets play Hangman! Try and guess my word!')
    while True:
        if num_lives == 0:
            print('Game over, you lose! The word was',word)
        if num_letters > 0:
            print('You have',num_lives,'lives left.',word_guessed)
            Hangman.ask_for_input()
        if num_lives != 0 and num_letters < 1:
            print('Congratulations you won! The word was',word.title())
            break

class Hangman:
    
    def __init__(self,word_list,num_lives):
        self.num_lives = num_lives
        self.word_list = word_list
    
    def check_guess(guess):
        global num_letters, num_lives
        guess = guess.lower()
        if guess in word:
            for i in range (len(word)+1):
                if guess == word[i-1]:
                    word_guessed[i-1] = guess
            num_letters -= 1
            print('Good guess!',guess.upper(),'was in the word!')
        else:
            num_lives -= 1
            print('Sorry ',guess.upper()," isn't in the word!")
            
    
    def ask_for_input(): 
        guess = input('Guess a letter:').strip()
        if guess.isalpha() == False or len(guess) != 1:
            print("Invalid letter. Please, enter a single alphabetical character.")
        elif guess in list_of_guesses:
            print("You already tried that letter!")
        else:
            Hangman.check_guess(guess)
            list_of_guesses.append(guess)
play_game(word_list)