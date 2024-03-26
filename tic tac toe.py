print("Давайте же начнём игру!")
field = [['-'] * 3 for i in range(3)]
for i, row in enumerate(field):
    row_str = str(i) + ' ' + ' '.join(map(str, row))
    print(row_str)
print('Начинают крестики')
while True:
    move_cross = (list(map(int, input('Введите номер столбца и строки через пробел соответствено: ').split())))
    one, two = move_cross[0], move_cross[1]
    field[one][two] = 'x'
    for i, row in enumerate(field):
        row_str = str(i) + ' ' + ' '.join(map(str, row))
        print(row_str)
    move_zero = (list(map(int, input('Введите номер столбца и строки через пробел соответствено: ').split())))
    one, two = move_zero[0], move_zero[1]
    field[one][two] = 'o'
    for i, row in enumerate(field):
        row_str = str(i) + ' ' + ' '.join(map(str, row))
        print(row_str)