from django.db import models

# Create your models here.
class TaskList(models.Model):
    title = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.title

from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    tasklist = models.ForeignKey('TaskList', on_delete=models.CASCADE)  # Assuming a TaskList relation
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title