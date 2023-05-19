from django.shortcuts import render, redirect
from .models import Board
from .game_util import *

# Create your views here.
def index(request):
    if Board.objects.count() == 0:
        new_board = Board()
        new_board.save()

    board = Board.objects.get()

    board_str: str = board.content
    print('board_str:', board_str)
    
    return render(request, 'chessapp/index.html', {
        'board': board,
    })

def move(request, move: str) -> redirect:
    board_model: Board = Board.objects.get()
    whites_turn: bool = board_model.whites_turn
    board_str: str = board_model.content
    board: list[list[str]] = []
    
    for i in range(64):
        if i % 8 == 0:
            board.append([])
        
        board[-1].append(board_str[i])
    
    
    i1: int = int(move[0])
    j1: int = int(move[1])
    i2: int = int(move[2])
    j2: int = int(move[3])
    
    new_board, new_whites_turn = update_board(board, i1, j1, i2, j2, whites_turn)

    new_board_str: str = ' '
    for i in range(64):
        new_board_str += new_board[i // 8][i % 8]
    
    #new_board_str = ' ' * 64
    board_model.content = new_board_str
    board_model.whites_turn = new_whites_turn
    board_model.save()

    print('new str:', new_board_str)

    return redirect('index')

