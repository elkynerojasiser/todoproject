from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    done = models.BooleanField(default=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
