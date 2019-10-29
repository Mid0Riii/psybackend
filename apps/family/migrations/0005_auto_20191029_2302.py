# Generated by Django 2.2.5 on 2019-10-29 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0004_auto_20191026_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familyonduty',
            name='relate_family',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='family.FamilyBasic', verbose_name='学号'),
        ),
        migrations.AlterField(
            model_name='result',
            name='relate_family',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='family.FamilyBasic', verbose_name='学号'),
        ),
        migrations.AlterField(
            model_name='resultextra',
            name='relate_family',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='family.FamilyBasic', verbose_name='学号'),
        ),
        migrations.CreateModel(
            name='Total',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('family', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='family.FamilyBasic', verbose_name='学生')),
            ],
            options={
                'verbose_name': '心理学员招生信息总览',
                'verbose_name_plural': '心理学员招生信息总览',
            },
        ),
    ]