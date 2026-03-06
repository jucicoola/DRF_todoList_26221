from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect



urlpatterns = [
    path("admin/", admin.site.urls),
    path("todo/", include("todo.urls")),
    path("", lambda request: redirect("todo:todo_list")),#람다로 임시로 화면 확인용 만듦
]
