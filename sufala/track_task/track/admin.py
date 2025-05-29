from django.contrib import admin
from .models import Task, TaskActivityLog

# Register your models here.


admin.site.register(Task)
admin.site.register(TaskActivityLog)

