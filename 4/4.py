class Passport:
    def __init__(self, passport_string):
        self.fields = {}
        passport_string = passport_string.split()
        for i in passport_string:
            i = i.split(':')
            self.fields[i[0]] = i[1]

    def check_fields_validity(self):
        if len(self.fields) == 8:
            return True
        elif (len(self.fields) == 7) and 'cid' not in self.fields:
            return True
        else:
            return False
    
    def check_data_validity(self):
        if self.check_fields_validity():
            pass
        else:
            return False
        #birth year validation
        if self.fields['byr'].isdigit() and len(self.fields['byr']) == 4 and (int(self.fields['byr']) >= 1920 ) and (int(self.fields['byr']) <= 2002):
            pass
        else:
            return False
        #issue year validation
        if self.fields['iyr'].isdigit() and len(self.fields['iyr']) == 4 and (int(self.fields['iyr']) >= 2010 ) and (int(self.fields['iyr']) <=2020):
            pass
        else:
            return False
        #expiration year validation
        if self.fields['eyr'].isdigit() and len(self.fields['eyr']) == 4 and (int(self.fields['eyr']) >= 2020 ) and (int(self.fields['eyr']) <=2030):
            pass
        else:
            return False
        #height validation
        if self.fields['hgt'].endswith('cm'):
            if 150 <=int(self.fields['hgt'].replace('cm', '')) <=193:
                pass
            else: 
                return False
        elif self.fields['hgt'].endswith('in'):
            if 59 <= int(self.fields['hgt'].replace('in', '')) <=76:
                pass
            else:
                return False
        else:
            return False
        #hair colour validation
        if self.fields['hcl'].startswith('#') and self.fields['hcl'][1:].isalnum() and (self.fields['hcl'][1:] == self.fields['hcl'][1:].lower() ) and (len(self.fields['hcl'][1:]) == 6):
            #print(self.fields['hcl'])
            pass
        else:
            return False
        #eyes validation
        if self.fields['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth' ]:
            pass
        else:
            return False

        #passport id validation
        if self.fields['pid'].isdigit() and len(self.fields['pid']) == 9 :
            pass
        else:
            return False
        return True
    
    def __str__(self):
        return str(self.fields)

with open("input4.txt", "r") as file:
    passport_string = file.read()
    separated_strings = passport_string.split("\n\n")
    separated_strings = [passport.replace('\n', ' ') for passport in separated_strings]
    valid_passports = 0

    passport_list = [Passport(string) for string in separated_strings]

    for passport in passport_list:
        if passport.check_data_validity():
            valid_passports += 1
    print(valid_passports)