from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register([Follower,Following,FollowList,FriendsList,ChatRoom,Room,RoomMessages])