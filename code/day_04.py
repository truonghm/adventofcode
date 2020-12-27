# day 4
import os 

def process_passport(path, validation=False):
    with open(path, 'r') as f:
        sections = f.read().split("\n\n")
        # excluding cid in fields as it's optional
        fields = {
            'byr':[1920, 2002],
            'iyr':[2010, 2020],
            'eyr':[2020, 2030],
            'hgt':{'cm':[150,193],'in':[59, 76]},
            'hcl':'0123456789abcdef',
            'ecl':['amb','blu','brn','gry','grn','hzl','oth'],
            'pid':'0123456789'
        }
        s=0
        for section in sections:
            passport = [p for p in section.replace('\n',' ').split(" ") if p]
            field_list=[f.split(':')[0] for f in passport]
            isvalid =  all(f in field_list for f in list(fields.keys()))
            if isvalid:
                if validation==False:
                    s=s+1
                else:
                    passport_dict = dict(map(lambda s : s.split(':'), passport))
                    try:
                        check_conds = (
                            len(passport_dict['byr']) == 4 and
                            int(passport_dict['byr']) >= fields['byr'][0] and
                            int(passport_dict['byr']) <= fields['byr'][1] and
                            len(passport_dict['iyr']) == 4 and
                            int(passport_dict['iyr']) >= fields['iyr'][0] and
                            int(passport_dict['iyr']) <= fields['iyr'][1] and
                            len(passport_dict['eyr']) == 4 and
                            int(passport_dict['eyr']) >= fields['eyr'][0] and
                            int(passport_dict['eyr']) <= fields['eyr'][1] and
                            (
                                (
                                    passport_dict['hgt'][-2:]=='cm' and
                                    int(passport_dict['hgt'][:len(passport_dict['hgt'])-2]) >= fields['hgt']['cm'][0] and
                                    int(passport_dict['hgt'][:len(passport_dict['hgt'])-2]) <= fields['hgt']['cm'][1]
                                ) or
                                (
                                    passport_dict['hgt'][-2:]=='in' and
                                    int(passport_dict['hgt'][:len(passport_dict['hgt'])-2]) >= fields['hgt']['in'][0] and
                                    int(passport_dict['hgt'][:len(passport_dict['hgt'])-2]) <= fields['hgt']['in'][1]
                                )
                            ) and
                            passport_dict['hcl'][0]=='#' and
                            len(passport_dict['hcl'])==7 and
                            all(c in fields['hcl'] for c in passport_dict['hcl'][1:]) and
                            passport_dict['ecl'] in fields['ecl'] and
                            len(passport_dict['pid']) == 9 and
                            all(n in fields['pid'] for n in passport_dict['pid'])
                        )
                        if check_conds:
                            s=s+1
                    except:
                        pass
                
    return s


filename = os.path.basename(__file__).replace('.py','.txt')
filepath = os.path.dirname(os.path.realpath(__file__)) + '\\input\\'
path = filepath+filename
print('part 1:', process_passport(path, validation=False))
print('part 2:', process_passport(path, validation=True))
