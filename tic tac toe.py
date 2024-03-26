print("Давайте же начнём игру!")
field = [['-'] * 3 for i in range(3)]
for i, row in enumerate(field):
    row_str = str(i) + ' ' + ' '.join(map(str, row))
    print(row_str)
print('Начинают крестики')

#while True:
