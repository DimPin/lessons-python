from loggers import get_data
from models import write_data
from views import read_data

def process_start(data):
    if data == 1:
        list = get_data()
        write_data(list)
        print('Данные записаны')
    else:
        read_data()