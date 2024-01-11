import sys
import time
import heapq

def main(DATA_INPUT):
    start_time = time.time()

    with open(DATA_INPUT, 'r') as f:
        bricks = []
        for brick in f.read().splitlines():
            brick_list = [[int(i) for i in end.split(',')] for end in brick.split('~')]
            heapq.heappush(bricks, ([min(brick_list[0][2], brick_list[1][2])] + 
                                [tuple(brick_list[0])] + 
                                [tuple(brick_list[1])]))
    
    x_max = max([max(brick[1][0], brick[2][0]) for brick in bricks])
    y_max = max([max(brick[1][1], brick[2][1]) for brick in bricks])
    height_map = [[0 for _ in range(y_max + 1)] 
                 for _ in range(x_max + 1)]
    
    settled_bricks = set()
    while bricks:
        brick = heapq.heappop(bricks)
        if brick[1][2] == brick[2][2]:
            x_1 = min(brick[1][0], brick[2][0])
            x_2 = max(brick[1][0], brick[2][0])
            y_1 = min(brick[1][1], brick[2][1])
            y_2 = max(brick[1][1], brick[2][1])
            max_height = 0
            for xx in range(x_1, x_2 + 1):
                for yy in range(y_1, y_2 + 1):
                    if height_map[xx][yy] > max_height:
                        max_height = height_map[xx][yy]
            settled_bricks.add((max_height + 1, 
                                (brick[1][0], brick[1][1], max_height + 1), 
                                (brick[2][0], brick[2][1], max_height + 1)))
            for xx in range(x_1, x_2 + 1):
                for yy in range(y_1, y_2 + 1):
                    height_map[xx][yy] = max_height + 1
        else:
            x = brick[1][0]
            y = brick[1][1]
            brick_len = abs(brick[1][2] - brick[2][2]) + 1
            max_height = height_map[x][y]
            settled_bricks.add((max_height + 1, 
                                (x, y, max_height + 1), 
                                (x, y, max_height + brick_len)))
            height_map[x][y] = max_height + brick_len
    
    disintegrate = set()
    not_disintegrate = set()
    visited = set()
    for brick in settled_bricks:
        x_1 = min(brick[1][0], brick[2][0])
        x_2 = max(brick[1][0], brick[2][0])
        y_1 = min(brick[1][1], brick[2][1])
        y_2 = max(brick[1][1], brick[2][1])
        z_1 = min(brick[1][2], brick[2][2])

        bottum = []
        for brick_1 in settled_bricks:
            x_1_1 = min(brick_1[1][0], brick_1[2][0])
            x_1_2 = max(brick_1[1][0], brick_1[2][0])
            y_1_1 = min(brick_1[1][1], brick_1[2][1])
            y_1_2 = max(brick_1[1][1], brick_1[2][1])
            z_1_2 = max(brick_1[1][2], brick_1[2][2])
            if (((x_1 <= x_1_2 and x_2 >= x_1_1) and 
                 (y_1 <= y_1_2 and y_2 >= y_1_1)) and 
                z_1 == z_1_2 + 1):
                bottum.append(brick_1)
                visited.add(brick_1)
        if len(bottum) >= 2:
            disintegrate.update(bottum)
        elif len(bottum) == 1:
            not_disintegrate.add(bottum[0])
    
    disintegrate -= not_disintegrate
    disintegrate.update(settled_bricks - visited)

    nb_disintegrate = len(disintegrate)
    
    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'The number of bricks could be disintegrated is: {nb_disintegrate}')

if __name__ == '__main__':
    main(sys.argv[1])