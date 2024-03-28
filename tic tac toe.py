def draw_field():  # Расстановка поля
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
            print('Введите числовые координаты от 0 до 2')
            continue
        x, y = int(x), int(y)

        if not (0 <= x <= 2) or not (0 <= y <= 2) :  # Проверяем, что координаты входят в наш диапазон поля
            print('Координаты выходят за диапазон поля, введите координаты повторно')
            continue

        if field[x][y] != '-':  # Проверяем, что ячейка еще не занята
            print('Ячейка занята, введите координаты повторно')
            continue
        return x,y

def end_game():  # Проверка условий окончания игры
    win = [((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)),  # Пишем комбинации для победы
           ((2, 0), (2, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
           ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)),
           ((0, 0), (1, 1), (2, 2)), ((0, 2), (1, 1), (2, 0))]
    for a in win:  # Проверяем наличие победной комбинации
        test_win =[]
        for b in a:
            test_win.append(field[b[0]][b[1]])
        if test_win == ['X', 'X', 'X']:
            print('Крестики выиграли!')
            return True
        if test_win == ['O', 'O', 'O']:
            print('Нолики выиграли!')
            return True

    if '-' not in field[0] and '-' not in field[1] and '-' not in field[2]:  # Проверяем возможность ничьи
        print('Ничья!')
        return True

print('Давайте же начнём игру в крестики-нолики!')
field = [['-'] * 3 for i in range(3)]  # Создаём пустые ячейки
queue = 0  # Заводим счетчик ходов
draw_field()  # Расставляем поле
print('Для хода введите номер столбца и строки через пробел соответственно')

while True:  # Процесс игры
    queue += 1  # Обновляем счетчик ходов
    if queue % 2 == 1:  # Проверка очередности ходов
        print('Ходят крестики')
    else:
        print('Ходят нолики')
    x,y = ask()  # Запрашиваем координаты у игрока
    if queue % 2 == 1:  # Проставляем значение в ячейку в зависимости от очередности хода
        field[x][y] = 'X'
    else:
        field[x][y] = 'O'
    draw_field()  # Расставляем поле
    if end_game():  # Запрашиваем начало новой игры
        new_game = input('Желаете начать новую игру? Y - да, N - нет: ')
        if new_game == 'Y':
            field = [['-'] * 3 for i in range(3)]  # Обновляем пустые ячейки
            draw_field()  # Расставляем поле
            queue = 0
            continue
        else:
            break
