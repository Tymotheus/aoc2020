import sys

numbers = open("input9.txt").read().splitlines()
numbers = [int(i) for i in numbers]

preamble = 25
wrong_number = -1

i = preamble
for i in range(preamble, len(numbers)):
    correct = False
    for j in range(i-preamble,i):
        for k in range(j+1,i):
            if numbers[j] + numbers[k] == numbers[i]:
                correct = True
                break
            else:
                continue
    if correct == False:
        wrong_number = numbers[i]
        print("Wrong number is {}".format(wrong_number))
        break

#that's not gonna be not efficient at all, srsly sry
for i in range(len(numbers)):
    sum = numbers[i]
    for j in range(i+1,len(numbers)):
        sum += numbers[j]
        if sum == wrong_number:
            x = numbers[i:j]
            min = min(x)
            max = max(x)
            print(min+max)
            sys.exit(0)
        elif sum < wrong_number:
            continue
        elif sum > wrong_number:
            break
    sum = 0
