N = 8

def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve_n_queens(row = 0, board = None):
    if board is None:
        board = [-1] * N 
    if row == N:
        return board
    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            res = solve_n_queens(row + 1, board)
            if res:
                return res
            board[row] = -1
    return None

solution = solve_n_queens()
print("8-Queens Solution Board:")
for r in range(N):
    line = ["Q" if solution[r] == c else "." for c in range(N)]
    print(" ".join(line))
