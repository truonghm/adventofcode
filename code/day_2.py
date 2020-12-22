# day 2- part 1
import urllib.request
url='https://raw.githubusercontent.com/truonghm/adventofcode/main/input/Day_2_Password_Philosophy.txt'
s = 0
for line in urllib.request.urlopen(url):
    pw = line.decode('utf-8').replace('\n','').split(': ')
    char = pw[0][-1]
    char_count = pw[1].count(char)
    lb = int(pw[0].split(' ')[0].split('-')[0])
    ub = int(pw[0].split(' ')[0].split('-')[1])
    if char_count >= lb and char_count <= ub:
        s = s + 1
print(s)

# day 2- part 2
s = 0
for line in urllib.request.urlopen(url):
    pw = line.decode('utf-8').replace('\n','').split(': ')
    char = pw[0][-1]
    id1 = int(pw[0].split(' ')[0].split('-')[0])
    id2 = int(pw[0].split(' ')[0].split('-')[1])
    if (pw[1][id1-1]==char or pw[1][id2-1]==char) and not (pw[1][id1-1]==char and pw[1][id2-1]==char):
        s = s + 1
print(s)
