'''
1 Standard Library : 없음
2 Third-party: django 
3 Local application : views, views_page
'''
# 2-1 django 
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render

# 2-2 django.rest_framework 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

# 3 serializer 
from ..serializers import SignupSerializers
# Create your views here.


class SignupAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = SignupSerializers(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {"detail": "회원가입 완료"},
            status = status.HTTP_201_CREATED
        )
    
class SessionLoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username", "")
        password = request.data.get("password", "")

        user = authenticate(request, username=username, password=password)

        permit_login_try = 5 # POST 말고 보안 관련해서 따로 묶는 것을 여기다가 해놓으면 포스트할때마다 초기화 됨고려 43:57
        count_login_try = 0 

        if not user:
            if count_login_try <= permit_login_try:
                count_login_try += 1 

                return Response(
                    {"detail": "아이디/비밀번호가 올바르지 않습니다. 5번 이상 틀릴 경우 로그인이 제한됩니다. 현재 시도 횟수{count_login_try}"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            else: 
                return Response(
                    {"로그인 시도 횟수 초과로 본인 인증이 필요합니다." }
                )
        
        login(request, user)

        return Response(
            {"detail": "로그인 성공"},
            status = status.HTTP_200_OK
        )
    
class SessionLogoutAPIView(APIView):
    def post(self, request):
        logout(request)
        return Response(
            {"detail": "로그아웃"},
            status = status.HTTP_200_OK
        )