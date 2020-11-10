from django.shortcuts import render
from .models import Todo
from .forms import TodoForm


def index(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            headline = form.cleaned_data['headline']
            description = form.cleaned_data['description']
            deadline = form.cleaned_data['deadline']
            recurring = form.cleaned_data['recurring']

            todo = Todo(headline=headline, description=description, deadline=deadline, recurring=recurring)
            todo.save()
        return render(request, 'todo_overview.html', {'todos': Todo.objects.all(), 'form': TodoForm()})
    else:
        return render(request, 'todo_overview.html', {'todos': Todo.objects.all(), 'form': TodoForm()})
# Create your views here.
