print('Давайте же начнём игру!')
field = [['-'] * 3 for i in range(3)]
print('  0 1 2')
for i, row in enumerate(field):
    row_str = str(i) + ' ' + ' '.join(map(str, row))
    print(row_str)
print('Для хода введите номер столбца и строки через пробел соответствено')

while True:
    move_cross = (list(map(int, input('Ход крестиков: ').split())))
    one, two = move_cross[0], move_cross[1]
    field[one][two] = 'x'
    print('  0 1 2')
    for i, row in enumerate(field):
        row_str = str(i) + ' ' + ' '.join(map(str, row))
        print(row_str)
    if any([field[0] == ['x', 'x', 'x'],
    field[1] == ['x', 'x', 'x'],
    field[2] == ['x', 'x', 'x'],
    field[0][0] == 'x' and field[1][0] == 'x' and field[2][0] == 'x',
    field[0][1] == 'x' and field[1][1] == 'x' and field[2][1] == 'x',
    field[0][2] == 'x' and field[1][2] == 'x' and field[2][2] == 'x',
    field[0][0] == 'x' and field[1][1] == 'x' and field[2][2] == 'x',
    field[0][2] == 'x' and field[1][1] == 'x' and field[2][0] == 'x']):
        print('Крестики выиграли')
        continuation = input('Желаете начать новую игру? Y - да, N - нет: ')
        if continuation == 'Y':
            field = [['-'] * 3 for i in range(3)]
            print('  0 1 2')
            for i, row in enumerate(field):
                row_str = str(i) + ' ' + ' '.join(map(str, row))
                print(row_str)
            continue
        else:
            break
    move_zero = (list(map(int, input('Ход ноликов: ').split())))
    one, two = move_zero[0], move_zero[1]
    field[one][two] = 'o'
    print('  0 1 2')
    for i, row in enumerate(field):
        row_str = str(i) + ' ' + ' '.join(map(str, row))
        print(row_str)
    if any([field[0] == ['o', 'o', 'o'],
    field[1] == ['o', 'o', 'o'],
    field[2] == ['o', 'o', 'o'],
    field[0][0] == 'o' and field[1][0] == 'o' and field[2][0] == 'o',
    field[0][1] == 'o' and field[1][1] == 'o' and field[2][1] == 'o',
    field[0][2] == 'o' and field[1][2] == 'o' and field[2][2] == 'o',
    field[0][0] == 'o' and field[1][1] == 'o' and field[2][2] == 'o',
    field[0][2] == 'o' and field[1][1] == 'o' and field[2][0] == 'o']):
        print('Нолики выиграли')
        continuation = input('Желаете начать новую игру? Y - да, N - нет: ')
        if continuation == 'Y':
            field = [['-'] * 3 for i in range(3)]
            print('  0 1 2')
            for i, row in enumerate(field):
                row_str = str(i) + ' ' + ' '.join(map(str, row))
                print(row_str)
            continue
        else:
            break