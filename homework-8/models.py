import json
import os

def set_student(list):
    data_base[list] = {}

def set_rating(name, lesson, rating):
    if data_base.get(name) is None:
        print(f'Ученик с фамилией {name} не найден')
        print(data_base)
    else:
        if lesson in data_base[name]:
            data_base[name][lesson].extend(rating)
        else:
            data_base[name][lesson] = rating

def see_raiting(name):
    if data_base.get(name) is None:
        print(f'Ученик с фамилией {name} не найден')
    else:
        data = data_base[name]
        print(name)

        for key, value in data.items():
            print(*[f'{key}: {", ".join(value)}'], sep='\n')

def save_db():
    json.dump(data_base, open('homework-8/db_student.json', 'w'))

def load_db():
    global data_base

    if os.stat('homework-8/db_student.json').st_size == 0:
        data_base = {}
    else:
        data_base = json.load(open('homework-8/db_student.json'))