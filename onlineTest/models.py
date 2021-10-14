from django.db import models
from django.contrib.auth.models import User
class Questions(models.Model):
    queno=models.IntegerField()
    que=models.CharField(max_length=200)
    ans=models.CharField(max_length=200)
    marks=models.IntegerField()
    def __str__(self):
        return self.que


class test_user(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    real_name=models.CharField(max_length=40)