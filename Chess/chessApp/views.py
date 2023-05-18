from django.shortcuts import render, redirect
from .models import Board

# Create your views here.
def index(request):
    if Board.objects.count() == 0:
        new_board = Board()
        new_board.save()

    board = Board.objects.get()
    
    return render(request, 'chessapp/index.html', {
        'board': board,
    })

def move(request, move: str) -> redirect:
    board_model: Board = Board.objects.get()
    turn: bool = Board.whites_turn
    board_str: str = Board.content
    board: list[list[str]] = []

    for i in range(64):
        if i % 8 == 0:
            board.append([])
        
        board[-1].append(board_str[i])
    
    



    i1: int = int(move[0])
    j1: int = int(move[1])
    i2: int = int(move[2])
    j2: int = int(move[3])







    return redirect('index')

