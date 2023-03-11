import csv
import functions
import os

csvFilepath = "Data/TwitterExport/data.csv"
rows = functions.read_csv_file(csvFilepath)

for i in range(len(rows)):
    print(rows[i])
    if i == 10:
        break

conversations = functions.generate_conversations_quotes(rows, False)
print(len(conversations))

