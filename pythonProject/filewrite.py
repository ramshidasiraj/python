import csv
with open("student.csv", "w") as file:
    fd = ["stdno", "name", "mark"]
    writer=csv.DictWriter(file, fieldnames=fd)
    writer.writeheader()
    writer.writerow({"stdno":"001", "name":"ramshi", "mark":28})
    writer.writerow({"stdno":"002", "name":"ayisha", "mark":23})
    writer.writerow({"stdno":"003", "name":"shahana", "mark":24})
    writer.writerow({"stdno":"004", "name":"farha", "mark":27})
    writer.writerow({"stdno":"005", "name":"akshaya", "mark":22})
with open("student.csv", "r") as file:
    reader = csv.reader(file)
    for x in reader:
     print(x)

