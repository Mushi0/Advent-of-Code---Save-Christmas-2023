import sys
import time
import numpy as np

def main(DATA_INPUT):
    start_time = time.time()

    total = 0
    with open(DATA_INPUT) as f:
        for line in f:
            history = line.strip().split()
            history = np.array([int(h) for h in history])

            first_number = []
            while not np.all(history == 0):
                first_number.append(history[0])
                history = history[1:] - history[:-1]
            
            sign = -1*pow(-1, len(first_number))
            for _ in range(len(first_number)):
                total += sign*first_number.pop()
                sign *= -1

    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'The sum of these extrapolated values is: {total}')

if __name__ == '__main__':
    main(sys.argv[1])