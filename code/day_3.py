# day 3 - part 1
s=0
import urllib.request
from math import ceil
url='https://raw.githubusercontent.com/truonghm/adventofcode/main/input/Day_3_Toboggan_Trajectory.txt'
tob = [line.decode('utf-8').replace('\n','') for line in urllib.request.urlopen(url)]

for num, line in enumerate(tob):
    row = line*len(tob)
    try:
        if row[num*3]=='#':
            s=s+1
    except:
        pass

print(s)
