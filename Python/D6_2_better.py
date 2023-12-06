import sys
import math
import time

def main(DATA_INPUT):
    start_time = time.time()

    with open(DATA_INPUT) as f:
        my_str = f.readlines()

    race_time = int(''.join(my_str[0].split()).split(':')[1])
    distance = int(''.join(my_str[1].split()).split(':')[1])
    
    # x(time - x) > distance
    # x^2 - time*x + distance < 0
    a = 1
    b = -race_time
    c = distance
    d = (b**2) - (4*a*c)
    sol1 = (-b - math.sqrt(d))/(2*a)
    sol2 = (-b + math.sqrt(d))/(2*a)
    total = math.floor(sol2) - math.ceil(sol1) + 1
    
    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'The number of ways you can beat the record in this one much longer race is: {total}')

if __name__ == '__main__':
    main(sys.argv[1])