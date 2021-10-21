import csv
with open ("records.csv") as file:
    reader=csv.DictReader(file)
    for row in reader:
        print(row["id"])