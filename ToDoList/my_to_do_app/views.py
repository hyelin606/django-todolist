from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import * 


'''
def index(request):
   return HttpResponse("My_to_do_app first page")
'''

# after
def index(request):
    #DB에서 데이터를 받아서 index.html 뿌려주기
    todos = Todo.objects.all()
    content = {
        "todos" : todos
    }
    return render(request, "my_to_do_app/index.html", content)

def createTodo(request):
    user_input_str = request.POST['todoContent']
    new_todo = Todo(content = user_input_str)
    
    # 데이터 DB에 저장
    new_todo.save()
    return HttpResponseRedirect(reverse('index'))

def deleteTodo(request):
    delete_todo_id= request.GET['todoNum']
    print("삭제할 todo의 id:", delete_todo_id)
    todo = Todo.objects.get(id = delete_todo_id)
    todo.delete()
    return HttpResponseRedirect(reverse('index'))