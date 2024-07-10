# pages/urls.py
from django.urls import path
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path
from .views import *

urlpatterns = [
  # path('partial/<str:page>/', partial_content, name='partial_content'),

  # navigation
  path("", scene, name="home"),
  path("menuPong/", menuPong),

  # account
  path("register/", register),
  path("createUser", createUser),
  path("login/", login),
  path('api/login_status/', get_login_status, name='login_status'),
  path("account/", account),
  path("logout/", logout),
  path("user_avatar/", user_avatar, name='user_avatar'),

  # Game
  path('create_session/', create_session, name='create_session'),
  path('join_session/<str:session_id>/', join_session, name='join_session'),
  path("pong/<str:session_id>/", pong, name="pong_session"),  # Add this line
]
