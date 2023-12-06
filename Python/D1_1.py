import sys
import re
import time

def main(DATA_INPUT):
    start_time = time.time()
    
    total = 0
    with open(DATA_INPUT) as f:
        my_str = f.readline()
        while my_str:
            my_number_list = re.findall(r'\d', my_str)
            total += int(my_number_list[0] + my_number_list[-1])
            my_str = f.readline()
    
    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'The sum of all of the calibration values is: {total}')

if __name__ == '__main__':
    main(sys.argv[1])