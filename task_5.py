# Вывести на экран столько элементов ряда Фибоначчи, сколько на вход приняла функция.
# Ряд Фибоначчи – это последовательность натуральных чисел, где каждое последующее число является
# суммой двух предыдущих:
# 1 1 2 3 5 8 13 21 34 55 89 …

from typing import List


def main(n: int) -> List[int]:
    if n == 1:
        return [1]
    fibonachi_list = [1, 1]
    for i in range(2, n):
        fibonachi_list.append(fibonachi_list[i-1]+ fibonachi_list[i-2])
    return fibonachi_list

print(main(0))