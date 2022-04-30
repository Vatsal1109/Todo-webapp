from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('todolist',views.todolist,name='todolist'),
    path('contact',views.contact,name='contact'),
    path('delete/<int:task_id>',views.delete_task,name='delete_task'),
    path('edit/<int:task_id>',views.edit_task,name='edit_task'),
    path('complete/<int:task_id>',views.complete_task,name='complete'),
    path('pending/<int:task_id>',views.pending_task,name='pending'),
]
