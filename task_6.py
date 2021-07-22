# В одномерном массиве найти сумму элементов, находящихся между первым минимальным и последним
# максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.

from typing import List


def main(numbers_list: List[int]) -> int:
    ind_min_elem = numbers_list.index(min(numbers_list))
    ind_max_elem = len(numbers_list) - numbers_list[::-1].index(max(numbers_list)) - 1
    if ind_min_elem > ind_max_elem:
        return sum(numbers_list[ind_max_elem+1:ind_min_elem])
    return sum(numbers_list[ind_min_elem+1:ind_max_elem])


print(main(
    [1, 12, -3, 5, 7, 8, 100]
))