import json

with open('students.json', encoding='utf-8') as f:
    students = json.load(f)

sorted_students = sorted(
    [s for s in students if isinstance(s.get('age'), int)],
    key=lambda s: s['age']
)

for s in sorted_students:
    print(f"{s['name']} {s['surname']} - {s['age']} yosh")
