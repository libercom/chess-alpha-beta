import chess

PAWN_TABLE = [
    0,  0,  0,  0,  0,  0,  0,  0,
    50, 50, 50, 50, 50, 50, 50, 50,
    10, 10, 20, 30, 30, 20, 10, 10,
    5,  5, 10, 25, 25, 10,  5,  5,
    0,  0,  0, 20, 20,  0,  0,  0,
    5, -5,-10,  0,  0,-10, -5,  5,
    5, 10, 10,-20,-20, 10, 10,  5,
    0,  0,  0,  0,  0,  0,  0,  0
]

KNIGHTS_TABLE = [
    -50,-40,-30,-30,-30,-30,-40,-50,
    -40,-20,  0,  0,  0,  0,-20,-40,
    -30,  0, 10, 15, 15, 10,  0,-30,
    -30,  5, 15, 20, 20, 15,  5,-30,
    -30,  0, 15, 20, 20, 15,  0,-30,
    -30,  5, 10, 15, 15, 10,  5,-30,
    -40,-20,  0,  5,  5,  0,-20,-40,
    -50,-40,-30,-30,-30,-30,-40,-50
]

BISHOPS_TABLE = [
    -20,-10,-10,-10,-10,-10,-10,-20,
    -10,  0,  0,  0,  0,  0,  0,-10,
    -10,  0,  5, 10, 10,  5,  0,-10,
    -10,  5,  5, 10, 10,  5,  5,-10,
    -10,  0, 10, 10, 10, 10,  0,-10,
    -10, 10, 10, 10, 10, 10, 10,-10,
    -10,  5,  0,  0,  0,  0,  5,-10,
    -20,-10,-10,-10,-10,-10,-10,-20
]

ROOKS_TABLE = [
    0,  0,  0,  0,  0,  0,  0,  0,
    5, 10, 10, 10, 10, 10, 10,  5,
    -5,  0,  0,  0,  0,  0,  0, -5,
    -5,  0,  0,  0,  0,  0,  0, -5,
    -5,  0,  0,  0,  0,  0,  0, -5,
    -5,  0,  0,  0,  0,  0,  0, -5,
    -5,  0,  0,  0,  0,  0,  0, -5,
    0,  0,  0,  5,  5,  0,  0,  0
]

QUEENS_TABLE = [
    -20,-10,-10, -5, -5,-10,-10,-20,
    -10,  0,  0,  0,  0,  0,  0,-10,
    -10,  0,  5,  5,  5,  5,  0,-10,
    -5,  0,  5,  5,  5,  5,  0, -5,
    0,  0,  5,  5,  5,  5,  0, -5,
    -10,  5,  5,  5,  5,  5,  0,-10,
    -10,  0,  5,  0,  0,  0,  0,-10,
    -20,-10,-10, -5, -5,-10,-10,-20
]

KINGS_TABLE = [
    -50,-40,-30,-20,-20,-30,-40,-50,
    -30,-20,-10,  0,  0,-10,-20,-30,
    -30,-10, 20, 30, 30, 20,-10,-30,
    -30,-10, 30, 40, 40, 30,-10,-30,
    -30,-10, 30, 40, 40, 30,-10,-30,
    -30,-10, 20, 30, 30, 20,-10,-30,
    -30,-30,  0,  0,  0,  0,-30,-30,
    -50,-30,-30,-30,-30,-30,-30,-50
]

# Evaluation function. A higher evaluation score indicates an advantage for the white player, while a lower score suggests an advantage for the black player.
def evaluate(board):
    boardvalue = 0
    
    # Determine the number of pieces of each type on the board for both players
    wp = len(board.pieces(chess.PAWN, chess.WHITE))
    bp = len(board.pieces(chess.PAWN, chess.BLACK))
    wn = len(board.pieces(chess.KNIGHT, chess.WHITE))
    bn = len(board.pieces(chess.KNIGHT, chess.BLACK))
    wb = len(board.pieces(chess.BISHOP, chess.WHITE))
    bb = len(board.pieces(chess.BISHOP, chess.BLACK))
    wr = len(board.pieces(chess.ROOK, chess.WHITE))
    br = len(board.pieces(chess.ROOK, chess.BLACK))
    wq = len(board.pieces(chess.QUEEN, chess.WHITE))
    bq = len(board.pieces(chess.QUEEN, chess.BLACK))
    
    # Calculate the material advatange
    material = 100 * (wp - bp) + 300 * (wn - bn) + 300 * (wb - bb) + 500 * (wr - br) + 900 * (wq - bq)
    
    # PAWNS: Calculate the positional advantage by summing up all the WHITE positions and then subtracting the BLACK positions.
    pawn_sum = 0
    for square in board.pieces(chess.PAWN, chess.WHITE):
        pawn_sum += PAWN_TABLE[square]

    for square in board.pieces(chess.PAWN, chess.BLACK):
        pawn_sum -= PAWN_TABLE[chess.square_mirror(square)]

    # KNIGHTS: Calculate the positional advantage by summing up all the WHITE positions and then subtracting the BLACK positions.
    knight_sum = 0
    for square in board.pieces(chess.KNIGHT, chess.WHITE):
        knight_sum += KNIGHTS_TABLE[square]

    for square in board.pieces(chess.KNIGHT, chess.BLACK):
        knight_sum -= KNIGHTS_TABLE[chess.square_mirror(square)]

    # BISHOPS: Calculate the positional advantage by summing up all the WHITE positions and then subtracting the BLACK positions.
    bishop_sum = 0
    for square in board.pieces(chess.BISHOP, chess.WHITE):
        bishop_sum += BISHOPS_TABLE[square]

    for square in board.pieces(chess.BISHOP, chess.BLACK):
        bishop_sum -= BISHOPS_TABLE[chess.square_mirror(square)]

    # ROOKS: Calculate the positional advantage by summing up all the WHITE positions and then subtracting the BLACK positions.
    rook_sum = 0
    for square in board.pieces(chess.ROOK, chess.WHITE):
        rook_sum += ROOKS_TABLE[square]

    for square in board.pieces(chess.ROOK, chess.BLACK):
        rook_sum -= ROOKS_TABLE[chess.square_mirror(square)]

    # QUEENS: Calculate the positional advantage by summing up all the WHITE positions and then subtracting the BLACK positions.
    queens_sum = 0
    for square in board.pieces(chess.QUEEN, chess.WHITE):
        queens_sum += QUEENS_TABLE[square]

    for square in board.pieces(chess.QUEEN, chess.BLACK):
        queens_sum -= QUEENS_TABLE[chess.square_mirror(square)]

    # KINGS: Calculate the positional advantage by summing up all the WHITE positions and then subtracting the BLACK positions.
    kings_sum = 0
    for square in board.pieces(chess.KING, chess.WHITE):
        kings_sum += KINGS_TABLE[square]

    for square in board.pieces(chess.KING, chess.BLACK):
        kings_sum -= KINGS_TABLE[chess.square_mirror(square)]
    
    # Put everything together
    boardvalue = material + pawn_sum + knight_sum + bishop_sum + rook_sum + queens_sum + kings_sum
    
    return boardvalue