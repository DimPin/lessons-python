from models import set_student, set_rating

def add_student():
    name = input('Введите фамилию: ')
    set_student(name)

def add_raiting():
    name = input('Введите фамилию ученика: ')
    lesson = input('Введите урок: ')
    rating = input('Введите оценку или оценки через пробел: ').split()
    set_rating(name, lesson, rating)