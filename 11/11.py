from copy import deepcopy

def occupied_neighbours_number(board, row, column):
    neighbours = 0
    #first we are choosing the direction - i and j are corresponding to coordinates
    #in (pixel-screen-modified) cartesian coordinate system
    for i in range(row-1,row+2):
        for j in range(column-1, column+2):
            try:
                if (i==-1) or (j==-1):
                    raise IndexError()
                elif (i!=row or j!=column ):
                    if (board[i][j] == '#'):
                        neighbours+=1
            except IndexError:
                continue
    return neighbours

def far_neighbours_number(board, row, column):
    neighbours = 0
    #coordinate directions
    #print("Passed row is {} passed column is {}".format(row,column))
    for rows_direction in range(-1,+2): #aka down-up
        for columns_direction in range(-1, +2): #aka left-right
            #print("rows_direction = {} columns_direction = {}".format(rows_direction, columns_direction))
            if (rows_direction==0) and (columns_direction==0):
                continue
            for depth in range( max(len(board),len(board[0]))  ):
                #print("depth is {}".format(depth))
                try:
                    if False: #delete this ugly thing
                        pass
                    else:
                        if rows_direction == 0:
                            row_index = row
                        else:
                            row_index = row + rows_direction + (depth if rows_direction > 0 else - depth)
                        if columns_direction == 0:
                            column_index = column
                        else:
                            column_index = column + columns_direction + (depth if columns_direction > 0 else - depth)
                        #print("row index={} column index={}".format(row_index, column_index))
                        if ((column_index==-1) or (row_index==-1)):
                            raise IndexError()
                        elif (board[row_index][column_index] == '#'):
                            #print("neighbours++")
                            neighbours+=1
                            break
                        elif (board[row_index][column_index] == 'L'):
                            break
                        elif (board[row_index][column_index] == '.'):
                            #print("Continuing")
                            continue
                except IndexError:
                    #print("Breaking cause of index error")
                    break
    return neighbours

def count_occupied_seats(board):
    occupied = 0
    for row in board:
        for seat in row:
            if seat == '#':
                occupied+=1
    return occupied

def print_board(board):
    for line in board:
        str = ""
        for char in line:
            str += char
        print(str)

def save_board_to_file(board):
    with open("board_after_stabilisation.txt", "w") as file:
        for line in board:
            str = ""
            for char in line:
                str += char
            str += '\n'
            file.write(str)

def solve_first():
    #'L' stands for empty, '#' stands forr occupied, "." stands for floor
    data = open("input11.txt", 'r').read().splitlines()
    board = [ [char for char in line] for line in data]
    print("Board number of rows={}".format(len(board)))
    print("Board number of columns={}".format(len(board[0])))

    board_stabilised = False
    iteration = 0
    while board_stabilised == False:
        iteration += 1
        print("Iteration {}".format(iteration))
        temp_board = deepcopy(board)
        for row in range(len(board)):
            for column in range(len(board[0])):
                if ( board[row][column] == 'L') and (occupied_neighbours_number(board, row, column) == 0):
                    temp_board[row][column] = '#'
                elif (board[row][column] == '#') and (occupied_neighbours_number(board, row, column) >= 4):
                    temp_board[row][column] = 'L'
        if temp_board != board:
            board = temp_board
            continue
        else:
            board_stabilised = True
            save_board_to_file(board)
    print(count_occupied_seats(board))


def solve_second():
    #'L' stands for empty, '#' stands forr occupied, "." stands for floor
    data = open("input11.txt", 'r').read().splitlines()
    board = [ [char for char in line] for line in data]
    print("Board number of rows={}".format(len(board)))
    print("Board number of columns={}".format(len(board[0])))

    board_stabilised = False
    iteration = 0
    while board_stabilised == False:
        iteration += 1
        print("Iteration {}".format(iteration))
        #print_board(board)
        #print()
        temp_board = deepcopy(board)
        for row in range(len(board)):
            for column in range(len(board[0])):
                if ( board[row][column] == 'L') and (far_neighbours_number(board, row, column) == 0):
                    temp_board[row][column] = '#'
                elif (board[row][column] == '#') and (far_neighbours_number(board, row, column) >= 5):
                    temp_board[row][column] = 'L'
        if temp_board != board:
            board = temp_board
            continue
        else:
            board_stabilised = True
            save_board_to_file(board)
    print(count_occupied_seats(board))

if __name__ == "__main__":
    #solve_first()
    solve_second()
    # data = open("test.txt", 'r').read().splitlines()
    # board = [ [char for char in line] for line in data]
    # for i in range(1, len(board[0])-8):
    #     print("Number of neigbours of column {} and row {} = {}".format(i, 0, far_neighbours_number(board,0,i)))
    #print(board[0][1])
