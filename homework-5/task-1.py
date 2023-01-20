from random import randrange

def bot_step(candys):
    if candys >= 28:
        return randrange(28 + 1)
    else:
        return randrange(candys + 1)

def human_step(candys):
    step = int(input('Введите колическтво конфет: '))

    if step > 28 or step > candys or step < 1:
        print('Введено не допустимое значение, попробуйте ещё раз')
        step = 0
        return human_step(candys)
    else:
        return step

def count_candys(candys):
    print('Количество конфет: ', candys)

candys = 120
is_human = True

count_candys(candys)

while candys > 0:
    if is_human:
        candys -= human_step(candys)
        count_candys(candys)
        is_human = False
    else:
        step = bot_step(candys)
        print('Бот забрал', step)
        candys -= step
        count_candys(candys)
        is_human = True

if not is_human:
    print('Поздравляю, с победой!')
else:
    print('Game over')