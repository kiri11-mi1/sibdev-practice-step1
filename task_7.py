# Заваривай горячий чай, садись поудобнее и поехали 😉
# Даны два массива одинаковой размерности. Тебе необходимо сформировать новый массив,
# состоящий из меньших элементов, стоящих на одинаковых позициях первых массивов.

from typing import List


def main(numbers_list1: List[int], numbers_list2: List[int]) -> List[int]:
    return [elem_1 if elem_1 < elem_2 else elem_2 for elem_1, elem_2 in zip(numbers_list1, numbers_list2)]


print(main(
    [1, 4, 5, 7, 8],
    [0, 4, 2, 8, 3]
))