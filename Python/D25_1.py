import sys
import time
import networkx as nx

## I KNEW IT! I HAVE TO USE GRAPH THEORY! 
## use Ford–Fulkerson algorithm to find the minimum cut! 

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
                    all_connections.append({name, connection})
                all_components.add(connection)
            all_components.add(name)
    nb_components = len(all_components)
        
    G = nx.DiGraph()
    for compo_1, compo_2 in all_connections:
        G.add_edge(compo_1, compo_2, capacity = nb_components)
        G.add_edge(compo_2, compo_1, capacity = nb_components)
    
    for compo_1 in all_components:
        for compo_2 in all_components:
            if not compo_1 == compo_2:
                _, partition = nx.minimum_cut(G, compo_1, compo_2)
                count = 0
                for compo_1, compo_2 in list(all_connections):
                    if ((compo_1 in partition[0] and compo_2 in partition[1]) or 
                        (compo_1 in partition[1] and compo_2 in partition[0])):
                        count += 1
                if count == 3:
                    prod = len(partition[0]) * len(partition[1])
                    break
        if count == 3:
            break

    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'The product of the sizes of the two groups is: {prod}')

if __name__ == '__main__':
    main(sys.argv[1])