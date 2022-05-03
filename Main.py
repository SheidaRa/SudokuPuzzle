from queue import Empty
import tkinter as tk

from matplotlib.pyplot import grid

# window=tk.Tk()
# window.title(Sudoku Solver)
# window.geometry("300x200+10+20")
# window.mainloop()
if __name__ == '__main__':


    board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]


def blankBoard():
    board = []
    for x in range(9):
        row = []
        for y in range(9):
            row.append(0)
        board.append(row)
    return board


# prints the unsolved sudoku puzzle
def printBoard(Puzzle):
    for x in range(len(Puzzle)):
        if x % 3 == 0 and x != 0:
            print("- - - - - - - - - - - - - ")

        for y in range(len(Puzzle[x])):
            if y % 3 == 0 and y != 0:
                print(" | ", end="")

            if y == 8:
                print(Puzzle[x][y])
            else:
                print(str(Puzzle[x][y]) + " ", end="")\



def isEmpty(Puzzle):
    '''determines whether the cell is empty'''
    for x in range(len(Puzzle)):
        for y in range(len(Puzzle[x])):
            if Puzzle[x][y] == 0:
                return (x,y)


# create a nested list with each list representing a row and each value being the coordinate of an empty cell
def emptyMatrix(Puzzle): # not needed in a recursive function
    gridList = []
    for x in range(len(Puzzle)):
        tupleList = []
        for y in range(len(Puzzle[x])):
            if Puzzle[x][y] == 0:
                tupleList.append((x,y))
        gridList.append(tupleList)
    return gridList


# checks validity of the cell across neighbors in the row
def validRow(Puzzle, cell, num):
    for a in range(len(Puzzle)):
        if Puzzle[cell[0]][a] == num and (cell[0], a) != cell:
            return False


# checks validity of the cell across neighbors in the column
def validCol(Puzzle, cell, num):
    for b in range(len(Puzzle)):
        if Puzzle[b][cell[1]] == num and (b, cell[1]) != cell:
            return False


# checks validity of the cell across neighbors in the box
def validBox(Puzzle, cell, num):
    startX = cell[0] - cell[0] % 3
    startY = cell[1] - cell[1] % 3

    for x in range(startX, startX + 3):
        for y in range(startY, startY + 3):
            if Puzzle[x][y] == num and (x,y) != cell:
                return False


# condensed validRow, validCol, and validBox
'''
Couldn't run validRow, validCol, and validBox within validNum. Calls to the function either return None or False.
Using if statement with the function would end validNum early.
'''
def validNum(Puzzle, cell, num):
    for a in range(len(Puzzle)):
        if Puzzle[cell[0]][a] == num and (cell[0], a) != cell:
            return False

    for b in range(len(Puzzle)):
        if Puzzle[b][cell[1]] == num and (b, cell[1]) != cell:
            return False

    startX = cell[0] - cell[0] % 3
    startY = cell[1] - cell[1] % 3

    for x in range(startX, startX + 3):
        for y in range(startY, startY + 3):
            if Puzzle[x][y] == num and (x, y) != cell:
                return False

    return True


def solve(Puzzle):
    blank = isEmpty(Puzzle)
    if not blank:
        return True

    for num in range(1,10):
        if validNum(Puzzle, blank, num):

            Puzzle[blank[0]][blank[1]] = num

            if solve(Puzzle):
                return True
            Puzzle[blank[0]][blank[1]] = 0

    return False

printBoard(board)
solve(board)
print(solve(board))
printBoard(board)

print("________________________________________________")

blank = blankBoard()
printBoard(blank)
solve(blank)
print(solve(blank))
printBoard(blank)



