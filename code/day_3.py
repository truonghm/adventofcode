# day 3

import urllib.request
from math import ceil

def tree_count(right, down):
    s=0
    url='https://raw.githubusercontent.com/truonghm/adventofcode/main/input/Day_3_Toboggan_Trajectory.txt'
    tob = [line.decode('utf-8').replace('\n','') for line in urllib.request.urlopen(url)][::down]

    for num, line in enumerate(tob):
        row = line*ceil((right*len(tob)/len(line)))
        try:
            if row[num*right]=='#':
                s=s+1
        except:
            pass

    return s

tree_count(1,1)*tree_count(3,1)*tree_count(5,1)*tree_count(7,1)*tree_count(1,2)
