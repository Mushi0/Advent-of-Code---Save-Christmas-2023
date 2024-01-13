import sys
import time
# from sympy import symbols, Eq, solve

AREA_MIN = 7
AREA_MAX = 27
# AREA_MIN = 200000000000000
# AREA_MAX = 400000000000000

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
        hail_1 = hails[i]
        for j in range(i + 1, len(hails)):
            hail_2 = hails[j]
            
            if hail_1[1][0] == hail_2[1][0]:
                if hail_1[0][0] != hail_2[0][0]:
                    continue
                else:
                    t = (hail_1[0][1] - hail_2[0][1])/(hail_2[1][1] - hail_1[1][1])
            else:
                t = (hail_1[0][0] - hail_2[0][0])/(hail_2[1][0] - hail_1[1][0])
                if (hail_1[0][1] + t*hail_1[1][1] != hail_2[0][1] + t*hail_2[1][1]):
                    continue
                    
            x = hail_1[0][0] + hail_1[1][0]*t
            y = hail_1[0][1] + hail_1[1][1]*t
            if (x >= AREA_MIN and x <= AREA_MAX and 
                y >= AREA_MIN and y <= AREA_MAX):
                nb_intersections += 1

    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'The number of intersections occur within the area is: {nb_intersections}')

if __name__ == '__main__':
    main(sys.argv[1])