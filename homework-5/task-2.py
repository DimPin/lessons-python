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

    if move > 0 and move < 10 and field[move - 1] == 0:
        if player_1:
            field[move - 1] = 1
        else:
            field[move - 1] = 2
    else:
        print('Ой что-то не так, попробуй ещё раз')
        player_1 = not player_1
        i -= 1

    if (field[0] == field[1] == field[2] and field[0] > 0) or (field[3] == field[4] == field[5] and field[3] > 0) or (field[6] == field[7] == field[8] and field[6] > 0) or (field[0] == field[3] == field[6] and field[0] > 0) or (field[1] == field[4] == field[7] and field[1] > 0) or (field[2] == field[5] == field[8] and field[2] > 0) or (field[0] == field[4] == field[8] and field[0] > 0) or (field[2] == field[4] == field[6] and field[2] > 0):
        draw_board(field)

        if player_1:
            print('Выйграл первый игрок')
        else:
            print('Выйграл второй игрок')
        
        break
    
    player_1 = not player_1
    i += 1