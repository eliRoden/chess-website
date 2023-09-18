from copy import deepcopy
from typing import Optional, List

def update_board(
    board: List[List[str]],
    i1: int, j1: int,
    i2: int,
    j2: int,
    whites_turn: bool,
    left_white_rook_moved: bool,
    right_white_rook_moved: bool,
    white_king_moved: bool,
    left_black_rook_moved: bool,
    right_black_rook_moved: bool,
    black_king_moved: bool,
) -> tuple[list[list[str]], bool, bool, bool, bool, bool, bool, bool, bool]:
    previous_state = (
        board, 
        whites_turn, 
        False, 
        left_white_rook_moved,
        right_white_rook_moved,
        white_king_moved,
        left_black_rook_moved,
        right_black_rook_moved,
        black_king_moved,
    )
    
    if i1 == 7 and j1 == 4 and i2 == 7 and j2 == 2:
        if not whites_turn:
            return previous_state

        if not can_castle(
            deepcopy(board),
            whites_turn,
            left_white_rook_moved,
            right_white_rook_moved,
            white_king_moved,
            left_black_rook_moved,
            right_black_rook_moved,
            black_king_moved,
            True,
        ):
            return previous_state
        
        board[7][4] = ' '
        board[7][2] = 'k'
        board[7][0] = ' '
        board[7][3] = 'r'
        white_king_moved = True
        left_white_rook_moved = True

        mate = checkmate(deepcopy(board), i1, j1, i2, j2, not whites_turn)
        
        return (
            board, 
            not whites_turn, 
            mate,
            left_white_rook_moved,
            right_white_rook_moved,
            white_king_moved,
            left_black_rook_moved,
            right_black_rook_moved,
            black_king_moved,
        )
    
    if i1 == 7 and j1 == 4 and i2 == 7 and j2 == 6:
        if not whites_turn:
            return previous_state

        if not can_castle(
            deepcopy(board),
            whites_turn,
            left_white_rook_moved,
            right_white_rook_moved,
            white_king_moved,
            left_black_rook_moved,
            right_black_rook_moved,
            black_king_moved,
            False,
        ):
            return previous_state
        
        board[7][4] = ' '
        board[7][6] = 'k'
        board[7][7] = ' '
        board[7][5] = 'r'
        white_king_moved = True
        right_white_rook_moved = True

        mate = checkmate(deepcopy(board), not whites_turn)
        
        return (
            board, 
            not whites_turn, 
            mate,
            left_white_rook_moved,
            right_white_rook_moved,
            white_king_moved,
            left_black_rook_moved,
            right_black_rook_moved,
            black_king_moved,
        )

    if i1 == 0 and j1 == 4 and i2 == 0 and j2 == 2:
        if whites_turn:
            return previous_state

        if not can_castle(
            deepcopy(board),
            whites_turn,
            left_white_rook_moved,
            right_white_rook_moved,
            white_king_moved,
            left_black_rook_moved,
            right_black_rook_moved,
            black_king_moved,
            True,
        ):
            return previous_state
        
        board[0][4] = ' '
        board[0][2] = 'K'
        board[0][0] = ' '
        board[0][3] = 'R'
        black_king_moved = True
        left_black_rook_moved = True

        mate = checkmate(deepcopy(board), not whites_turn)
        
        return (
            board, 
            not whites_turn, 
            mate,
            left_white_rook_moved,
            right_white_rook_moved,
            white_king_moved,
            left_black_rook_moved,
            right_black_rook_moved,
            black_king_moved,
        )
    
    if i1 == 0 and j1 == 4 and i2 == 0 and j2 == 6:
        if whites_turn:
            return previous_state

        if not can_castle(
            deepcopy(board),
            whites_turn,
            left_white_rook_moved,
            right_white_rook_moved,
            white_king_moved,
            left_black_rook_moved,
            right_black_rook_moved,
            black_king_moved,
            False,
        ):
            return previous_state
        
        board[0][4] = ' '
        board[0][6] = 'K'
        board[0][7] = ' '
        board[0][5] = 'R'
        black_king_moved = True
        right_black_rook_moved = True

        mate = checkmate(deepcopy(board), not whites_turn)
        
        return (
            board, 
            not whites_turn, 
            mate,
            left_white_rook_moved,
            right_white_rook_moved,
            white_king_moved,
            left_black_rook_moved,
            right_black_rook_moved,
            black_king_moved,
        )

    if not valid_move_piece(board[i1][j1], i1, j1, i2 , j2):
        return previous_state
    
    if not is_valid_move(deepcopy(board), i1, j1, i2, j2, whites_turn):
        return previous_state
    
    if not is_valid_check(deepcopy(board), i1, j1, i2, j2, whites_turn):
        return previous_state

    if i1 == 0 and j1 == 0:
        left_black_rook_moved = True
    if i1 == 0 and j1 == 4:
        black_king_moved = True
    if i1 == 0 and j1 == 7:
        right_white_rook_moved = True
    if i1 == 7 and j1 == 0:
        left_white_rook_moved = True
    if i1 == 7 and j1 == 4:
        white_king_moved = True
    if i1 == 7 and j1 == 7:
        right_white_rook_moved = True

    if board[i1][j1] == 'p' and i2 == 0:
        board[i2][j2] = 'q'
    elif board[i1][j1] == 'P' and i2 == 7:
        board[i2][j2] = 'Q'
    else:
        board[i2][j2] = board[i1][j1]

    board[i1][j1] = ' '

    mate = checkmate(deepcopy(board), not whites_turn)
    
    return (
        board, 
        not whites_turn, 
        mate,
        left_white_rook_moved,
        right_white_rook_moved,
        white_king_moved,
        left_black_rook_moved,
        right_black_rook_moved,
        black_king_moved,
    )


