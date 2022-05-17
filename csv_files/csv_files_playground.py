import csv
import os
# with open ("/ H:\Neeta_SheCode\python_repo\she-codes-python-exercises-neets1981\csv_files") as file:
#     file_reader=csv.reader(file)
#     for row in file_reader:
#         print(row)

'''with open ("csv_files/2016_pilbara.csv") as file: # file is variable 
        file_reader=csv.reader(file) # create object called file_reader
        for row in file_reader: # row is arbitary vriable and it can be anything 
            print(row) '''


# CSV Files Exercises Q4 - code for the example we worked through in class
with open ("csv_files/2016_pilbara.csv") as CSV_file: # file is variable      

    list_words = ['red', 'green', 'blue', 'yellow']
    red_total = 0
    green_total = 0
    blue_total = 0
    yellow_total = 0
import csv 
with open("csv_files\colours_20.csv") as csv_file:
    reader = csv.reader(csv_file)
    # next(reader)         # to remove the first line in file (eg Header)
    for line in reader:
        # print(line[4])   # prints each word in that column of file (index [4]) on a new line
        if list_words[0] in line[4].lower(): #to make all the data lowercase as the list is lower case
            red_total += 1
        if list_words[1] in line[4].lower():
            green_total += 1
        if list_words[2] in line[4].lower():
            blue_total += 1
        if list_words[3] in line[4].lower():
            yellow_total += 1
print(f'Red: {red_total}')
print(f'Green: {green_total}')
print(f'Blue: {blue_total}')
print(f'Yellow: {yellow_total}')       