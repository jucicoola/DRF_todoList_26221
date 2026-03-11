'''
1 Standard Library 없음
2 Third-party: django
3 Local application :
4 delete
'''
# 2-1 Third-party
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import render

# 3. loacal application
from ..models import todo

'''
화면으로쏴주는 로직
3개 모두 가상릴레이션을 만드는 로직으로 todo 관련 데이터를 전부 불러서 진행 
아래로 갈 수록 간편하지만 커스터마이징이 힘들다. 
'''
# def todo_list(request):
#     todos = todo.objects.all()
#     return render(request, "todo.html", {"todos": todos})

class TodoListView(ListView):
    """Todo 목록 페이지. 최신 생성순으로 정렬해서 보여줌."""

    model = todo
    template_name = "todo/list.html"
    context_object_name = "todos"  # 템플릿에서 {{ todos }}로 접근
    ordering = ["-created_at"]
    success_url = reverse_lazy("todo:list")

# class TodoListGenericView(ListView):
#     model = todo
#     template_name = "todo.html"
#     context_object_name = "todos"
#     success_url = reverse_lazy('todo:list') 작업 성공 후 이동할 url

class TodoCreateView(CreateView):
    model = todo
    fields = ['title', 'description', 'complete', 'exp', 'img']
    template_name = "todo/create.html"
    success_url = reverse_lazy('todo_list')

class TodoDetailView(DetailView):
    model = todo
    template_name = "todo/detail.html"
    context_object_name = "todo"

class TodoUpdateView(UpdateView):
    model = todo
    fields = [
        "title", "description", "complete", "exp", 'img'
    ]
    template_name = "todo/update.html"
    context_object_name = "todo"
    success_url = reverse_lazy("todo_list")
        

