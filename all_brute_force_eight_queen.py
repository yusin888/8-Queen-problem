import itertools
import matplotlib.pyplot as plt
import numpy as np

def is_valid(board):
    N = len(board)
    for i in range(N):
        for j in range(i + 1, N):
            # Check if the two queens are in the same column
            if board[i] == board[j]:
                return False
            # Check diagonals
            if abs(board[i] - board[j]) == abs(i - j):
                return False
    return True

def visualize_board_matplotlib(board):
    N = len(board)
    board_matrix = np.zeros((N, N))
    
    for i in range(N):
        board_matrix[i][board[i]] = 1
    
    fig, ax = plt.subplots()
    ax.matshow(board_matrix, cmap='gray')
    
    for i in range(N):
        for j in range(N):
            if board_matrix[i, j] == 1:
                ax.text(j, i, 'Q', va='center', ha='center', color='red', fontsize=20)
            else:
                ax.text(j, i, '.', va='center', ha='center', color='white', fontsize=20)
    
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title("8 Queens Solution")
    plt.show()

def brute_force_8_queens():
    N = 8
    # Generate all possible permutations of columns
    perms = itertools.permutations(range(N))
    solutions = 0
    for perm in perms:
        if is_valid(perm):
            print(perm)
            solutions += 1
            print("Solution #", solutions)
            visualize_board_matplotlib(perm)

brute_force_8_queens()
