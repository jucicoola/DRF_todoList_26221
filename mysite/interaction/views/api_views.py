# 1. Standard library : 없음 

# 2. Third-party: django
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework import viewsets
from django.db.models import Q

# 3-1. Local application:
from todo.models import todo
from todo.serializers import TodoSerializer
# 3-2. Local application:
from ..models import TodoLike, TodoBookmark, TodoComment 


class TodoViewSet(viewsets.ModelViewSet):
    queryset = todo.objects.none()  # ✅ Router용으로만 남겨둠 (빈 쿼리셋)
    serializer_class = TodoSerializer


    def get_permissions(self):
        # 목록/상세 조회는 비로그인도 허용
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        return [IsAuthenticated()]  # ✅ 나머지는 로그인 필요

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return todo.objects.filter(
                Q(is_public=True) | Q(user=user)  # ✅ 공개글 + 본인글
            ).order_by("-created_at")
        return todo.objects.filter(is_public=True).order_by("-created_at")  # ✅ 비로그인은 공개글만

    def get_serializer_context(self):
        return {"request": self.request}

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # ✅ 작성자 자동 저장

    def perform_update(self, serializer):
        if serializer.instance.user != self.request.user:
            raise PermissionDenied("본인의 글만 수정할 수 있습니다.")  # ✅
        serializer.save()

    def perform_destroy(self, instance):
        if instance.user != self.request.user:
            raise PermissionDenied("본인의 글만 삭제할 수 있습니다.")  # ✅
        instance.delete()
    
    def list(self, request, *args, **kwargs):
        qs = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(qs)
        if page is not None:
            serializer = self.get_serializer(
                page,
                many=True,
                context={"request": request},
            )

            return Response({
                "data": serializer.data,

                # 현재 페이지
                "current_page": int(request.query_params.get("page", 1)),

                # 전체 페이지 수
                "page_count": self.paginator.page.paginator.num_pages,

                # 다음 페이지 존재 여부
                "next": self.paginator.get_next_link() is not None,

                # 이전 페이지 존재 여부
                "previous": self.paginator.get_previous_link() is not None,
            })

        # ---------------------------------------------
        # pagination이 없는 경우
        # ---------------------------------------------
        serializer = self.get_serializer(
            qs,
            many=True,
            context={"request": request},
        )

        return Response({
            "data": serializer.data,
            "current_page": 1,
            "page_count": 1,
            "next": False,
            "previous": False,
        })

    @action(detail=True, methods=["post"], permission_classes=[IsAuthenticated])
    def like(self, request, pk=None):
        #내용 불러오기 
        instance = self.get_object()
        user = request.user
        obj, created = TodoLike.objects.get_or_create(
            todo=instance,
            user=user
        )
        # 좋아요 처리 
        if created:
            liked = True

        else:
            obj.delete()
            liked = False

        #좋아요 개수 
        like_count = TodoLike.objects.filter(todo=instance).count()


        return Response({
            "liked": liked,
            "like_count": like_count
        })

 
    @action(detail=True, methods=["post"], permission_classes=[IsAuthenticated])
    def bookmark(self, request, pk=None):

        instance = self.get_object()
        user = request.user
        obj, created = TodoBookmark.objects.get_or_create(
            todo=instance,
            user=user
        )

        if created:
            bookmarked = True

        else:
            obj.delete()
            bookmarked = False

        bookmark_count = TodoBookmark.objects.filter(todo=instance).count()

        return Response({
            "bookmarked": bookmarked,
            "bookmark_count": bookmark_count
        })

 
    @action(detail=True, methods=["post"], permission_classes=[IsAuthenticated])
    def comments(self, request, pk=None):

        instance = self.get_object()
        user = request.user
        content = (request.data.get("content") or "").strip()

        # 댓글 내용 검증
        if not content:
            return Response(
                {"detail": "content is required"},
                status=400
            )

        # 댓글 생성
        TodoComment.objects.create(
            todo=instance,
            user=user,
            content=content
        )

        # 댓글 개수 계산
        comment_count = TodoComment.objects.filter(todo=instance).count()

        return Response({
            "comment_count": comment_count
        })