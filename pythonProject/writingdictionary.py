import csv
with open("student.csv", "w") as file:
    fd=["stdno", "name", "mark"]
    writer = csv.DictWriter(file, fd)
    writer.writerow({"stdno": "001", "name": "ramshi", "mark": 27})
    writer.writerow({"stdno": "002", "name": "rashi", "mark": 24})
    writer.writrow({"stdno": "003", "name": "sasi", "mark": 58})
    writer.writerow({"stdno": "004", "name": "shashi", "mark": 38})
    writer.writerow({"stdno": "005", "name": "rahi", "mark": 38})
