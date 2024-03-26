print('Давайте же начнём игру!')
field = [['-'] * 3 for i in range(3)] #Создаём пустые ячейки
print('  0 1 2') #Выводим названия координат столбцов
for i, row in enumerate(field): #Расставляем поле
    row_str = str(i) + ' ' + ' '.join(map(str, row))
    print(row_str)
print('Для хода введите номер столбца и строки через пробел соответственно')

while True: #Процесс игры
    move_cross = (list(map(int, input('Ход крестиков: ').split()))) #Запрашиваем постановки
    one, two = move_cross[0], move_cross[1] #Присваиваем координаты переменным
    field[one][two] = 'x' #Устанавливаем крестик в веденные координаты
    print('  0 1 2') #Выводим названия координат столбцов
    for i, row in enumerate(field): #Расставляем поле с добавлением крестика в введенные координаты
        row_str = str(i) + ' ' + ' '.join(map(str, row))
        print(row_str)
    if any([field[0] == ['x', 'x', 'x'], #Проверяем условия победы крестиков
    field[1] == ['x', 'x', 'x'],
    field[2] == ['x', 'x', 'x'],
    field[0][0] == 'x' and field[1][0] == 'x' and field[2][0] == 'x',
    field[0][1] == 'x' and field[1][1] == 'x' and field[2][1] == 'x',
    field[0][2] == 'x' and field[1][2] == 'x' and field[2][2] == 'x',
    field[0][0] == 'x' and field[1][1] == 'x' and field[2][2] == 'x',
    field[0][2] == 'x' and field[1][1] == 'x' and field[2][0] == 'x']):
        print('Крестики выиграли')
        continuation = input('Желаете начать новую игру? Y - да, N - нет: ') #Запрашиваем начало новой игры
        if continuation == 'Y':
            field = [['-'] * 3 for i in range(3)] #Обновляем пустые ячейки
            print('  0 1 2') #Выводим названия координат столбцов
            for i, row in enumerate(field): #Расставляем поле
                row_str = str(i) + ' ' + ' '.join(map(str, row))
                print(row_str)
            continue
        else:
            break
    move_zero = (list(map(int, input('Ход ноликов: ').split()))) #Запрашиваем постановки
    one, two = move_zero[0], move_zero[1] #Присваиваем координаты переменным
    field[one][two] = 'o' #Устанавливаем нолик в веденные координаты
    print('  0 1 2') #Выводим названия координат столбцов
    for i, row in enumerate(field): #Расставляем поле с добавлением нолика в введенные координаты
        row_str = str(i) + ' ' + ' '.join(map(str, row))
        print(row_str)
    if any([field[0] == ['o', 'o', 'o'], #Проверяем условия победы ноликов
    field[1] == ['o', 'o', 'o'],
    field[2] == ['o', 'o', 'o'],
    field[0][0] == 'o' and field[1][0] == 'o' and field[2][0] == 'o',
    field[0][1] == 'o' and field[1][1] == 'o' and field[2][1] == 'o',
    field[0][2] == 'o' and field[1][2] == 'o' and field[2][2] == 'o',
    field[0][0] == 'o' and field[1][1] == 'o' and field[2][2] == 'o',
    field[0][2] == 'o' and field[1][1] == 'o' and field[2][0] == 'o']):
        print('Нолики выиграли')
        continuation = input('Желаете начать новую игру? Y - да, N - нет: ') #Запрашиваем начало новой игры
        if continuation == 'Y':
            field = [['-'] * 3 for i in range(3)] #Обновляем пустые ячейки
            print('  0 1 2') #Выводим названия координат столбцов
            for i, row in enumerate(field): #Расставляем поле
                row_str = str(i) + ' ' + ' '.join(map(str, row))
                print(row_str)
            continue
        else:
            break