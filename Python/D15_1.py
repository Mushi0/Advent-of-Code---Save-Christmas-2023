import sys
import time

MULTIPLE = 17
TOTAL_CODE = 256

def hash_func(string):
    current_value = 0
    for c in string:
        current_value += ord(c)
        current_value *= MULTIPLE
        current_value %= TOTAL_CODE
    return current_value

def main(DATA_INPUT):
    start_time = time.time()

    with open(DATA_INPUT) as f:
        strings = f.readline().strip().split(',')

    total = 0    
    for string in strings:
        total += hash_func(string)

    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'The sum of the results is: {int(total)}')

if __name__ == '__main__':
    main(sys.argv[1])