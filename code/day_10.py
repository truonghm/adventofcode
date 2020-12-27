import os

filename = os.path.basename(__file__).replace('.py','.txt')
filepath = os.path.dirname(os.path.realpath(__file__)) + '\\input\\'

def open_input(path):
    with open(path,'r') as f:
        ratings = [int(line) for line in f.read().split("\n") if line]
        ratings.append(max(ratings)+3)
    return ratings

ratings = sorted(open_input(filepath + filename))
diffs = []
for num, val in enumerate(ratings):
    if num==0:
        diffs.append(val)
    else:
        diffs.append(val-ratings[num-1])
print(diffs.count(1)*diffs.count(3))
print(ratings)

def prod(num_list) :
    result = 1
    for x in num_list:
         result = result * x 
    return result 

test = [len(x) for x in ''.join([str(d) for d in diffs]).split('3') if x]

    

