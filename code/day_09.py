import os
import itertools

filename = os.path.basename(__file__).replace('.py','.txt')
filepath = os.path.dirname(os.path.realpath(__file__)) + '\\input\\'

def open_input(path):
    with open(path,'r') as f:
        cypher = []
        for line in f.read().split("\n"):
            if line:
                cypher.append(int(line))
    return cypher


def find_wrong_num(cypher):
    for num, val in enumerate(cypher):
        if num > 24:
            preamble = sorted(cypher[(num - 25):num])
            preamble_2 = [val - p for p in preamble]
            if all(i not in preamble for i in preamble_2):
                return val


def find_weakness(cypher, wrong_num):
    valid_input = [c for c in cypher if c <= wrong_num - min(cypher)]
    for num, val in enumerate(valid_input):
        check_list = valid_input[num:]
        for i, j in enumerate(check_list):
            if wrong_num == sum(check_list[:i]):
                return sorted(check_list[:i])[0]+sorted(check_list[:i])[-1]


cypher=open_input(filepath+filename)
wrong_num = find_wrong_num(cypher)
print('part 1:', wrong_num)
print('part 2:', find_weakness(cypher, wrong_num))
