# Generated by Django 3.1.5 on 2021-02-11 22:52

from django.db import migrations, models
import django.db.models.deletion
import semifinals.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('se_forms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='ID')),
                ('upstream_id', models.IntegerField(blank=True, help_text="ID de l'ER sur le site Prologin", null=True)),
                ('display_name', models.CharField(help_text='Nom affiché de la session', max_length=100)),
                ('date_start', models.DateTimeField(verbose_name='Début')),
                ('date_end', models.DateTimeField(verbose_name='Fin')),
                ('status', models.IntegerField(choices=[(0, 'Not Published'), (1, 'Teased'), (2, 'Open'), (3, 'Submissions Closed')], verbose_name='Statut')),
                ('subject', models.FileField(blank=True, null=True, upload_to=semifinals.models.get_session_subject_path)),
                ('contestant_instructions', models.TextField(max_length=1000)),
                ('file_upload', models.BooleanField(verbose_name='Les participants doivent rendre un fichier')),
                ('subject_download_count', models.IntegerField(default=0, verbose_name='Nb. de téléchargements du sujet')),
                ('form_allow_review', models.BooleanField(verbose_name='Autoriser la relecture')),
                ('form', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='se_forms.forminstance')),
            ],
        ),
    ]
