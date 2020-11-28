from django.db import models
from .classmodel import MarriageClass
from django.utils.html import format_html


class MarriageBasic(models.Model):
    class Meta:
        verbose_name = '婚姻指导招生信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.mar_number)

    def save(self, *args, **kwargs):
        # TODO CODEVIEW 重写保存方法需要创建外键约束时务必先保存当前对象
        super(MarriageBasic, self).save(*args, **kwargs)
        from .tuitionmodel import MarriageTuition
        from .textbookmodel import MarriageTextbook
        from .wechatmodel import MarriageWechat
        from .exammodel import MarriageExam
        from .certificationmodel import MarriageCertification
        from .ondutymodel import MarriageOnduty
        from .totalmodel import Total
        try:
            MarriageTuition.objects.get(relate_marriage=self)
            MarriageExam.objects.get(relate_marriage=self)
            MarriageWechat.objects.get(relate_marriage=self)
            MarriageTextbook.objects.get(relate_marriage=self)
            MarriageCertification.objects.get(relate_marriage=self)
            MarriageOnduty.objects.get(relate_marriage=self)
            Total.objects.get(marriage=self)
        except Exception as e:
            MarriageTuition.objects.create(relate_marriage=self, relate_class=self.mar_class)
            MarriageExam.objects.create(relate_marriage=self, relate_class=self.mar_class)
            MarriageWechat.objects.create(relate_marriage=self, relate_class=self.mar_class)
            MarriageTextbook.objects.create(relate_marriage=self, relate_class=self.mar_class)
            MarriageCertification.objects.create(relate_marriage=self, relate_class=self.mar_class)
            MarriageOnduty.objects.create(relate_marriage=self, relate_class=self.mar_class)
            Total.objects.create(marriage=self)
        # super(marriageBasic, self).save(*args, **kwargs)

    def get_verbose_name(self, field):
        return str(field)

    mar_type = models.CharField(max_length=128, verbose_name='学员类型', blank=True, null=True, default='空')
    mar_group = models.CharField(max_length=128, verbose_name='组别和职务', blank=True, null=True, default='空')
    mar_number = models.CharField(max_length=128, verbose_name='学号', unique=True)
    mar_name = models.CharField(max_length=128, verbose_name='姓名', blank=True, null=True, default='空')
    mar_gender = models.CharField(max_length=16, choices=(('男', '男'), ('女', '女')), verbose_name='性别', blank=True,
                                  null=True, default='空')
    mar_id_number = models.CharField(max_length=128, verbose_name='身份证号', default='空')
    mar_loc = models.CharField(max_length=128, verbose_name='所在地', blank=True, null=True, default='空')
    mar_deg = models.CharField(max_length=128, verbose_name='学历', blank=True, null=True, default='空')
    mar_major = models.CharField(max_length=128, verbose_name='专业', blank=True, null=True, default='空')
    mar_company = models.CharField(max_length=128, verbose_name='工作单位', blank=True, null=True, default='空')
    mar_duty = models.CharField(max_length=128, verbose_name='职务', blank=True, null=True, default='空')
    mar_status = models.CharField(max_length=128, verbose_name='职称', blank=True, null=True, default='空')
    # mar_profession = models.CharField(max_length=128, verbose_name='所属行业', blank=True, null=True)
    mar_origin = models.CharField(max_length=128, verbose_name='生源来源', blank=True, null=True, default='空')
    mar_cellphone = models.CharField(max_length=128, verbose_name='手机号', blank=True, null=True, default='空')
    mar_wechat = models.CharField(max_length=128, verbose_name='微信', blank=True, null=True, default='空')
    mar_email = models.CharField(max_length=128, verbose_name='邮箱', blank=True, null=True, default='空')
    mar_signup_date = models.CharField(max_length=128, verbose_name='报名日期', blank=True, null=True, default='空')
    mar_signup_people = models.CharField(max_length=128, verbose_name='具体招生人', blank=True, null=True, default='空')
    # mar_teacher_level = models.CharField(max_length=32,verbose_name='心师级别',blank=True,null=True,default='空')
    mar_other = models.TextField(verbose_name='备注', blank=True, null=True, default='空')
    mar_class = models.ForeignKey(MarriageClass, on_delete=models.CASCADE, verbose_name='班级')
    mar_class_num = models.CharField(max_length=128, verbose_name='班内序号', null=True, blank=True, default='空')

# TODO 为表格添加jquery-ui中的resizeable方法实现自由改变表格列宽
