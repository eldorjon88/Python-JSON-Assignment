import json
import os

filename = 'students.json'

if not os.path.exists(filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump([], f, ensure_ascii=False, indent=4)
    print(f"'{filename}' fayli yaratildi.")
else:
    print(f"'{filename}' fayli allaqachon mavjud.")
