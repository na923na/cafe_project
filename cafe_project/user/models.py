from django.db import models
from django.contrib.auth.models import AbstractUser #추상 > 유저 새로 만들때 많이 사용
from django.utils import timezone

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=10, null=True, blank=True) #null은 완전 비었다. 데이터의 유무를 신경 x , blank는 데이터 자체가 없는 빈칸 
    birth_day = models.DateField(default=timezone.now) #이거 다음으로는 settings.py 들어가서 AUTH_USER_MODEL해서 유저 가져오는 방법 따로 등록해줘야함
    
