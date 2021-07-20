# Разработать программу, которая будет определять сколько цифр X содержится в диапазоне чисел от a1 до a2 (включительно).

def main(x: int, a1: int, a2: int) -> int:
    return ' '.join([str(num) for num in range(a1, a2+1)]).count(str(x))
