# Generated by Django 2.2.5 on 2019-12-02 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0023_auto_20191125_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentbasic',
            name='stu_level',
            field=models.CharField(blank=True, choices=[('二级', '二级'), ('三级', '三级'), ('三升二', '三升二'), ('中科院', '中科院'), ('心理辅导师', '心理辅导师')], default='空', max_length=16, null=True, verbose_name='级别'),
        ),
    ]
