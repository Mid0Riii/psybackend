# Generated by Django 2.2.5 on 2020-05-15 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0015_familyonduty_homework'),
        ('teacher', '0005_auto_20191109_0938'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamTeacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_name', models.CharField(max_length=128, verbose_name='上课教师')),
                ('teacher_info', models.CharField(max_length=256, verbose_name='上课内容')),
                ('teacher_date', models.CharField(max_length=128, verbose_name='上课时间')),
                ('teacher_fare', models.CharField(max_length=128, verbose_name='课时费用')),
                ('teacher_paid', models.CharField(choices=[('是', '是'), ('否', '否')], max_length=16, verbose_name='课时费是否已支付')),
                ('teacher_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='family.FamilyClass', verbose_name='教师上课班级')),
            ],
            options={
                'verbose_name': '团体教师授课信息',
                'verbose_name_plural': '团体教师授课信息',
            },
        ),
        migrations.CreateModel(
            name='SandboxTeacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_name', models.CharField(max_length=128, verbose_name='上课教师')),
                ('teacher_info', models.CharField(max_length=256, verbose_name='上课内容')),
                ('teacher_date', models.CharField(max_length=128, verbose_name='上课时间')),
                ('teacher_fare', models.CharField(max_length=128, verbose_name='课时费用')),
                ('teacher_paid', models.CharField(choices=[('是', '是'), ('否', '否')], max_length=16, verbose_name='课时费是否已支付')),
                ('teacher_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='family.FamilyClass', verbose_name='教师上课班级')),
            ],
            options={
                'verbose_name': '沙盒教师授课信息',
                'verbose_name_plural': '沙盒教师授课信息',
            },
        ),
        migrations.CreateModel(
            name='MarriageTeacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_name', models.CharField(max_length=128, verbose_name='上课教师')),
                ('teacher_info', models.CharField(max_length=256, verbose_name='上课内容')),
                ('teacher_date', models.CharField(max_length=128, verbose_name='上课时间')),
                ('teacher_fare', models.CharField(max_length=128, verbose_name='课时费用')),
                ('teacher_paid', models.CharField(choices=[('是', '是'), ('否', '否')], max_length=16, verbose_name='课时费是否已支付')),
                ('teacher_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='family.FamilyClass', verbose_name='教师上课班级')),
            ],
            options={
                'verbose_name': '婚姻教师授课信息',
                'verbose_name_plural': '婚姻教师授课信息',
            },
        ),
    ]
