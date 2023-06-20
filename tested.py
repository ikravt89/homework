import csv

with open ("csv.csv", 'r', encoding="UTF-8") as r_file:
    file_reader = csv.reader(r_file, delimiter=',')
    count = 0
    for row in file_reader:
        if count == 0:
            print(f"Файл содержит столбцы: {','.join(row)}")
        else:
            print(f"      {row[0]} - {row[1]} - {row[2]}")
        count +=1
    print(f"Total: {count} lines")

