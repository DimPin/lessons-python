def get_write_read():
    data = int(input('Введите 1 - записать данные или 2 - вывести данные: '))
    return data

def get_data():
    data_surname = input('Введите фамилию: ')
    data_name = input('Введите имя: ')
    data_number = input('Введите номер телефона: ')
    data_descrip = input('Введите описание номера телефона: ')

    data = [data_surname, data_name, data_number, data_descrip]
    return data