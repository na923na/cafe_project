from django.urls import path
from . import views #. 은 현재경로 (여기서 현재경로는 main). 해당구문은 views에 만들어지는걸 url을 통해서 연결(뚫어주겠다)

urlpatterns = [
    path('read/', views.board_read, name="board_read"),
    path('create/', views.board_create, name="board_create"),
    path('read/<int:pk>', views.board_read_one, name="board_read_one"), #url 자체에다가 데이터를 받아오는 것 (POST,GET 사용하지 않고)
    path('update/<int:pk>', views.board_update, name="board_update"),
    path('pre_update/<int:pk>', views.pre_update, name="pre_update"),
    path('delete/<int:pk>', views.board_delete, name="board_delete"),
]
