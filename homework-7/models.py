def write_data(list_data: list):
    path = 'homework-7/text1.txt'
    data = open(path, 'a')
    path2 = 'homework-7/text2.txt'
    data2 = open(path2, 'a')

    for i in range(len(list_data)):
        data.write(f'{list_data[i]} \n')
        data2.write(f'{list_data[i]} ')

    data.write('\n')
    data2.write('\n')
    data.close()
    data2.close()