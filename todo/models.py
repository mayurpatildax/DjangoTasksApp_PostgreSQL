from django.db import models
from django.utils import timezone

# Create your models here.
class Task(models.Model):
    id = models.AutoField(primary_key = True)
    title = models.CharField(max_length = 200)
    description = models.TextField()
    tag = models.CharField(max_length = 50)
    status = models.CharField(max_length = 50)
    created_date = models.DateTimeField(default = timezone.now)
    updated_date = models.DateTimeField(blank = True, null = True)

    def __str__(self):
        return self.title

