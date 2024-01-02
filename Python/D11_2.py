import sys
import time

N = 1000000 - 1

def main(DATA_INPUT):
    start_time = time.time()

    map = []
    with open(DATA_INPUT) as f:
        for line in f:
            map.append(line.strip())

    galaxies = []
    for i, row in enumerate(map):
        for j, char in enumerate(row):
            if char == '#':
                galaxies.append((i, j))

    new_galaxies = galaxies.copy()
    # row expansion
    for row_index, row in enumerate(map):
        if all(char == '.' for char in row):
            for i, galaxy in enumerate(galaxies):
                if galaxy[0] > row_index:
                    new_galaxies[i] = (new_galaxies[i][0] + N, new_galaxies[i][1])
    # column expansion
    for column_index in range(len(map[0])):
        if all(row[column_index] == '.' for row in map):
            for i, galaxy in enumerate(galaxies):
                if galaxy[1] > column_index:
                    new_galaxies[i] = (new_galaxies[i][0], new_galaxies[i][1] + N)
    
    total_distance = 0
    for i in range(len(new_galaxies)):
        for j in range(i, len(new_galaxies)):
            galaxy = new_galaxies[i]
            other_galaxy = new_galaxies[j]
            total_distance += (abs(galaxy[0] - other_galaxy[0]) + 
                                abs(galaxy[1] - other_galaxy[1]))

    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'The sum of these lengths is: {total_distance}')

if __name__ == '__main__':
    main(sys.argv[1])