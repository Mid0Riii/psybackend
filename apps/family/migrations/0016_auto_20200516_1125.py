# Generated by Django 2.2.5 on 2020-05-16 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0015_familyonduty_homework'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familybasic',
            name='fam_qq',
            field=models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='邮箱'),
        ),
    ]