# Generated by Django 3.1.5 on 2021-02-11 22:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import written_exams.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('semifinals', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_updated', models.DateTimeField(blank=True, null=True)),
                ('file', models.FileField(upload_to=written_exams.models.get_path)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='semifinals.session')),
                ('user', models.ForeignKey(limit_choices_to={'is_staff': False}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Utilisateur')),
            ],
            options={
                'unique_together': {('user', 'session')},
            },
        ),
    ]
