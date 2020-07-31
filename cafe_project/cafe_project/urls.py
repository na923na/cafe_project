from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('board/', include('board.urls')),
    path('user/', include('user.urls')),    #''은 주소창에 아무것도 안해도(기본화면)이 이 화면으로 하겠다
]