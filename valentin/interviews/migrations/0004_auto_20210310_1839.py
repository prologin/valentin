# Generated by Django 3.1.5 on 2021-03-10 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interviews', '0003_auto_20210308_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interviewscore',
            name='comments',
            field=models.TextField(max_length=4000, verbose_name="Commentaires sur l'entretien"),
        ),
    ]
