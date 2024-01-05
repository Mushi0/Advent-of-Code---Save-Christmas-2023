import sys
import time
import numpy as np
from dataclasses import dataclass
from tqdm import tqdm

# Node class
@dataclass(frozen = False)
class node:
    loss: int = np.inf

@dataclass(frozen = False)
class node(node):
    prev: node = None

    def update_node(self, loss = np.inf, prev = None):
        self.loss = loss
        self.prev = prev

    def print_node(self):
        print(f'heatloss: {self.loss}, prev: {self.prev}')

class track_direction():
    directions: list = []

    def __init__(self, max_straight = 3):
        self.max_straight = max_straight
    
    def copy(self):
        new = track_direction()
        new.directions = self.directions.copy()
        new.max_straight = self.max_straight
        return new

    def add(self, direction):
        self.directions.append(direction)
        if len(self.directions) > self.max_straight:
            self.directions.pop(0)

    def check_valid(self, direction):
        return ((len(self.directions) < self.max_straight) or 
                (not all(d == direction for d in self.directions)))

def Dijkstra_heat_loss(heat_loss_map):
    m, n = heat_loss_map.shape
    I = range(m); J = range(n)

    # Defining the map
    my_map = [[node() for _ in I] for _ in J]
    Q = set([(i, j) for i in I for j in J])
    my_map[0][0].update_node(0)
    dir_map = [[track_direction() for _ in I] for _ in J]

    # Dijkstra's Algorithm
    node_to_remove = (0, 0)
    Q.remove(node_to_remove)

    pbar = tqdm(total = m*n)
    while not len(Q) == 0:
        x = node_to_remove[0]
        y = node_to_remove[1]
        smallest_heat_loss = np.inf
        heatloss = my_map[x][y].loss
        if (x + 1 < n and (x + 1, y) in Q and
            my_map[x + 1][y].loss > heatloss + heat_loss_map[x + 1][y] and 
            dir_map[x][y].check_valid('d')):
            my_map[x + 1][y].update_node(heatloss + heat_loss_map[x + 1][y], my_map[x][y])
            dir_map[x + 1][y] = dir_map[x][y].copy()
            dir_map[x + 1][y].add('d')
        if (y + 1 < m and (x, y + 1) in Q and
            my_map[x][y + 1].loss > heatloss + heat_loss_map[x][y + 1] and 
            dir_map[x][y].check_valid('r')):
            my_map[x][y + 1].update_node(heatloss + heat_loss_map[x][y + 1], my_map[x][y])
            dir_map[x][y + 1] = dir_map[x][y].copy()
            dir_map[x][y + 1].add('r')
        if (x - 1 >= 0 and (x - 1, y) in Q and
            my_map[x - 1][y].loss > heatloss + heat_loss_map[x - 1][y] and 
            dir_map[x][y].check_valid('u')):
            my_map[x - 1][y].update_node(heatloss + heat_loss_map[x - 1][y], my_map[x][y])
            dir_map[x - 1][y] = dir_map[x][y].copy()
            dir_map[x - 1][y].add('u')
        if (y - 1 >= 0 and (x, y - 1) in Q and
            my_map[x][y - 1].loss > heatloss + heat_loss_map[x][y - 1] and 
            dir_map[x][y].check_valid('l')):
            my_map[x][y - 1].update_node(heatloss + heat_loss_map[x][y - 1], my_map[x][y])
            dir_map[x][y - 1] = dir_map[x][y].copy()
            dir_map[x][y - 1].add('l')

        for coord in Q:
            if my_map[coord[0]][coord[1]].loss < smallest_heat_loss:
                smallest_heat_loss = my_map[coord[0]][coord[1]].loss
                node_to_remove = coord
                # print(f'Removing node {node_to_remove}, heatloss: {smallest_heat_loss}, previous dir: {dir_map[node_to_remove[0]][node_to_remove[1]].directions}')

        if node_to_remove == (n - 1, m - 1):
            print(f'Finished, heatloss: {my_map[n - 1][m - 1].loss}')
            break

        Q.remove(node_to_remove)

        pbar.update(1)

    pbar.close()

    return my_map[n - 1][m - 1].loss

def main(DATA_INPUT):
    start_time = time.time()

    with open(DATA_INPUT) as f:
        heat_loss_map = np.array([list(map(int, list(row))) for row in f.read().splitlines()])

    smallest_heat_loss = Dijkstra_heat_loss(heat_loss_map)

    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'The least heat loss it can incur is: {smallest_heat_loss}')

if __name__ == '__main__':
    main(sys.argv[1])