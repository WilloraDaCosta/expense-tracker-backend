from django.db import models

class Expense(models.Model):
    name = models.CharField(max_length=200)
    amount = models.FloatField()
    date = models.DateField()
    category = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.amount}"