def valid_move_piece(piece: str, i1: int, j1: int, i2: int, j2: int) -> Optional[bool]:
    if piece == 'P':
        if i1 == 1 and i2 == 3 and j1 == j2:
            return True
        elif i2 - i1 == 1 and j1 == j2:
            return True
        elif i2 - i1 == 1 and abs(j2 - j1) == 1:
            return True
        else:
            return False
    elif piece == 'p':
        if i1 == 6 and i2 == 4 and j1 == j2:
            return True
        elif i2 - i1 == -1 and j1 == j2:
            return True
        elif i2 - i1 == -1 and abs(j2 - j1) == 1:
            return True
        else:
            return False
    elif piece == 'r' or piece == 'R':
       return i1 == i2 or j1 == j2
    elif piece == 'n' or piece == 'N':
        if abs(i2 - i1) == 1 and abs(j2 - j1) == 2:
            return True
        elif abs(i2 - i1) == 2 and abs(j2 - j1) == 1:
            return True
        else:
            return False
    elif piece == 'b' or piece == 'B':
        return abs(i2 - i1) == abs(j2 - j1)
    elif piece == 'q' or piece == 'Q':
        return i1 == i2 or j1 == j2 or abs(i2 - i1) == abs(j2 - j1)
    elif piece == 'k' or piece == 'K':
        return abs(i2 - i1) <= 1 and abs(j2 - j1) <= 1
    else:
        return None
    

def is_valid_move(board: list[list[str]], i1: int, j1: int, i2: int, j2: int, whites_turn) -> bool:
    piece: str = board[i1][j1]
    if (whites_turn and piece.isupper()) or (not whites_turn and piece.islower()):
        return False
    if i1 == i2 and j1 == j2:
        return False
    elif piece == ' ':
        return False
    elif board[i2][j2] != ' ' and ((board[i1][j1].islower() and board[i2][j2].islower()) or (board[i1][j1].isupper() and board[i2][j2].isupper())):
        return False
    elif (piece == 'p' or piece == 'P') and j1 != j2 and board[i2][j2] == ' ':
        return False
    elif (piece == 'p' or piece == 'P') and j1 == j2 and board[i2][j2] != ' ':
        return False 
    elif not valid_move_piece(piece, i1, j1, i2, j2): 
        return False
    else:
        return True


def is_valid_check(board: list[list[str]], i1: int, j1: int, i2: int, j2, whites_turn: bool) -> bool:
    if board[i1][j1] == 'p' and i2 == 0:
        board[i2][j2] = 'q'
    elif board[i1][j1] == 'P' and i2 == 7:
        board[i2][j2] = 'Q'
    else:
        board[i2][j2] = board[i1][j1]

    board[i1][j1] = ' '

    return not in_check(board, whites_turn)


