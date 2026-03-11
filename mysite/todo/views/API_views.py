
'''
1 Standard Library 없음
2 Third-party
3 Local application :
'''
# 2. django
from django.db.models import Q
# 2-1. django third_party 
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.exceptions import PermissionDenied


#3 Local application
from ..models import todo
from ..serializers import TodoSerializer

class TodoListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = "page_size"
    max_page_size = 50
    
class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = TodoListPagination

    
    def get_queryset(self):
        user = self.request.user
        return todo.objects.filter(
            Q(is_public=True) | Q(user=user)
        ).order_by("-created_at")
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def perform_update(self, serializer):  # ✅ 추가
        if serializer.instance.user != self.request.user:
            raise PermissionDenied("본인의 글만 수정할 수 있습니다.")
        serializer.save()

    def perform_destroy(self, instance):  # ✅ 추가
        if instance.user != self.request.user:
            raise PermissionDenied("본인의 글만 삭제할 수 있습니다.")
        instance.delete()


