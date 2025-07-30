from django.urls import path
from tasks import views

app_name = 'tasks'

urlpatterns = [
    path("/task", views.TaskListView.as_view, "task_view"),
    path("/create", views.TaskCreateView.as_view, "task_create"),
    path("<int:pk>/detail", views.TaskDetailView.as_view, "task_detail"),
]