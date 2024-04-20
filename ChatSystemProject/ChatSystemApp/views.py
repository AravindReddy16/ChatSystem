from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import *
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse

# Create your views here.

def registerPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if not User.objects.filter(username=username).exists():
            if password1 == password2:
                newuser = User.objects.create_user(username=username, password=password1)
                newuser.save()
                return redirect('loginPage')
            else:
                messages.error(request,'Password mismatch')
        else:
            messages.error(request,'Username already in use')
    return render(request,'ChatSystemApp/register.html')

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            if not Follower.objects.filter(followerdata = user).exists():
                follower = Follower.objects.create(followerdata = user)
                follower.save()
            if not Following.objects.filter(followingdata = user).exists():
                following = Following.objects.create(followingdata = user)
                following.save()
            return redirect('friendsPage')
        else:
            messages.error(request,'Username or Password is mismatch')
    return render(request,'ChatSystemApp/login.html')

def logoutPage(request):
    logout(request)
    return redirect('loginPage')

@login_required(login_url='loginPage')
def friendsPage(request):
    follower_pk = Follower.objects.get(followerdata=request.user.id)
    following_pk = Following.objects.get(followingdata=request.user.id)
    list_friends = FriendsList.objects.filter(Q(follower=follower_pk) | Q(following=following_pk))
    friends = list_friends.exclude(following=following_pk).order_by('-following')
    friends_count = list_friends.exclude(following=following_pk).count()
    result = True
    if request.method == 'POST':
        q = request.POST.get('q')
        if friends.filter(following__followingdata__username__icontains = q).exists():
            friends = friends.filter(following__followingdata__username__icontains = q)
            result = True
        else:
            result = False
    context = {'friends': friends,'result': result,'friends_count': friends_count}
    return render(request,'ChatSystemApp/friends.html',context)

@login_required(login_url='loginPage')
def usersPage(request):
    users = User.objects.exclude(id = request.user.id).order_by('username')
    result = True
    if request.method == 'POST':
        q = request.POST.get('q')
        if users.filter(username__icontains = q).exists():
            users = users.filter(username__icontains = q)
            result = True
        else:
            result = False
    context = {'users':users, 'result':result}
    return render(request,'ChatSystemApp/users.html',context)

@login_required(login_url='loginPage')
def chatPage(request,follower_id,following_id):
    user = User.objects.get(id=following_id)
    follower1 = Follower.objects.get(followerdata=follower_id)
    following1 = Following.objects.get(followingdata=following_id)
    if request.method == 'POST':
        msg=request.POST.get('msg')
        if len(msg) != 0:
            new_msg = ChatRoom.objects.create(follower = follower1,following = following1,message=msg)
            new_msg.save()
    getMessages(request,follower_id,following_id)
    get_follow(request,follower_id,following_id)
    friends_count(request,follower_id,following_id)
    context = {'user':user,'follower':follower1}
    return render(request,'ChatSystemApp/chat.html',context)

def friends_count(request,follower_id,following_id):
    follower2 = Follower.objects.get(followerdata=following_id)
    friends_count = FriendsList.objects.filter(follower=follower2).count()
    return JsonResponse({'friends_count':friends_count})

