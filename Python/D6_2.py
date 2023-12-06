import sys
import math
import time

def main(DATA_INPUT):
    start_time = time.time()

    with open(DATA_INPUT) as f:
        my_str = f.readlines()

    race_time = int(''.join(my_str[0].split()).split(':')[1])
    distance = int(''.join(my_str[1].split()).split(':')[1])
    
    tt = int(race_time/2)
    while tt*(race_time - tt) > distance:
            tt -= 1
    if race_time % 2 != 0:
        total = ((math.floor(race_time/2) - tt)*2)
    else:
        total = ((int(race_time/2) - tt)*2 - 1)
    
    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'The number of ways you can beat the record in this one much longer race is: {total}')

if __name__ == '__main__':
    main(sys.argv[1])