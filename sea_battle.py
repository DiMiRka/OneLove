class Exceptions:
    pass

class BoardOutExceptions(Exceptions):
    def __str__(self):
        return 'Вы пытаетесь выстрелить за доску!'

class BoardUsedExceptions(Exceptions):
    def __str__(self):
        return 'Вы уже стреляли в эту клетку!'

class BoardWrongShipExceptions(Exceptions):
    pass
class Dot:  # Класс координат (точки x и y)
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f'Координата x: {self.x}, Координата y: {self.y}'

class Ship:  # Класс кораблей
    def __init__(self, ship_nose, size, direction):
        self.size = size  # Длина корабля
        self.ship_nose = ship_nose  # Нос корабля (объект класса Dot)
        self.direction = direction  # Направление корабля вертикальное/горизонтальное (0/1)
        self.heart = size  # Количество жизней корабля

    @property
    def dots(self):  # Координаты корабля
        ship_dots = []
        for i in range(self.size):
            dot_x = self.ship_nose.x
            dot_y = self.ship_nose.y
            if self.direction == 0:
                dot_x += i
            elif self.direction == 1:
                dot_y += i
            ship_dots.append(Dot(dot_x, dot_y))
        return ship_dots

    def shoots(self, shot):  # Проверка выстрелов по координатам корабля
        return shot in self.dots


class Board:  # Класс игрового поля
    def __init__(self, hid=False, size = 6):
        self.hid = hid  # Отображение кораблей на поле отображаются/не отображаются (True/False)
        self.size = size  # Размер корабля
        self.living_ships = 0  # Живые корабли
        self.field = [['O'] * size for i in range(size)]  # Расчерчивает поле
        self.busy = []  # Список занятых клеток (кораблями или ранее сделанными выстрелами)
        self.ships = []  # Список кораблей на поле

    def __str__(self):
        draw = '   | 1 | 2 | 3 | 4 | 5 | 6 |'  # Пишем верхние координаты
        draw += '\n --------------------------- '
        for i, row in enumerate(self.field):  # Чертим поле
            draw += f'\n {i+1} | ' + ' | '.join(row) + ' | '

        if self.hid:  # Проверяем прячем ли корабли на поле
            draw = draw.replase('■', 'O')
        return draw

    def out(self, b):  # Проверяем выходят ли координаты за поле
        return not (0 <= b.x < self.size) and (0 <= b.y < self.size)

    def contour(self, ship, look=False):  # Делаем контур корабля + соседние от него клетки
        near = [
            (-1, -1), (0, -1), (1, -1),
            (-1, 0), (0, 0), (1, 0),
            (-1, 1), (0, 1), (1, 1)
        ]
        for i in ship.dots:
            for ix, iy in near:
                crd = Dot(i.x + ix, i.y + iy)
                if crd not in self.busy and not self.out(crd):
                    if look:
                        self.field[crd.x][crd.y] = '·'
                    self.busy.append(crd)

    def add_ship(self, ship):  # Добавляем корабль на поле
        for i in ship.dots:
            if self.out(i) or i in self.busy:
                raise BoardWrongShipExceptions()
            else:
                self.field[i.x][i.y] = '■'
                self.busy.append(i)
        self.ships.append(ship)
        self.contour(ship)
        self.living_ships += 1
    def shot(self, c):  # Делаем выстрел
        if self.out(c):  # Проверяем не выходит ли выстрел за поле
            raise BoardOutExceptions()

        if c in self.busy:  # Проверяем не стреляли ли в эту клетку ранее
            raise BoardUsedExceptions()

        self.busy.append(c)  # Добавляем выстрел в занятую клетку

        for ship in self.ships:
            if c in ship.shoots(c):
                ship.heart -= 1
                self.field[c.x][c.y] = 'X'
                print('Корабль ранен')
                if ship.heart == 0:
                    self.living_ships -= 1
                    self.contour(ship, look=True)
                    print('Корабль уничтожен!')
                    return False
            else:
                self.field[c.x][c.y] = '·'
                print('Мимо!')
                return True




ship_1 = Ship(Dot(3, 3), 2, 0)
board_1 = Board()
board_1.add_ship(ship_1)
board_1.contour(ship_1)

print(board_1)