'''
1 Standard Library : 없음
2 Third-party: django 
3 Local application : 없음
'''
#2-1   
from django.contrib import admin
#2-2 
from django.urls import path, include
from django.shortcuts import redirect
#2-3 
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path("admin/", admin.site.urls),
    path("todo/", include("todo.urls")),
    path("", lambda request: redirect("todo:todo_list")),#람다로 임시로 화면 확인용 만듦
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)