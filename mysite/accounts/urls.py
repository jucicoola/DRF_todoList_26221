'''
1 Standard Library : 없음
2 Third-party: django 
3 Local application : views, views_page
'''
# 2. django 
from django.urls import path, include

# 3. views, views_page
from .views.views import SignupAPIView, SessionLoginAPIView, SessionLogoutAPIView
from .views.views_page import LoginPageView, SignupPageView


urlpatterns = [
    path("api/signup/", SignupAPIView.as_view(), name="api-signup"),
    path("api/login/", SessionLoginAPIView.as_view(), name="api-login"),
    path("api/logout/", SessionLogoutAPIView.as_view(), name="api-logout"),

    path("signup_page/", SignupPageView.as_view(), name="page-signup"),
    path("login/", LoginPageView.as_view(), name="page-login"),
]