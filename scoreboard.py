import csv

filename = 'score.csv'

def print_scoreboard():
    pass

def read_data():
    pass

def write_data(name, tries, key, words):
    global filename

    data = {'name': name, 'tries': tries, 'key': key, 'words': words}
    
    with open(filename, 'a') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)
    
        # write the data
        csvwriter.writerow(data.values())