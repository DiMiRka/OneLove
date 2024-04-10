class Dot:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f'Dot ({self.x},{self.y})'

class Ship:
    def __init__(self, ship_nose, size, direction):
        self.size = size  # Длина корабля
        self.ship_nose = ship_nose  # Нос корабля (точка х)
        self.direction = direction  # Направление корабля (вертикальное/горизонтальное)
        self.heart = size  # Количество жизней

    @property
    def dots(self):
        ship_dots = []
        for i in range (self.size):
            dot_x = self.ship_nose.x
            dot_y = self.ship_nose.y
            if self.direction == 0:
                dot_x += i
            elif self.direction == 1:
                dot_y += i
            ship_dots.append(Dot(dot_x, dot_y))
        return ship_dots

    def shooten(self, shot):
        return shot in self.dots

s = Ship(Dot(1,2), 2, 0)
print(s.dots)
print(s.shooten(Dot(2, 2)))