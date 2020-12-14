import re

def solve_first():
    data = open("input14.txt", 'r').read().splitlines()
    mask = ''
    number = 0
    cell = 0
    memory = dict()
    for instruction in data:
        if instruction.startswith('mask'):
            mask = instruction.split('= ')[1]
            and_temp = list(map(lambda bit :( '0' if bit == '0' else '1' ), mask))
            or_temp = list(map(lambda bit :( '1' if bit == '1' else '0' ), mask))
            and_mask = or_mask = ''
            for i in range(len(and_temp)):
                and_mask += and_temp[i]
                or_mask += or_temp[i]
            and_mask = int(and_mask, 2)
            or_mask = int(or_mask, 2)

        elif instruction.startswith('mem'):
            cell = int(re.findall('\[(\d+)\]', instruction)[0])
            number = int(instruction.split('= ')[1])
            result = int(number & and_mask)
            result = int(result | or_mask)
            memory[cell] = result
            result = 0
    print(sum(memory.values()) )

def solve_second():
    data = open("input14.txt", 'r').read().splitlines()
    mask = ''
    number = 0
    cell = 0
    memory = dict()
    addresses = ['']
    for instruction in data:
        if instruction.startswith('mask'):
            mask = instruction.split('= ')[1]
        elif instruction.startswith('mem'):
            cell = int(re.findall('\[(\d+)\]', instruction)[0])
            cell = format(cell, '036b')
            number = int(instruction.split('= ')[1])
            addresses = ['']
            for i in range(len(mask)): #looping on the mask bits
                if (mask[i] == '0'):
                    for j in range(len(addresses)):
                        addresses[j] += str(cell[i])
                elif (mask[i] == '1'):
                    for j in range(len(addresses)):
                        addresses[j] += '1'
                elif (mask[i] == 'X'): #doubling the array, and splitting on 2 possible ways
                    addresses = 2 * addresses
                    for j in range( int(len(addresses)/2)):
                        addresses[j] += '0'
                    for j in range( int(len(addresses)/2), len(addresses)):
                        addresses[j] += '1'
            for ad in addresses:
                memory[int(ad,2)] = number
    #print(memory)
    print(sum(memory.values()) )

solve_first()
solve_second()
