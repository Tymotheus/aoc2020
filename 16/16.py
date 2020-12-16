import re
import copy

def solve_first():
    rules = dict()
    with open("input16.txt", "r") as file:
        lines = file.read().splitlines()
    for line in lines[0:20]: #input specific solution
            name = line.split(':')[0]
            ranges = re.findall(r"(\d+)-(\d+)", line)
            rules[name] = [ [int(tuple[0]), int(tuple[1])] for tuple in ranges  ]
    your_ticket = [ int(num) for num in lines[22].split(',')]
    tickets = [[int(num) for num in line.split(',')] for line in lines[25:] ]
    error_rate = 0
    for tick in tickets:
        for number in tick:
            correct_value = False
            for key in rules:
                if  rules[key][0][0] <= number <= rules[key][0][1]:
                    correct_value = True
                    pass
                elif rules[key][1][0] <= number <= rules[key][1][1]:
                    correct_value = True
                    pass
            if correct_value == False:
                print("This value " + str(number) + " is not valid for any rule")
                error_rate += number
    print(error_rate)

def solve_second():
    rules = dict()
    with open("input16.txt", "r") as file:
        lines = file.read().splitlines()
    for line in lines[0:20]: #input specific solution
            name = line.split(':')[0]
            ranges = re.findall(r"(\d+)-(\d+)", line)
            rules[name] = [ [int(tuple[0]), int(tuple[1])] for tuple in ranges ]
    your_ticket = [ int(num) for num in lines[22].split(',')]
    tickets = [[int(num) for num in line.split(',')] for line in lines[25:] ]
    valid_tickets = copy.deepcopy(tickets)
    error_rate = 0
    counter = 0
    for tick in tickets:
        for number in tick:
            correct_value = False
            for key in rules:
                if  rules[key][0][0] <= number <= rules[key][0][1]:
                    correct_value = True
                    pass
                elif rules[key][1][0] <= number <= rules[key][1][1]:
                    correct_value = True
                    pass
            if correct_value == False:
                valid_tickets.remove(tick)
                error_rate += number
                counter += 1

    column_names = [[] for i in range(len(your_ticket))] #potential names of columns

    for column in range(0, 20):#checking every column
        for key in rules: #and verifying validity of every rule
            valid_rule = True
            for ticket in valid_tickets: #for every valid ticket
                if  rules[key][0][0] <= ticket[column] <= rules[key][0][1]:
                    continue
                elif rules[key][1][0] <= ticket[column] <= rules[key][1][1]:
                    continue
                else:
                    valid_rule = False
                    break
            if valid_rule == True:
                column_names[column].append(key)

    for i in range(len(column_names)):
        print("Column {}: {}".format(i, column_names[i]))

    desired_set = ['departure location', 'departure station', 'departure platform', 'departure track', 'departure date', 'departure time']

    # print("")
    # for col in column_names:
    #     for i in desired_set:
    #         if i in col:
    #             print("Column {}: {}".format(column_names.index(col), col))
    #             break
    #manually deleting some names
    for col in column_names:
        if 'wagon' in col:
            col.remove('wagon')
        if 'arrival platform' in col:
            col.remove('arrival platform')
        if 'route' in col:
            col.remove('route')
        if 'row' in col:
            col.remove('row')
        if 'type' in col:
            col.remove('type')
        if 'arrival station' in col:
            col.remove('arrival station')
        if 'zone' in col:
            col.remove('zone')
        if 'departure station' in col:
            col.remove('departure station')
        if 'departure time' in col:
            col.remove('departure time')
        if 'departure platform' in col:
            col.remove('departure platform')
        if 'departure date' in col:
            col.remove('departure date')

    print("")
    for i in range(len(column_names)):
        print("Column {}: {}".format(i, column_names[i]))

    value = your_ticket[1] * your_ticket[5] * your_ticket[11] * your_ticket[12] * your_ticket[16] * your_ticket[17]
    print(value)
#solve_first()
solve_second()
