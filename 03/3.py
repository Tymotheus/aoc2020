
def solve(column_increment, row_increment):
    with open("input3.txt", "r") as file:
        board = [line.strip() for line in file]
        row_position = 0
        column_position = 0
        row_width = len(board[0])
        board_height = len(board)
        tree_counter = 0
        for level in range(0, board_height):
            row_position += row_increment
            if row_position >= board_height:
                break
            column_position = (column_position+column_increment)%row_width
            if board[row_position][column_position] == '#':
                tree_counter += 1
        print(tree_counter)
        return tree_counter

print(solve(1,1)*solve(3,1)*solve(5,1)*solve(7,1)*solve(1,2))
