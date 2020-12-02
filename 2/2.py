import re

def solve_first_part():
    correct_passwords = 0
    with open("input2.txt", "r") as file:
        for line in file:
            number_pattern = '\d+'
            password_pattern = '[a-z]{2,50}'
            letter_pattern = ' ([a-z]):'
            letter = re.search(letter_pattern, line).group(1)
            minimum, maximum = re.findall(number_pattern, line)
            password = re.findall(password_pattern, line)[0]
           
            if password.count(letter) in range(int(minimum),int(maximum)+1):
                correct_passwords += 1

    print(correct_passwords)

def solve_second_part():
    correct_passwords = 0
    with open("input2.txt", "r") as file:
        for line in file:
            number_pattern = '\d+'
            password_pattern = '[a-z]{2,50}'
            letter_pattern = ' ([a-z]):'
            letter = re.search(letter_pattern, line).group(1)
            index_one, index_two = re.findall(number_pattern, line)
            password = re.findall(password_pattern, line)[0]
            if ( (password[int(index_one)-1] == letter) != (password[int(index_two)-1] == letter) ):
                correct_passwords+=1

    print(correct_passwords)

solve_first_part()
solve_second_part()