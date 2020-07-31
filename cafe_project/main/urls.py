from django.urls import path
from . import views #. 은 현재경로 (여기서 현재경로는 main). 해당구문은 views에 만들어지는걸 url을 통해서 연결(뚫어주겠다)

urlpatterns = [
    path('', views.home, name='home'),
]
