import sys
import time
import itertools
from functools import lru_cache

def check_if_end(nodes):
    for node in nodes:
        if node[-1] != 'Z':
            return False
    return True

nodes = {}

@lru_cache(maxsize = None)
def get_next_z(node, direction):
    nb_steps = 1
    node = nodes[node][next(direction)]
    while node[-1] != 'Z':
        node = nodes[node][next(direction)]
        nb_steps += 1
    return nb_steps, node, direction

def main(DATA_INPUT):
    start_time = time.time()

    with open(DATA_INPUT) as f:
        direction = f.readline().strip()
        direction = [0 if d == 'L' else 1 for d in direction]
        f.readline()
        
        for line in f:
            node = line.strip().split()
            nodes[node[0]] = (node[2][1:-1], node[3][:-1])
    
    current_nodes = []
    for node in nodes.keys():
        if node[-1] == 'A':
            current_nodes.append(node)
    
    direction_cycles = [itertools.cycle(direction) for _ in range(len(current_nodes))]
    
    nb_steps = [0] * len(current_nodes)
    while not (check_if_end(current_nodes) and all(x == nb_steps[0] for x in nb_steps)):
        smallest_index = nb_steps.index(min(nb_steps))
        update_step, current_nodes[smallest_index], direction_cycles[smallest_index] = \
            get_next_z(current_nodes[smallest_index], direction_cycles[smallest_index])
        nb_steps[smallest_index] += update_step
        print(nb_steps[smallest_index])
    
    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'The number of steps to reach ZZZ is: {nb_steps[0]}')

if __name__ == '__main__':
    main(sys.argv[1])