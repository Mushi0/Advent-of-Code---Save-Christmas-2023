import sys
import time

def search_left(my_str, i):
    i -= 1
    number = ''
    while (i >= 0) and (my_str[i].isdigit()):
        number = my_str[i] + number
        i -= 1
    return number

def search_right(my_str, i):
    i += 1
    str_length = len(my_str)
    number = ''
    while (i < str_length) and (my_str[i].isdigit()):
        number += my_str[i]
        i += 1
    return number

def search_left_and_right(my_str, i):
    str_length = len(my_str)
    if my_str[i].isdigit():
        number = my_str[i]
        if i >= 1:
            number = search_left(my_str, i) + number
        if i <= str_length - 2:
            number += search_right(my_str, i)
        return [number]
    numbers = []
    if (i >= 1) and (my_str[i - 1].isdigit()):
        numbers.append(search_left(my_str, i))
    if (i <= str_length - 1) and (my_str[i + 1].isdigit()):
        numbers.append(search_right(my_str, i))
    return numbers

def get_ratio(first_str, second_str, third_str):
    total_one_line = 0
    str_length = len(second_str)
    for i, char in enumerate(second_str):
        if char == '*':
            gear_ratio = 1
            nb_parts = 0
            if (i >= 1) and (second_str[i - 1].isdigit()):
                nb_parts += 1
                gear_ratio *= int(search_left(second_str, i))
            if (i <= str_length - 2) and (second_str[i + 1].isdigit()):
                nb_parts += 1
                gear_ratio *= int(search_right(second_str, i))
            numbers_first_str = search_left_and_right(first_str, i)
            for number in numbers_first_str:
                nb_parts += 1
                gear_ratio *= int(number)
            numbers_third_str = search_left_and_right(third_str, i)
            for number in numbers_third_str:
                nb_parts += 1
                gear_ratio *= int(number)
            if nb_parts == 2:
                total_one_line += gear_ratio
    return total_one_line

def main(DATA_INPUT):
    start_time = time.time()
    
    total = 0
    with open(DATA_INPUT) as f:
        second_str = f.readline().strip('\n')
        third_str = f.readline().strip('\n')
        first_str = '.' * len(second_str)
        while third_str:
            total += get_ratio(first_str, second_str, third_str)
            first_str = second_str
            second_str = third_str
            third_str = f.readline().strip('\n')
        third_str = '.' * len(second_str)
        total += get_ratio(first_str, second_str, third_str)
    
    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'The sum of all of the gear ratios in your engine schematic is: {total}')

if __name__ == '__main__':
    main(sys.argv[1])