import sys

def main(DATA_INPUT):
    almanac = {'seed-to-soil': [], 
            'soil-to-fertilizer': [], 
            'fertilizer-to-water': [], 
            'water-to-light': [], 
            'light-to-temperature': [], 
            'temperature-to-humidity': [], 
            'humidity-to-location': []}
    
    with open(DATA_INPUT) as f:
        my_str = f.readline()
        seeds_to_plant = my_str.split(' ')[1:]
        seeds_to_plant = [int(seed) for seed in seeds_to_plant]
        f.readline()
        
        while my_str:
            [category, _] = f.readline().split(' ')
            my_str = f.readline()
            while my_str and (my_str != '\n'):
                my_map = my_str.strip('\n').split(' ')
                my_map = [int(number) for number in my_map]
                almanac[category].append(my_map)
                my_str = f.readline()
        
    locations_to_plant = []
    for seed in seeds_to_plant:
        intermediate = seed
        for value in almanac.values():
            for my_map in value:
                if (intermediate >= my_map[1]) and (intermediate < my_map[1] + my_map[2]):
                    intermediate = my_map[0] + intermediate - my_map[1]
                    break
        locations_to_plant.append(intermediate)
    
    print(min(locations_to_plant))

if __name__ == '__main__':
    main(sys.argv[1])