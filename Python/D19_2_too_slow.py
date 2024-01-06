import sys
import time
from copy import deepcopy
from tqdm import tqdm

RULES = {}

def get_next(part_limit: dict, rules: list):
    part_limits = []
    for rule in rules:
        new_part_limit = deepcopy(part_limit)
        if len(rule) == 1 and not (rule[0] == 'A' or rule[0] == 'R'):
            part_limits += get_next(new_part_limit, RULES[rule[0]])
        elif rule[0] == 'A':
            new_part_limit['result'] = 'A'
            part_limits.append(new_part_limit)
        elif rule[0] != 'R':
            if rule[0][1] == '>':
                if not new_part_limit[rule[0][0]][0] > int(rule[0][2:]):
                    new_part_limit[rule[0][0]][0] = int(rule[0][2:]) + 1
            elif rule[0][1] == '<':
                if not new_part_limit[rule[0][0]][1] < int(rule[0][2:]):
                    new_part_limit[rule[0][0]][1] = int(rule[0][2:]) - 1
            
            if rule[1] == 'A':
                new_part_limit['result'] = 'A'
                part_limits.append(new_part_limit)
            elif rule[1] != 'R':
                part_limits += get_next(new_part_limit, RULES[rule[1]])
    
    return part_limits

def main(DATA_INPUT):
    start_time = time.time()

    with open(DATA_INPUT, 'r') as f:
        oneline = f.readline().strip()
        while oneline != '':
            [key, rules] = oneline.split('{')
            rules = rules[:-1].split(',')
            parsed_rules = []
            for one_rule in rules:
                if ':' in one_rule:
                    parsed_rules.append(one_rule.split(':'))
                else:
                    parsed_rules.append([one_rule])
            RULES[key] = parsed_rules
            oneline = f.readline().strip()
    
    part_limit = {'x': [1, 4000], 
                'm': [1, 4000], 
                'a': [1, 4000], 
                's': [1, 4000], 
                'result': 'R'}
    accepted_limits = get_next(part_limit, RULES['in'])
    
    possible_set = set()
    for limit in tqdm(accepted_limits):
        for xx in range(limit['x'][0], limit['x'][1] + 1):
            for mm in range(limit['m'][0], limit['m'][1] + 1):
                for aa in range(limit['a'][0], limit['a'][1] + 1):
                    for ss in range(limit['s'][0], limit['s'][1] + 1):
                        possible_set.add((xx, mm, aa, ss))
    
    accepted_combinations = len(possible_set)

    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'The number of combinations of ratings that will be accepted is: {accepted_combinations}')

if __name__ == '__main__':
    main(sys.argv[1])