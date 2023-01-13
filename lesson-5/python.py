# 1) В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, 
# чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.

# Чтение данных:

path = 'lesson-5/file.txt'
data = open(path, 'r')

my_list = []

for line in data:
    my_list = list(map(int, line.split()))

data.close

print(my_list)

for i in range(1, len(my_list)):
    if my_list[i] - 1 != my_list[i-1]:
        print(my_list[i] - 1)

# 2) Написать программу, которая будет удалять все слова в которых есть "абв"

# Ввод:
# привет приаб приабвет
# Вывод:
# привет приаб

string = input('Введите слова через пробел: ').split()

for word in string:
    if 'абв' in word:
        string.remove(word)

print(*string)