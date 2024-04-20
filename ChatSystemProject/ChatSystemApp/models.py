from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Follower(models.Model):
    followerdata = models.ForeignKey(User,on_delete=models.CASCADE)

class Following(models.Model):
    followingdata = models.ForeignKey(User,on_delete=models.CASCADE)

class FollowList(models.Model):
    follower = models.ForeignKey(Follower,on_delete=models.CASCADE)
    following = models.ForeignKey(Following,on_delete=models.CASCADE)

class FriendsList(models.Model):
    follower = models.ForeignKey(Follower,on_delete=models.CASCADE)
    following = models.ForeignKey(Following,on_delete=models.CASCADE)

class ChatRoom(models.Model):
    follower = models.ForeignKey(Follower,on_delete=models.CASCADE)
    following = models.ForeignKey(Following,on_delete=models.CASCADE)
    message = models.CharField(max_length=1000,null=False,blank=False)
    time = models.DateTimeField(auto_now_add=True)

class Room(models.Model):
    name = models.CharField(max_length=200,blank=False,null=False)

class RoomMessages(models.Model):
    room_name = models.ForeignKey(Room,on_delete=models.CASCADE)
    user_name = models.CharField(max_length=1000,null=False,blank=False)
    message = models.CharField(max_length=1000,null=False,blank=False)
    time = models.DateTimeField(auto_now_add=True)