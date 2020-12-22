# day 1 - part 1

import urllib.request
url='https://raw.githubusercontent.com/truonghm/adventofcode/main/input/Day_1_Report_Repair.txt'
exp=sorted([int(line.decode('utf-8').replace('\n','')) for line in urllib.request.urlopen(url)])
exp_2 = [2020-i for i in exp]

for i in exp_2:
    if i in exp:
        print(i*(2020-i))

# day 1 - part 2

import random
from math import factorial, prod
random.seed(a=12)
exp_3=[i for i in exp if i+sum(exp[:2])<=2020]
c=int(factorial(len(exp_3))/(factorial(3)*factorial(len(exp_3)-3)))

for i in range(c):
    s = random.sample(exp_3, 3)
    if sum(s) == 2020:
        print(prod(s))
        break
