import random
from colors import *
from scoreboard import *
from printout import *

#list of valid words
valid = open("valid-wordle-words.txt", "r").read()
f = open("wordle-La.txt", "r")
wordle_ls = []

#list of words that can be used as keys
for i in f:
    wordle_ls.append(i[:-1])

clear_screen()

def correct(key, test, words, tries):
    won_in = 6 - tries
    
    clear_screen()
    green()
    print(f"{test} ", end="")
    reset()
    print("is correct!")
    print(f"Guessed in: {won_in} tries")

    print("list of words tried: ")
    print_tries(words, key)

    print("Insert your name: ", end="")
    write_data(input(), 6-tries, key, words, 'score.csv')

    print("Type anything to go back to the menu: ", end="")
    input()

def game():
    
    key = wordle_ls[random.randint(0, len(wordle_ls))]
    
    tries = 6
    letters_used = []
    words = ()

    while tries > 0 :
        clear_screen()
        print(f"key = {key}")
        print_game_menu(tries, letters_used)
        print_tries(words, key)
                    
        test = input("Input your try (5 letter word): ").lower()

        if test == key:
            return True, key, test, words, tries
        
        if test in valid and len(test)==5:
            words = words + (test,)
            for a in range(len(test)):
                if test[a] not in letters_used:
                    letters_used.append(test[a])
            tries -= 1
        else:
            print("Incorrect word")

    clear_screen()
    red()
    print("YOU LOST!")
    reset()
    print(f"Correct word: ", end="")
    green()
    print(key)
    reset()
    
    print("Your guesses:")
    print_tries(words, key)

    print("Insert your name: ", end="")
    write_data(input(), 6-tries, key, words, 'score.csv')

    print("press any key to go back to the menu: ", end="")
    input()
    
    return False, key, test, words, tries
              
while True:
    clear_screen()
    print_menu()
    opt = input()
    if opt == 'q':
        break
    elif opt == '1':
        clear_screen()
        won, key, test, words, tries = game()
        if won:
            correct(key, test, words, tries)
    elif opt == '2':
        clear_screen()
        scoreboard()
    else:
        clear_screen()
        print("Incorrect option")