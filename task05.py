import json

with open('students.json', encoding='utf-8') as f:
    students = json.load(f)

for s in students:
    if s.get('age', 0) > 20:
        print(f"{s['name']} - {s['age']} yosh")

