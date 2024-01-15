import sys
import time
from copy import deepcopy
from tqdm import tqdm
import random

def check_separated(all_connections):
    while len(all_connections) > 2:
        group_1 = all_connections.pop(0)
        for group_2 in all_connections:
            if group_1.intersection(group_2):
                all_connections.remove(group_2)
                all_connections.append(group_1.union(group_2))
                break

    if not all_connections[0].intersection(all_connections[1]):
        return True, len(all_connections[0]), len(all_connections[1])
    else:
        return False, 0, 0
        
def main(DATA_INPUT):
    start_time = time.time()
    
    all_connections = []
    with open(DATA_INPUT, 'r') as f:
        for line in f:
            name, connections = line.strip().split(': ')
            connections = connections.split(' ')
            for connection in connections:
                if not {name, connection} in all_connections:
                    all_connections.append({name, connection})
    
    random.seed(42)
    random.shuffle(all_connections)
    for i in tqdm(range(len(all_connections))):
        connection_1 = all_connections[i]
        for j in tqdm(range(i + 1, len(all_connections))):
            connection_2 = all_connections[j]
            for k in tqdm(range(j + 1, len(all_connections))):
                connection_3 = all_connections[k]
                new_connections = deepcopy(all_connections)
                new_connections.remove(connection_1)
                new_connections.remove(connection_2)
                new_connections.remove(connection_3)
                separated, nb_group1, nb_group2 = check_separated(new_connections)
                if separated:
                    prod = nb_group1 * nb_group2
                    break
            if separated:
                break
        if separated:
            break

    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'The product of the sizes of the two groups is: {prod}')

if __name__ == '__main__':
    main(sys.argv[1])