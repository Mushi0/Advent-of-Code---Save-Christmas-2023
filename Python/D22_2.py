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
    
    # get the position of the bricks
    settled_bricks = []
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
            settled_bricks.append(((brick[1][0], brick[1][1], max_height + 1), 
                                    (brick[2][0], brick[2][1], max_height + 1)))
            for xx in range(x_1, x_2 + 1):
                for yy in range(y_1, y_2 + 1):
                    height_map[xx][yy] = max_height + 1
        else:
            x = brick[1][0]
            y = brick[1][1]
            brick_len = abs(brick[1][2] - brick[2][2]) + 1
            max_height = height_map[x][y]
            settled_bricks.append(((x, y, max_height + 1), 
                                (x, y, max_height + brick_len)))
            height_map[x][y] = max_height + brick_len
    
    # get the top and bottum bricks
    new_settled_bricks = []
    for i, brick in enumerate(settled_bricks):
        x_1 = min(brick[0][0], brick[1][0])
        x_2 = max(brick[0][0], brick[1][0])
        y_1 = min(brick[0][1], brick[1][1])
        y_2 = max(brick[0][1], brick[1][1])
        z_1 = max(brick[0][2], brick[1][2])
        z_2 = min(brick[0][2], brick[1][2])

        top = []
        bottum = []
        for j, brick_1 in enumerate(settled_bricks):
            x_1_1 = min(brick_1[0][0], brick_1[1][0])
            x_1_2 = max(brick_1[0][0], brick_1[1][0])
            y_1_1 = min(brick_1[0][1], brick_1[1][1])
            y_1_2 = max(brick_1[0][1], brick_1[1][1])
            z_1_2 = max(brick_1[0][2], brick_1[1][2])
            z_2_2 = min(brick_1[0][2], brick_1[1][2])
            if ((x_1 <= x_1_2 and x_2 >= x_1_1) and 
                 (y_1 <= y_1_2 and y_2 >= y_1_1)):
                if z_1 + 1 == z_2_2 and i != j:
                    top.append(j)
                elif z_2 == z_1_2 + 1 and i != j:
                    bottum.append(j)
        
        new_settled_bricks.append((brick[0], brick[1], tuple(top), tuple(bottum)))
    
    # update the top and bottum bricks while one brick is removed
    def fall(brick_id):
        global new_settled_bricks_copy

        top = new_settled_bricks_copy[brick_id][2]
        for brick_1_id in top:
            brick_1 = new_settled_bricks_copy[brick_1_id]
            new_settled_bricks_copy[brick_1_id] = (brick_1[0], 
                                            brick_1[1], 
                                            brick_1[2], 
                                            tuple([i for i in brick_1[3] if i != brick_id]))
            if len(brick_1[3]) == 1:
                fall(brick_1_id)

    # count the number of bricks that are on the top for calculation
    top_bircks = 0
    for i, (brick) in enumerate(new_settled_bricks):
        if len(brick[3]) == 0:
            top_bircks += 1

    nb_fall = 0
    global new_settled_bricks_copy
    for i in range(len(new_settled_bricks)):
        new_settled_bricks_copy = new_settled_bricks.copy()
        fall(i)
        nb_fall += sum([1 for brick in new_settled_bricks_copy if len(brick[3]) == 0]) - top_bircks
            
    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'The sum of the number of other bricks that would fall is: {nb_fall}')

if __name__ == '__main__':
    main(sys.argv[1])