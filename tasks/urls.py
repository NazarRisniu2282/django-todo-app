from django.urls import path
from . import views
from django.urls import include
from .views import Login, RegisterUser, Logout


urlpatterns = [
    path("", views.home, name="home"),
    path("login/", Login.as_view(), name="login"),
    path("register/", RegisterUser.as_view(), name="register"),
    path("logout/", Logout.as_view(), name="logout"),
    path("tasks/", views.tasks, name="task_page"),
    path("create_task/", views.create_task, name="create_task"),
    path("task/<str:pk>", views.task, name="task"),
    path("delete_task/<str:pk>", views.delete_task, name='delete_task'),
    path("update_task/<str:pk>", views.update_task, name='update_task')
]

