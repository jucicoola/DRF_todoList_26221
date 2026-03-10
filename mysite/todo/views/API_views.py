
'''
1 Standard Library 없음
2 Third-party
3 Local application :
'''
# 2. django
# 2-1. django third_party 
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination


#3 Local application
from ..models import todo
from ..serializers import TodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    queryset = todo.objects.all().order_by("-created_at")
    serializer_class = TodoSerializer
   