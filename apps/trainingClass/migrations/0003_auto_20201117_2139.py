# Generated by Django 2.2.5 on 2020-11-17 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainingClass', '0002_auto_20201117_2137'),
    ]

    operations = [
        migrations.RenameField(
            model_name='total',
            old_name='relate_trainingclass',
            new_name='trainingclass',
        ),
    ]
