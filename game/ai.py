import copy

def check_winner(board):
    # Check rows, columns, and diagonals
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not None:
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]

    return None

def is_draw(board):
    return all(cell is not None for row in board for cell in row)

def minimax(board, is_ai_turn):
    winner = check_winner(board)
    if winner == 'O':  # AI
        return 1
    elif winner == 'X':  # User
        return -1
    elif is_draw(board):
        return 0

    if is_ai_turn:
        max_score = float('-inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] is None:
                    board[row][col] = 'O'
                    score = minimax(board, False)
                    board[row][col] = None
                    max_score = max(max_score, score)
        return max_score
    else:
        min_score = float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] is None:
                    board[row][col] = 'X'
                    score = minimax(board, True)
                    board[row][col] = None
                    min_score = min(min_score, score)
        return min_score

def best_move(board):
    best_score = float('-inf')
    move = None
    for row in range(3):
        for col in range(3):
            if board[row][col] is None:
                board[row][col] = 'O'
                score = minimax(board, False)
                board[row][col] = None
                if score > best_score:
                    best_score = score
                    move = (row, col)
    return move
