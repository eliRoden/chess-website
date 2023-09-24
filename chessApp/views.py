from django.shortcuts import render, redirect
from .models import Board
from .game_util import *
import logging

logger = logging.getLogger('chessApp')

def index(request):
    logger.info("in index view")
    if request.method == "POST":
        logger.info('post')
        game_id = request.POST.get('game_id')
        game = Board.objects.filter(game_id=game_id).first()
        logger.info('passed board creation')
        if not game:
            game = Board(game_id=game_id)
            game.save()    
        
        return redirect('game', game_id)
    else:
        return render(request, 'chessapp/index.html')


def move(request, game_id: str, move: str) -> redirect:
    board_model: Board = Board.objects.filter(game_id=game_id).first()
    whites_turn: bool = board_model.whites_turn
    board_str: str = board_model.content
    left_white_rook_moved: bool = board_model.left_white_rook_moved
    right_white_rook_moved: bool = board_model.right_white_rook_moved
    white_king_moved: bool = board_model.white_king_moved
    left_black_rook_moved: bool = board_model.left_black_rook_moved
    right_black_rook_moved: bool = board_model.right_black_rook_moved
    black_king_moved: bool = board_model.black_king_moved

    board: list[list[str]] = []
    for i in range(64):
        if i % 8 == 0:
            board.append([])
        
        board[-1].append(board_str[i])

    i1: int = int(move[0])
    j1: int = int(move[1])
    i2: int = int(move[2])
    j2: int = int(move[3])
    
    (
        new_board, 
        new_whites_turn, 
        new_mate, 
        new_left_white_rook_moved,
        new_right_white_rook_moved,
        new_white_king_moved,
        new_left_black_rook_moved,
        new_right_black_rook_moved,
        new_black_king_moved,
    ) = update_board(
        board, 
        i1, 
        j1, 
        i2, 
        j2, 
        whites_turn,
        left_white_rook_moved,
        right_white_rook_moved,
        white_king_moved,
        left_black_rook_moved,
        right_black_rook_moved,
        black_king_moved,
    )


    new_board_str: str = ''
    for i in range(64):
        new_board_str += new_board[i // 8][i % 8]
    
    board_model.content = new_board_str
    board_model.whites_turn = new_whites_turn
    board_model.checkmate = new_mate
    board_model.left_white_rook_moved = new_left_white_rook_moved
    board_model.right_white_rook_moved = new_right_white_rook_moved
    board_model.white_king_moved = new_white_king_moved
    board_model.left_black_rook_moved = new_left_black_rook_moved
    board_model.right_black_rook_moved = new_right_black_rook_moved
    board_model.black_king_moved = new_black_king_moved
    board_model.save()

    return redirect('game', game_id)


def game(request, game_id: str):
    logger.info("in game view")
    if game_id == 'default':
        return render(request, 'chessapp/index.html')

    board = Board.objects.filter(game_id=game_id).first()
    if not board:
        board = Board()
        board.game_id = game_id
        board.save()
    print('board made')
    return render(request, 'chessapp/game.html', {
        'game_id': game_id,
        'board': board,
    })

def new_game(request, game_id: str):
    Board.objects.filter(game_id=game_id).delete()
    return redirect('game', game_id)