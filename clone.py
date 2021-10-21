import csv
with open ("prueba.csv") as file:
    reader=csv.DictReader(file)
    for row in reader:
        print(row["id"])