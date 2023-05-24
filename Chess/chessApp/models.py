from django.db import models

# Create your models here.
class Board(models.Model):
    content = models.CharField(max_length = 64, default=("RNBKQBNR" + "P" * 8 + " "*32 + "p" * 8 + "rnbkqbnr"))
    whites_turn = models.BooleanField(default = True)
    checkmate = models.BooleanField(default = False)

    def __str__(self) -> str:
        return self.content




