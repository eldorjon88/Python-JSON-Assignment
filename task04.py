import json

name = input('ism kiriting : ')
surname = input('familiya kiriting : ')
age = int(input('yosh kiriting : '))

new_dict = {
    'name':name,
    'surname':surname,
    'age':age
}

with open('students.json','r') as f1:
    students_str = f1.read()
    students = json.loads(students_str)
    students.append(new_dict)
    
students_dump = json.dumps(students,indent = 4)

with open('students.json','w') as f2:
    f2.write(students_dump)
