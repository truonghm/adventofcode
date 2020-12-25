# day 8

def open_input(path):
    with open(path,'r') as f:
        inst_dict={}
        inst_id=0
        for line in f.read().split("\n"):
            if line:
                inst = line.split(' ')
                if inst[1][0]=='+':
                    inst_dict[inst_id]=[inst[0],int(inst[1][1:])]
                else:
                    inst_dict[inst_id]=[inst[0],-int(inst[1][1:])]
                inst_id=inst_id+1
    return inst_dict

def next_inst(inst_dict, inst_id):
    """
    find the next step of a provided step in the instruction list
    """
        step=inst_dict[inst_id]
        if step[0] in ['acc','nop']:
            next_inst_id=inst_id+1
        else:
            next_inst_id=inst_id+step[1]
        return next_inst_id

def inst_sequel(inst_dict):
    """
    create the list of steps that would be run in the neverending-loop.
    also is the sequence of unique steps before any step is repeated. 
    """
    
    inst_list=[0]
    while len(inst_list) == len(set(inst_list)):
        try:
            ns=next_inst(inst_dict,inst_list[len(inst_list)-1])
            inst_list.append(ns)
        except:
            break
        
    return inst_list[:-1]

# 0. the step needed changing (X) has to be within inst_list 
# as we have to break out of this loop.
# 1. reverse inst_list for faster runtime, with the assumption that the step needed changing has to be 
# near the end of the instruction list.
# 2. for each step in inst_list, swap 'jmp' with 'nop' and vice versa, then create a new dictionary
# of instructions with the modified step.
# 3. check whether the new dictionary will arrive at the last step of the original dictionary
def fix_inst(inst_dict):
    inst_list=reversed(inst_sequel(inst_dict))
    for i in inst_list:
        if inst_dict[i][0]=='nop':
            new_inst='jmp'
        elif inst_dict[i][0]=='jmp':
            new_inst='nop'
        else:
            continue
        test_dict={}
        for k,v in inst_dict.items():
            if k==i:
                test_dict[k]=[new_inst, v[1]]
            else:
                test_dict[k]=v
        test_list = inst_sequel(test_dict)
        if test_list[-1]==len(test_dict)-1:
            return test_dict
        
        
inst_dict=open_input(filepath+'Day_8_Handheld_Halting.txt')
inst_list=inst_sequel(inst_dict)
acc_values = [inst_dict[inst_id][1] for inst_id in inst_list if inst_dict[inst_id][0]=='acc']

print('part 1:', sum(acc_values))

fixed_dict=fix_inst(inst_dict)
fixed_list=inst_sequel(fixed_dict)
fixed_acc_values = [fixed_dict[inst_id][1] for inst_id in fixed_list if fixed_dict[inst_id][0]=='acc']

print('part 2:', sum(fixed_acc_values))
