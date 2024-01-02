import sys
import time

def main(DATA_INPUT):
    start_time = time.time()

    map = []
    with open(DATA_INPUT) as f:
        for line in f:
            map.append(line.strip())
    
    new_map = []
    # row expansion
    for row in map:
        new_map.append(row)
        if all(char == '.' for char in row):
            new_map.append(row)
    nb_expanded = 0
    # column expansion
    for column_index in range(len(map[0])):
        if all(row[column_index] == '.' for row in map):
            for i in range(len(new_map)):
                new_map[i] = new_map[i][:column_index + nb_expanded] + '.' + \
                            new_map[i][column_index + nb_expanded:]
            nb_expanded += 1
    
    # # plot-----------------------------------------------
    # for line in new_map:
    #     print(line)
    # # end plot-------------------------------------------
    
    galaxies = []
    for i, row in enumerate(new_map):
        for j, char in enumerate(row):
            if char == '#':
                galaxies.append((i, j))
    
    total_distance = 0
    for i in range(len(galaxies)):
        for j in range(i, len(galaxies)):
            galaxy = galaxies[i]
            other_galaxy = galaxies[j]
            total_distance += (abs(galaxy[0] - other_galaxy[0]) + 
                                abs(galaxy[1] - other_galaxy[1]))

    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'The sum of these lengths is: {total_distance}')

if __name__ == '__main__':
    main(sys.argv[1])