import csv
import ast
from colors import *
from utils import *


filename = 'score.csv'

csvfile = open(filename, "r+")

def scoreboard():
    #clear_screen()
    data = read_data()

    dict_ls = []

    for row in data:
        curr = {'name': row[0], 'tries': int(row[1]), 'key': row[2], 'words': row[3]}
        
        dict_ls.append(curr)

    dict_ls = bubble_sort_dicts(dict_ls, 'tries') #sort the dictionaries by the 'tries' key

    for i in range(len(dict_ls)):
        print(f"{i+1}. Name: {dict_ls[i]['name']} tries: {dict_ls[i]['tries']} key: {dict_ls[i]['key']}")
        words = ast.literal_eval(dict_ls[i]['words'])
        print("    Words tried:")
        for i in range(len(words)):
            print("        " + words[i])


    input("Input anything to continue: ")

def read_data():
    global filename
    global csvfile

    csvreader = csv.reader(csvfile)

    return csvreader
        

def write_data(name, tries, key, words):
    global filename
    global csvfile

    data = {'name': name, 'tries': tries, 'key': key, 'words': words}
    
    csvwriter = csv.writer(csvfile)

    csvwriter.writerow(data.values())

def print_scoreboard():
    pass