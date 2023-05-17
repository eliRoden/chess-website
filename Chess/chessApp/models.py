from django.db import models

# Create your models here.
class Board(models.Model):
    content = models.CharField(max_length = 64)
    whites_turn = models.BooleanField(default = True)

