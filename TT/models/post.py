from django.db import models
from TT.models.user_tt import UserTT


class Post(models.Model):
    userTT = models.ForeignKey(UserTT, on_delete=models.CASCADE, null=True)
    content = models.CharField(max_length=256)
    post_pic = models.ImageField(upload_to='post_pics', blank=True, null=True)
    date = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return f"/post/{self.id}"