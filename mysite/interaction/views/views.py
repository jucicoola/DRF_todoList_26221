# 1. Standard library : 없음 
# 2. Third-party: django, rest_framework
# 3. Local application: .models

# 2-1. Third-party: django
from django.shortcuts import get_object_or_404
# 2-2. Third-party: rest_framework 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# 3-1 Local application: todo app
from todo.models import todo as Todo
# 3-2 Local application: interaction
from ..models import TodoLike, TodoBookmark, TodoComment
from ..serializers import TodoCommentSerializer


class TodoLikeToggleAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request, todo_id):
        todo = get_object_or_404(Todo, id=todo_id)

        obj, created = TodoLike.objects.get_or_create(
            todo=todo,
            user=request.user
        )

        if not created:
            obj.delete()
            liked = False

        else:
            liked = True

        count = TodoLike.objects.filter(todo=todo).count()

        return Response({
            "liked": liked,        # 현재 좋아요 상태
            "like_count": count    # 총 좋아요 수
        })


class TodoBookmarkToggleAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request, todo_id):

        todo = get_object_or_404(Todo, id=todo_id)
        obj, created = TodoBookmark.objects.get_or_create(
            todo=todo,
            user=request.user
        )
        if not created:
            obj.delete()
            bookmarked = False

        else:
            bookmarked = True

        count = TodoBookmark.objects.filter(todo=todo).count()

        return Response({
            "bookmarked": bookmarked,     # 현재 북마크 상태
            "bookmark_count": count       # 전체 북마크 수
        })


class TodoCommentCreateAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request, todo_id):

        todo = get_object_or_404(Todo, id=todo_id)

        content = request.data.get("content", "").strip()

        if not content:

            return Response(
                {"detail": "내용이 필요합니다."},
                status=400
            )

        comment = TodoComment.objects.create(
            todo=todo,              # 어떤 Todo에 달렸는지
            user=request.user,      # 작성자
            content=content         # 댓글 내용
        )

        serializer = TodoCommentSerializer(comment)

        return Response(serializer.data)


class TodoCommentListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, todo_id):

        todo = get_object_or_404(Todo, id=todo_id)

        comments = TodoComment.objects.filter(
            todo=todo
        ).order_by("-created_at")

        serializer = TodoCommentSerializer(
            comments,
            many=True   # 여러 개 객체이기 때문에 many=True
        )

        return Response(serializer.data)