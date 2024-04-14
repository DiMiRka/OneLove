from random import randint


class Exceptions (Exception):
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
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f'Координата x: {self.x}, Координата y: {self.y}'


class Ship:  # Класс кораблей
    def __init__(self, ship_nose, ship_size, direction):
        self.ship_nose = ship_nose  # Нос корабля (объект класса Dot)
        self.ship_size = ship_size  # Длина корабля
        self.direction = direction  # Направление корабля вертикальное/горизонтальное (0/1)
        self.heart = ship_size  # Количество жизней корабля

    @property
    def dots(self):  # Координаты корабля
        ship_dots = []
        for i in range(self.ship_size):
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
    def __init__(self, hid=False, size=6):
        self.hid = hid  # Скрытие кораблей на поле (True/False)
        self.size = size  # Размер поля
        self.living_ships = 0  # Живые корабли
        self.field = [['O'] * size for _ in range(size)]  # Расчерчивает поле
        self.busy = []  # Список занятых клеток (кораблями и его контуром)
        self.ships = []  # Список кораблей на поле
        self.shots_taken = []  # Список сделанных выстрелов

    def __str__(self):
        draw = '   | 1 | 2 | 3 | 4 | 5 | 6 |'  # Пишем верхние координаты
        draw += '\n --------------------------- '
        for i, row in enumerate(self.field):  # Чертим поле
            draw += f'\n {i+1} | ' + ' | '.join(row) + ' | '

        if self.hid:  # Проверяем скрываем ли корабли на поле
            draw = draw.replace('■', 'O')
        return draw

    def out(self, b):  # Проверяем выходят ли координаты за поле
        return not ((0 <= b.x < self.size) and (0 <= b.y < self.size))

    def contour(self, ship, look=False):  # Делаем контур корабля
        near = [
            (-1, -1), (0, -1), (1, -1),
            (-1, 0), (0, 0), (1, 0),
            (-1, 1), (0, 1), (1, 1)
        ]
        for d in ship.dots:
            for dx, dy in near:
                crd = Dot(d.x + dx, d.y + dy)
                if crd not in self.busy and not (self.out(crd)):
                    if look and self.field[crd.x][crd.y] != 'X':
                        self.field[crd.x][crd.y] = '·'
                        self.shots_taken.append(crd)
                    self.busy.append(crd)

    def add_ship(self, ship):  # Добавляем корабль на поле
        for i in ship.dots:
            if self.out(i) or i in self.busy:
                raise BoardWrongShipExceptions()
        for i in ship.dots:
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

    def begin(self):
        self.busy = []

    def end(self):
        return self.living_ships == 0


class Player:
    def __init__(self, board, board_2):
        self.board = board
        self.board_2 = board_2

    def ask(self):
        raise NotImplementedError()

    def move(self):
        while True:
            try:
                target = self.ask()
                repeat = self.board_2.shot(target)
                return repeat
            except Exception as e:
                print(e)


class AI(Player):
    def ask(self):
        d = Dot(randint(0, 5), randint(0, 5))
        print(f'Ход компьютера: {d.x + 1} {d.y + 1}')
        return d


class User(Player):
    def ask(self):
        while True:
            d = input('Введите координаты выстрела через пробел: ').split()

            if len(d) != 2:  # Проверяем, что введены 2 координаты
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
    def __init__(self, size=6):
        self.size = size
        us_board = self.random_board()
        ai_board = self.random_board()
        ai_board.hid = True
        self.us = User(us_board, ai_board)
        self.ai = AI(ai_board, us_board)

    def try_board(self):
        ship_lens = [3, 2, 2, 1, 1, 1, 1]
        board = Board(size=self.size)
        attempts = 0
        for lens in ship_lens:
            while True:
                attempts += 1
                if attempts > 2000:
                    return None
                new_ship = Ship(Dot(randint(0, self.size - 1), randint(0, self.size - 1)), lens, randint(0, 1))
                try:
                    board.add_ship(new_ship)
                    break
                except BoardWrongShipExceptions:
                    pass
        board.begin()
        return board

    def random_board(self):
        board = None
        while board is None:
            board = self.try_board()
        return board

    def greet(self):
        print('  -----------------------  ')
        print('  Добро пожаловать в игру  ')
        print('        Морской Бой        ')
        print('  -----------------------  ')
        print('      Формат хода: х y     ')
        print('      x - номер строки     ')
        print('      y - номер столбца    ')
        print('     Вводите координаты    ')
        print('        через пробел       ')
        print('  -----------------------  ')

    def loop(self):
        num = 0
        while True:
            print('-' * 23)
            print('Доска игрока')
            #print(f'Живых кораблей {self.us.living_ship}')
            print(self.us.board)
            print('-' * 23)
            print('Доска компьютера')
            print(self.ai.board)
            print('-' * 23)
            if num % 2 == 0:
                print('Ходит игрок')
                repeat = self.us.move()
            else:
                print('Ходит компьютер')
                repeat = self.ai.move()
            if repeat:
                num -= 1

            if self.ai.board.end():
                print('-' * 23)
                print('Игрок победил!')
                break

            if self.us.board.end():
                print('-' * 23)
                print('Компьютер победил!')
                break

            num += 1

    def start(self):
        self.greet()
        self.loop()


g = Game()
g.start()
