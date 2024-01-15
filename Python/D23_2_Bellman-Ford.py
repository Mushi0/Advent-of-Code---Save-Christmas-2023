import sys
import time

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bellman_ford(graph, source):
    distance = [-float('Inf')] * len(graph)
    distance[source] = 0

    for _ in range(len(graph) - 1):
        for node in range(len(graph)):
            for neighbour, weight in enumerate(graph[node]):
                if distance[node] != -float('Inf') and distance[node] - weight > distance[neighbour]:
                    distance[neighbour] = distance[node] - weight

    for node in range(len(graph)):
        for neighbour, weight in enumerate(graph[node]):
            if distance[node] != -float('Inf') and distance[node] - weight > distance[neighbour]:
                print("Graph contains a positive-weight cycle")
                return

    return [-d for d in distance]

def main(DATA_INPUT):
    start_time = time.time()

    with open(DATA_INPUT, 'r') as f:
        my_map = f.read().splitlines()

    # which one is faster? 
    for i, line in enumerate(my_map):
        my_map[i] = my_map[i].replace('>', '.')
        my_map[i] = my_map[i].replace('<', '.')
        my_map[i] = my_map[i].replace('^', '.')
        my_map[i] = my_map[i].replace('v', '.')

    start_pos = (0, 1)
    end_pos = (len(my_map) - 1, len(my_map[0]) - 2)

    forks = []
    for i in range(1, len(my_map) - 1):
        line = my_map[i]
        for j in range(1, len(line) - 1):
            if (my_map[i][j] == '.' and 
                sum([1 for dir in dirs if my_map[i + dir[0]][j + dir[1]] in '.']) >= 3):
                forks.append((i, j))
    forks = [start_pos] + forks + [end_pos] 

    network = [[float('inf') for _ in range(len(forks))] for _ in range(len(forks))]
    for i, fork in enumerate(forks):
        for dir in dirs:
            if ((fork[0] == 0 and dir == (-1, 0)) or 
                (fork[0] == len(my_map) - 1 and dir == (1, 0))):
                continue
            this_pos = (fork[0] + dir[0], fork[1] + dir[1])
            if my_map[this_pos[0]][this_pos[1]] == '#':
                continue

            step_count = 1
            previous_pos = fork
            end = False
            start = False
            while sum([1 for d in dirs if my_map[this_pos[0] + d[0]][this_pos[1] + d[1]] == '.']) == 2:
                step_count += 1
                for dir_2 in dirs:
                    next_pos = (this_pos[0] + dir_2[0], this_pos[1] + dir_2[1])
                    if previous_pos != end_pos and next_pos == end_pos:
                        network[i][-1] = step_count
                        end = True
                        break
                    if previous_pos != start_pos and next_pos == start_pos:
                        network[i][0] = step_count
                        start = True
                        break
                    if ((next_pos[0], next_pos[1]) != previous_pos and 
                        my_map[next_pos[0]][next_pos[1]] != '#'):
                        previous_pos = this_pos
                        this_pos = next_pos
                        break
                if end or start:
                    break
            if not (end or start):
                network[i][forks.index(next_pos)] = step_count
    
    print(bellman_ford(network, 0))

    print(f'Time taken: {(time.time() - start_time):.3e}s')
    # print(f'The longest hike is: {nb_steps} steps long')

if __name__ == '__main__':
    main(sys.argv[1])