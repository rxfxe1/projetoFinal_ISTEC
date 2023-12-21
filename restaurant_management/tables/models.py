from django.db import models

class Table(models.Model):
    number = models.IntegerField(unique=True)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return f"Table {self.number} - Capacity: {self.capacity}"
