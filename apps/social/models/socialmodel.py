from django.db import models
from .classmodel import SocialClass
from django.utils.html import format_html


class SocialBasic(models.Model):
    class Meta:
        verbose_name = '社会工作师招生信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.social_number)

    def save(self, *args, **kwargs):
        # TODO CODEVIEW 重写保存方法需要创建外键约束时务必先保存当前对象
        super(SocialBasic, self).save(*args, **kwargs)
        from .tuitionmodel import SocialTuition
        from .textbookmodel import SocialTextbook
        from .wechatmodel import SocialWechat
        from .exammodel import SocialExam
        from .certificationmodel import SocialCertification
        from .ondutymodel import SocialOnduty
        from .totalmodel import Total
        try:
            SocialTuition.objects.get(relate_social=self)
            SocialExam.objects.get(relate_social=self)
            SocialWechat.objects.get(relate_social=self)
            SocialTextbook.objects.get(relate_social=self)
            SocialCertification.objects.get(relate_social=self)
            SocialOnduty.objects.get(relate_social=self)
            Total.objects.get(social=self)
        except Exception as e:
            SocialTuition.objects.create(relate_social=self, relate_class=self.social_class)
            SocialExam.objects.create(relate_social=self, relate_class=self.social_class)
            SocialWechat.objects.create(relate_social=self, relate_class=self.social_class)
            SocialTextbook.objects.create(relate_social=self, relate_class=self.social_class)
            SocialCertification.objects.create(relate_social=self, relate_class=self.social_class)
            SocialOnduty.objects.create(relate_social=self, relate_class=self.social_class)
            Total.objects.create(social=self)
        # super(socialBasic, self).save(*args, **kwargs)

    def get_verbose_name(self, field):
        return str(field)

    social_type = models.CharField(max_length=128, verbose_name='学员类型', blank=True, null=True, default='空')
    social_group = models.CharField(max_length=128, verbose_name='组别和职务', blank=True, null=True, default='空')
    social_number = models.CharField(max_length=128, verbose_name='学号', unique=True)
    social_name = models.CharField(max_length=128, verbose_name='姓名', blank=True, null=True, default='空')
    social_gender = models.CharField(max_length=16, choices=(('男', '男'), ('女', '女')), verbose_name='性别', blank=True,
                                     null=True, default='空')
    social_id_number = models.CharField(max_length=128, verbose_name='身份证号', default='空')
    social_loc = models.CharField(max_length=128, verbose_name='所在地', blank=True, null=True, default='空')
    social_deg = models.CharField(max_length=128, verbose_name='学历', blank=True, null=True, default='空')
    social_major = models.CharField(max_length=128, verbose_name='专业', blank=True, null=True, default='空')
    social_company = models.CharField(max_length=128, verbose_name='工作单位', blank=True, null=True, default='空')
    social_duty = models.CharField(max_length=128, verbose_name='职务', blank=True, null=True, default='空')
    social_status = models.CharField(max_length=128, verbose_name='职称', blank=True, null=True, default='空')
    social_origin = models.CharField(max_length=128, verbose_name='生源来源', blank=True, null=True, default='空')
    social_cellphone = models.CharField(max_length=128, verbose_name='手机号', blank=True, null=True, default='空')
    social_wechat = models.CharField(max_length=128, verbose_name='微信', blank=True, null=True, default='空')
    social_email = models.CharField(max_length=128, verbose_name='邮箱', blank=True, null=True, default='空')
    social_signup_date = models.CharField(max_length=128, verbose_name='报名日期', blank=True, null=True, default='空')
    social_signup_people = models.CharField(max_length=128, verbose_name='具体招生人', blank=True, null=True, default='空')
    social_other = models.TextField(verbose_name='备注', blank=True, null=True, default='空')
    social_class = models.ForeignKey(SocialClass, on_delete=models.CASCADE, verbose_name='班级')
    social_class_num = models.CharField(max_length=128, verbose_name='班内序号', null=True, blank=True, default='空')
