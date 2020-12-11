

def solve_first():
    instructions = open("input8.txt").read().splitlines()
    counter = i = step = 0
    current_instruction = instructions[0]
    instruction_order = [0 for i in range(len(instructions))]

    while True:
        if current_instruction[:3] == 'jmp':
            i+= int(current_instruction[4:])
        elif current_instruction[:3] == 'acc':
            counter += int(current_instruction[4:])
            i+=1
        elif current_instruction[:3] == 'nop':
            i+=1
        step += 1
        if instruction_order[i] != 0:
            break
        else:
            instruction_order[i] = step
        current_instruction = instructions[i]
    print(counter)
    return counter

def solve_second():
    instructions = open("input8.txt").read().splitlines()
    counter = i = step = 0
    #last_changed is saying which index we changed the last time
    #we start with the guard, and it will systematically decrease
    last_changed = len(instructions)
    current_instruction = instructions[0]
    instruction_order = [0 for i in range(len(instructions))]

    while True:
        if current_instruction[:3] == 'jmp':
            i  += int(current_instruction[4:])
        elif current_instruction[:3] == 'acc':
            counter += int(current_instruction[4:])
            i+=1
        elif current_instruction[:3] == 'nop':
            i+=1
        step += 1
        print(current_instruction)
        if instruction_order[i] != 0:
            print(instruction_order)
            while True: #loop for going back
                step -= 1
                #get the index of the previous instruction
                i = instruction_order.index(step)
                current_instruction = instructions[i]
                instruction_order[i] = 0

                if current_instruction[:3] == 'nop':
                    if last_changed < i:
                        continue
                    elif last_changed == i:
                        instructions[i] = 'jmp' +  current_instruction[3:]
                        continue
                    elif last_changed > i:
                        last_changed = i
                        instructions[i] = 'jmp' +  current_instruction[3:]
                        break

                elif current_instruction[:3] == 'jmp':
                    if last_changed < i:
                        continue
                    elif last_changed == i:
                        instructions[i] = 'nop' +  current_instruction[3:]
                        continue
                    elif last_changed > i:
                        last_changed = i
                        instructions[i] = 'nop' +  current_instruction[3:]
                        break
                else:
                    while current_instruction[:3] == 'acc':
                        counter -= int(current_instruction[4:])
        else:
            instruction_order[i] = step
        if i == (len(instructions)-1): #terminating the program
            if instructions[i][:3] == "acc":
                counter += int(instructions[i][:3])
            break
        else:
            current_instruction = instructions[i]
    print(counter)
    return counter

solve_first()
solve_second()
