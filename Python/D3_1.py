import sys
import time

def get_sum(first_str, second_str, third_str):
    total_one_line = 0
    str_length = len(second_str)
    i = 0
    is_part_number = False
    while i < str_length:
        number = ''
        if second_str[i].isdigit():
            while (i < str_length) and (second_str[i].isdigit()):
                number += second_str[i]
                if not is_part_number:
                    if i == 0:
                        check_string = first_str[i: i + 2] + second_str[i + 1] + third_str[i: i + 2]
                    elif i == str_length - 1:
                        check_string = first_str[i - 1: i + 1] + second_str[i - 1] + third_str[i - 1: i + 1]
                    else:
                        check_string = first_str[i - 1: i + 2] + second_str[i - 1] + second_str[i + 1] + third_str[i - 1: i + 2]
                    for char in check_string:
                        if (char != '.') and (not char.isdigit()):
                            is_part_number = True
                            break
                i += 1
            if is_part_number:
                total_one_line += int(number)
                is_part_number = False
        i += 1
    return total_one_line

def main(DATA_INPUT):
    start_time = time.time()
    
    total = 0
    with open(DATA_INPUT) as f:
        second_str = f.readline().strip('\n')
        third_str = f.readline().strip('\n')
        first_str = '.' * len(second_str)
        while third_str:
            total += get_sum(first_str, second_str, third_str)
            first_str = second_str
            second_str = third_str
            third_str = f.readline().strip('\n')
        third_str = '.' * len(second_str)
        total += get_sum(first_str, second_str, third_str)
    
    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'The sum of all of the part numbers in the engine schematic is: {total}')

if __name__ == '__main__':
    main(sys.argv[1])