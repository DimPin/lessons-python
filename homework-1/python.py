import math

# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, 
# является ли этот день выходным.

a = int(input('Введите число: '))

if a >= 1 and a <= 7:
    if a == 6 or a == 7: print('Да')
    else: print('Нет')
else: print('Введённое число не является днём недели')

# (!!!Доп!!!) Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# для всех значений предикат.

x = 0
y = 0
z = 0

def isTrueState(x, y, z):
    if not (x or y or z) == (not x) and (not y) and (not z):
        print(True)
    else:
        print(False)

isTrueState(0, 0, 0)
isTrueState(0, 0, 1)
isTrueState(0, 1, 0)
isTrueState(0, 1, 1)
isTrueState(1, 0, 0)
isTrueState(1, 0, 1)
isTrueState(1, 1, 0)
isTrueState(1, 1, 1)

# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и 
# выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

x = int(input('Input x: '))
y = int(input('Input y: '))

if x != 0 and y != 0:
    if x > 0 and y > 0:
        print(1)
    elif x > 0 and y < 0:
        print(4)
    elif x < 0 and y > 0:
        print(2)
    elif x < 0 and y < 0:
        print(3)
else:
    print('x or y = 0')

# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат 
# точек в этой четверти (x и y).

num_quarter = int(input('Input number: '))

if num_quarter > 0 and num_quarter < 5:
    if num_quarter == 1:
        print('x > 0, y > 0')
    if num_quarter == 2:
        print('x < 0, y > 0')
    if num_quarter == 3:
        print('x < 0, y < 0')
    if num_quarter == 4:
        print('x > 0, y < 0')
else:
    print('Its not number quarter')

# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между 
# ними в 2D пространстве.

x1 = int(input('Input x1: '))
y1 = int(input('Iput y1: '))
x2 = int(input('Input x2: '))
y2 = int(input('Input y2: '))

distance = round(math.sqrt((pow(x2 - x1, 2)) + (pow(y2 - y1, 2))), 2)
print(distance)