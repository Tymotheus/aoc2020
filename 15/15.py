def solve_first():
    numbers = [0,13,1,16,6,17]
    for _ in range(2020-len(numbers)):
        last = numbers[-1]
        counter = 0
        first_occurence = True
        for i in reversed(numbers[:-1]):
            counter += 1
            if i == last:
                numbers.append(counter)
                first_occurence = False
                break
        if first_occurence:
            numbers.append(0)
    print(numbers[-1])

def solve_second():
    numbers = {0:1, 13:2, 1:3, 16:4, 6:5} #number, and its last occurence index
    counter = 5
    last = 17
    for _ in range(30000000-len(numbers)+1):
        counter+=1
        if last in numbers:
            distance = counter - numbers[last]
            numbers[last] = counter
            last = distance
        else:
            numbers[last] = counter
            last = 0
    for key, value in numbers.items():
        if value == 30000000:
            print(key)

solve_first()
solve_second()
