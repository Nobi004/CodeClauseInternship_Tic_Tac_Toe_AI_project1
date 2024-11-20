from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .ai import best_move, check_winner, is_draw

# Default empty board
def create_board():
    return [[None, None, None], [None, None, None], [None, None, None]]

# Store the board state
board_state = create_board()

def reset_game(request):
    global board_state
    board_state = create_board()
    return JsonResponse({'status': 'reset'})

def play_game(request):
    global board_state
    if request.method == 'POST':
        data = json.loads(request.body)  # Parse JSON data from the request
        row, col = data['row'], data['col']
        board_state[row][col] = 'X'  # Player's move

        # Check for a winner or draw
        winner = check_winner(board_state)
        if winner or is_draw(board_state):
            return JsonResponse({'board': board_state, 'winner': winner, 'draw': is_draw(board_state)})

        # AI's turn
        ai_move = best_move(board_state)
        if ai_move:
            board_state[ai_move[0]][ai_move[1]] = 'O'

        # Check for a winner or draw after AI's move
        winner = check_winner(board_state)
        return JsonResponse({'board': board_state, 'winner': winner, 'draw': is_draw(board_state)})

    return render(request, 'home.html')
