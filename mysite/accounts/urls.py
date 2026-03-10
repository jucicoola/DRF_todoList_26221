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
from .views.views import SignupAPIView, SessionLoginAPIView, SessionLogoutAPIView
from .views.views_page import LoginPageView, SignupPageView


urlpatterns = [
    path("api/signup/", SignupAPIView.as_view(), name="api-signup"),
    path("api/login/", TokenObtainPairView.as_view(), name="jwt-login"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="jwt-refresh"),

    path("signup_page/", SignupPageView.as_view(), name="page-signup"),
    path("login/", LoginPageView.as_view(), name="page-login"),
]

    # path("api/logout/", SessionLogoutAPIView.as_view(), name="api-logout")
    # jwt로 넘어온 순간 토큰 관리 정책이 필요하지 세션 관리는 필요 없음 다만, 사용자 경험 측면에서 로그아웃을 토큰으로 어떻게 관리할지는 필요
