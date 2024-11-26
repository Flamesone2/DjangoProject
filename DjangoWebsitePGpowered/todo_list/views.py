from http.client import HTTPResponse

from django.http import HttpRequest
from django.shortcuts import render
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,)
from django.urls import reverse

from .forms import ToDoItemForm
from .models import ToDoItem



def index_view(request: HttpRequest) -> HTTPResponse:
    todo_items = ToDoItem.objects.all()
    return render(request, "todo_list/index.html",
                  context={"todo_items": todo_items}
    )

class ToDoListIndexView(ListView):
    template_name = "todo_list/index.html"
    queryset = ToDoItem.objects.all()[:2]

class ToDoListView(ListView):

    model = ToDoItem

class ToDoListDoneView(ListView):
    queryset = ToDoItem.objects.filter(done=True).all()

class ToDoDetailView(DetailView):
    model = ToDoItem


class ToDoItemCreateView(CreateView):
    model = ToDoItem
    form_class = ToDoItemForm
    # fields = ("title", "description")

