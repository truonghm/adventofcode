# day 2
import os

def open_input(path):
    pw_list=[]
    with open(path,'r') as f:
        for line in f:
            pw = line.replace('\n','').split(': ')
            pw_list.append(pw)
    return pw_list

def day_2_part_1(pw_list):
    s = 0
    for pw in pw_list:
        char = pw[0][-1]
        char_count = pw[1].count(char)
        lb = int(pw[0].split(' ')[0].split('-')[0])
        ub = int(pw[0].split(' ')[0].split('-')[1])
        if char_count >= lb and char_count <= ub:
            s = s + 1
    return s

def day_2_part_2(pw_list):
    s = 0
    for pw in pw_list:
        char = pw[0][-1]
        id1 = int(pw[0].split(' ')[0].split('-')[0])
        id2 = int(pw[0].split(' ')[0].split('-')[1])
        if (pw[1][id1-1]==char or pw[1][id2-1]==char) and not (pw[1][id1-1]==char and pw[1][id2-1]==char):
            s = s + 1
    return s


filename = os.path.basename(__file__).replace('.py','.txt')
filepath = os.path.dirname(os.path.realpath(__file__)) + '\\input\\'
pw_list=open_input(filepath+filename)
print('part 1: ', day_2_part_1(pw_list))
print('part 2: ', day_2_part_2(pw_list))
