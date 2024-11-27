from http.client import HTTPResponse

from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
from django.urls import reverse, reverse_lazy

from .forms import ToDoItemCreateForm, ToDoItemUpdateForm

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
    # model = ToDoItem
    queryset = ToDoItem.objects.filter(archived=False)


class ToDoListDoneView(ListView):
    queryset = ToDoItem.objects.filter(done=True).all()


class ToDoDetailView(DetailView):
    # model = ToDoItem
    queryset = ToDoItem.objects.filter(archived=False)

class ToDoItemCreateView(CreateView):
    model = ToDoItem
    form_class = ToDoItemCreateForm


class ToDoItemUpdateView(UpdateView):
    model = ToDoItem
    template_name_suffix = "_update_form"
    form_class = ToDoItemUpdateForm


class ToDoItemDeleteView(DeleteView):
    model = ToDoItem
    success_url = reverse_lazy("todo_list:list")

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.archived = True
        self.object.save()
        return HttpResponseRedirect(success_url)
