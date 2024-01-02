import sys
import time
import itertools

def main(DATA_INPUT):
    start_time = time.time()

    with open(DATA_INPUT) as f:
        direction = f.readline().strip()
        direction = [0 if d == 'L' else 1 for d in direction]
        direction_cycle = itertools.cycle(direction)
        f.readline()
        
        nodes = {}
        for line in f:
            node = line.strip().split()
            nodes[node[0]] = (node[2][1:-1], node[3][:-1])
    
    nb_steps = 0
    node = 'AAA'
    while node != 'ZZZ':
        node = nodes[node][next(direction_cycle)]
        nb_steps += 1
    
    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'The number of steps to reach ZZZ is: {nb_steps}')

if __name__ == '__main__':
    main(sys.argv[1])