# day 2

def day_2_part_1(path):
    with open(path,'r') as f:
        s = 0
        for line in f:
            pw = line.replace('\n','').split(': ')
            char = pw[0][-1]
            char_count = pw[1].count(char)
            lb = int(pw[0].split(' ')[0].split('-')[0])
            ub = int(pw[0].split(' ')[0].split('-')[1])
            if char_count >= lb and char_count <= ub:
                s = s + 1
    return s

def day_2_part_2(path):
    with open(path,'r') as f:
        s = 0
        for line in f:
            pw = line.replace('\n','').split(': ')
            char = pw[0][-1]
            id1 = int(pw[0].split(' ')[0].split('-')[0])
            id2 = int(pw[0].split(' ')[0].split('-')[1])
            if (pw[1][id1-1]==char or pw[1][id2-1]==char) and not (pw[1][id1-1]==char and pw[1][id2-1]==char):
                s = s + 1
    return s

filename = 'Day_2_Password_Philosophy.txt'
print('part 1: ', day_2_part_1(filepath+filename))
print('part 2: ', day_2_part_2(filepath+filename))
