import csv
with open("city.csv") as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)
        
