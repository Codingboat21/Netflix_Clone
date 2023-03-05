from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path("",home,name='home'),
    path('login/',Login,name='login'),
    path('signup/',Signup,name='signup'),

    path('movielist/<str:profile_id>/',movielist,name='movielist'),
    path('movielist/moviedetail/<str:movie_id>/',movieDetail,name='moviedetail'),
    path('profile/',profiles,name='profile'),
    path('profilecreate/',profileCreate,name='profilecreate'),
    path('moviedetail/playM/<str:movie_id>',PlayMovie,name='play-movie')


]
