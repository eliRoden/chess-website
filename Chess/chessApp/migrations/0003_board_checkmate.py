# Generated by Django 4.2.1 on 2023-05-24 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chessApp', '0002_alter_board_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='checkmate',
            field=models.BooleanField(default=False),
        ),
    ]