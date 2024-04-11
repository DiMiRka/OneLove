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
        self.wrecked_ships = 0  # Пораженные корабли
        self.field = [['O'] * size for i in range(size)]  # Расчерчивает поле
        self.busy = []  # Список занятых клеток (кораблями или ранее сделанными выстрелами)
        self.ships = []  # Список кораблей на поле

    def __str__(self):
        draw = '   | 1 | 2 | 3 | 4 | 5 | 6 |'  # Пишем верхние координаты
        draw += '\n --------------------------- '
        for i, row in enumerate(self.field):  # Чертим поле
            draw += f'\n {i+1} | ' + ' | '.join(row) + ' | '

        if self.hid:  # Проверяем показывать ли корабли на поле
            draw = draw.replase('■', 'O')
        return draw
