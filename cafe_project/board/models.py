from django.db import models
from user.models import CustomUser
from django.utils import timezone

class Board(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now=True)