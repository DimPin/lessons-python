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