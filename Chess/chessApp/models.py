from django.db import models

# Create your models here.
class Board(models.Model):
    content = models.CharField(max_length = 64, default=("RNBQKBNR" + "P" * 8 + " "*32 + "p" * 8 + "rnbqkbnr"))
    whites_turn = models.BooleanField(default = True)
    checkmate = models.BooleanField(default = False)

    left_white_rook_moved = models.BooleanField(default = False)
    right_white_rook_moved = models.BooleanField(default = False)
    white_king_moved = models.BooleanField(default = False)
    left_black_rook_moved = models.BooleanField(default = False)
    right_black_rook_moved = models.BooleanField(default = False)
    black_king_moved = models.BooleanField(default = False)

    def __str__(self) -> str:
        return self.content



