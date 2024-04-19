from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    priority = models.IntegerField()
    column = models.ForeignKey(to='column.Column', on_delete=models.CASCADE)

    class Meta:
        db_table = 'Task'