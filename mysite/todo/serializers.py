# 1 Standard Library : 없음

# 2 Third-party: django 
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

# 3-1 Local application
from .models import todo

# 3-2 Local application
from interaction.models import TodoLike, TodoBookmark, TodoComment

class  TodoSerializer(ModelSerializer):

    username = serializers.CharField(source="user.username", read_only=True)

    like_count = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()
    bookmark_count = serializers.SerializerMethodField()
    is_bookmarked = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()


    class Meta:
        model = todo

        fields = [
            "id",
            "title",
            "description",
            "complete",
            "exp",
            "img",
            "created_at",


            "user",
            "username",

            "is_public",

            "like_count",
            "is_liked",

            "bookmark_count",
            "is_bookmarked",

            "comment_count",
        ]

        read_only_fields = ["user"]

    def _user(self):
        request = self.context.get("request")

        if request and request.user.is_authenticated:
            return request.user

        return None
    
    def get_like_count(self, obj):
        return TodoLike.objects.filter(todo=obj).count()

    def get_is_liked(self, obj):
        user = self._user()
        if not user:
            return False
        return TodoLike.objects.filter(
            todo=obj,
            user=user
        ).exists()
    
    def get_bookmark_count(self, obj):

        return TodoBookmark.objects.filter(
            todo=obj
        ).count()


    def get_is_bookmarked(self, obj):

        user = self._user()

        if not user:
            return False

        return TodoBookmark.objects.filter(
            todo=obj,
            user=user
        ).exists()


    def get_comment_count(self, obj):

        return TodoComment.objects.filter(
            todo=obj
        ).count()



