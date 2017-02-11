import csv
import os

data_file = open('data.csv', 'rb')
data = csv.reader(data_file, delimiter=',', quotechar='|')

sum_data = []

for row in data:
    sum_row = []
    s = 0
    for i in range(0, 4):
        s += int(row[i])
    sum_row.append(str(s))
    for i in row[4:]:
        sum_row.append(i)
    sum_data.append(sum_row)

sum_data_file = open('sum_data.csv', 'wb')
writer = csv.writer(sum_data_file, delimiter=',', quotechar='|')
for row in sum_data:
    writer.writerow(row)
