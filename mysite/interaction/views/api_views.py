# 1. Standard library : 없음 

# 2. Third-party: django
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

# 3-1. Local application:
from todo.models import todo
from todo.serializers import TodoSerializer
# 3-2. Local application:
from ..models import TodoLike, TodoBookmark, TodoComment 


class TodoViewSet(viewsets.ModelViewSet):

    queryset = todo.objects.all().order_by("-created_at")
    serializer_class = TodoSerializer
    permission_classes = [AllowAny]
    
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
        todo = self.get_object()
        user = request.user
        obj, created = TodoLike.objects.get_or_create(
            todo=todo,
            user=user
        )
        # 좋아요 처리 
        if created:
            liked = True

        else:
            obj.delete()
            liked = False

        #좋아요 개수 
        like_count = TodoLike.objects.filter(todo=todo).count()


        return Response({
            "liked": liked,
            "like_count": like_count
        })

 
    @action(detail=True, methods=["post"], permission_classes=[IsAuthenticated])
    def bookmark(self, request, pk=None):

        todo = self.get_object()
        user = request.user
        obj, created = TodoBookmark.objects.get_or_create(
            todo=todo,
            user=user
        )

        if created:
            bookmarked = True

        else:
            obj.delete()
            bookmarked = False

        bookmark_count = TodoBookmark.objects.filter(todo=todo).count()

        return Response({
            "bookmarked": bookmarked,
            "bookmark_count": bookmark_count
        })

 
    @action(detail=True, methods=["post"], permission_classes=[IsAuthenticated])
    def comments(self, request, pk=None):

        todo = self.get_object()
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
            todo=todo,
            user=user,
            content=content
        )

        # 댓글 개수 계산
        comment_count = TodoComment.objects.filter(todo=todo).count()

        return Response({
            "comment_count": comment_count
        })