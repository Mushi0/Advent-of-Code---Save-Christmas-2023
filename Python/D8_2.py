import sys
import time
import itertools
import math
from functools import reduce

def lcm_of_list(numbers):
    def lcm(a, b):
        return abs(a*b) // math.gcd(a, b)
    return reduce(lcm, numbers)

def main(DATA_INPUT):
    start_time = time.time()

    with open(DATA_INPUT) as f:
        direction = f.readline().strip()
        direction = [0 if d == 'L' else 1 for d in direction]
        f.readline()
        
        nodes = {}
        for line in f:
            node = line.strip().split()
            nodes[node[0]] = (node[2][1:-1], node[3][:-1])
    
    current_nodes = []
    for node in nodes.keys():
        if node[-1] == 'A':
            current_nodes.append(node)
    
    nb_steps_to_z = []
    for node in current_nodes:
        current_node = node
        direction_cycle = itertools.cycle(direction)

        nb_steps = 0
        while current_node[-1] != 'Z':
            current_node = nodes[current_node][next(direction_cycle)]
            nb_steps += 1
        
        nb_steps_to_z.append(nb_steps)
    
    nb_steps = lcm_of_list(nb_steps_to_z)
    
    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'The number of steps to reach ZZZ is: {nb_steps}')

if __name__ == '__main__':
    main(sys.argv[1])