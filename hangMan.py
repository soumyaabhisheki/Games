import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words) #randomly chooses a word from the list
    while '-' in word or ' ' in word: #returns a word without - or space in it
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #to keep track of letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # to keep track of what user has guessed
    lives = 6

    #user letter input
    while len(word_letters)>0 and lives >0:
        #for user to know the listof guessed words
        print("You have ",lives," lives left.You Have Used These Letters: ",' '.join(used_letters))
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print("Current Word: ",' '.join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print("Letter is not in the word.")

        elif user_letter in used_letters:
            print("Letter Guessed Already.Please try again!")

        else:
            print("Invalid Input. Please try Again!")
    if lives == 0:
        print("Sorry You Died!! The word is ",word)
    else:
        print("You guessed the word",word)

hangman()