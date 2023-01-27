def is_who():
    data = int(input('Введите 1, если вы учитель; 2, если ученик: '))
    return data

def is_teacher():
    subject = input('Введите предмет: ')
    student = input('Введите ученика: ')
    estimation = int(input('Введите оценку: '))
    return [subject, student, estimation]

def is_student():
    subjest = input('Введите предмет с большой буквы: ')
    return subjest