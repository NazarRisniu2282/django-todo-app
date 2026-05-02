from django.contrib import admin
from .models import User, Task, Messages, Room
from django.contrib.auth.admin import UserAdmin

admin.site.register(User, UserAdmin)
admin.site.register(Task)
admin.site.register(Messages)
admin.site.register(Room)
