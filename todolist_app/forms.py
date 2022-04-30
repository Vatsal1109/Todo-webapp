from django import forms
from .models import TaskList

class TaskForm(forms.ModelForm):
   class Meta:
       model=TaskList #instance
       fields=['task','done'] 