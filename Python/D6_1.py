import sys
import math
import time

def main(DATA_INPUT):
    start_time = time.time()

    total = 1
    with open(DATA_INPUT) as f:
        my_str = f.readlines()

    race_time = my_str[0].strip('\n').split()[1:]
    race_time = [int(t) for t in race_time]
    distance = my_str[1].strip('\n').split()[1:]
    distance = [int(d) for d in distance]
    
    for i, t in enumerate(race_time):
        tt = int(t/2)
        while tt*(t - tt) > distance[i]:
            tt -= 1
        if t % 2 != 0:
            total *= ((math.floor(t/2) - tt)*2)
        else:
            total *= ((int(t/2) - tt)*2 - 1)
    
    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'The multiplication of the numbers is: {total}')

if __name__ == '__main__':
    main(sys.argv[1])