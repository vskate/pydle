import random
from colors import *

#list of valid words
valid = open("valid-wordle-words.txt", "r").read()
f = open("wordle-La.txt", "r")
wordle_ls = []

#list of words that can be used as keys
for i in f:
    wordle_ls.append(i[:-1])

#word = input("input a word: ")

clear_screen()

#print out main menu
def print_menu():
    print("Welcome to \033[32mPYDLE\033[0m")
    print("select and press enter to continue:")
    print("1: start a new game")
    print("2: view scoreboard")
    print("q: exit")

def print_game_menu(tries, letters_used):
    print(f"Tries left: {tries}")
    print("Letters used: ", end="")
    for a in letters_used:
        print(a, end="")
    print("\n")

def print_tries(words, key):
    for i in words:
        curr = []
        for j in range(len(i)):
            curr.append(i[j])
        for x in range(5):
            if curr[x] in key:
                if curr[x] == key[x]:
                    green()
                    print(curr[x], end=" ")
                    reset()
                else:
                    yellow()
                    print(curr[x], end=" ")
                    reset()
            else:
                print(curr[x], end=" ")
        print("")


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





def game():
    
    key = wordle_ls[random.randint(0, len(wordle_ls))]
    
    tries = 6
    letters_used = []
    words = []

    while tries >= 0 :
        clear_screen()
        print(f"key = {key}")
        print_game_menu(tries, letters_used)
        print_tries(words, key)
        """for i in words:
            curr = []
            for j in range(len(i)):
                curr.append(i[j])
            for x in range(5):
                if curr[x] in key:
                    if curr[x] == key[x]:
                        green()
                        print(curr[x], end=" ")
                        reset()
                    else:
                        yellow()
                        print(curr[x], end=" ")
                        reset()
                else:
                    print(curr[x], end=" ")
            print("")"""
                    
        test = input("Input your try (5 letter word): ").lower()
        
        if test in valid and len(test)==5:
            words.append(test)
            if test == key:
                correct(key, test, words, tries)
            tries -= 1
        else:
            print("Incorrect word")

        
              

while True:
    clear_screen()
    print_menu()
    opt = input()
    if opt == 'q':
        break
    elif opt == '1':
        clear_screen()
        game()
    elif opt == '2':
        clear_screen()
        scoreboard()
    else:
        clear_screen()
        print("Incorrect option")


