import sys
import re

def main(DATA_INPUT):
    total = 0
    with open(DATA_INPUT) as f:
        my_str = f.readline()
        while my_str:
            my_number_list = re.findall(r'\d', my_str)
            total += int(my_number_list[0] + my_number_list[-1])
            my_str = f.readline()
    print(total)

if __name__ == '__main__':
    main(sys.argv[1])