# Все задачи решать с помощью использования лямбд, filter, map, zip, enumerate, List Comprehension

# 1) Вводится список целых чисел в одну строчку через пробел. Необходимо оставить в нем только двузначные числа.
# Реализовать программу с использованием функции filter. Результат отобразить на экране в виде последовательности
# оставшихся чисел в одну строчку через пробел.
# [1,2,3,4,22,234,24] ----> [22, 24]

def two_digit():
    numbers = list(map(int, input('Введите числа через пробел: ').split()))
    return ' '.join(map(str, filter(lambda x: 9 < abs(x) < 100, numbers)))

print(two_digit())

# Все задачи решать с помощью использования лямбд, filter, map, zip, enumerate, List Comprehension
# 2) Дан список, вывести отдельно буквы и цифры, пользуясь filter.

# [12,'sadf',5643] ---> ['sadf'] ,[12,5643]

my_list = [17, 'hudfr', 8464, 'uhgfkj', 'fsefsef']
print(*my_list)
print()

result = list(filter(lambda x: type(x) == int, my_list))
result2 = list(filter(lambda x: type(x) == str, my_list))

print('Числа: ', *result)
print('Строки: ', *result2)

# Все задачи решать с помощью использования лямбд, filter, map, zip, enumerate, List Comprehension
# 3) Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:
# - 6782 -> 23
# - 0,56 -> 11

def sum_numbers(number):
    return sum(map(int, number.replace('-', '').replace('.', '')))

number = input('Введите любое число: ')
print('Сумма чисел этого числа: ', sum_numbers(number))