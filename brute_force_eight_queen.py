import itertools
import matplotlib.pyplot as plt
import numpy as np

N = 8

def is_valid(solution):
    """
    Check if a given solution is valid (no two queens attack each other).
    """
    for i in range(N):
        for j in range(i+1, N):
            if abs(i - j) == abs(solution[i] - solution[j]):
                return False
    return True

def visualizeBoard(board):
    fig, ax = plt.subplots(figsize=(12, 12))
    ax.set_xlim(0, N)
    ax.set_ylim(0, N)
    ax.set_xticks(np.arange(0.5, N + 1, 1))
    ax.set_yticks(np.arange(0.5, N + 1, 1))
    ax.grid(True)
    ax.set_title(f"N-Queens Solution (N={N})")

    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                ax.scatter(j + 1, i + 1, s=800, marker='X', color='red')
            else:
                ax.scatter(j + 1, i + 1, s=800, marker='o', color='white')

    plt.show()

def solve_8_queens():
    solutions = []
    for solution in itertools.permutations(range(N)):
        if is_valid(solution):
            solutions.append(solution)
            board = [[0 for _ in range(N)] for _ in range(N)]
            for i, row in enumerate(solution):
                board[i][row] = 1
            visualizeBoard(board)
    if not solutions:
        print("No solution found.")
    else:
        print(f"Number of solutions: {len(solutions)}")

solve_8_queens()