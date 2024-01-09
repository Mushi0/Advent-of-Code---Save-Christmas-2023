import sys
import time
from tqdm import tqdm

# NB_BOTTON_PRESSED = 4
NB_BOTTON_PRESSED = 1000

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

    def return_module_type(self):
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

    def return_module_type(self):
        return 'conjunction'

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
    
    # get all dead end modules
    dead_end = set()
    for module_name in modules.keys():
        for next_module in modules[module_name].get_destinations():
            if next_module not in modules.keys():
                dead_end.add(next_module)
    
    nb_high_pulses = 0
    nb_low_pulses = 0
    status_record = []
    for itr in tqdm(range(NB_BOTTON_PRESSED)):
        # # print out --------------------------------------------
        # print('=======' + str(itr) + '========')
        # print('button -low-> broadcaster')
        # # ------------------------------------------------------
        current_pulses = ['broadcaster']
        nb_low_pulses += 1
        while current_pulses:
            next_module_name = current_pulses.pop(0)
            destinations, pulse_status = modules[next_module_name].send()
            for destination in destinations:
                # # print out --------------------------------------------
                # if modules[next_module_name].get_pulse_status() == 1:
                #     print(next_module_name + ' -high-> ' + destination)
                # elif modules[next_module_name].get_pulse_status() == -1:
                #     print(next_module_name + ' -low-> ' + destination)
                # # ------------------------------------------------------

                if modules[next_module_name].get_pulse_status() == 1:
                    nb_high_pulses += 1
                elif modules[next_module_name].get_pulse_status() == -1:
                    nb_low_pulses += 1
                if destination in dead_end:
                    continue
                
                # if destination pulse status changed, send again
                changed = modules[destination].receive(next_module_name, pulse_status)
                if changed or modules[destination].return_module_type() == 'conjunction':
                    current_pulses.append(destination)
        
        status_one_itr = {}
        loop_detedted = False
        for key, value in modules.items():
            status_one_itr[key] = value.get_pulse_status()
        for itr in status_record:
            itr_new = {k: v for k, v in itr.items() if k not in ['nb_high_pulses', 'nb_low_pulses']}
            if itr_new == status_one_itr:
                loop_detedted = True
                break
        if loop_detedted:
            break
        
        status_one_itr['nb_high_pulses'] = nb_high_pulses
        status_one_itr['nb_low_pulses'] = nb_low_pulses
        status_record.append(status_one_itr)
    
    loop_len = len(status_record)
    nb_high_pulses_total = ((NB_BOTTON_PRESSED - 1) // loop_len)*status_record[-1]['nb_high_pulses'] + \
                            status_record[(NB_BOTTON_PRESSED - 1) % loop_len]['nb_high_pulses']
    nb_low_pulses_total = ((NB_BOTTON_PRESSED - 1) // loop_len)*status_record[-1]['nb_low_pulses'] + \
                            status_record[(NB_BOTTON_PRESSED - 1) % loop_len]['nb_low_pulses']
    product = nb_high_pulses_total * nb_low_pulses_total
    
    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'The product of the total number of low and high pulses sent is: {product}')

if __name__ == '__main__':
    main(sys.argv[1])