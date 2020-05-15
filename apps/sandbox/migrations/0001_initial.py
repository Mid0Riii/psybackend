# Generated by Django 2.2.5 on 2020-05-11 05:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SandboxBasic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('san_type', models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='学员类型')),
                ('san_group', models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='组别和职务')),
                ('san_number', models.CharField(max_length=128, unique=True, verbose_name='学号')),
                ('san_name', models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='姓名')),
                ('san_gender', models.CharField(blank=True, choices=[('男', '男'), ('女', '女')], default='空', max_length=16, null=True, verbose_name='性别')),
                ('san_id_number', models.CharField(default='空', max_length=128, verbose_name='身份证号')),
                ('san_loc', models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='所在地')),
                ('san_deg', models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='学历')),
                ('san_major', models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='专业')),
                ('san_company', models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='工作单位')),
                ('san_duty', models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='职务')),
                ('san_status', models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='职称')),
                ('san_origin', models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='生源来源')),
                ('san_cellphone', models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='手机号')),
                ('san_wechat', models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='微信')),
                ('san_email', models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='邮箱')),
                ('san_signup_date', models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='报名日期')),
                ('san_signup_people', models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='具体招生人')),
                ('san_other', models.TextField(blank=True, default='空', null=True, verbose_name='备注')),
                ('san_class_num', models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='班内序号')),
            ],
            options={
                'verbose_name': '沙盘分析指导招生信息',
                'verbose_name_plural': '沙盘分析指导招生信息',
            },
        ),
        migrations.CreateModel(
            name='SandboxClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=64, verbose_name='班级名')),
                ('class_index', models.IntegerField(blank=True, null=True, verbose_name='班级序号')),
                ('class_id_example', models.CharField(blank=True, max_length=128, null=True, verbose_name='学号命名')),
                ('class_recruit_teacher', models.CharField(blank=True, default='空', max_length=64, null=True, verbose_name='招生老师')),
                ('class_teacher', models.CharField(blank=True, default='空', max_length=64, null=True, verbose_name='跟班老师')),
                ('class_date', models.CharField(blank=True, default='空', max_length=64, null=True, verbose_name='开班年份')),
            ],
            options={
                'verbose_name': '沙盘分析指导班级',
                'verbose_name_plural': '沙盘分析指导班级',
            },
        ),
        migrations.CreateModel(
            name='Total',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sandbox', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sandbox.SandboxBasic', verbose_name='学生')),
            ],
            options={
                'verbose_name': '沙盘分析指导信息总览',
                'verbose_name_plural': '沙盘分析指导信息总览',
            },
        ),
        migrations.CreateModel(
            name='SandboxOnduty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('onduty', models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='出勤')),
                ('homework', models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='作业打卡')),
                ('other', models.TextField(blank=True, default='空', null=True, verbose_name='备注')),
                ('relate_class', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sandbox.SandboxClass', verbose_name='班级')),
                ('relate_sandbox', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sandbox.SandboxBasic', verbose_name='学号')),
            ],
            options={
                'verbose_name': '沙盘分析指导考勤信息',
                'verbose_name_plural': '沙盘分析指导考勤信息',
            },
        ),
        migrations.CreateModel(
            name='SandboxExam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch', models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='考试批次')),
                ('exam_total', models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='总分')),
                ('exam_nation', models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='国考笔试成绩')),
                ('exam_practice', models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='实操考核成绩')),
                ('other', models.TextField(blank=True, default='空', null=True, verbose_name='备注')),
                ('relate_class', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sandbox.SandboxClass', verbose_name='班级')),
                ('relate_sandbox', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sandbox.SandboxBasic', verbose_name='学号')),
            ],
            options={
                'verbose_name': '沙盘分析指导考核成绩',
                'verbose_name_plural': '沙盘分析指导考核成绩',
            },
        ),
        migrations.AddField(
            model_name='sandboxbasic',
            name='san_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sandbox.SandboxClass', verbose_name='班级'),
        ),
        migrations.CreateModel(
            name='SandboxWechat',
            fields=[
                ('relate_sandbox', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='sandbox.SandboxBasic', verbose_name='学号')),
                ('wechat_number', models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='平台绑定号码')),
                ('wechat_nickname', models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='微信昵称')),
                ('wechat_date', models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='开通日期')),
                ('wechat_other', models.TextField(blank=True, default='空', null=True, verbose_name='备注')),
                ('relate_class', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sandbox.SandboxClass', verbose_name='班级')),
            ],
            options={
                'verbose_name': '沙盘分析指导365开通情况',
                'verbose_name_plural': '沙盘分析指导365开通情况',
            },
        ),
        migrations.CreateModel(
            name='SandboxTuition',
            fields=[
                ('relate_sandbox', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='sandbox.SandboxBasic', verbose_name='学号')),
                ('fee_train', models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='培训费')),
                ('fee_material', models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='教材费')),
                ('fee_exam', models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='考试费')),
                ('fee_total', models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='总费用')),
                ('fee_date', models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='缴费日期')),
                ('fee_method', models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='缴费方式')),
                ('fee_tax', models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='发票号')),
                ('fee_invoice_header', models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='发票抬头')),
                ('fee_invoice_id', models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='发票机构代码')),
                ('fee_invoice_date', models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='发票开票日期')),
                ('fee_other', models.TextField(blank=True, default='空', null=True, verbose_name='备注')),
                ('relate_class', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sandbox.SandboxClass', verbose_name='班级')),
            ],
            options={
                'verbose_name': '沙盘分析指导交费信息',
                'verbose_name_plural': '沙盘分析指导交费信息',
            },
        ),
        migrations.CreateModel(
            name='SandboxTextbook',
            fields=[
                ('relate_sandbox', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='sandbox.SandboxBasic', verbose_name='学号')),
                ('text_basic', models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='基础技能知识')),
                ('text_skill', models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='技能教材')),
                ('text_workbook', models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='习题集')),
                ('text_train', models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='培训指南')),
                ('text_manual', models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='学员手册')),
                ('text_other', models.TextField(blank=True, default='空', null=True, verbose_name='备注')),
                ('relate_class', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sandbox.SandboxClass', verbose_name='班级')),
            ],
            options={
                'verbose_name': '沙盘分析分析指导教材',
                'verbose_name_plural': '沙盘分析分析指导教材',
            },
        ),
        migrations.CreateModel(
            name='SandboxCertification',
            fields=[
                ('relate_sandbox', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='sandbox.SandboxBasic', verbose_name='学号')),
                ('ass_cert_id', models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='协会证书编号')),
                ('ass_cert_date', models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='协会证书发证日期')),
                ('ass_cert_draw_people', models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='协会证书领取人')),
                ('ass_cert_draw_date', models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='协会证书领取时间')),
                ('nation_cert_id', models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='国证证书编号')),
                ('nation_cert_date', models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='国征证书发证日期')),
                ('nation_cert_draw_people', models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='国证证书领取人')),
                ('nation_cert_draw_date', models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='国证证书领取时间')),
                ('other', models.TextField(blank=True, default='空', null=True, verbose_name='备注')),
                ('relate_class', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sandbox.SandboxClass', verbose_name='班级')),
            ],
            options={
                'verbose_name': '沙盘分析指导证书',
                'verbose_name_plural': '沙盘分析指导证书',
            },
        ),
    ]