def in_check(board: list[list[str]], whites_turn: bool) -> bool:
    for i, row in enumerate(board):
        for j, piece in enumerate(row):
            if (whites_turn and piece == 'k') or (not whites_turn and piece == 'K'):
                ki, kj = i, j
    
    for i, row in enumerate(board):
        for j, piece in enumerate(row):
            if is_valid_move(board, i, j, ki, kj, not whites_turn):
                if piece == 'n' or piece == 'N':
                    return True
                elif piece == 'p' or piece == 'P':
                    return True
                elif piece == 'k' or piece == 'K':
                    return True
                elif piece == 'b' or piece == 'B':
                    king_safe = False

                    if i < ki and j < kj:
                        for d in range(1, ki - i):
                            if i + d > 7 or j + d > 7:
                                break
                            if board[i + d][j + d] != ' ':
                                king_safe = True
                                break
                    
                    if i < ki and j > kj:
                        for d in range(1, ki - i):
                            if i + d > 7 or j - d < 0:
                                break
                            if board[i + d][j - d] != ' ':
                                king_safe = True
                                break
                    
                    if i > ki and j < kj:
                        for d in range(1, i - ki):
                            if i - d < 0 or j + d > 7:
                                break
                            if board[i - d][j + d] != ' ':
                                king_safe = True
                                break
                    # print('king_safe before loop', king_safe)
                    if i > ki and j > kj:
                        # print('entered correct if statement')
                        for d in range(1, i - ki):
                            if i - d < 0 or j - d < 0:
                                break
                            if board[i - d][j - d] != ' ':
                                # print('BAD', i, j, board[i-d][j-d], board[i - d][j - d] != ' ')
                                king_safe = True
                                break
                            
                    if not king_safe:
                        return True

                elif piece == 'r' or piece == 'R':
                    king_safe = False

                    if i < ki:
                        for d in range(1, ki - i):
                            if i + d > 7:
                                break
                            if board[i + d][j] != ' ':
                                king_safe = True
                                break
                    
                    if i > ki:
                        for d in range(1, i - ki):
                            if i - d < 0:
                                break
                            if board[i - d][j] != ' ':
                                king_safe = True
                                break

                    if j < kj:
                        for d in range(1, kj - j):
                            if j + d > 7:
                                break
                            if board[i][j + d] != ' ':
                                king_safe = True
                                break   

                    if j > kj:
                        for d in range(1, j - kj):
                            if j - d < 0:
                                break
                            if board[i][j - d] != ' ':
                                king_safe = True
                                break   


                    if not king_safe:
                        return True
                    
                elif piece == 'q' or piece == 'Q':
                    king_safe = False

                    if i < ki and j < kj:
                        for d in range(1, ki - i):
                            if i + d > 7 or j + d > 7:
                                break
                            if board[i + d][j + d] != ' ':
                                king_safe = True
                                break
                    
                    if i < ki and j > kj:
                        for d in range(1, ki - i):
                            if i + d > 7 or j - d < 0:
                                break
                            if board[i + d][j - d] != ' ':
                                king_safe = True
                                break
                    
                    if i > ki and j < kj:
                        for d in range(1, i - ki):
                            if i - d < 0 or j + d > 7:
                                break
                            if board[i - d][j + d] != ' ':
                                king_safe = True
                                break

                    if i > ki and j > kj:
                        for d in range(1, i - ki):
                            if i - d < 0 or j - d < 0:
                                break
                            if board[i - d][j - d] != ' ':
                                king_safe = True
                                break
                    
                    if i < ki:
                        for d in range(1, ki - i):
                            if i + d > 7:
                                break
                            if board[i + d][j] != ' ':
                                king_safe = True
                                break
                    
                    if i > ki:
                        for d in range(1, i - ki):
                            if i - d < 0:
                                break
                            if board[i - d][j] != ' ':
                                king_safe = True
                                break

                    if j < kj:
                        for d in range(1, kj - j):
                            if j + d > 7:
                                break
                            if board[i][j + d] != ' ':
                                king_safe = True
                                break   

                    if j > kj:
                        for d in range(1, j - kj):
                            if j - d < 0:
                                break
                            if board[i][j - d] != ' ':
                                king_safe = True
                                break   


                    if not king_safe:
                        return True


def checkmate(board: list[list[str]], whites_turn: bool) -> bool:
    if not in_check(board, whites_turn):
        return False

    for i1 in range(8):
        for j1 in range(8):
            for i2 in range(8):
                for j2 in range(8):
                    if valid_move_piece(board[i1][j1], i1, j1, i2 , j2) and is_valid_move(deepcopy(board), i1, j1, i2, j2, whites_turn) and is_valid_check(deepcopy(board), i1, j1, i2, j2, whites_turn):
                        return False
    
    return True


def can_castle(
    board: list[list[str]], 
    whites_turn: bool,
    left_white_rook_moved: bool,
    right_white_rook_moved: bool,
    white_king_moved: bool,
    left_black_rook_moved: bool,
    right_black_rook_moved: bool,
    black_king_moved: bool,
    castling_left: bool,
) -> bool:
    if in_check(board, whites_turn):
        return False
    
    if whites_turn and castling_left:
        if white_king_moved or left_white_rook_moved:
            return False
        
        for j in range(1, 4):
            if board[7][j] != ' ':
                return False
            
    if whites_turn and not castling_left:
        if white_king_moved or right_white_rook_moved:
            return False
        
        for j in range(5, 7):
            if board[7][j] != ' ':
                return False
        
    if not whites_turn and castling_left:
        if black_king_moved or left_black_rook_moved:
            return False
        
        for j in range(1, 4):
            if board[0][j] != ' ':
                return False
            
    if not whites_turn and not castling_left:
        if black_king_moved or right_black_rook_moved:
            return False
        
        for j in range(5, 7):
            if board[0][j] != ' ':
                return False
    
    return True
    

