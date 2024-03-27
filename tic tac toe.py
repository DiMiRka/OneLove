print('Давайте же начнём игру!')
field = [['-'] * 3 for i in range(3)]  # Создаём пустые ячейки


def draw_field():  # Растоновка поля
    print('  0 1 2')  # Пишем верхние координаты
    for i, row in enumerate(field):  # Чертим поле
        row_str = str(i) + ' ' + ' '.join(map(str, row))
        print(row_str)


draw_field()  # Расставляем поле
print('Для хода введите номер столбца и строки через пробел соответственно')

while True:  # Процесс игры
    cross = True
    while cross:
        move_cross = (list(map(int, input('Ход крестиков: ').split())))  # Запрашиваем координаты
        one, two = move_cross[0], move_cross[1]  # Присваиваем координаты переменным
        if field[one][two] == '-':
            field[one][two] = 'x'  # Устанавливаем крестик в веденные координаты
            cross = False
        else:
            print('Ячейка занята, введите координаты повторно')
    draw_field()  # Расставляем поле
    if any([field[0] == ['x', 'x', 'x'],  # Проверяем условия победы крестиков
            field[1] == ['x', 'x', 'x'],
            field[2] == ['x', 'x', 'x'],
            field[0][0] == 'x' and field[1][0] == 'x' and field[2][0] == 'x',
            field[0][1] == 'x' and field[1][1] == 'x' and field[2][1] == 'x',
            field[0][2] == 'x' and field[1][2] == 'x' and field[2][2] == 'x',
            field[0][0] == 'x' and field[1][1] == 'x' and field[2][2] == 'x',
            field[0][2] == 'x' and field[1][1] == 'x' and field[2][0] == 'x']):
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
    zero = True
    while zero:
        move_zero = (list(map(int, input('Ход ноликов: ').split())))  # Запрашиваем координаты
        one, two = move_zero[0], move_zero[1]  # Присваиваем координаты переменным
        if field[one][two] == '-':
            field[one][two] = 'o'  # Устанавливаем нолик в веденные координаты
            zero = False
        else:
            print('Выбранная ячейка уже занята')
        continue
    draw_field()  # Расставляем поле
    if any([field[0] == ['o', 'o', 'o'],  # Проверяем условия победы ноликов
            field[1] == ['o', 'o', 'o'],
            field[2] == ['o', 'o', 'o'],
            field[0][0] == 'o' and field[1][0] == 'o' and field[2][0] == 'o',
            field[0][1] == 'o' and field[1][1] == 'o' and field[2][1] == 'o',
            field[0][2] == 'o' and field[1][2] == 'o' and field[2][2] == 'o',
            field[0][0] == 'o' and field[1][1] == 'o' and field[2][2] == 'o',
            field[0][2] == 'o' and field[1][1] == 'o' and field[2][0] == 'o']):
        print('Нолики выиграли!')
        new_game = input('Желаете начать новую игру? Y - да, N - нет: ')  # Запрашиваем начало новой игры
        if new_game == 'Y':
            field = [['-'] * 3 for i in range(3)]  # Обновляем пустые ячейки
            draw_field()  # Расставляем поле
            continue
        else:
            break