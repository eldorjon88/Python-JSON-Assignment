import json

with open('students.json', encoding='utf-8') as f:
    students = json.load(f)

ages = [s.get('age', 0) for s in students if isinstance(s.get('age', None), int)]

if ages:
    average_age = sum(ages) / len(ages)
    print(f"O'rtacha yosh: {average_age:.2f}")
else:
    print("Faylda yosh ma'lumotlari mavjud emas.")
