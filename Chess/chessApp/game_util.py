from copy import deepcopy
from typing import Optional

def update_board(board: list[list[str]], i1: int, j1: int, i2: int, j2: int, whites_turn: bool) -> tuple[list[list[str]], bool, bool]:
    if not valid_move_piece(board[i1][j1], i1, j1, i2 , j2):
        print('valid_move_piece failed')
        return (board, whites_turn, False)
    elif not is_valid_move(deepcopy(board), i1, j1, i2, j2, whites_turn):
        print('is_valid_move failed')
        return (board, whites_turn, False)
    elif not is_valid_check(deepcopy(board), i1, j1, i2, j2, whites_turn):
        print('is_valid_check failed')
        return (board, whites_turn, False)
    board[i2][j2] = board[i1][j1]
    board[i1][j1] = ' '
    mate = checkmate(deepcopy(board), i1, j1, i2, j2, not whites_turn)
    return (board, not whites_turn, mate)


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
    elif (piece == 'p' or piece == 'P') and j1 != j2 and board[j1][j2] == None:
        return False 
    elif not valid_move_piece(piece, i1, j1, i2, j2): 
        return False
    else:
        return True


def is_valid_check(board: list[list[str]], i1: int, j1: int, i2: int, j2, whites_turn: bool) -> bool:
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
            print('     ', i, j,is_valid_move(board, i, j, ki, kj, not whites_turn))
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
                    print('king_safe before loop', king_safe)
                    if i > ki and j > kj:
                        print('entered correct if statement')
                        for d in range(1, i - ki):
                            if i - d < 0 or j - d < 0:
                                break
                            if board[i - d][j - d] != ' ':
                                print('BAD', i, j, board[i-d][j-d], board[i - d][j - d] != ' ')
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


def checkmate(board: list[list[str]], i1: int, j1: int, i2: int, j2: int, whites_turn: bool) -> bool:
    if not in_check(board, whites_turn):
        print('not check')
        return False

    ki, kj = 0, 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != None and board[i][j].islower() and whites_turn:
                ki, kj = i, j
                break
    
    for i in range(ki-1, ki+2):
        for j in range(kj-1, kj+2):
            if is_valid_move(deepcopy(board), i1, j1, i2, j2, whites_turn) and is_valid_check(deepcopy(board), i1, j1, i2, j2):
                print('valid move found')
                return False
    return True