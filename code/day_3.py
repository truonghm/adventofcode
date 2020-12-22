# day 3 - part 1
s=0
import urllib.request
url='https://raw.githubusercontent.com/truonghm/adventofcode/main/input/Day_3_Toboggan_Trajectory.txt'
for num, line in enumerate(urllib.request.urlopen(url)):
    row = line.decode('utf-8').replace('\n','').split(': ')[0]
    if len(row) > num*3:
        if row[num*3]=='#':
            print(num*3, row, row[num*3])
            s=s+1
print(s)
