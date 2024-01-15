import sys
import time
from copy import deepcopy
from tqdm import tqdm
import random

def check_separated(components):
    remaining = list(components.keys())
    to_visit = [remaining.pop()]
    while to_visit:
        current = to_visit.pop()
        for connection in components[current]:
            if connection in remaining:
                to_visit.append(connection)
                remaining.remove(connection)
    if len(remaining) == 0:
        return False, 0, 0
    return True, len(remaining), (len(components) - len(remaining))
        
def main(DATA_INPUT):
    start_time = time.time()

    components = {}
    with open(DATA_INPUT, 'r') as f:
        for line in f:
            name, connections = line.strip().split(': ')
            connections = connections.split(' ')
            components[name] = set(connections)
    
    new_compoents = {}
    all_connections = []
    for component, connections in components.items():
        for connection in connections:
            if not [connection, component] in all_connections:
                all_connections.append([component, connection])
            if not connection in components:
                if not connection in new_compoents:
                    new_compoents[connection] = {component}
                else:
                    new_compoents[connection].add(component)
            else:
                components[connection].add(component)
    components.update(new_compoents)
    
    random.seed(42)
    random.shuffle(all_connections)
    for i in tqdm(range(len(all_connections))):
        connection_1 = all_connections[i]
        for j in tqdm(range(i + 1, len(all_connections))):
            connection_2 = all_connections[j]
            for k in tqdm(range(j + 1, len(all_connections))):
                connection_3 = all_connections[k]
                new_compoents = deepcopy(components)
                new_compoents[connection_1[0]].remove(connection_1[1])
                new_compoents[connection_1[1]].remove(connection_1[0])
                new_compoents[connection_2[0]].remove(connection_2[1])
                new_compoents[connection_2[1]].remove(connection_2[0])
                new_compoents[connection_3[0]].remove(connection_3[1])
                new_compoents[connection_3[1]].remove(connection_3[0])
                separated, nb_group1, nb_group2 = check_separated(new_compoents)
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