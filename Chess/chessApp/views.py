from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'chessapp/index.html')

def move(request, move):
    return redirect('index')

