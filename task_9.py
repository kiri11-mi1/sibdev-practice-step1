# Требуется написать программу, которая бы переводила числа из римской системы счисления 
# (состоящих только из трех римских цифр - X, V, I) в арабскую.

def main(roman_number: str) -> int:
    numbers = {'X': 10, 'V': 5, 'I': 1}
    result = 0
    for i, rom_num in enumerate(roman_number):
        if len(roman_number) - 1 == i:
            result += numbers[rom_num]
            continue
        if numbers[rom_num] >= numbers[roman_number[i+1]]:
            result += numbers[rom_num]
        else:
            result -= numbers[rom_num]

    return result


print(main('XIV'))