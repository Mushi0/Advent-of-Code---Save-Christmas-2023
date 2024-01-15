import sys
import time
from itertools import chain, combinations
from tqdm import tqdm
        
def main(DATA_INPUT):
    start_time = time.time()

    all_components = set()
    all_connections = []
    with open(DATA_INPUT, 'r') as f:
        for line in f:
            name, connections = line.strip().split(': ')
            connections = connections.split(' ')
            for connection in connections:
                if not {name, connection} in all_connections:
                    all_connections.append([name, connection])
                all_components.add(connection)
            all_components.add(name)
    
    # divide the set into all combinations of 2 groups
    # found the division with exactly 3 connections between the groups
    all_components = list(all_components)
    power_set = chain.from_iterable(combinations(all_components, r) for r in range(len(all_components) + 1))
    all_components = set(all_components)
    for group_1 in tqdm(power_set):
        group_1 = set(group_1)
        if len(group_1) == 0:
            continue
        group_2 = set(all_components) - group_1
        if len(group_2) == 0:
            continue
        count = 0
        for connection in all_connections:
            if ((connection[0] in group_1 and connection[1] in group_2) or 
                (connection[0] in group_2 and connection[1] in group_1)):
                count += 1
                if count > 3:
                    break
        if count == 3:
            prod = len(group_1) * len(group_2)
            break

    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'The product of the sizes of the two groups is: {prod}')

if __name__ == '__main__':
    main(sys.argv[1])