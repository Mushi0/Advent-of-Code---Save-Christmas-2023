import sys
import time
from docplex.mp.model import Model
from itertools import chain, combinations

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

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

    network = [[0 for _ in range(len(forks))] for _ in range(len(forks))]
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
    
    # for line in network:
    #     print(line)
    
    forks_len = len(forks)
    forks_index = [i for i in range(forks_len)]
    mdl = Model()
    
    x = mdl.binary_var_matrix(len(forks), len(forks), name='x')
    
    # flow constraints, one in one out
    mdl.add_constraints(mdl.sum(x[i, j] for j in range(forks_len)) == mdl.sum(x[j, i] for j in range(forks_len)) for i in range(1, forks_len - 1))
    
    # at most visit once
    mdl.add_constraints(mdl.sum(x[i, j] for j in range(forks_len)) <= 1 for i in range(1, forks_len - 1))
    
    # start and end
    mdl.add_constraint(mdl.sum(x[0, j] for j in range(forks_len)) == 1)
    mdl.add_constraint(mdl.sum(x[j, forks_len - 1] for j in range(forks_len)) == 1)
    mdl.add_constraint(mdl.sum(x[i, 0] for i in range(forks_len)) == 0)
    mdl.add_constraint(mdl.sum(x[forks_len - 1, i] for i in range(forks_len)) == 0)
    
    # eleminate sub-tours
    mdl.add_constraints(x[i, j] + x[j, i] <= 1 for i in range(forks_len) 
                        for j in range(forks_len) if i != j)
    mdl.add_constraints(x[i, j] + x[j, k] + x[k, i] <= 2 
                        for i in range(forks_len) 
                        for j in range(forks_len) 
                        for k in range(forks_len) 
                        if i != j and j != k and i != k)
    mdl.add_constraints(x[i, j] + x[j, k] + x[k, l] + x[l, i] <= 3 
                        for i in range(forks_len) 
                        for j in range(forks_len) 
                        for k in range(forks_len) 
                        for l in range(forks_len) 
                        if i != j and j != k and k != l and i != k and i != l and j != l)
    mdl.add_constraints(x[i, j] + x[j, k] + x[k, l] + x[l, m] + x[m, i] <= 4 
                        for i in range(forks_len) 
                        for j in range(forks_len) 
                        for k in range(forks_len) 
                        for l in range(forks_len) 
                        for m in range(forks_len) 
                        if i != j and j != k and k != l and l != m and i != k and i != l and i != m and j != l and j != m and k != m)
    
    # power_set = chain.from_iterable(combinations(forks_index, r) for r in range(forks_len + 1))
    # for group in power_set:
    #     if len(group) < 2:
    #         continue
    #     elif len(group) > 3:
    #         continue
    #     mdl.add_constraint(mdl.sum(x[i, j] for i in group for j in group if i != j) <= len(group) - 1)
    
    # maximum cost
    obj = mdl.sum(x[i, j]*network[i][j] for i in range(forks_len) for j in range(forks_len))
    mdl.maximize(obj)
    mdl.print_information()
    msol = mdl.solve(log_output = True, clean_before_solve = True)
    for i in range(forks_len):
        for j in range(forks_len):
            if msol[x[i, j]] > 0.5:
                print(f'({i}, {j})')

    print(f'Time taken: {(time.time() - start_time):.3e}s')
    # print(f'The longest hike is: {nb_steps} steps long')

if __name__ == '__main__':
    main(sys.argv[1])