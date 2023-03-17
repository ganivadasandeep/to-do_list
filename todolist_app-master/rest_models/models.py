from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=50,default='Task')
    done = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Tasks'