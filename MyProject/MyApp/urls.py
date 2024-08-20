from django.urls import path
from .views import TaskListView, TaskDetailView, TaskCreateView, TaskDeleteView, TaskUpdateView

urlpatterns = [
    path('tasks/', TaskListView.as_view(), name='task_list'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('tasks/create/', TaskCreateView.as_view(), name='task_create'),
    path('tasks/delete/<int:pk>/', TaskDeleteView.as_view(), name='task_delete'),
    path('tasks/update/<int:pk>/', TaskUpdateView.as_view(), name='task_update'),
]
