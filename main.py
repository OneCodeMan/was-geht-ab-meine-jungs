import csv
import os
import pathlib

# Get all files of directory
path = pathlib.Path(__file__).parent.absolute() # directory of script
extension = '.csv'

files = os.listdir(path)    
files = list(filter(lambda f: f.endswith(extension), files))

passages = []

# Get all passages and store in list
for file in files:
    with open(file) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            passage = row[3]

            passages.append(passage)

# Clean passages variable, get rid of newlines
passages = [passage for passage in passages if passage][1:]

# Save in text file
file_name = 'lines.txt'
f = open(file_name,'w')
l1 = map(lambda x: x+'\n', passages)
f.writelines(l1)
f.close()

# next step, make a pdf
# https://realpython.com/creating-modifying-pdf/#creating-a-pdf-file-from-scratch