import sys
import time
import numpy as np

# AREA_MIN = 7
# AREA_MAX = 27
AREA_MIN = 200000000000000
AREA_MAX = 400000000000000

def main(DATA_INPUT):
    start_time = time.time()

    hails = []
    with open(DATA_INPUT, 'r') as f:
        for line in f:
            hail = line.strip().split(' @ ')
            hail = [[int(i) for i in item.split(', ')] for item in hail]
            hails.append(hail)

    nb_intersections = 0
    for i in range(len(hails)):
        [[x1_0, y1_0, _], [v1_x, v1_y, _]] = hails[i]
        for j in range(i + 1, len(hails)):
            [[x2_0, y2_0, _], [v2_x, v2_y, _]] = hails[j]
            
            # x = x_0 + v_x/v_y * (y - y_0)
            # x - v_x/v_y * y = x_0 - v_x/v_y * y_0

            if v1_x/v1_y == v2_x/v2_y:
                continue # parallel

            A = np.array([[1, -(v1_x/v1_y)], [1, -(v2_x/v2_y)]])
            b = np.array([x1_0 - (v1_x/v1_y) * y1_0, x2_0 - (v2_x/v2_y) * y2_0])
            x = np.linalg.solve(A, b)
            
            if (x[0] >= AREA_MIN and x[0] <= AREA_MAX and 
                x[1] >= AREA_MIN and x[1] <= AREA_MAX and
                ((v1_x > 0 and x[0] >= x1_0) or (v1_x < 0 and x[0] < x1_0)) and 
                ((v2_x > 0 and x[0] >= x2_0) or (v2_x < 0 and x[0] < x2_0))):
                nb_intersections += 1

    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'The number of intersections occur within the area is: {nb_intersections}')

if __name__ == '__main__':
    main(sys.argv[1])