# day 6
def open_input(path):
    with open(path,'r') as f:
        sections = f.read().split("\n\n")
        answers=[section.split('\n') for section in sections]

    return answers

def get_unique(a):
    answer=''.join(a)
    unique_answer=list(set(answer))
    return unique_answer

def day_6_part_1(answers):
    count=0
    for a in answers:
        unique_answer=get_unique(a)
        count=count+len(unique_answer)
    return count

def day_6_part_2(answers):
    count=0
    for answer in answers:
        unique_answer=get_unique(answer)
        a_list=[]
        for u in unique_answer:
            if all(u in a for a in answer):
                a_list.append(u)
        count=count+len(a_list)
                
                
    return count

answers=open_input(filepath+'Day_6_Custom_Customs.txt')
# print(day_6_part_1(answers))
print(day_6_part_2(answers))
