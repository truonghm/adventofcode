# day 3

from math import ceil
import os 

def tree_count(path, right, down):
    s=0
    with open(path, 'r') as f:
        tob = [line.replace('\n','') for line in f][::down]

        for num, line in enumerate(tob):
            row = line*ceil((right*len(tob)/len(line)))
            try:
                if row[num*right]=='#':
                    s=s+1
            except:
                pass

    return s

filename = os.path.basename(__file__).replace('.py','.txt')
filepath = os.path.dirname(os.path.realpath(__file__)) + '\\input\\'
path = filepath + filename
part_1 = tree_count(path,3,1)
part_2 = tree_count(path,1,1)*tree_count(path,3,1)*tree_count(path,5,1)*tree_count(path,7,1)*tree_count(path,1,2)
print('part 1:', part_1)
print('part 2:', part_2)
