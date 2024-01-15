import sys
import time
from copy import deepcopy
from tqdm import tqdm
import random

def check_separated(all_connections):
    groups = [{all_connections[0][0], all_connections[0][1]}]
    for connection in all_connections[1:]:
        found_in_group = False
        for group in groups:
            if connection[0] in group:
                group.add(connection[1])
                found_in_group = True
                break
            elif connection[1] in group:
                group.add(connection[0])
                found_in_group = True
                break
        if not found_in_group:
            groups.append({connection[0], connection[1]})
    
    while len(groups) > 2:
        group_1 = groups.pop()
        for group_2 in groups:
            if group_1.intersection(group_2):
                groups.remove(group_2)
                groups.append(group_1.union(group_2))
                break
    if not groups[0].intersection(groups[1]):
        print(groups[0], groups[1])
        return True, len(groups[0]), len(groups[1])
    else:
        return False, 0, 0
        
def main(DATA_INPUT):
    start_time = time.time()

    components = {}
    with open(DATA_INPUT, 'r') as f:
        for line in f:
            name, connections = line.strip().split(': ')
            connections = connections.split(' ')
            components[name] = set(connections)
    
    all_connections = []
    for component, connections in components.items():
        for connection in connections:
            if not [connection, component] in all_connections:
                all_connections.append([component, connection])
    
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