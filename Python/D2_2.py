import sys
import re
import numpy as np
import time

def main(DATA_INPUT):
    start_time = time.time()
    
    total = 0
    id = 1
    with open(DATA_INPUT) as f:
        my_str = f.readline()
        while my_str:
            my_list = re.findall(r'\d+ .', my_str)
            min_cubes = {'r': 0, 'g': 0, 'b': 0}
            for balls in my_list:
                [num, colour] = balls.split(' ')
                if int(num) > min_cubes[colour]:
                    min_cubes[colour] = int(num)
            total += np.prod(list(min_cubes.values()))
            my_str = f.readline()
            id += 1
    
    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'The sum of the power of the sets is: {total}')

if __name__ == '__main__':
    main(sys.argv[1])