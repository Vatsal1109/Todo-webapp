from django.contrib import admin
from .models import TaskList

class TaskAdmin(admin.ModelAdmin):
    list_display=['task','manager','done']
# Register your models here.
admin.site.register(TaskList,TaskAdmin)