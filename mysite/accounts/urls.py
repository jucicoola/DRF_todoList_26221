'''
1 Standard Library : 없음
2 Third-party: django 
3 Local application : views, views_page
'''
# 2. django 
from django.urls import path, include

# 2-1. django(rest_framework_simplejwt) 
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# 3. views, views_page
from .views.views import SignupAPIView, SessionLogoutAPIView
from .views.views_page import LoginPageView, SignupPageView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView 
from .views.views import  MeAPIView

urlpatterns = [
    path("api/signup/", SignupAPIView.as_view(), name="api-signup"),
    path("api/login/", TokenObtainPairView.as_view(), name="jwt-login"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="jwt-refresh"),
    path("api/logout/", SessionLogoutAPIView.as_view(), name="api-logout"),
    path("me/", MeAPIView.as_view()),
]
