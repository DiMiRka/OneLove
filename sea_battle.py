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

            if self.direction == 0:  # Проверка вертикального расположения корабля
                dot_x += i

            elif self.direction == 1:  # Проверка горизонтального расположения корабля
                dot_y += i

            ship_dots.append(Dot(dot_x, dot_y))  # Добавляем точки в координаты корабля
        return ship_dots

    def shoots(self, shot):  # Проверка выстрелов по координатам корабля
        return shot in self.dots


class Board:  # Класс игровой доски
    def __init__(self, hid=False, size=6):
        self.hid = hid  # Скрытие кораблей на поле (True/False)
        self.size = size  # Размер поля
        self.living_ships = 0  # Живые корабли
        self.field = [['O'] * size for _ in range(size)]  # Чертим поле
        self.busy = []  # Список занятых клеток (корабль и его контур)
        self.ships = []  # Список кораблей на доске
        self.shots_taken = []  # Список сделанных выстрелов

    def __str__(self):  # Чертим доску
        draw = '   | 1 | 2 | 3 | 4 | 5 | 6 |'  # Пишем нумерацию столбцов
        draw += '\n --------------------------- '
        for i, row in enumerate(self.field):  # Чертим поле с нумерацией строк
            draw += f'\n {i+1} | ' + ' | '.join(row) + ' | '

        if self.hid:  # Проверяем скрываем ли корабли на доске
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
        for d in ship.dots:  # Проходим по координатам корабля
            for dx, dy in near:  # Проходим по списку контура
                crd = Dot(d.x + dx, d.y + dy)  # Присваиваем координаты контура корабля
                if crd not in self.busy and not (self.out(crd)):  # Добавляем контур в списоке занятых клеток доски
                    if look and self.field[crd.x][crd.y] != 'X':  # Показываем контур и добавляем его координаты в список сделанных выстрелов доски (чтобы не допускать выстрелы по известому контуру)
                        self.field[crd.x][crd.y] = '·'
                        self.shots_taken.append(crd)
                    self.busy.append(crd)

    def add_ship(self, ship):  # Добавляем корабль на поле
        for i in ship.dots:  # Проверяем координаты корабля на выход за поле и занятость клеток
            if self.out(i) or i in self.busy:
                raise BoardWrongShipExceptions()
        for i in ship.dots:  # Добавляем координату на поле и в список занятых клеток доски
            self.field[i.x][i.y] = '■'
            self.busy.append(i)

        self.ships.append(ship)  # Добавляем корабль в список кораблей доски
        self.contour(ship)  # Делаем контур корабля
        self.living_ships += 1  # Добавляем корабль в число живых кораблей доски

    def shot(self, c):  # Делаем выстрел
        if self.out(c):  # Проверяем не выходит ли выстрел за поле
            raise BoardOutExceptions()

        if c in self.shots_taken:  # Проверяем не стреляли ли в эту клетку ранее
            raise BoardUsedExceptions()

        self.shots_taken.append(c)  # Добавляем выстрел в список выстрелов доски

        for ship in self.ships:  # Проходим по списку кораблей доски
            if ship.shoots(c): # Проверяем попадание выстрела в один из кораблей
                ship.heart -= 1
                self.field[c.x][c.y] = 'X'
                if ship.heart == 0:  # Проверям добивание корабля
                    self.living_ships -= 1
                    self.contour(ship, look=True)
                    print('Корабль уничтожен!')
                    return False
                else:
                    print('Корабль ранен')
                    return True

        self.field[c.x][c.y] = '·'
        print('Мимо!')
        return False

    def begin(self):  # Обновляем список занятых клеток доски
        self.busy = []

    def end(self):  # Проверяем условие победы
        return self.living_ships == 0


class Player:  # Общий класс игроков
    def __init__(self, board, board_2):
        self.board = board  # Собственная доска
        self.board_2 = board_2  # Доска соперника

    def ask(self):  # Делаем пустой метод запроса выстрела для дальнешейго полиморфизма дочерных классов
        raise NotImplementedError()

    def move(self):  # Делаем выстрел по запрошенным координатам
        while True:
            try:
                target = self.ask()
                repeat = self.board_2.shot(target)
                return repeat
            except Exception as e:
                print(e)


class AI(Player):  # Клас игрока компьютера
    def ask(self):  # Случайно определяем координаты выстрела
        d = Dot(randint(0, 5), randint(0, 5))
        print(f'Ход компьютера: {d.x + 1} {d.y + 1}')
        return d


class User(Player):  # Клас игрока пользователя
    def ask(self):  # Запрашиваем координаты выстрела
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


class Game:  # Класс логики самой игры
    def __init__(self, size=6):
        self.size = size  # Размер поля
        us_board = self.random_board()  # Доска пользователя
        ai_board = self.random_board()  # Доска компьютера
        ai_board.hid = True  # Скрываем корабли компьютера с доски
        self.us = User(us_board, ai_board)  # Создаем игрока пользователя
        self.ai = AI(ai_board, us_board)  # Создаем игрока компьютер

    def try_board(self):  # Случайно распределяем корабли на поле
        ship_lens = [3, 2, 2, 1, 1, 1, 1]  # Список размеров кораблей, которые необходимо разместить
        board = Board(size=self.size)
        attempts = 0  # Количество попыток распределить корабли
        for lens in ship_lens:  # Проходим по списку размеров кораблей, которые необходимо разместить
            while True:
                attempts += 1
                if attempts > 2000:
                    return None
                new_ship = Ship(Dot(randint(0, self.size - 1), randint(0, self.size - 1)), lens, randint(0, 1))  # Присвавыем случайные координаты кораблю
                try:
                    board.add_ship(new_ship)  # Пробуем разместить корабль на поле
                    break
                except BoardWrongShipExceptions:
                    pass
        board.begin()
        return board

    def random_board(self):  # Создаем доску со случайным расположением кораблей
        board = None
        while board is None:
            board = self.try_board()
        return board

    def greet(self):  # Печатаем привествие и краткую инструкцию
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

    def loop(self):  # Отображение процесса игры
        num = 0
        while True:
            print('-' * 23)
            print('Доска игрока')
            print(f'Живых кораблей {self.us.board.living_ships}')
            print(self.us.board, self.ai.board, sep=' ')
            print('-' * 23)
            print('Доска компьютера')
            print(f'Живых кораблей {self.ai.board.living_ships}')
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

    def start(self):  # Начинаем игру
        self.greet()
        self.loop()


g = Game()
g.start()
