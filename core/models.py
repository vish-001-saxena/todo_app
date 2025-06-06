from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    scheduled_date = models.DateField(null=True, blank=True)
    completed = models.BooleanField(default=False)


    def __str__(self):
        return self.title
