'''
1 Standard Library 없음
2 Third-party
3 Local application : 
'''

# 2. Third-party 외부 라이브러리 django 
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static 

# 2-1. Third-party 외부라이브러리 REST
from rest_framework.routers import DefaultRouter

# 3. local application 외부 라이브러리 django 
from .views.template_views import TodoListView, TodoCreateView, TodoDetailView, TodoUpdateView
from .views.API_views import TodoViewSet

app_name = 'todo'

router = DefaultRouter()
router.register("view", TodoViewSet, basename="todo")

urlpatterns = [
    path("list/", TodoListView.as_view(), name="todo_list"),
    path("create/", TodoCreateView.as_view(), name="todo_create"),
    path("detail/<int:pk>/", TodoDetailView.as_view(), name="todo_Detail"),
    path("update/<int:pk>/", TodoUpdateView.as_view(), name="todo_update"),


    # path("api/list/", TodoListAPI.as_view(), name="todo_api_list"),
    # path("api/create/", TodoCreateAPI.as_view(), name="todo_api_create"),
    # path("api/retrieve/<int:pk>/", TodoRetrieveAPI.as_view(), name="todo_api_retrieve"),
    # path("api/update/<int:pk>/", TodoUpdateAPI.as_view(), name="todo_api_update"),
    # path("api/delete/<int:pk>/", TodoDeleteAPI.as_view(), name="todo_api_delete"),

    path("viewsets/", include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
