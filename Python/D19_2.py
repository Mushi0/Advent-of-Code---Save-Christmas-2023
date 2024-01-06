import sys
import time
from copy import deepcopy

RULES = {}

def count_combinations(part_limit: dict):
    return (part_limit['x'][1] - part_limit['x'][0] + 1) * \
            (part_limit['m'][1] - part_limit['m'][0] + 1) * \
            (part_limit['a'][1] - part_limit['a'][0] + 1) * \
            (part_limit['s'][1] - part_limit['s'][0] + 1)

def get_accepted(part_limit: dict, rules: list):
    count = 0
    for rule in rules:
        if len(rule) == 1:
            if rule[0] == 'A':
                count += count_combinations(part_limit)
            elif rule[0] != 'R':
                count += get_accepted(part_limit, RULES[rule[0]])
            return count
        else:
            new_part_limit = deepcopy(part_limit)
            if (rule[0][1] == '>' and 
                not new_part_limit[rule[0][0]][0] > int(rule[0][2:])):
                new_part_limit[rule[0][0]][0] = int(rule[0][2:]) + 1
                part_limit[rule[0][0]][1] = int(rule[0][2:])
            elif (rule[0][1] == '<' and 
                not new_part_limit[rule[0][0]][1] < int(rule[0][2:])):
                new_part_limit[rule[0][0]][1] = int(rule[0][2:]) - 1
                part_limit[rule[0][0]][0] = int(rule[0][2:])
            
            if rule[1] == 'A':
                count += count_combinations(new_part_limit)
            elif rule[1] != 'R':
                count += get_accepted(new_part_limit, RULES[rule[1]])
    
    return count

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
                's': [1, 4000]}
    accepted_combinations = get_accepted(part_limit, RULES['in'])

    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'The number of combinations of ratings that will be accepted is: {accepted_combinations}')

if __name__ == '__main__':
    main(sys.argv[1])