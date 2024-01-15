import sys
import time

## Try maximal matching

def maximal_matching(graph):
    matching = set()
    matched = set()
    for v in graph:
        if v not in matched:
            for u in graph[v]:
                if u not in matched:
                    matching.add((v, u))
                    matched.add(v)
                    matched.add(u)
                    break
    return matching
        
def main(DATA_INPUT):
    start_time = time.time()

    components = {}
    with open(DATA_INPUT, 'r') as f:
        for line in f:
            name, connections = line.strip().split(': ')
            connections = connections.split(' ')
            components[name] = set(connections)

    new_compoents = {}
    for component, connections in components.items():
        for connection in connections:
            if not connection in components:
                if not connection in new_compoents:
                    new_compoents[connection] = {component}
                else:
                    new_compoents[connection].add(component)
            else:
                components[connection].add(component)
    components.update(new_compoents)
    
    for key, value in components.items():
        components[key] = list(value)
        print(key, value)

    max_matching = maximal_matching(components)
    print(max_matching)

    print(f'Time taken: {(time.time() - start_time):.3e}s')
    # print(f'The product of the sizes of the two groups is: {prod}')

if __name__ == '__main__':
    main(sys.argv[1])