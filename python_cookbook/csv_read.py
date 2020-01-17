import csv
FILENAME = "trips.csv"
spreadsheet = []
with open(FILENAME, newline="") as file: # read from CSV file
    reader = csv.reader(file) # selected reader
    for row in reader: # for each row...
        spreadsheet.append(row) # append it to the list