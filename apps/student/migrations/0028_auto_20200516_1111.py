# Generated by Django 2.2.5 on 2020-05-16 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0027_auto_20200514_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onduty',
            name='onduty',
            field=models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='出勤率'),
        ),
        migrations.AlterField(
            model_name='studentexam',
            name='exam_practise_result',
            field=models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='国考实操总分'),
        ),
        migrations.AlterField(
            model_name='studentexam',
            name='exam_theory_result',
            field=models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='国考理论总分'),
        ),
        migrations.AlterField(
            model_name='studentwechat',
            name='wechat_date2',
            field=models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='开通日期'),
        ),
        migrations.AlterField(
            model_name='tuition',
            name='fee_material',
            field=models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='教材费'),
        ),
    ]