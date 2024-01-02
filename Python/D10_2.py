import sys
import time

map = []

def find_path(coord, last_step):
    if map[coord[0]][coord[1]] == 'F':
        if last_step[0] > coord[0]:
            return (coord[0], coord[1] + 1)
        else:
            return (coord[0] + 1, coord[1])
    elif map[coord[0]][coord[1]] == '7':
        if last_step[0] > coord[0]:
            return (coord[0], coord[1] - 1)
        else:
            return (coord[0] + 1, coord[1])
    elif map[coord[0]][coord[1]] == 'J':
        if last_step[0] < coord[0]:
            return (coord[0], coord[1] - 1)
        else:
            return (coord[0] - 1, coord[1])
    elif map[coord[0]][coord[1]] == 'L':
        if last_step[0] < coord[0]:
            return (coord[0], coord[1] + 1)
        else:
            return (coord[0] - 1, coord[1])
    elif map[coord[0]][coord[1]] == '|':
        if last_step[0] < coord[0]:
            return (coord[0] + 1, coord[1])
        else:
            return (coord[0] - 1, coord[1])
    elif map[coord[0]][coord[1]] == '-':
        if last_step[1] < coord[1]:
            return (coord[0], coord[1] + 1)
        else:
            return (coord[0], coord[1] - 1)

def find_start_dir(coord):
    coords = []
    if map[coord[0]][coord[1] + 1]in '-J7':
        coords.append((coord[0], coord[1] + 1))
    if map[coord[0]][coord[1] - 1] in '-FL':
        coords.append((coord[0], coord[1] - 1))
    if map[coord[0] + 1][coord[1]] in '|JL':
        coords.append((coord[0] + 1, coord[1]))
    if map[coord[0] - 1][coord[1]] in '|F7':
        coords.append((coord[0] - 1, coord[1]))
    return coords

def main(DATA_INPUT):
    start_time = time.time()

    with open(DATA_INPUT) as f:
        for line in f:
            map.append(list(line.strip()))
    
    for i, line in enumerate(map):
        if 'S' in line:
            start_coord = (i, line.index('S'))
            break
    
    [coord_1, coord_2] = find_start_dir(start_coord)
    pips = set([start_coord, coord_1, coord_2])
    new_coord_1 = coord_1
    new_coord_2 = coord_2
    old_coord_1 = start_coord
    old_coord_2 = start_coord
    while coord_1 != coord_2:
        new_coord_1 = find_path(coord_1, old_coord_1)
        new_coord_2 = find_path(coord_2, old_coord_2)
        old_coord_1 = coord_1
        old_coord_2 = coord_2
        coord_1 = new_coord_1
        coord_2 = new_coord_2
        pips.add(coord_1)
        pips.add(coord_2)
    
    nb_tiles = 0
    not_egde = {'FJ', 'L7'}
    for i, line in enumerate(map):
        out_side = -1
        last_edge = '-'
        for j in range(len(line)):
            if ((i, j) in pips) and (map[i][j] != '-'):
                if last_edge + map[i][j] in not_egde:
                    continue
                else:
                    last_edge = map[i][j]
                    out_side *= -1
            elif (((i, j) in pips) and (map[i][j] == '-')) or (map[i][j] == 'S'):
                continue
            
        # # plot-----------------------------------------------
        #     else:
        #         if out_side == -1:
        #             map[i][j] = 'O'
        #         else:
        #             map[i][j] = 'I'
        # print("".join(map[i]))
        # nb_tiles += map[i].count('I')
        # # end plot-------------------------------------------
        
        # no plot--------------------------------------------
            elif out_side == 1:
                nb_tiles += 1
        # end no plot----------------------------------------

    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'The number of tiles enclosed by the loop is: {nb_tiles}')

if __name__ == '__main__':
    main(sys.argv[1])