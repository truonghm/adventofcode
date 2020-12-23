# day 5
import math
 
def log2(x):
    if x == 0:
        return false
    return (math.log10(x)/math.log10(2))

def cut_point(d,n):
    if math.ceil(log2(n)) == math.floor(log2(n)):
        row_bound=[0,n]
        for c in d:
            if c=='B' or c=='R':
                row_bound=[row_bound[0]+(row_bound[1]-row_bound[0])/2, row_bound[1]]
            elif c=='F' or c=='L':
                row_bound=[row_bound[0], row_bound[0]+(row_bound[1]-row_bound[0])/2]
    return int(row_bound[0])

def find_seat(path, rows=128, cols=8):
    seat_ids=[]
    with open(path, 'r') as f:
        for line in f.read().split('\n'):
            seat_ids.append(cut_point(line[:7], rows)*8+cut_point(line[7:], cols))
    return seat_ids

seat_ids = find_seat(filepath + 'Day_5_Binary_Boarding.txt')

# part 1
max_seat=max(seat_ids)
print('highest seat ID is:', max_seat)

# part 2
missing_seats=[i for i in range(max_seat) if i not in seat_ids and i-1 in seat_ids and i+1 in seat_ids]
if len(missing_seats)==1:
    print('missing seat id is:', missing_seats[0])
else:
    print('missing seat id are:', missing_seats)
