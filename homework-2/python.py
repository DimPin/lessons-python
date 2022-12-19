from random import randrange

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

def factorial(n):
    res = 1
    i = 1

    while i <= n:
        res *= i
        i += 1

    return res

n = int(input('Input n: '))
print(factorial(n))

# Требуется найти наименьший натуральный делитель целого числа N, отличный от 1.

def smallestDivisor(n):
    i = 2
    while i <= n:
        if n % i == 0:
            print(i)
            break
        i += 1

n = int(input('Input n: '))
smallestDivisor(n)

# Задайте список из (2*N+1) элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных ИНДЕКСАХ. Пять ИНДЕКСОВ хранятся в списке, 
# который вы сами заполняете.

n = int(input('Input n: '))

list = []
c = -n
while c != n + 1:
    list.append(c)
    c += 1
print(list)

list_index = []
for i in range(5 + 1):
    list_index.append(randrange(len(list) + 1))
print(list_index)

res = 1
for i in range(len(list_index)):
    res *= list[list_index[i]]

print(res)

# Требуется посчитать сумму чётных чисел, расположенных между числами 1 и N включительно.

n = int(input('Input n: '))
i = 1
res = 0

while i <= n:
    if i % 2 == 0:
        res += i
    i += 1

print(res)