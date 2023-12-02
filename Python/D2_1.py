import sys
import re

limit = {'r': 12, 
        'g': 13, 
        'b': 14}

def main(DATA_INPUT):
    total = 0
    id = 1
    with open(DATA_INPUT) as f:
        my_str = f.readline()
        while my_str:
            my_list = re.findall(r'\d+ .', my_str)
            id_add = id
            for balls in my_list:
                [num, colour] = balls.split(' ')
                if int(num) > limit[colour]:
                    id_add = 0
                    break
            total += id_add
            my_str = f.readline()
            id += 1
    print(total)

if __name__ == '__main__':
    main(sys.argv[1])