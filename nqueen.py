# import requests
# print(requests.get("https://github.com/Kundan1804/LP2/raw/master/pract4.py").text)


def is_safe(board, row, col, n):
    # Check if the queen can be placed in the given position without conflicts
    # Check for conflicts in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False
    i = row - 1                   # Check for conflicts in the upper-left diagonal
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    i = row - 1                 # Check for conflicts in the upper-right diagonal
    j = col + 1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1
    return True
def backtrack_queens(board, row, n, count):
    # Base case: All queens have been placed
    if row == n:
        count[0] += 1
        print_solution(board, n)
        return
    # Try placing the queen in each column of the current row
    for col in range(n):
        if is_safe(board, row, col, n):
            # Place the queen in the current position
            board[row][col] = 1
            # Recursive call for the next row
            backtrack_queens(board, row + 1, n, count)
            # Backtrack: Remove the queen from the current position
            board[row][col] = 0
def branch_and_bound_queens(n):
    board = [[0] * n for _ in range(n)]
    count = [0]  # To keep track of the number of solutions
    backtrack_queens(board, 0, n, count)
    print("Total solutions:", count[0])
def print_solution(board, n):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()
    print()
n = int(input("Enter the number of queens: "))
branch_and_bound_queens(n)