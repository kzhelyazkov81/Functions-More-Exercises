from math import floor


def coordinates(x1, y1, x2, y2):
    if x1 ** 2 + y1 ** 2 > x2 ** 2 + y2 ** 2:
        print(f'({floor(x2)}, {floor(y2)})')
    else:
        print(f'({floor(x1)}, {floor(y1)})')


a, b, c, d = float(input()), float(input()), float(input()), float(input())

coordinates(a, b, c, d)
