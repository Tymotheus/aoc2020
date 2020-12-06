def get_row(code):
    row = 0
    for i in range(6,-1,-1):
        if code[6-i] == 'F':
            pass
        elif code[6-i] == 'B':
            row += 2**i
        else:
            print("Wrong input data")
    return row

def get_column(code):
    column = 0
    for i in range(2,-1,-1):
        if code[9-i] == 'L':
            pass
        elif code[9-i] == 'R':
            column += 2**i
        else:
            print("Wrong input data")
    return column

def get_id(code):
    return 8*get_row(code) + get_column(code)

with open("input5.txt", "r") as file:
    seats = [line.strip() for line in file]

max = 0

dict = {}
for seat in seats:
    seat_id = get_id(seat)
    dict[seat_id] = 'taken'
    if seat_id > max:
        max = seat_id
print(max)
taken_seats = sorted(dict)
for i in range(0, len(taken_seats)-1):
    if taken_seats[i] != taken_seats[i+1]-1:
        print("There is an empty space after the seat with id: " + str(taken_seats[i]))
