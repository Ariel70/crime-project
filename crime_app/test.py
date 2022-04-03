import csv
from models import Crime

file = open("PastData.csv")

csvreader = csv.reader(file)

header = next(csvreader)
print(header)

rows = []
for row in csvreader:
    c = Crime(date=row[0], borough=row[1], description=row[2], count=row[3])
    rows.append(c)
    c.save()
print(rows)


file.close()
