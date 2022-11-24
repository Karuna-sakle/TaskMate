from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    manage = models.ForeignKey(User,on_delete=models.CASCADE ,default=True)
    task = models.CharField(max_length=500)
    done = models.BooleanField(default= False)

    def __str__(self):
        return self.task+"_"+str(self.done)