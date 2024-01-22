from colors import *

#print out main menu
def print_menu():
    green()
    print_logo()
    reset()
    print("select and press enter to continue:")
    print("1: start a new game")
    print("2: view scoreboard")
    print("q: exit")

def print_game_menu(tries, letters_used):
    print(f"Tries left: {tries}")
    print("Letters used: ", end="")
    letters_used.sort()
    for a in letters_used:
        print(a, end=" ")
    print("\n")

def print_tries(words, key):
    for i in words:
        curr = []
        for j in range(len(i)):
            curr.append(i[j])
        for x in range(len(curr)):
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