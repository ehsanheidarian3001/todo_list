from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm


def index(request):
    todo_list = Todo.objects.order_by('id')
    if request.POST:
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TodoForm
    context = {
        'todo_list': todo_list,
        'form': form,
    }

    return render(request, 'todo/index.html', context)


def completed(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.completed = not todo.completed
    todo.save()

    return redirect('index')


def delete_completed(request):
    todos = Todo.objects.filter(completed__exact='True').delete()
    print(todos)

    return redirect('index')


def delete_all(request):
    Todo.objects.all().delete()

    return redirect('index')
