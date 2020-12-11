def read_data():
    data = open("input6.txt", "r").read().splitlines()
    elements = []
    tmp_el = []
    data.append('')
    for n, i in enumerate(data):
        if i == '' or n == len(data):
            elements.append(tmp_el)
            tmp_el = []
            continue
        tmp_el += i.split()
    return elements

def solve_first(elements):
    group_set = set()
    answers = 0
    for group in elements:
        for form in group:
            for letter in form:
                group_set.add(letter)
        answers+=len(group_set)
        group_set.clear()
    return answers

def solve_second(elements):
    answers = 0
    for group in elements:
        group_set = set(group[0])
        temp_set = group_set.copy() #cause we can not remove elements while iterating
        for form in group:
            for letter in group_set:
                if letter not in form:
                    temp_set.discard(letter)
        answers += len(temp_set)
        group_set.clear()
        temp_set.clear()
    return answers


def main():
    elements = read_data()
    print(solve_first(elements))
    print(solve_second(elements))
main()
