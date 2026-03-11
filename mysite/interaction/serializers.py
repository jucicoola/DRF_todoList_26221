# 1. Standard library : 없음 
# 2. Third-party: django rest_framework
# 3. Local application: .models

# 2. Third-party
from rest_framework import serializers

# 3. Local application
from .models import TodoLike, TodoBookmark, TodoComment


class TodoLikeSerializer(serializers.ModelSerializer):

    class Meta:

        model = TodoLike

        fields = "__all__"



class TodoBookmarkSerializer(serializers.ModelSerializer):

    class Meta:

        model = TodoBookmark

        fields = "__all__"


class TodoCommentSerializer(serializers.ModelSerializer):

    username = serializers.CharField(
        source="user.username",
        read_only=True
    )


    class Meta:

        model = TodoComment

        fields = [
            "id",          # 댓글 id
            "todo",        # 어떤 Todo에 달린 댓글인지
            "user",        # 댓글 작성자
            "username",    # 작성자 username (추가 필드)
            "content",     # 댓글 내용
            "created_at"   # 작성 시간
        ]

        read_only_fields = ["user"]
