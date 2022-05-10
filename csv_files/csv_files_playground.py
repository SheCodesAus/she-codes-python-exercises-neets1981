import csv
import os
# with open ("/ H:\Neeta_SheCode\python_repo\she-codes-python-exercises-neets1981\csv_files") as file:
#     file_reader=csv.reader(file)
#     for row in file_reader:
#         print(row)

with open ("csv_files/2016_pilbara.csv") as file:
        file_reader=csv.reader(file)
        for row in file_reader:
            print(row) 