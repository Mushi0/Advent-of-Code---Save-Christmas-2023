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

            last_number = []
            while not np.all(history == 0):
                last_number.append(history[-1])
                history = history[1:] - history[:-1]
            
            total += sum(last_number)

    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'The sum of these extrapolated values is: {total}')

if __name__ == '__main__':
    main(sys.argv[1])