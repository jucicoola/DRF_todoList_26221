'''
1 Standard Library : 없음
2 Third-party: django 
3 Local application : views, views_page
'''
# 2-1 django 
from django.contrib.auth import authenticate, login

# 2-2 django.rest_framework 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated

# 3 serializer 
from ..serializers import SignupSerializers
# Create your views here.


class SignupAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = SignupSerializers(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"detail": "회원가입 완료"}, status = status.HTTP_201_CREATED )
    
    
class SessionLogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({"detail": "로그아웃(세션 정리)"},status = status.HTTP_200_OK )