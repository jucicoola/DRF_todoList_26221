from django.shortcuts import render
from ..models import todo
# from ..serializers import TodoSerializer
from django.views import View
from django.views.generic import CreateView, DetailView, UpdateView
from django.urls import reverse_lazy
'''
화면으로쏴주는 로직
3개 모두 가상릴레이션을 만드는 로직으로 todo 관련 데이터를 전부 불러서 진행 
아래로 갈 수록 간편하지만 커스터마이징이 힘들다. 
'''
# def todo_list(request):
#     todos = todo.objects.all()
#     return render(request, "todo.html", {"todos": todos})

class TodoListView(View):
    def get(self, request):
        todos = todo.objects.all()
        return render(request, "todo.html", {"todos": todos})

# class TodoListGenericView(ListView):
#     model = todo
#     template_name = "todo.html"
#     context_object_name = "todos"
#     success_url = reverse_lazy('todo:list') 작업 성공 후 이동할 url

class TodoCreateView(CreateView):
    model = todo
    fields = ['title', 'description', 'complete', 'exp']
    template_name = "create.html"
    success_url = reverse_lazy('todo:list')

class TodoDetailView(DetailView):
    model = todo
    template_name = "detail.html"
    context_object_name = "todo"

class TodoUpdateView(UpdateView):
    model = todo
    fields = [
        "title", "description", "complete", "exp"
    ]
    template_name = "update.html"
    context_object_name = "todo"
    success_url = reverse_lazy("todo:list")
        

