def SearchingNumbers(data, operate):
    numberFirst = data[operate - 1]
    numberSecond = data[operate + 1]

    first = operate - 1
    second = operate + 2

    if data[operate] == '/':
        res = numberFirst / numberSecond
    elif data[operate] == '*':
        res = numberFirst * numberSecond
    elif data[operate] == '-':
        res = numberFirst - numberSecond
    elif data[operate] == '+':
        res = numberFirst + numberSecond
    
    result = data[0:first]
    result.append(res)
    result += data[second:len(data)]
    return result

data = input('Введите выражение через пробел: ').split()
for i in range(len(data)):
    if data[i].isdigit():
        data[i] = int(data[i])
print(*data)

operations = ['/', '*', '-', '+']

for i in range(len(operations)):
    j = 0
    while j in range(len(data)):
        if data[j] == operations[i]:
            operate = j
            data = SearchingNumbers(data, operate)
            j -= 2
        j += 1

print(*data)