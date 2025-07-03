import json

with open('students.json', encoding='utf-8') as f:
    students = json.load(f)

valid_students = [s for s in students if isinstance(s.get('age'), int)]

if valid_students:

    top_student = max(valid_students, key=lambda s: s['age'])
    print(f"Eng katta yoshli talaba: {top_student['name']} {top_student['surname']} - {top_student['age']} yosh")
else:
    print("Faylda yosh ma'lumotlari mavjud emas.")
