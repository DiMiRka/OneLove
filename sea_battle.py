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
class Dot:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f'Координата x: {self.x}, Координата y: {self.y}'

class Ship:
    def __init__(self, ship_nose, size, direction):
        self.size = size  # Длина корабля
        self.ship_nose = ship_nose  # Нос корабля (точка х)
        self.direction = direction  # Направление корабля (вертикальное/горизонтальное)
        self.heart = size  # Количество жизней

    @property
    def dots(self):
        ship_dots = []
        dot_x = self.ship_nose
        dot_y =
        for i in range (self.size):
            dot_x = self.ship_nose.x
            dot_y = self.ship_nose.y
            if self.direction == 0:
                dot_x += i
            elif self.direction == 1:
                dot_y += i
            ship_dots.append(Dot(dot_x, dot_y))
        return ship_dots


class Board:
    field = [['O'] * 6 for i in range(6)]

    def draw_field(self):
        print('   | 1 | 2 | 3 | 4 | 5 | 6 |')  # Пишем верхние координаты
        print(' --------------------------- ')
        for i, row in enumerate(self.field):  # Чертим поле
            row_str = f' {i+1} | {' | '.join(map(str, row))} | '
            print(row_str)
            print(' --------------------------- ')




obj = Board()
obj.draw_field()