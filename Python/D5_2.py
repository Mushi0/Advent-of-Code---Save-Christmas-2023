import sys
import time

next_category = {'seed-to-soil': 'soil-to-fertilizer', 
                     'soil-to-fertilizer': 'fertilizer-to-water', 
                     'fertilizer-to-water': 'water-to-light', 
                     'water-to-light': 'light-to-temperature', 
                     'light-to-temperature': 'temperature-to-humidity', 
                     'temperature-to-humidity': 'humidity-to-location'}

def main(DATA_INPUT):
    start_time = time.time()

    almanac = {'seed-to-soil': [], 
            'soil-to-fertilizer': [], 
            'fertilizer-to-water': [], 
            'water-to-light': [], 
            'light-to-temperature': [], 
            'temperature-to-humidity': [], 
            'humidity-to-location': []}
    
    with open(DATA_INPUT) as f:
        my_str = f.readline()
        seeds_list = my_str.split(' ')[1:]
        seeds_to_plant = []
        for i in range(int(len(seeds_list)/2)):
            seeds_to_plant.append((int(seeds_list[2*i]), int(seeds_list[2*i + 1])))
        f.readline()
        
        while my_str:
            [category, _] = f.readline().split(' ')
            my_str = f.readline()
            while my_str and (my_str != '\n'):
                my_map = my_str.strip('\n').split(' ')
                my_map = [int(number) for number in my_map]
                added = False
                for i, item in enumerate(almanac[category]):
                    if my_map[1] < item[1]:
                        almanac[category] = almanac[category][:i] + [my_map] + almanac[category][i:]
                        added = True
                        break
                if not added:
                    almanac[category].append(my_map)
                my_str = f.readline()
        
    def get_destination(category, this_range):
        range_left = this_range[0]
        range_right = this_range[0] + this_range[1] - 1
        destination = []
        s_to_d_map = almanac[category]
        for my_map in s_to_d_map:
            map_left = my_map[1]
            map_right = my_map[1] + my_map[2] - 1
            if range_left <= map_left:
                if range_right >= map_right:
                    destination.append([my_map[0], my_map[2]])
                elif range_right >= map_left:
                    destination.append([my_map[0], this_range[1] - (my_map[1] - this_range[0])])
            elif range_left <= map_right:
                if range_right >= map_right:
                    destination.append([my_map[0] + (this_range[0] - my_map[1]), my_map[2] - (this_range[0] - my_map[1])])
                else:
                    destination.append([my_map[0] + (this_range[0] - my_map[1]), this_range[1]])
        if range_left < s_to_d_map[0][1]:
            if range_right < s_to_d_map[0][1]:
                destination.append(this_range)
            else:
                destination.append([this_range[0], s_to_d_map[0][1] - this_range[0]])
        if range_right > s_to_d_map[-1][1] + s_to_d_map[-1][2] - 1:
            if range_left > s_to_d_map[-1][1] + s_to_d_map[-1][2] - 1:
                destination.append(this_range)
            else:
                destination.append([s_to_d_map[-1][1] + s_to_d_map[-1][2], this_range[0] + this_range[1] - (s_to_d_map[-1][1] + s_to_d_map[-1][2])])
        if category == 'humidity-to-location':
            return destination
        else:
            update_destination = []
            for d in destination:
                update_destination += get_destination(next_category[category], d)
            return update_destination
    
    destination = []
    for seed in seeds_to_plant:
        destination += get_destination('seed-to-soil', seed)
    min_location = destination[0][0]
    for d in destination:
        if d[0] < min_location:
            min_location = d[0]

    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'The lowest location number that corresponds to any of the initial seed numbers is: {min_location}')

if __name__ == '__main__':
    main(sys.argv[1])