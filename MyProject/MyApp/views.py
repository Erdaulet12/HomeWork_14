from django.views.generic import ListView
from .models import Task
from django.views.generic import DetailView
from django.http import JsonResponse
from django.views.generic.edit import CreateView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView


class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task_list.html'  # Укажите свой шаблон, если нужен
    context_object_name = 'tasks'

    def render_to_response(self, context, **response_kwargs):
        task_data = [{"id": task.id, "title": task.title, "description": task.description, "is_completed": task.is_completed} for task in context['tasks']]
        return JsonResponse(task_data, safe=False)


class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'  # Укажите свой шаблон, если нужен
    context_object_name = 'task'

    def render_to_response(self, context, **response_kwargs):
        task = context['task']
        task_data = {"id": task.id, "title": task.title, "description": task.description, "is_completed": task.is_completed}
        return JsonResponse(task_data)


@method_decorator(csrf_exempt, name='dispatch')
class TaskCreateView(CreateView):
    model = Task
    fields = ['title', 'description']

    def form_valid(self, form):
        self.object = form.save()
        task_data = {"id": self.object.id, "title": self.object.title, "description": self.object.description,
                     "is_completed": self.object.is_completed}
        return JsonResponse(task_data)

    def form_invalid(self, form):
        return JsonResponse(form.errors, status=400)


class TaskDeleteView(DeleteView):
    model = Task
    success_url = '/tasks/'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return JsonResponse({"message": "Task deleted successfully"})


class TaskUpdateView(UpdateView):
    model = Task
    fields = ['title', 'description', 'is_completed']

    def form_valid(self, form):
        self.object = form.save()
        task_data = {"id": self.object.id, "title": self.object.title, "description": self.object.description,
                     "is_completed": self.object.is_completed}
        return JsonResponse(task_data)

    def form_invalid(self, form):
        return JsonResponse(form.errors, status=400)
