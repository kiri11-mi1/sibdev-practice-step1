# В русском языке 33 буквы, ваша задача сделать программу которая сможет производить
# операции со словами (переводить каждый символ в цифру, складывать её с остальными цифрами
# и в результате получать число округленное до целого числа) - впоследствии производить операции над этим числом.

import re


ALPHABET_LOWER = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']


def main(input_string: str) -> int:
    words = re.split(r'\+|\-|\*|\/', input_string.lower())
    sum_first = sum([ALPHABET_LOWER.index(symb) + 1 for symb in words[0]])
    sum_second = sum([ALPHABET_LOWER.index(symb) + 1 for symb in words[1]])
    if '+' in input_string:
        return sum_first + sum_second
    elif '-' in input_string:
        return sum_first - sum_second
    elif '*' in input_string:
        return sum_first * sum_second
    elif '/' in input_string:
        return int(sum_first / sum_second)
