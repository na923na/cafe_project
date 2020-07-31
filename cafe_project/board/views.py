from django.shortcuts import render , get_object_or_404, redirect
from .models import Board
from user.models import CustomUser


def board_read(request) : 
    boards = Board.objects.all()
    context = {'boards': boards}
    return render(request, 'board/read.html', context)

def board_read_one (request, pk) : 
    board = get_object_or_404(Board, pk=pk) #데이터가 없으면 에러페이지를 띄워주겠다는 것
    context = {'board' : board}
    return render(request, 'board/read_one.html', context)

def board_create(request) :
    if request.method == 'POST' and request.session.get('user', False) : #세션에 유저 정보가 없다면, 게시물을 저장할 수 없게 만들어 놓은 것 (로그인한 유저만 온리 가능 > 그럼 로그인 만들어야)
       title = request.POST['title']
       author = get_object_or_404(CustomUser, username=request.session['user'] )
       content = request.POST['content']

       board = Board (
           author = author,
           title = title,
           content = content
          
       )
       board.save()

       return redirect('board_read')
    else :
        return render(request, 'board/create.html')

def board_update(request,pk) : 
        title = request.POST['title']
        content = request.POST['content']
        board = Board.objects.get(pk=pk)
        board.title = title
        board.content = content
        board.save()
        return redirect('home')

def pre_update(request,pk):
    board= Board.objects.get(pk=pk)
    context= {'board':board}
    return render (request, "board/update.html",context) 


def board_delete(request,pk) : 
    board = Board.objects.get(pk=pk)
    board.delete()
    return redirect('board_read')

# Create your views here.
