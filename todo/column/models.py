from django.db import models


class Column(models.Model):
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=20)

    class Meta:
        db_table = 'Column'