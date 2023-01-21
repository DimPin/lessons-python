def read_data():
    path = 'homework-7/text1.txt'
    data = open(path, 'r')
    path2 = 'homework-7/text2.txt'
    data2 = open(path2, 'r')
    
    print('Первый файл: ')

    for line in data:
        print(line)

    print('Второй файл: ')

    for line in data2:
        print(line)
    
    data.close()
    data2.close()