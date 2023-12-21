from django.db import models
from django.contrib.auth.models import User
from tables.models import Table

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    items = models.TextField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - Table {self.table.number} - Total: ${self.total_amount}"
