import chess
from engines.board_evaluator import evaluate

# This function implements the alpha-beta pruning algorithm to search for the best move in a chess board state.
# It explores the game tree up to a certain depth, considering both maximizing and minimizing players.
def alpha_beta(board: chess.Board, depth, alpha, beta, maximizing_player):
    # Edge case: When the search reaches the specified depth or the game is over, the function evaluates the current board state.
    if depth == 0 or board.is_game_over():
        return evaluate(board)

    # Edge case: When the current player is the maximezer player
    if maximizing_player:
        # Initialize variables to keep track of the best evaluation
        max_eval = -float('inf')

        # Loop through all legal moves in the current board state
        for move in board.legal_moves:
            # Make the move on the board
            board.push(move)
            # Recursive call to the alpha-beta function to obtain the evaluation at the next depth of the game tree
            eval = alpha_beta(board, depth - 1, alpha, beta, False)
            # Undo the move to explore the next move
            board.pop()
            # Calculate the maximum evaluation among the available moves
            max_eval = max(max_eval, eval)

            # Prune the search if the current branch is worse than the best found so far
            alpha = max(alpha, eval)
            if beta <= alpha:
                break

        return max_eval
    # Edge case: When the current player is the minimizer player
    else:
        # Initialize variables to keep track of the best evaluation
        min_eval = float('inf')

        # Loop through all legal moves in the current board state
        for move in board.legal_moves:
            # Make the move on the board
            board.push(move)
            # Recursive call to the alpha-beta function to obtain the evaluation at the next depth of the game tree
            eval = alpha_beta(board, depth - 1, alpha, beta, True)
            # Undo the move to explore the next move
            board.pop()
            # Calculate the min evaluation among the available moves
            min_eval = min(min_eval, eval)
            # Prune the search if the current branch is worse than the best found so far
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval
    
# This function finds the best move for the current player (either white or black) in a given chess board state.
# It uses the alpha-beta pruning algorithm to search for the optimal move within a specified depth.
def find_best_move(board, depth):
    # Determine if the current player is white or black
    is_white = True if board.turn == chess.WHITE else False

    # Initialize variables to keep track of the best move and its evaluation
    best_move = None
    max_eval = -float('inf') if is_white else float('inf')

    # Initialize alpha and beta values for alpha-beta pruning
    alpha = -float('inf')
    beta = float('inf')

    # Loop through all legal moves in the current board state
    for move in board.legal_moves:
        # Make the move on the board
        board.push(move)

        # Evaluate the board state using the alpha-beta pruning algorithm
        eval = alpha_beta(board, depth - 1, alpha, beta, False)

        # Undo the move to explore the next move
        board.pop()

        # Update the best move and evaluation based on the current player
        # A higher evaluation score indicates an advantage for the white player, while a lower score suggests an advantage for the black player.
        if (is_white and eval > max_eval) or (not is_white and eval < max_eval):
            max_eval = eval
            best_move = move

    # Return the best move found after searching through all legal moves
    return best_move