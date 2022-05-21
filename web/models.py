from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Expense(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    amount = models.BigIntegerField()
    user = models.ForeignKey(User , on_delete=models.CASCADE)

    def __str__(self):
        return self.text

class Income(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    amount = models.BigIntegerField()
    user = models.ForeignKey(User , on_delete=models.CASCADE)

    def __str__(self):
        return self.text