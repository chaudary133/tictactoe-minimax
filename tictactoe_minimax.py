"""
Tic Tac Toe: Computer vs Computer using the Minimax algorithm.
The game starts randomly: a random computer goes first and plays a random opening move.
After that, both computers play optimally using minimax.
"""

import random

WIN_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),   # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),   # columns
    (0, 4, 8), (2, 4, 6),              # diagonals
]


def print_board(board):
    for i in range(0, 9, 3):
        print(" " + " | ".join(board[i:i + 3]))
        if i < 6:
            print("---+---+---")
    print()


def winner(board):
    """Return 'X' or 'O' if someone has won, else None."""
    for a, b, c in WIN_LINES:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]
    return None


def is_full(board):
    return " " not in board


def minimax(board, is_maximizing, me, opponent):
    """
    Returns the score of the board from the point of view of player `me`.
    +1 = `me` wins, -1 = `opponent` wins, 0 = draw.
    """
    w = winner(board)
    if w == me:
        return 1
    if w == opponent:
        return -1
    if is_full(board):
        return 0

    if is_maximizing:                       # `me` is to move: pick the max
        best = -2
        for i in range(9):
            if board[i] == " ":
                board[i] = me
                best = max(best, minimax(board, False, me, opponent))
                board[i] = " "
        return best
    else:                                   # `opponent` is to move: pick the min
        best = 2
        for i in range(9):
            if board[i] == " ":
                board[i] = opponent
                best = min(best, minimax(board, True, me, opponent))
                board[i] = " "
        return best


def best_move(board, me, opponent):
    """Try every empty cell and choose the one with the highest minimax score."""
    best_score = -2
    move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = me
            score = minimax(board, False, me, opponent)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move


def play():
    board = [" "] * 9
    players = ["X", "O"]

    # Random start: random player goes first and plays a random opening move
    current = random.choice(players)
    print(f"Computer {current} was randomly chosen to start.\n")
    first_move = random.randint(0, 8)
    board[first_move] = current
    print(f"Computer {current} plays randomly at position {first_move + 1}:")
    print_board(board)
    current = "O" if current == "X" else "X"

    # Both computers now play using minimax
    while not winner(board) and not is_full(board):
        opponent = "O" if current == "X" else "X"
        move = best_move(board, current, opponent)
        board[move] = current
        print(f"Computer {current} plays (minimax) at position {move + 1}:")
        print_board(board)
        current = opponent

    w = winner(board)
    print(f"Result: Computer {w} wins!" if w else "Result: It's a draw!")


if __name__ == "__main__":
    play()
