# У вас есть определенное количество монет (разного номинала), 
# от копеек до рублей. Разработайте возможность перевода 
# этих денег в купюры различного номинала,
# с возможностью выдавать остаток. 
# Размен осуществляется с использованием наиболее крупных купюр.
# Монеты - 1, 5, 10, 25, 50 копеек. 1, 5, 10 рублей.
# Купюры - 10, 50, 100, 500, 1000 рублей.

from typing import List, Tuple


def main(input_coins: List[float]) -> Tuple[List[int], List[float]]:
    summ = sum(input_coins)
    banknotes = []
    coins = []
    for banknote in [1000, 500, 100, 500, 1000]:
        while round(summ, 2) >= banknote:
            banknotes.append(banknote)
            summ -= banknote
    
    for coin in [1, 5, 0.5, 0.25, 0.1, 0.05, 0.01]:
        while round(summ, 2) >= coin:
            coins.append(coin)
            summ -= coin
    
    return banknotes, coins


print(main([0.01, 0.01, 0.05, 0.5, 0.5, 0.5, 1, 1, 1, 1, 5, 5, 5, 10, 10, 10, 10]))