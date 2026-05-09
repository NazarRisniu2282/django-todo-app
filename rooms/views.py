from django.shortcuts import render, redirect, get_object_or_404
from .forms import RoomForm, RoomTaskForm, RoomTaskUpdateForm
from tasks.models import Room, RoomTask


def rooms_home(request):
    rooms = Room.objects.all()
    context = {"rooms": rooms}
    return render(request, "rooms/rooms_home.html", context)


def room(request, pk):
    room = Room.objects.get(id=pk)
    tasks = RoomTask.objects.filter(room=room)
    context = {
        "room": room,
        "tasks": tasks,
        "task_count": tasks.filter(is_completed=False).count()
               }
    return render(request, "rooms/room.html", context)


def deleteroom(request, pk):
    room = Room.objects.get(id=pk)

    if request.method == "POST":
        room.delete()
        return redirect("rooms_home")

    context = {"room": room}
    return render(request, "rooms/delete_room.html", context)


def updateroom(request, pk):
    room = Room.objects.get(id=pk)

    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect("rooms_home")
    else:
        form = RoomForm(instance=room)
    context = {"room": room, "form": form}
    return render(request, "rooms/update_room.html", context)


def createroom(request):
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.host = request.user
            room.save()
            return redirect("rooms_home")
    else:
        form = RoomForm()

    return render(request, "rooms/create_room.html", {"form": form})


def create_task(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomTaskForm()

    if request.method == "POST":
        form = RoomTaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.room = room
            task.host = request.user
            task.save()
            return redirect("room", pk=room.id)
    else:
        form = RoomTaskForm()

    return render(request, "rooms/room_create_task.html", {"form": form})


def update_task(request, pk):
    task = get_object_or_404(RoomTask, id=pk)

    if request.method == "POST":
        form = RoomTaskUpdateForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("room_task", pk=task.id) 
    else:
        form = RoomTaskUpdateForm(instance=task)
    
    context = {"task": task, "form": form}
    return render(request, "rooms/room_task_update.html", context)

def delete_task(request, pk):
    task = get_object_or_404(RoomTask, id=pk)
    room_id = task.room.id

    if request.method == "POST":
        task.delete()
        return redirect("room", pk=room_id)
    
    return render(request, "rooms/delete_room_task.html", {"task": task})

def task(request, pk):
    task = get_object_or_404(RoomTask, id=pk) 
    
    context = {
        "task": task,
    }
    return render(request, "rooms/room_task.html", context)

