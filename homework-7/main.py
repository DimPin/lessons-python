from controllers import process_start
from loggers import get_write_read

def run(data):
    process_start(data)

if __name__ == '__main__':
    run(get_write_read())