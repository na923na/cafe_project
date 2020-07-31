"""cafe_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views #. 은 현재경로 (여기서 현재경로는 main). 해당구문은 views에 만들어지는걸 url을 통해서 연결(뚫어주겠다)

urlpatterns = [
    path('signup/', views.sign_up, name="sign_up"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name='logout'),
    
]
