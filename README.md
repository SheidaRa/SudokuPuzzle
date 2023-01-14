# Sudoku-Puzzles

We created a program that solves Sudoku puzzles by using Backtracking.
You can input your unsolved Puzzle in "board" yousing the number 0 as the empty slots. Then as you run the code you can see the solved puzzle in the terminal. 
we used the "printBoard" function to print the board in a sorted 3 by 3 squares display so it is easier to read.

This script that solves a Sudoku puzzle using a backtracking algorithm. The code defines various functions to check if a given number is a valid move in a given cell, based on the current state of the board. The isEmpty() function is used to find the next empty cell in the board, and the validNum() function is used to check the row, column, and box of that cell to see if the given number is a valid move. If the move is not valid, the script will backtrack and try a different number. The script will continue this process until it finds a solution for the Sudoku puzzle. The input board is a 2D array.
It also has Tkinter window code commented out which is not related to solving the puzzle it's just for creating a window.

The script first defines a 2D array called board which is the initial state of the Sudoku puzzle that needs to be solved.

The blankBoard() function is defined, which creates a 2D array of size 9x9 and initializes all its cells to 0. This function is not used in the script.

The printBoard() function is defined, which takes a 2D array as input and prints it in the format of a Sudoku puzzle. It prints a horizontal line after every third row to separate the boxes.

The isEmpty() function is defined, which takes a 2D array as input and returns the coordinates (x, y) of the first empty cell (i.e. cell with value 0) that it finds in the array. If no empty cells are found, it returns None.

The emptyMatrix() function is defined, which takes a 2D array as input and returns a nested list with each list representing a row and each value being the coordinate of an empty cell. This function is not used in the script.

The validRow() function is defined, which takes a 2D array, a cell (x, y) and a number as input, and checks if that number already exists in the same row as the given cell. If it does, the function returns False, otherwise True.

The validCol() function is defined, which takes a 2D array, a cell (x, y) and a number as input, and checks if that number already exists in the same column as the given cell. If it does, the function returns False, otherwise True.

The validBox() function is defined, which takes a 2D array, a cell (x, y) and a number as input, and checks if that number already exists in the same 3x3 box as the given cell. If it does, the function returns False, otherwise True.

The validNum() function is defined, which takes a 2D array, a cell (x, y) and a number as input, and checks if that number is a valid move in the given cell. The function calls validRow(), validCol() and validBox() functions to check if the number is valid in the row, column and box of the given cell respectively. If any of these functions return False, the validNum() function also returns False, otherwise True.

The script then defines a function called solve() which takes a 2D array as input. Inside this function, it uses the isEmpty() function to find the next empty cell in the board. If no empty cells are found, it means the puzzle is solved and the function returns True.

If an empty cell is found, the script uses a for loop to try numbers from 1 to 9 in that cell. It uses the validNum() function to check if the number is a valid move in that cell.

If the number is a valid move, the script makes that move and recursively calls the solve() function with the updated board. If the recursive call to solve() returns True, it means the puzzle is solved and the function returns True.

If the recursive call to solve() returns False, it means the move that was made is not a part of the solution, so the script backtracks by undoing that move and trying the next number in the for loop. This process is repeated until a valid move is found or all numbers have been tried. If all numbers have been tried and none of them led to a solution, the function returns False.

Finally, the script checks if the script is being run as the main program (if __name__ == '__main__':) and calls the solve() function with the initial state of the board.

If the solve() function returns True, it means the puzzle is solved, and the script uses the printBoard() function to print the solved puzzle.

If the solve() function returns False, it means the puzzle could not be solved with the given initial state.

Note that the Tkinter window code is commented out and not related to solving the puzzle, it's just for creating a window.


