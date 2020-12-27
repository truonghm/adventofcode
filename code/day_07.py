# day 7
import os 

def get_amount(bag_count):
    amount=bag_count.split(' ')[0]
    bag = bag_count[(len(amount)+1):]
    if amount=='no':
        amount=0
    else:
        amount=int(amount)
    return bag, amount

def prod(num_list) :
    result = 1
    for x in num_list:
         result = result * x 
    return result 

def open_input(path):
    with open(path,'r') as f:
        bag_dict={}
        for line in f.read().split("\n"):
            if line:
                bag = line.replace('bags','bag').replace('.','').split(' contain ')
                content=bag[1].split(', ')
                bag_dict[bag[0]]={get_amount(c)[0]: get_amount(c)[1] for c in content}
    return bag_dict

def is_inside(bag_dict, bag, bag_inside):
    """
    recursively check if bag_inside is in bag.
    check until the function arrives at a bag with no other bags inside.
    """
    if list(bag_dict[bag].values())!=[0]:
        if bag_inside in bag_dict[bag].keys():
            return 1
        else:
            return sum([is_inside(bag_dict, b, bag_inside) for b in bag_dict[bag].keys()])
    else:
        return 0

def count_inside(bag_dict, bag):
    if list(bag_dict[bag].values())!=[0]:
        return sum(bag_dict[bag].values()) + sum([count_inside(bag_dict, k)*v for k,v in bag_dict[bag].items()])
    else:
        return 0


filename = os.path.basename(__file__).replace('.py','.txt')
filepath = os.path.dirname(os.path.realpath(__file__)) + '\\input\\'
bag_dict=open_input(filepath+filename)
    
print('part 1:', sum([1 for b in bag_dict.keys() if is_inside(bag_dict, b, 'shiny gold bag')!=0]))
print('part 2:', count_inside(bag_dict, 'shiny gold bag'))
