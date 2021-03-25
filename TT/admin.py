from django.contrib import admin
from TT.models.comment import Comment
from TT.models.post import Post
from TT.models.user_tt import UserTT

admin.site.register(UserTT)
admin.site.register(Post)
admin.site.register(Comment)