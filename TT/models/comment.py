from django.db import models
from TT.models.post import Post
from TT.models.user_tt import UserTT


class Comment(models.Model):
    user = models.ForeignKey(UserTT, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    content = models.CharField(max_length=240)
