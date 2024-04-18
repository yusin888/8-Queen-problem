import matplotlib.pyplot as plt
import numpy as np

N = 8  # Size of the chessboard

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
    fig, ax = plt.subplots(figsize=(12, 12))  # Adjust the figure size as needed
    ax.set_xlim(0, N)
    ax.set_ylim(0, N)
    ax.set_xticks(np.arange(0.5, N + 1, 1))
    ax.set_yticks(np.arange(0.5, N + 1, 1))
    ax.grid(True, linewidth=2, color='gray')  # Adjust the grid line width and color
    ax.set_title(f"N-Queens Solution (N={N})", fontsize=18, fontweight='bold')  # Adjust the title font size and weight

    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                ax.scatter(j + 1, i + 1, s=800, marker='X', color='red', edgecolor='black', linewidth=2)  # Adjust the marker size, color, and outline
            else:
                ax.scatter(j + 1, i + 1, s=800, marker='o', color='white', edgecolor='lightgray', linewidth=2)  # Adjust the marker size, color, and outline

    plt.show()

board = [[0 for x in range(N)] for y in range(N)]
if not solveNQueens(board, 0):
    print("No solution found")