from django.contrib.auth.models import User
from django.db import models

class UserTT(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=140, null=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
