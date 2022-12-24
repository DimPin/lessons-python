# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.

list = [2, 3, 9, 6, 7]
sum = 0

for i in range(len(list) - 1):
    if i % 2 != 0:
        sum += list[i]

print(list)
print(sum)

# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний 
# элемент, второй и предпоследний и т.д.

list = [1, 7, 8, 4, 5]
el1 = 0
el2 = len(list) - 1

print(list)

while el1 <= el2:
    print(list[el1] * list[el2])
    el1 += 1
    el2 -= 1

# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между 
# максимальным и минимальным значением дробной части элементов.

list = [1.1, 1.2, 3.1, 5, 10.01]
max = 0
min = 0

for i in range(len(list) - 1):
    if list[max] % 1 < list[i] % 1:
        max = i
    if list[min] % 1 > list[i] % 1:
        min = i

print(list)
print(list[max] % 1 - list[min] % 1)

# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

print(bin(45))
print(bin(3))
print(bin(2))

# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

k = int(input('Input k: '))
i = -k
list = []

def fib(n):
    if n < 2 and n >= 0:
        return 1
    elif n >= 2:
        return fib(n - 2) + fib(n - 1)
    else:
        return fib(n + 2) - fib(n + 1)

while i <= k:
    list.append(fib(i))
    i += 1

print(list)