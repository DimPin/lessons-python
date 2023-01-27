from subjects.physics import physic
from subjects.chemisrty import chemistry
from subjects.history import history
from subjects.maths import math
from subjects.russian import russian

def for_teacher(list):
    if list[0] == 'Физика':
        physic[list[1]] += [list[2]]
    elif list[0] == 'Химия':
        chemistry[list[1]] += [list[2]]
    elif list[0] == 'История':
        history[list[1]] += [list[2]]
    elif list[0] == 'Математика':
        math[list[1]] += [list[2]]
    elif list[0] == 'Россия':
        russian[list[1]] += [list[2]]