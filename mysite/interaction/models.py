# 1. Standard Library: 없음
# 2. Third-party :django 
# 3. Local Application : 없음

# 2. Third-party :django 
from django.db import models
from django.conf import settings

class TodoLike(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    todo = models.ForeignKey(
        "todo.todo",   # 기존 todo 앱 모델 참조
        on_delete=models.CASCADE,
        related_name="likes"
    )
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:

        unique_together = ("user", "todo")


class TodoBookmark(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    todo = models.ForeignKey(
        "todo.todo",
        on_delete=models.CASCADE,
        related_name="bookmarks"
    )

    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:

        unique_together = ("user", "todo")


class TodoComment(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    todo = models.ForeignKey(
        "todo.todo",
        on_delete=models.CASCADE,
        related_name="comments"
    )

    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
