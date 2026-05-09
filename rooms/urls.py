from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
    path("", views.rooms_home, name="rooms_home"),
    path("create_room/", views.createroom, name="create_room"),
    path("room/<str:pk>/", views.room, name="room"),
    path("delete_room/<str:pk>/", views.deleteroom, name="delete_room"),
    path("update_room/<str:pk>/", views.updateroom, name="update_room"),
    path("create_task/<str:pk>/", views.create_task, name="room_create_task"),
    path("delete_task/<str:pk>/", views.delete_task, name="room_delete_task"),
    path("room_task/<str:pk>/", views.task, name="room_task"),
    path("update_task/<str:pk>/", views.update_task, name="room_update_task"),
]