import sys
import time
from tqdm import tqdm
from functools import lru_cache

NB_CYCLES = 1000000000
# NB_CYCLES = 3

@lru_cache(maxsize = None)
def roll(N_ROWS, N_COLS, rocks: tuple, stable_rocks: tuple):
    # north
    rocks = list(rocks)
    new_stable_rocks = list(stable_rocks)
    for j in range(N_COLS):
        for i in range(N_ROWS):
            if (i, j) in rocks:
                fixed = False
                for k in range(1, i + 1):
                    if (i - k, j) in new_stable_rocks:
                        new_stable_rocks.append((i - k + 1, j))
                        rocks.remove((i, j))
                        rocks.append((i - k + 1, j))
                        fixed = True
                        break
                if not fixed:
                    rocks.remove((i, j))
                    rocks.append((0, j))
                    new_stable_rocks.append((0, j))
    
    # west
    new_stable_rocks = list(stable_rocks)
    for i in range(N_ROWS):
        for j in range(N_COLS):
            if (i, j) in rocks:
                fixed = False
                for k in range(1, j + 1):
                    if (i, j - k) in new_stable_rocks:
                        new_stable_rocks.append((i, j - k + 1))
                        rocks.remove((i, j))
                        rocks.append((i, j - k + 1))
                        fixed = True
                        break
                if not fixed:
                    rocks.remove((i, j))
                    rocks.append((i, 0))
                    new_stable_rocks.append((i, 0))
    
    # south
    new_stable_rocks = list(stable_rocks)
    for j in range(N_COLS):
        for i in range(N_ROWS - 1, -1, -1):
            if (i, j) in rocks:
                fixed = False
                for k in range(1, N_ROWS - i):
                    if (i + k, j) in new_stable_rocks:
                        new_stable_rocks.append((i + k - 1, j))
                        rocks.remove((i, j))
                        rocks.append((i + k - 1, j))
                        fixed = True
                        break
                if not fixed:
                    rocks.remove((i, j))
                    rocks.append((N_ROWS - 1, j))
                    new_stable_rocks.append((N_ROWS - 1, j))
    
    # east
    new_stable_rocks = list(stable_rocks)
    for i in range(N_ROWS):
        for j in range(N_COLS - 1, -1, -1):
            if (i, j) in rocks:
                fixed = False
                for k in range(1, N_COLS - j):
                    if (i, j + k) in new_stable_rocks:
                        new_stable_rocks.append((i, j + k - 1))
                        rocks.remove((i, j))
                        rocks.append((i, j + k - 1))
                        fixed = True
                        break
                if not fixed:
                    rocks.remove((i, j))
                    rocks.append((i, N_COLS - 1))
                    new_stable_rocks.append((i, N_COLS - 1))
    
    return tuple(rocks)

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
    
    rocks = tuple(rocks)
    stable_rocks = tuple(stable_rocks)

    for _ in tqdm(range(NB_CYCLES)):
        rocks = roll(N_ROWS, N_COLS, rocks, stable_rocks)

    total_load = sum((N_ROWS - i) for i, _ in rocks)

    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'The total load on the north support beams is: {total_load}')

if __name__ == '__main__':
    main(sys.argv[1])