def get_follow(request,follower_id,following_id):
    follower1 = Follower.objects.get(followerdata=follower_id)
    following1 = Following.objects.get(followingdata=following_id)
    follower2 = Follower.objects.get(followerdata=following_id)
    following2 = Following.objects.get(followingdata=follower_id)
    follow = False
    requested = False
    follow_back = False
    if FollowList.objects.filter(follower=follower1,following=following1).exists() and FollowList.objects.filter(follower=follower2,following=following2).exists():
        if not FriendsList.objects.filter(follower=follower1,following=following1).exists():
            new_friend = FriendsList.objects.create(follower=follower1,following=following1)
            new_friend.save()
        follow = True
        requested = False
        follow_back = False
    elif FollowList.objects.filter(follower=follower1,following=following1).exists() and not FollowList.objects.filter(follower=follower2,following=following2).exists():
        if FriendsList.objects.filter(follower=follower1,following=following1).exists():
            new_friend = FriendsList.objects.get(follower=follower1,following=following1)
            new_friend.delete()
        follow = False
        requested = True
        follow_back = False
    elif FollowList.objects.filter(follower=follower2,following=following2).exists() and not FollowList.objects.filter(follower=follower1,following=following1).exists():
        if FriendsList.objects.filter(follower=follower1,following=following1).exists():
            new_friend = FriendsList.objects.get(follower=follower1,following=following1)
            new_friend.delete()
        follow = False
        requested = False
        follow_back = True
    else:
        if FriendsList.objects.filter(follower=follower1,following=following1).exists():
            new_friend = FriendsList.objects.get(follower=follower1,following=following1)
            new_friend.delete()
        follow = False
        requested = False
        follow_back = False
    return JsonResponse({'follow':follow,'requested':requested,'follow_back':follow_back})

@login_required(login_url='loginPage')
def getMessages(request,follower_id,following_id):
    follower1 = Follower.objects.get(followerdata=follower_id)
    following1 = Following.objects.get(followingdata=following_id)
    follower2 = Follower.objects.get(followerdata=following_id)
    following2 = Following.objects.get(followingdata=follower_id)
    chat_messages = ChatRoom.objects.filter(Q(follower=follower1,following=following1) | Q(follower=follower2,following=following2)).order_by('time')
    return JsonResponse({'chat_messages':list(chat_messages.values())})

def deleteMessage(request,follower_id,following_id,message_id):
    message = ChatRoom.objects.get(id=message_id)
    message.delete()
    return JsonResponse({'success': 'Message Deleted.'})

@login_required(login_url='loginPage')
def createFollow(request,follower_id,following_id):
    follower_pk = Follower.objects.get(followerdata=follower_id)
    following_pk = Following.objects.get(followingdata=following_id)
    if FollowList.objects.filter(follower=follower_pk,following=following_pk).exists():
        data = FollowList.objects.get(follower=follower_pk,following=following_pk)
        data.delete()
    else:
        data = FollowList.objects.create(follower=follower_pk,following=following_pk)
        data.save()
    return JsonResponse({'success': 'Successfully Changed.'})

def aboutPage(request):
    return render(request,'ChatSystemApp/about.html')

@login_required(login_url='loginPage')
def roomPage(request):
    if request.method == 'POST':
        roomname = request.POST.get('roomname')
        if Room.objects.filter(name=roomname).exists():
            roomid = Room.objects.get(name=roomname)
            return redirect('roomchatPage',roomid.id)
        else:
            new_room = Room.objects.create(name=roomname)
            new_room.save()
            roomid = Room.objects.get(name=roomname)
            return redirect('roomchatPage',roomid.id)
    return render(request,'ChatSystemApp/room.html')

@login_required(login_url='loginPage')
def roomchatPage(request,room_id):
    room_details = Room.objects.get(id=room_id)
    user_details = User.objects.get(id=request.user.id)
    if request.method == 'POST':
        msg = request.POST.get('msg')
        if len(msg) != 0:
            new_msg = RoomMessages.objects.create(room_name = room_details,user_name = user_details.username,message = msg)
            new_msg.save()
    getroomMessages(request,room_id)
    context = {'room_details':room_details}
    return render(request,'ChatSystemApp/roomchat.html',context)

@login_required(login_url='loginPage')
def getroomMessages(request,room_id):
    room_messages = RoomMessages.objects.filter(room_name = room_id).order_by('time')
    return JsonResponse({'room_messages':list(room_messages.values())})

@login_required(login_url='loginPage')
def deleteroomMessage(request,msg_id):
    msg = RoomMessages.objects.get(id=msg_id)
    msg.delete()
    return JsonResponse({'success': 'Message Deleted.'})