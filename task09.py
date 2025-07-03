import json

with open('students.json', encoding='utf-8') as f:
    students = json.load(f)

print(f"Umumiy talabalar soni: {len(students)} ta")
