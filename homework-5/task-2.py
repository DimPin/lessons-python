def draw_board(field):
    i = 0
    while i in range(3):
        if i == 0 or i == 2:
            if field[i] == 0:
                print('|', i+1, '|', end='')
            elif field[i] == 1:
                print('|', 'X', '|', end='')
            else:
                print('|', 'O', '|', end='')
        else:
            if field[i] == 0:
                print(' ', i+1, ' ', end='')
            elif field[i] == 1:
                print(' ', 'X', ' ', end='')
            else:
                print(' ', 'O', ' ', end='')
        i += 1
    print()
    print('---------------')
    i = 3
    while i in range(6):
        if i == 3 or i == 5:
            if field[i] == 0:
                print('|', i+1, '|', end='')
            elif field[i] == 1:
                print('|', 'X', '|', end='')
            else:
                print('|', 'O', '|', end='')
        else:
            if field[i] == 0:
                print(' ', i+1, ' ', end='')
            elif field[i] == 1:
                print(' ', 'X', ' ', end='')
            else:
                print(' ', 'O', ' ', end='')
        i += 1
    print()
    print('---------------')
    i = 6
    while i in range(9):
        if i == 6 or i == 8:
            if field[i] == 0:
                print('|', i+1, '|', end='')
            elif field[i] == 1:
                print('|', 'X', '|', end='')
            else:
                print('|', 'O', '|', end='')
        else:
            if field[i] == 0:
                print(' ', i+1, ' ', end='')
            elif field[i] == 1:
                print(' ', 'X', ' ', end='')
            else:
                print(' ', 'O', ' ', end='')
        i += 1
    print()

field = [0, 0, 0, 0, 0, 0, 0, 0, 0]
player_1 = True
i = 0

while i in range(9):
    draw_board(field)

    move = int(input('Введите число куда хотите сделать ход: '))

    if field[move - 1] == 0 and move > 0 and move < 10:
        if player_1:
            field[move - 1] = 1
        else:
            field[move - 1] = 2
    else:
        print('Ой что-то не так, попробуй ещё раз')
        i -= 1

    i += 1