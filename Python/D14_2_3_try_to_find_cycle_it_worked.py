import sys
import time

NB_CYCLES = 1000000000
# NB_CYCLES = 3

def get_key(my_dict, val):
    for key, value in my_dict.items():
        if value == val:
            return key

def roll(N_ROWS, N_COLS, rocks: set, stable_rocks: set):
    # north
    new_stable_rocks = stable_rocks.copy()
    for j in range(N_COLS):
        for i in range(N_ROWS):
            if (i, j) in rocks:
                fixed = False
                for k in range(1, i + 1):
                    if (i - k, j) in new_stable_rocks:
                        new_stable_rocks.add((i - k + 1, j))
                        rocks.remove((i, j))
                        rocks.add((i - k + 1, j))
                        fixed = True
                        break
                if not fixed:
                    rocks.remove((i, j))
                    rocks.add((0, j))
                    new_stable_rocks.add((0, j))
    
    # west
    new_stable_rocks = stable_rocks.copy()
    for i in range(N_ROWS):
        for j in range(N_COLS):
            if (i, j) in rocks:
                fixed = False
                for k in range(1, j + 1):
                    if (i, j - k) in new_stable_rocks:
                        new_stable_rocks.add((i, j - k + 1))
                        rocks.remove((i, j))
                        rocks.add((i, j - k + 1))
                        fixed = True
                        break
                if not fixed:
                    rocks.remove((i, j))
                    rocks.add((i, 0))
                    new_stable_rocks.add((i, 0))
    
    # south
    new_stable_rocks = stable_rocks.copy()
    for j in range(N_COLS):
        for i in range(N_ROWS - 1, -1, -1):
            if (i, j) in rocks:
                fixed = False
                for k in range(1, N_ROWS - i):
                    if (i + k, j) in new_stable_rocks:
                        new_stable_rocks.add((i + k - 1, j))
                        rocks.remove((i, j))
                        rocks.add((i + k - 1, j))
                        fixed = True
                        break
                if not fixed:
                    rocks.remove((i, j))
                    rocks.add((N_ROWS - 1, j))
                    new_stable_rocks.add((N_ROWS - 1, j))
    
    # east
    new_stable_rocks = stable_rocks.copy()
    for i in range(N_ROWS):
        for j in range(N_COLS - 1, -1, -1):
            if (i, j) in rocks:
                fixed = False
                for k in range(1, N_COLS - j):
                    if (i, j + k) in new_stable_rocks:
                        new_stable_rocks.add((i, j + k - 1))
                        rocks.remove((i, j))
                        rocks.add((i, j + k - 1))
                        fixed = True
                        break
                if not fixed:
                    rocks.remove((i, j))
                    rocks.add((i, N_COLS - 1))
                    new_stable_rocks.add((i, N_COLS - 1))
    
    return rocks

def main(DATA_INPUT):
    start_time = time.time()

    total_load = 0
    rocks = set()
    stable_rocks = set()
    with open(DATA_INPUT) as f:
        lines = f.readlines()
        N_ROWS = len(lines)
        N_COLS = len(lines[0].strip())
        for i, line in enumerate(lines):
            for j, c in enumerate(line.strip()):
                if c == 'O':
                    rocks.add((i, j))
                elif c == '#':
                    stable_rocks.add((i, j))

    rock_cycles = {0: rocks.copy()}
    cycle = 0
    for _ in range(NB_CYCLES):
        rocks = roll(N_ROWS, N_COLS, rocks, stable_rocks)
        cycle += 1
        if rocks in rock_cycles.values():
            break
        rock_cycles[cycle] = rocks.copy()
    
    cycle_point = get_key(rock_cycles, rocks)
    id = (NB_CYCLES - cycle_point) % (cycle - cycle_point) + cycle_point
    rocks = rock_cycles[id]

    total_load = sum((N_ROWS - i) for i, _ in rocks)

    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'The total load on the north support beams is: {total_load}')

if __name__ == '__main__':
    main(sys.argv[1])