import re

def make_dict():
    data = open("input7.txt", "r").read().splitlines()
    bag_pattern = "(\d*) *([a-z]+ [a-z]+) bags?" #pattern to look for bag colours and numbers
    contain_gold = list()
    bags_dict = dict()
    for line in data:
        matches = re.findall(bag_pattern, line)
        temp_dict = dict()
        for number, colour in matches[1:]:
            if colour == 'no other':
                temp_dict = dict()
                continue
            else:
                temp_dict[colour] = number
                if colour == 'shiny gold':
                    contain_gold.append(matches[0][1])
        bags_dict[matches[0][1]] = temp_dict
    return bags_dict, contain_gold

def solve_first(bags_dict, contain_gold):
    values = bags_dict.values()
    for colour in contain_gold:
        for key in bags_dict.keys():
            if colour in bags_dict[key].keys() and key not in contain_gold:
                contain_gold.append(key)
    print(len(contain_gold))

def solve_second(bags_dict):
    #subtracting one, as we don't want to count 'shiny gold' itself
    print(get_load_number(bags_dict, 'shiny gold') - 1)

def get_load_number(bags_dict, colour_name): #check how many bags in a given bag (including the given one)
    if len(bags_dict[colour_name]) == 0:
        return 1
    else:
        sum = 0
        for colour in bags_dict[colour_name]:
            sum += get_load_number(bags_dict, colour) * int(bags_dict[colour_name][colour])
        return sum + 1 #adding the called back itself

def main():
    bags_dict, contain_gold = make_dict()
    solve_first(bags_dict, contain_gold)
    solve_second(bags_dict)

main()
