import sys
import time
import numpy as np

dir_map = {'R': np.array([0, 1]), 
           'L': np.array([0, -1]), 
           'U': np.array([-1, 0]), 
           'D': np.array([1, 0])}

dir_code = {'0': 'R',
            '1': 'D',
            '2': 'L',
            '3': 'U'}

def parse_input(color_str):
    step = int(color_str[2:7], 16)
    dir = dir_code[color_str[7]]
    return dir, step

# use Shoelace formula to calculate the area of a polygon
def get_polygon_area(vertices):
    area = 0
    n = len(vertices)
    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[j][0] * vertices[i][1]
    area = abs(area) / 2
    return area

def get_polygon_perimeter(vertices):
    perimeter = 0
    n = len(vertices)
    for i in range(n):
        j = (i + 1) % n
        perimeter += np.linalg.norm(vertices[j] - vertices[i])
    return perimeter

def main(DATA_INPUT):
    start_time = time.time()

    with open(DATA_INPUT) as f:
        dig_plan = [line.split() for line in f.read().splitlines()]
    
    # vertices should be ordered in a clockwise or counterclockwise manner
    current_location = np.array([0, 0])
    vertices = [current_location.copy()]
    for [_, _, color_str] in dig_plan:
        dir, step = parse_input(color_str)
        current_location += int(step) * dir_map[dir]
        vertices.append(current_location.copy())

    polygon_area = get_polygon_area(vertices)
    polygon_perimeter = get_polygon_perimeter(vertices)
    # for a grid-based system, 
    # a point on a non-corner edge counts as 1/2 in the area, 
    # an inner corner 1/4, and an outer corner 3/4
    # in this case the number of inner corners is 4 less than outer corners
    # with Pick's theorem: I + (L+4)/2 - 1 = I + L/2 + 1
    lava_vol = polygon_area + polygon_perimeter // 2 + 1

    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'It could hold: {int(lava_vol)} cubic meters of lava')

if __name__ == '__main__':
    main(sys.argv[1])