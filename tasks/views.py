from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import FormView
from .forms import RegistrationForm, TaskForm, TaskUpdateForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Task


def home(request):
    if request.user.is_authenticated:
        return redirect("task_page")
    return render(request, "tasks/home.html")


@login_required(login_url="login")
def tasks(request):
    q = request.GET.get("q", "").strip()
    task_filter = Task.objects.filter(
        Q(name__icontains=q) | Q(description__icontains=q)
    )
    uncompleted_task_count = Task.objects.filter(is_completed=False).count()
    completed_task_count = Task.objects.filter(is_completed=True).count()
    context = {
        "tasks": task_filter,
        "task_count": uncompleted_task_count,
        "c_task_count": completed_task_count,
    }
    return render(request, "tasks/task_page.html", context)


def task(request, pk):
    task = Task.objects.get(id=pk)
    context = {
        "task": task,
    }
    return render(request, "tasks/task.html", context)


def delete_task(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == "POST":
        task.delete()
        return redirect("task_page")
    context = {
        "tasks": task,
    }
    return render(request, "tasks/delete_task.html", context)


def update_task(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == "POST":
        form = TaskUpdateForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("task_page")
    else:
        form = TaskUpdateForm(instance=task)
    context = {"tasks": task, "form": form}
    return render(request, "tasks/update_task.html", context)


class Login(LoginView):
    template_name = "tasks/login.html"
    next_page = reverse_lazy("task_page")
    redirect_authenticated_user = True


class Logout(LogoutView):
    next_page = reverse_lazy("home")


class RegisterUser(FormView):
    template_name = "tasks/register.html"
    form_class = RegistrationForm
    success_url = reverse_lazy("task_page")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


@login_required(login_url="login")
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.host = request.user
            task.save()
            return redirect("task_page")
    else:
        form = TaskForm()

    return render(request, "tasks/create_task.html", {"form": form})
