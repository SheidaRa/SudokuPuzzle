board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

# Print the Board
def print_board(puzzle):
    for x in range(len(puzzle)):
        if x % 3 == 0 and x != 0:
            print("- - - - - - - - - - - - - ")

        for y in range(len(puzzle[0])):
            if y % 3 == 0 and y != 0:
                print(" | ", end="")

            if y == 8:
                print(puzzle[x][y])
            else:
                print(str(puzzle[x][y]) + " ", end="")
print_board(board)