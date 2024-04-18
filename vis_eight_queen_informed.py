import matplotlib.pyplot as plt
import numpy as np

N = 8 # Size of the chessboard

def solveNQueens(board, col):
    if col == N:
        visualizeBoard(board)
        return True
    for i in range(N):
        if isSafe(board, i, col):
            board[i][col] = 1
            if solveNQueens(board, col + 1):
                return True
            board[i][col] = 0
    return False

def isSafe(board, row, col):
    for x in range(col):
        if board[row][x] == 1:
            return False
    for x, y in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[x][y] == 1:
            return False
    for x, y in zip(range(row, N, 1), range(col, -1, -1)):
        if board[x][y] == 1:
            return False
    return True

def visualizeBoard(board):
    fig, ax = plt.subplots(figsize=(12, 12))  # Increased figure size
    ax.set_xlim(0, N)
    ax.set_ylim(0, N)
    ax.set_xticks(np.arange(0.5, N + 1, 1))
    ax.set_yticks(np.arange(0.5, N + 1, 1))
    ax.grid(True)
    ax.set_title(f"N-Queens Solution (N={N})")

    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                ax.scatter(j + 1, i + 1, s=800, marker='X', color='red')  # Increased marker size
            else:
                ax.scatter(j + 1, i + 1, s=800, marker='o', color='white')  # Increased marker size

    plt.show()

board = [[0 for x in range(N)] for y in range(N)]
if not solveNQueens(board, 0):
    print("No solution found")