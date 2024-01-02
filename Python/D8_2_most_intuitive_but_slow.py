import sys
import time
import itertools

def check_if_end(nodes):
    for node in nodes:
        if node[-1] != 'Z':
            return False
    return True

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
    
    current_nodes = []
    for node in nodes.keys():
        if node[-1] == 'A':
            current_nodes.append(node)
    
    nb_steps = 0
    while not check_if_end(current_nodes):
        next_direction = next(direction_cycle)

        next_nodes = []
        for node in current_nodes:
            next_nodes.append(nodes[node][next_direction])
        
        current_nodes = next_nodes
        nb_steps += 1
    
    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'The number of steps to reach ZZZ is: {nb_steps}')

if __name__ == '__main__':
    main(sys.argv[1])