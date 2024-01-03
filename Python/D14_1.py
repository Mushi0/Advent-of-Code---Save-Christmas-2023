import sys
import time

def main(DATA_INPUT):
    start_time = time.time()

    total_load = 0
    my_map = []
    with open(DATA_INPUT) as f:
        for line in f:
            my_map.append(line.strip())
    transpose_map = [list(row)[::-1] for row in zip(*my_map)]

    for line in transpose_map:
        rolling_rocks = 0
        for i, c in enumerate(line):
            if c == 'O':
                rolling_rocks += 1
            elif c == '#':
                total_load += (i + i - rolling_rocks + 1)*rolling_rocks/2
                rolling_rocks = 0
        
        if rolling_rocks:
            total_load += (i + i - rolling_rocks + 3)*rolling_rocks/2

    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'The total load on the north support beams is: {int(total_load)}')

if __name__ == '__main__':
    main(sys.argv[1])