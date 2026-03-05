from django.contrib import admin
from .models import todo

@admin.register(todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "created_at",
        "updated_at",
    )
# Register your models here.
