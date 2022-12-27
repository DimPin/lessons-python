# Пользователь вводит число, Вам необходимо вывести число Пи с той точностью знаков после запятой,
# сколько указал пользователь(БЕЗ round())

# from mpmath import mp
# mp.dps = int(input('Input PI digits: ')) + 1
# print(mp.pi)

# Задайте натуральное число N. Напишите программу, которая составит список простых
# множителей числа N.

# def prime_factor(n):
#     i = 2
#     prime_factors = []

#     while i * i <= n:
#         while n % i == 0:
#             prime_factors.append(i)
#             n /= i
#         i += 1

#     if n > 1:
#         prime_factors.append(n)

#     return prime_factors

# n = int(input('Input n: '))
# print(prime_factor(n))

# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся 
# элементов исходной последовательности.

# list = [2, 2, 3, 3, 4]
# print(set(list))

# def get_unique_numbers(numbers):
#     unique = []

#     for number in numbers:
#         if number not in unique:
#             unique.append(number)

#     return unique

# print(get_unique_numbers(list))

# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и вывести многочлен степени k.

import random

def coefficients(k):
    string = ''
    i = k

    while i >= 2:
        string = string + str(random.randrange(0, 100)) + 'xˆ' + str(i) + ' + '
        i -= 1

    string = string + str(random.randrange(0, 100)) + 'x' + ' + ' + str(random.randrange(0, 100))

    return string

k = int(input('Input k: '))
print(coefficients(k))