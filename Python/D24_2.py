import sys
import time
from sympy import symbols, Eq, solve

# This one is easy... 

def main(DATA_INPUT):
    start_time = time.time()

    hails = []
    with open(DATA_INPUT, 'r') as f:
        for line in f:
            hail = line.strip().split(' @ ')
            hail = [[int(i) for i in item.split(', ')] for item in hail]
            hails.append(hail)
    
    x, y, z, vx, vy, vz = symbols('x y z vx vy vz')
    
    A = ()
    for hail in hails[:7]:
        eq1 = Eq(hail[1][0]*y - vx*y + hail[0][1]*vx - hail[1][1]*x + vy*x - hail[0][0]*vy, hail[1][0]*hail[0][1] - hail[1][1]*hail[0][0])
        eq2 = Eq(hail[1][0]*z - vx*z + hail[0][2]*vx - hail[1][2]*x + vz*x - hail[0][0]*vz, hail[1][0]*hail[0][2] - hail[1][2]*hail[0][0])
        A = A + (eq1, eq2)
    solution = solve(A, (x, y, z, vx, vy, vz))
    
    sum_xyz = solution[0][0] + solution[0][1] + solution[0][2]

    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'The sum of the X, Y and Z is: {sum_xyz}')

if __name__ == '__main__':
    main(sys.argv[1])