from django.urls import path
from .import views

urlpatterns =[
    path('',views.friendsPage,name='friendsPage'),
    path('users/',views.usersPage,name='usersPage'),
    path('register/',views.registerPage,name='registerPage'),
    path('login/',views.loginPage,name='loginPage'),
    path('logout/',views.logoutPage,name='logoutPage'),
    path('chat/<str:follower_id>/<str:following_id>/',views.chatPage,name='chatPage'),
    path('count/<str:follower_id>/<str:following_id>/',views.friends_count,name='friendsCount'),
    path('getFollow/<str:follower_id>/<str:following_id>/',views.get_follow,name='getFollow'),
    path('create/<str:follower_id>/<str:following_id>/',views.createFollow,name='createFollow'),
    path('get/<str:follower_id>/<str:following_id>/',views.getMessages,name='getMessages'),
    path('deleteMessage/<str:follower_id>/<str:following_id>/<str:message_id>',views.deleteMessage,name='deleteMessage'),
    path('about/',views.aboutPage,name='aboutPage'),
    path('room/',views.roomPage,name='roomPage'),
    path('roomchat/<str:room_id>/',views.roomchatPage,name='roomchatPage'),
    path('getchat/<str:room_id>/',views.getroomMessages,name='getroomMessages'),
    path('deleteroomMessage/<str:msg_id>/',views.deleteroomMessage,name='deleteroomMessage'),
]