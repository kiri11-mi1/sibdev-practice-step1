# Требуется написать программу, которая будет сортировать строки матрицы по убыванию сумм элементов строк.

from typing import List


def main(matrix: List[List[int]]) -> List[List[int]]:
    for i in range(len(matrix)-1):
        for j in range(len(matrix)-i-1):
            if sum(matrix[j]) > sum(matrix[j+1]):
                matrix[j], matrix[j+1] = matrix[j+1], matrix[j]
    return matrix[::-1]
