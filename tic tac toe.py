print('Давайте же начнём игру!')
field = [['-'] * 3 for i in range(3)]  # Создаём пустые ячейки


def draw_field():  # Растоновка поля
    print('   | 0 | 1 | 2 |')  # Пишем верхние координаты
    print(' --------------- ')
    for i, row in enumerate(field):  # Чертим поле
        row_str = f' {i} | {' | '.join(map(str, row))} | '
        print(row_str)
        print(' -------------- ')

def ask():  # Запрос координат для хода игрока
    while True:
        move = input('Введите координаты: ').split()  # Запрашиваем координаты

        if len(move) != 2:  # Проверяем наличие 2-х координат
            print('Введите 2 координаты')
            continue
        x, y = move

        if not(x.isdigit()) or not (y.isdigit()):  # Проверяем, что в координаты ввели числа
            print('Введите числовые координты от 0 до 2')
            continue
        x, y = int(x), int(y)

        if not (0 <= x <= 2) or not (0 <= y <= 2) :  # Проверяем, что координаты входят в наш диапазон поля
            print('Координаты выходят за диапазон поля, введите координаты повторно')
            continue

        if field[x][y] != '-':  # Проверяем, что ячейка еще не занята
            print('Ячейка занята, введите координаты повторно')
            continue
        return x,y

def end_game():
    win = [((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)),
           ((2, 0), (2, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
           ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)),
           ((0, 0), (1, 1), (2, 2)), ((0, 2), (1, 1), (2, 0))]
    for a in win:
        test_win =[]
        for b in a:
            test_win.append(field[b[0]][b[1]])
        if test_win == ['X', 'X', 'X']:
            print('Крестики выиграли!')
            return True
        if test_win == ['O', 'O', 'O']:
            print('Нолики выиграли!')
            return True

    if '-' not in field[0] and '-' not in field[1] and '-' not in field[2]:
        print('Ничья!')
        return True

draw_field()  # Расставляем поле
print('Для хода введите номер столбца и строки через пробел соответственно')

while True:  # Процесс игры
    print('Ходят крестики')
    x,y = ask()
    field[x][y] = 'X'
    draw_field()  # Расставляем поле
    if end_game():
        new_game = input('Желаете начать новую игру? Y - да, N - нет: ')  # Запрашиваем начало новой игры
        if new_game == 'Y':
            field = [['-'] * 3 for i in range(3)]  # Обновляем пустые ячейки
            draw_field()  # Расставляем поле
            continue
        else:
            break
    elif '-' not in field[0] and '-' not in field[1] and '-' not in field[2]:
        print('Ничья!')
        new_game = input('Желаете начать новую игру? Y - да, N - нет: ')  # Запрашиваем начало новой игры
        if new_game == 'Y':
            field = [['-'] * 3 for i in range(3)]  # Обновляем пустые ячейки
            draw_field()  # Расставляем поле
            continue
        else:
            break
    print('Ходят нолики')
    x, y = ask()
    field[x][y] = 'O'
    draw_field()  # Расставляем поле
    if end_game():
        new_game = input('Желаете начать новую игру? Y - да, N - нет: ')  # Запрашиваем начало новой игры
        if new_game == 'Y':
            field = [['-'] * 3 for i in range(3)]  # Обновляем пустые ячейки
            draw_field()  # Расставляем поле
            continue
        else:
            break
