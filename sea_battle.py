from random import randint

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
        self.busy = []  # Список занятых клеток (кораблями или его контуром)
        self.ships = []  # Список кораблей на поле
        self.shots_taken = []  # Список сделанных выстрелов

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
                    self.busy.append(crd)
                if look and self.field[crd.x][crd.y] != 'X':
                    self.field[crd.x][crd.y] = '·'
                    self.shots_taken.append(crd)

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

        if c in self.shots_taken:  # Проверяем не стреляли ли в эту клетку ранее
            raise BoardUsedExceptions()

        self.shots_taken.append(c)  # Добавляем выстрел в список выстрелов

        for ship in self.ships:
            if ship.shoots(c):
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

class Player:
    def __int__(self, board, board_2):
        self.board = Board()
        self.board_2 = Board(hid=True)

    def ask(self):
        pass

    def move(self):
        while True:
            try:
                target = self.ask()
                repeat = self.board_2.shot(target)
            except Exceptions as e:
                print(e)

class AI (Player):
    def ask(self):
        d = Dot(randint(0, 5), randint(0, 5))
        print(f'Ход компьютера: {d.x + 1} {d.y + 1}')

class User (Player):
    def ask(self):
        while True:
            d =  input('Введите координаты выстрела через пробел: ').split()

            if len(d) != 2: # Проверяем, что введены 2 координаты
                print('Введите 2 координаты через пробел! ')
                continue
            x, y = d

            if not(x.isdigit()) or not (y.isdigit()):  # Проверяем, что в координаты ввели числа
                print('Введите числовые координаты')
                continue
            x, y = int(x), int(y)

            print(f'Ход игрока: {x} {y}')
            return Dot(x - 1, y - 1)

class Game:
    def __init__(self, user, board_user, ai, board_ai):
        self.user = User()
        self.board_user = user.board
        self.ai = AI()
        self.board_ai = user.board_2

ship_1 = Ship(Dot(3, 3), 2, 0)
board_1 = Board()
board_1.add_ship(ship_1)
board_1.contour(ship_1)
board_1.shot(Dot(0, 0))
board_1.shot(Dot(3,3))
board_1.shot(Dot(4,3))
print(board_1)