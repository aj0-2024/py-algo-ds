"""
Minimax algorithm recursively evaulates and finds the best move.

- turn
- move
- legal_moves
- is_win
- is_draw
- evaluate
"""
from enum import Enum
from copy import deepcopy

def make_move(board, location, piece):
    """Place a piece on board"""
    new_board = get_new_board()

    # copy existing board before the update
    for i in range(3):
        for j in range(3):
            new_board[i][j] = board[i][j]
    
    row, col = location
    new_board[row][col] = piece
    
    return new_board

def get_legal_moves(board):
    """Get a set of all legal moves possible, Here it is all the empty spots"""
    empty_spots = set()
    
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                empty_spots.add((row, col))
                
    return empty_spots

def is_draw(board):
    """Check if the position is draw"""
    return not is_win(board) and len(get_legal_moves(board)) == 0

def is_win(board):
    """Check three rows, three columns and two diagonals"""
    return any([
        is_win_rows(board),
        is_win_cols(board),
        is_win_diags(board)
    ])

def is_win_rows(board):
    for row in board:
        if is_all_x(row):
            return True

        if is_all_o(row):
            return True
    return False

def is_win_cols(board):
    # check the three colums
    col_1 = [
        board[0][0],
        board[1][0],
        board[2][0]
    ]
    col_2 = [
        board[0][1],
        board[1][1],
        board[2][1]
    ]
    col_3 = [
        board[0][2],
        board[1][2],
        board[2][2]
    ]
    for col in [col_1, col_2, col_3]:
        if is_all_x(col):
            return True

        if is_all_o(col):
            return True
    return False

def is_win_diags(board):
    # check diagonals
    diag_1 = [
        board[0][0],
        board[1][1],
        board[2][2]
    ]
    diag_2 = [
        board[0][2],
        board[1][1],
        board[2][0]
    ]
    for diag in [diag_1, diag_2]:
        if is_all_x(diag):
            return True

        if is_all_o(diag):
            return True

    return False
    
def is_all_x(values):
    """check if all the given values are X"""
    for val in values:
        if val != "X":
            return False
    return True

def is_all_o(values):
    """check if all the given values are O"""
    for val in values:
        if val != "O":
            return False
    return True

def evaluate(board, player, turn):
    if is_win(board) and turn == player:
        return -1
    elif is_win(board) and turn != player:
        return 1
    else:
        return 0
        
def switch_piece(piece):
    if piece == "X":
        return "O"
    elif piece == "O":
        return "X"
    else:
        return piece
    
def minimax(board, player, turn, depth = 0):
    max_depth = 8
    if is_win(board)\
        or is_draw(board)\
        or depth == max_depth:
        return evaluate(board, player, turn)

    # maximize player's position if player's turn
    if player == turn:
        best_eval = float("-inf")
        for move in get_legal_moves(board):
            best_eval = max(
                best_eval,
                minimax(
                    make_move(board, move, turn), 
                    player,
                    switch_piece(turn),
                    depth + 1
                )
            )
        return best_eval
    # minimize player's position if not player's turn
    else:
        worst_eval = float("inf")
        for move in get_legal_moves(board):
            worst_eval = min(
                worst_eval,
                minimax(
                    make_move(board, move, turn),
                    player,
                    switch_piece(turn),
                    depth + 1
                )
            )
        return worst_eval

def find_best_move(board, piece):
    best_so_far = float("-inf")
    best_move_so_far = None
    
    for move in get_legal_moves(board):
        result = minimax(
            make_move(board, move, piece),
            piece,
            switch_piece(piece)
        )

        if result > best_so_far:
            best_so_far = result
            best_move_so_far = move
    return best_move_so_far

def get_human_move(board):
    move = None, None
    while move not in get_legal_moves(board):
        row = int(input("Enter row:"))
        col = int(input("Enter col:"))
        move = row, col
    return move

def get_new_board():
    return [[" " for _ in range(3)] for _ in range(3)]

def make_human_move(board, piece):
    move = get_human_move(board)
    print(f"your move is {move} with {piece}")
    return make_move(board, move, piece)

def make_ai_move(board, piece):
    move = find_best_move(board, piece)
    print(f"computer move is {move} with {piece}")
    return make_move(board, move, piece)

def is_done(board):
    return is_win(board) or is_draw(board)

def play_tictactoe():
    board = get_new_board()
    human_piece = "X"
    ai_piece = "O"
    
    while not is_done(board):
        board = make_human_move(board, human_piece)
        if is_win(board):
            print("You win!")
            break

        if is_draw(board):
            print("Game Drawn")
            break
            
        board = make_ai_move(board, ai_piece)
        if is_win(board):
            print("Computer wins!")
            break

        if is_draw(board):
            print("Game Drawn")
            break

        for x in board:
            print(x)
        print("--------")

if __name__ == "__main__":
    play_tictactoe()
    
