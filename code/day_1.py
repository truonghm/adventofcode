# day 1

import random
from math import factorial, prod
filename = 'Day_1_Report_Repair.txt'
with open(filepath+filename,'r') as f:
    exp=sorted([int(line.replace('\n','')) for line in f])
    exp_2 = [2020-i for i in exp]

    for i in exp_2:
        if i in exp:
            print('part 1:', i*(2020-i))
            break

    random.seed(a=12)
    exp_3=[i for i in exp if i+sum(exp[:2])<=2020]
    c=int(factorial(len(exp_3))/(factorial(3)*factorial(len(exp_3)-3)))

    for i in range(c):
        s = random.sample(exp_3, 3)
        if sum(s) == 2020:
            print('part 2:', prod(s))
            break
