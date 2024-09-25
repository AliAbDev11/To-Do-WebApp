from django import forms
from .models import *

class TaskListForm(forms.ModelForm):
    
    class Meta:
        model = TaskList
        fields = ['title']
    
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if TaskList.objects.filter(title=title).exists():
            raise forms.ValidationError("Task List with this title already exists.")
        return title

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'completed']  # Specify the fields to include in the form
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Task Title'}),
            'completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }