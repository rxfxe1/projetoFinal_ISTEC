from django.db import models
from django.conf import settings
from tables.models import Table

class Reservation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    num_people = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.user.username} - {self.date} {self.time}"
