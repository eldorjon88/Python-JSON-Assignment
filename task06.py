import json
import csv

with open('students.json', encoding='utf-8') as f:
    students = json.load(f)

with open('students.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'surname', 'age'])  # sarlavha

    for s in students:
        writer.writerow([s['name'], s['surname'], s['age']])

print("students.csv fayli yaratildi.")
