# Generated by Django 4.2.1 on 2023-05-26 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chessApp', '0003_board_checkmate'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='black_king_moved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='board',
            name='left_black_rook_moved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='board',
            name='left_white_rook_moved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='board',
            name='right_black_rook_moved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='board',
            name='right_white_rook_moved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='board',
            name='white_king_moved',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='board',
            name='content',
            field=models.CharField(default='RNBQKBNRPPPPPPPP                                pppppppprnbqkbnr', max_length=64),
        ),
    ]
