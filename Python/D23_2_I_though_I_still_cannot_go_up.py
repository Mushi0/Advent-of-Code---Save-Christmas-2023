import sys
import time
import heapq

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def maximum_path(graph, start, end):
    n = len(graph)
    visited = [False] * n
    max_path = [0] * n
    prev = [None] * n
    max_path[start] = float('inf')
    queue = [(-max_path[start], start)]
    while queue:
        _, u = heapq.heappop(queue)
        if visited[u]:
            continue
        visited[u] = True
        for v, weight in enumerate(graph[u]):
            if weight > 0 and max_path[u] + weight > max_path[v]:
                max_path[v] = max_path[u] + weight
                prev[v] = u
                heapq.heappush(queue, (-max_path[v], v))
    path = []
    u = end
    while u is not None:
        path.append(u)
        u = prev[u]
    path.reverse()
    return path, max_path[end]

def main(DATA_INPUT):
    start_time = time.time()

    with open(DATA_INPUT, 'r') as f:
        my_map = f.read().splitlines()

    start_pos = (0, 1)
    end_pos = (len(my_map) - 1, len(my_map[0]) - 2)

    forks = []
    for i in range(1, len(my_map) - 1):
        line = my_map[i]
        for j in range(1, len(line) - 1):
            if sum([1 for dir in dirs if my_map[i + dir[0]][j + dir[1]] in '^v<>']) >= 3:
                forks.append((i, j))

    def check_slope_valid(pos, dir):
        return (my_map[pos[0]][pos[1]] == '.' or 
                (my_map[pos[0]][pos[1]] == '>' and dir == (0, 1)) or 
                (my_map[pos[0]][pos[1]] == 'v' and dir == (1, 0)) or 
                (my_map[pos[0]][pos[1]] == '<' and dir == (0, -1)) or 
                (my_map[pos[0]][pos[1]] == '^' and dir == (-1, 0)))

    network = [[0 for _ in range(len(forks) + 1)] for _ in range(len(forks) + 1)]
    for i, fork in enumerate(forks):
        for dir in dirs:
            this_pos = (fork[0] + dir[0], fork[1] + dir[1])
            if not check_slope_valid(this_pos, dir):
                continue

            step_count = 1
            previous_pos = fork
            end = False
            while sum([1 for d in dirs if my_map[this_pos[0] + d[0]][this_pos[1] + d[1]] in '^v<>']) <= 2:
                step_count += 1
                for dir_2 in dirs:
                    next_pos = (this_pos[0] + dir_2[0], this_pos[1] + dir_2[1])
                    if next_pos == end_pos:
                        network[i][len(forks)] = step_count
                        end = True
                        break
                    if ((next_pos[0], next_pos[1]) != previous_pos and 
                        check_slope_valid(next_pos, dir_2)):
                        previous_pos = this_pos
                        this_pos = next_pos
                        break
                if end:
                    break
            if not end:
                network[i][forks.index(next_pos)] = step_count
    
    previous = start_pos
    this_pos = (start_pos[0] + 1, start_pos[1])
    step_count = 1
    found = False
    while sum([1 for d in dirs if my_map[this_pos[0] + d[0]][this_pos[1] + d[1]] in '^v<>']) <= 2:
        step_count += 1
        for dir in dirs:
            next_pos = (this_pos[0] + dir[0], this_pos[1] + dir[1])
            if next_pos in forks:
                found = True
                break
            if ((next_pos[0], next_pos[1]) != previous and 
                check_slope_valid(next_pos, dir)):
                previous = this_pos
                this_pos = next_pos
                break
        if found:
            break
    
    forks = [start_pos] + forks + [end_pos]
    print(forks)
    fork_index = forks.index(next_pos)
    new_network = [[step_count if i == fork_index else 0 for i in range(len(forks))]]
    for i, line in enumerate(network):
        if i == fork_index:
            new_network.append([step_count] + line)
        else:
            new_network.append([0] + line)
    
    for line in new_network:
        print(line)
    
    path, max_sum = maximum_path(new_network, 0, len(forks) - 1)
    print("Path:", path)
    print("Maximum sum:", max_sum)

    max_sum = 0
    for i in range(len(path) - 1):
        max_sum += new_network[path[i]][path[i + 1]]
    
    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'The longest hike is: {max_sum} steps long')

if __name__ == '__main__':
    main(sys.argv[1])