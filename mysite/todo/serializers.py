from rest_framework.serializers import ModelSerializer
from .models import todo

class  TodoSerializer(ModelSerializer):
    class Meta:
        model = todo
        # fields = "__all__"
        # read_only_fields = ["created_at", "updated_at"]
        fields = [
            "id",
            "title",
            "description",
            "complete",
            "exp",
            "img"
            # "completed_at",
            # "created_at",
            # "updated_at",
        ]
