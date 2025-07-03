import json

with open('students.json', 'r', encoding='utf-8') as f:
    students = json.load(f)

new_student = {"name": "Shahzoda", "surname": "Nazarova", "age": 22}
students.append(new_student)

with open('students.json', 'w', encoding='utf-8') as f:
    json.dump(students, f, ensure_ascii=False, indent=4)

print("Yangi talaba students.json fayliga qo'shildi.")
