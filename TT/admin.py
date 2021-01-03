from django.contrib import admin

# Register your models here.
from TT.models.post import Post
from TT.models.user_tt import UserTT

admin.site.register(UserTT)
admin.site.register(Post)