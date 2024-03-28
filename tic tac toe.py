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

draw_field()  # Расставляем поле
print('Для хода введите номер столбца и строки через пробел соответственно')

while True:  # Процесс игры
    print('Ходят крестики')
    x,y = ask()
    field[x][y] = 'X'
    draw_field()  # Расставляем поле
    if any([field[0] == ['X', 'X', 'X'],  # Проверяем условия победы крестиков
            field[1] == ['X', 'X', 'X'],
            field[2] == ['X', 'X', 'X'],
            field[0][0] == 'X' and field[1][0] == 'X' and field[2][0] == 'X',
            field[0][1] == 'X' and field[1][1] == 'X' and field[2][1] == 'X',
            field[0][2] == 'X' and field[1][2] == 'X' and field[2][2] == 'X',
            field[0][0] == 'X' and field[1][1] == 'X' and field[2][2] == 'X',
            field[0][2] == 'X' and field[1][1] == 'X' and field[2][0] == 'X']):
        print('Крестики выиграли!')
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
    if any([field[0] == ['O', 'O', 'O'],  # Проверяем условия победы ноликов
            field[1] == ['O', 'O', 'O'],
            field[2] == ['O', 'O', 'O'],
            field[0][0] == 'O' and field[1][0] == 'O' and field[2][0] == 'O',
            field[0][1] == 'O' and field[1][1] == 'O' and field[2][1] == 'O',
            field[0][2] == 'O' and field[1][2] == 'O' and field[2][2] == 'O',
            field[0][0] == 'O' and field[1][1] == 'O' and field[2][2] == 'O',
            field[0][2] == 'O' and field[1][1] == 'O' and field[2][0] == 'O']):
        print('Нолики выиграли!')
        new_game = input('Желаете начать новую игру? Y - да, N - нет: ')  # Запрашиваем начало новой игры
        if new_game == 'Y':
            field = [['-'] * 3 for i in range(3)]  # Обновляем пустые ячейки
            draw_field()  # Расставляем поле
            continue
        else:
            break
