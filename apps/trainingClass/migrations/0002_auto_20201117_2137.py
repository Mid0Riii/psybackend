# Generated by Django 2.2.5 on 2020-11-17 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainingClass', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='total',
            old_name='trainingclass',
            new_name='relate_trainingclass',
        ),
    ]
