from django.shortcuts import render
from tasks import models
from django.views.generic import ListView, DetailView, CreateView


# Список існуючих завдань
class TaskListView(ListView):
    model = models.Task
    context_object_name = "tasks"
    template_name = "tasks/task_list.html"


# Детальний огляд завдань
class TaskDetailView(DetailView):
    model = models.Task
    context_object_name = "task"
    template_name = "tasks/task_detail.html"


class TaskCreateView(CreateView):
    model = models.Task
    template_name = "tasks/task_form.html"
    form_class = TaskForm
    """success_url = " " """
