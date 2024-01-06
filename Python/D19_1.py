import sys
import time
from dataclasses import dataclass

RULES = {}

@dataclass
class Part:
    x = 0
    m = 0
    a = 0
    s = 0

    def __init__(self, x, m, a, s):
        self.x = x
        self.m = m
        self.a = a
        self.s = s
    
    def get_sum(self):
        return self.x + self.m + self.a + self.s

def get_next(this_part: Part, rules: list):
    satisfied = False
    for rule in rules:
        if len(rule) == 1:
            return rule[0]
        else:
            locals = {'satisfied': satisfied, 'this_part': this_part}
            command = 'satisfied = this_part.' + rule[0]
            exec(command, globals(), locals)
            if locals['satisfied']:
                return rule[1]

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
        
        parts = []
        part = f.readline().strip()[1:-1]
        while part != '':
            part_data = [int(cat[2:]) for cat in part.split(',')]
            parts.append(Part(part_data[0], part_data[1], part_data[2], part_data[3]))
            part = f.readline().strip()[1:-1]
    
    rating_sum = 0
    for part in parts:
        next_rule = get_next(part, RULES['in'])
        
        while next_rule != 'A' and next_rule != 'R':
            next_rule = get_next(part, RULES[next_rule])
        
        if next_rule == 'A':
            rating_sum += part.get_sum()

    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'The total rating numbers of all the accepted parts is: {rating_sum}')

if __name__ == '__main__':
    main(sys.argv[1])