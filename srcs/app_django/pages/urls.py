# pages/urls.py
from django.urls import path
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path, include
from .views import *

urlpatterns = [
  # navigation
  path("", scene, name="home"),
  path("home_page/", home_page),
  path("menuPong/", menuPong),

  # account
	path('account/', include("account.urls")),

  # Game
  path('create_session/', create_session, name='create_session'),
  path('join_session/<str:session_id>/', join_session, name='join_session'),
  path("pong/<str:session_id>/", pong, name="pong_session"),  # Add this line
]
