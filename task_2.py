from typing import List, Literal
import math


def triangle_square(a, b, c):
    p = (a+b+c) / 2
    return round(math.sqrt(p * (p-a) * (p-b) * (p-c)), 2)


def rectangle_square(a, b):
    return round(a*b, 2)


def circle_square(r):
    return round(math.pi * r**2, 2)


def main(figure: Literal['circle', 'rectangle', 'triangle'], sides: List[int]) -> float:
    if figure == 'circle':
        return circle_square(*sides)
    elif figure == 'rectangle':
        return rectangle_square(*sides)
    elif figure == 'triangle':
        return triangle_square(*sides)
