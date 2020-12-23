# day 6
def open_input(path):
    with open(path,'r') as f:
        sections = f.read().split("\n\n")
        # get rid of empty strings
        answers=[[s for s in section.split('\n') if s] for section in sections]

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
        joined_a = ''.join(answer)
        unique_a=get_unique(answer)
        a_list=[u for u in unique_a if joined_a.count(u)==len(answer)]
        count=count+len(a_list)
    return count

answers=open_input(filepath+'Day_6_Custom_Customs.txt')
print('part 1:', day_6_part_1(answers))
print('part 2:', day_6_part_2(answers))
