from models import save_db, load_db, see_raiting
from teacher import add_student, add_raiting

def start():
    load_db()

    who = int(input('Укажите себя. 1 - учитель, 2 - ученик: '))

    if who == 1:
        while True:
            action = int(input('1 - записать ученика, 2 - выстовить оценку, 0 - выйти из программы: '))

            if action == 1:
                add_student()
            elif action == 2:
                add_raiting()
            elif action == 0:
                break
            
            save_db()
    elif who == 2:
        while True:
            name = input('Введите фамилию или 0 для выхода из программы: ')

            if name == '0':
                break
            else:
                see_raiting(name)