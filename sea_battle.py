class Ship:
    def __init__(self, size, ship_nose, direction, heart):
        self.size = size
        self.ship_nose = ship_nose
        self.direction = direction
        self.heart = heart

    def dots(self):
        return

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