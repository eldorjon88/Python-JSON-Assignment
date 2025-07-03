import json

name = input("Ismingizni kiriting: ")
surname = input("Familiyangizni kiriting: ")

while True:
    age_input = input("Yoshingizni kiriting: ")
    if age_input.isdigit():
        age = int(age_input)
        break
    else:
        print("Iltimos, yoshni butun son sifatida kiriting.")

with open('students.json', 'r', encoding='utf-8') as f:
    students = json.load(f)

new_student = {"name": name, "surname": surname, "age": age}
students.append(new_student)

with open('students.json', 'w', encoding='utf-8') as f:
    json.dump(students, f, ensure_ascii=False, indent=4)

print("Yangi talaba ma'lumotlari faylga yozildi.")
