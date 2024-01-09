import sys
import time
import math
from functools import reduce

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

def lcm_list(numbers):
    return reduce(lcm, numbers)

class c_module:
    def __init__(self, destinations: list):
        self.destinations: list = destinations
        self.pulse_status: int = -1 # -1: low pulse, 1: high pulse

    def send(self):
        return self.destinations, self.pulse_status
    
    def get_pulse_status(self):
        return self.pulse_status

    def get_destinations(self):
        return self.destinations

class flip_flop_module(c_module):    
    def receive(self, _: str, pulse_status: int): 
        # _ is not used here, but it is used in the conjunction_module
        old_status = self.pulse_status
        self.pulse_status *= pulse_status
        return (old_status != self.pulse_status) # return if pulse status changed

    def get_module_type(self):
        return 'flip_flop'

class conjunction_module(c_module):
    def __init__(self, destinations: list):
        super().__init__(destinations)
        self.previous_pulses: dict = {}
        self.pulse_status: int = -1 # -1: low pulse, 1: high pulse

    def add_previous_pulse(self, sender_name: str):
        self.previous_pulses[sender_name] = 0

    def _update_pulse_status(self):
        if sum([(p != 1) for p in self.previous_pulses.values()]):
            self.pulse_status = 1
        else:
            self.pulse_status = -1
    
    def receive(self, sender_name: str, pulse_status: int):
        old_status = self.pulse_status
        self.previous_pulses[sender_name] = pulse_status
        self._update_pulse_status()
        return (old_status != self.pulse_status) # return if pulse status changed

    def get_module_type(self):
        return 'conjunction'

    def get_previous_pulses(self):
        return self.previous_pulses.keys()

class broadcast_module(c_module):
    pass

def main(DATA_INPUT):
    start_time = time.time()

    modules = {}
    conjunction_modules = []
    with open(DATA_INPUT, 'r') as f:
        for line in f:
            line = line.strip('\n')
            line = line.split(' ')
            destination_list = [item[:-1] if i != len(line) - 3 else item 
                                    for i, item in enumerate(line[2:])]
            if '%' in line[0]:
                modules[line[0][1:]] = flip_flop_module(destination_list)
            elif '&' in line[0]:
                modules[line[0][1:]] = conjunction_module(destination_list)
                conjunction_modules.append(line[0][1:])
            elif line[0] == 'broadcaster':
                modules[line[0]] = broadcast_module(destination_list)
    
    # get all modules connecting to conjunction modules
    for con_module_name in conjunction_modules:
        for previous_name in modules.keys():
            if con_module_name in modules[previous_name].get_destinations():
                modules[con_module_name].add_previous_pulse(previous_name)
    
    # there's only one module connecting to rx
    # and this module is a conjunction module
    last_to_con_mods_cycle = {}
    for con_module_name in conjunction_modules:
        if 'rx' in modules[con_module_name].get_destinations():
            for previous_name in modules[con_module_name].get_previous_pulses():
                last_to_con_mods_cycle[previous_name] = 0
            break
    nb_modules_to_con = len(last_to_con_mods_cycle)

    itr_botton = 1
    while sum([1 if i != 0 else 0 for i in last_to_con_mods_cycle.values()]) != \
            nb_modules_to_con:
        current_pulses = ['broadcaster']
        while current_pulses:
            next_module_name = current_pulses.pop(0)
            destinations, pulse_status = modules[next_module_name].send()
            for destination in destinations:
                if destination in 'rx':
                    continue
                
                # if destination pulse status changed, send again
                changed = modules[destination].receive(next_module_name, pulse_status)
                if changed or modules[destination].get_module_type() == 'conjunction':
                    current_pulses.append(destination)
            
                if (destination in last_to_con_mods_cycle.keys() and 
                        modules[destination].get_pulse_status() == 1):
                    last_to_con_mods_cycle[destination] = itr_botton

        itr_botton += 1
    
    nb_botton_press = lcm_list(last_to_con_mods_cycle.values())

    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'The fewest number of button presses is: {nb_botton_press}')

if __name__ == '__main__':
    main(sys.argv[1])