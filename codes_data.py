import csv

with open("morse_codes.csv", newline="") as file:
    reader = csv.reader(file, delimiter=";")
    codes_dict = {}
    for row in reader:
        codes_dict[row[0]] = row[1]
