import sys
import math
import datetime

def time_log(func):
    def inner():
        currentDT = datetime.datetime.now()
        func()
        print("Execution of the program took {}".format( datetime.datetime.now() - currentDT ) )
    return inner

@time_log
def solve_challenge():
    with open("input.txt", "r") as file:
        numbers = [ int(x) for x in file.read().split('\n')]
    for i in numbers:
        for j in numbers[numbers.index(i)+1:]:
            for k in numbers[numbers.index(j)+1:]:
                if (i+j+k) == 2020:
                    print("Those number are: {}, {} and {} and their product is {}".format(i, j, k, i*j*k))
                    return 0
    print("Didn't find them :/ ")
    return 0

@time_log
def solve_challenge_worse():
    with open("input.txt", "r") as file:
        numbers = [ int(x) for x in file.read().split('\n')]
    for i in numbers:
        for j in numbers:
            for k in numbers:
                if (i+j+k) == 2020:
                    print("Those number are: {}, {} and {} and their product is {}".format(i, j, k, i*j*k))
                    return 0
    print("Didn't find them :/ ")
    return 0

if __name__ == "__main__":
    solve_challenge()
    solve_challenge_worse()
