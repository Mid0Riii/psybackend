from django.db import models
from .classmodel import TrainClass
from django.utils.html import format_html


class TrainBasic(models.Model):
    class Meta:
        verbose_name = '训练班招生信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.tra_number)

    def save(self, *args, **kwargs):
        super(TrainBasic, self).save(*args, **kwargs)
        from .tuitionmodel import TrainTuition
        from .textbookmodel import TrainTextbook
        from .wechatmodel import TrainWechat
        from .resultmodel import Result
        from .resultextramodel import ResultExtra
        from .certificationmodel import TrainCertification
        from .ondutymodel import TrainOnduty
        from .totalmodel import Total
        try:
            TrainTuition.objects.get(relate_trainingclass=self)
            Result.objects.get(relate_trainingclass=self)
            TrainWechat.objects.get(relate_trainingclass=self)
            ResultExtra.objects.get(relate_trainingclass=self)
            TrainTextbook.objects.get(relate_trainingclass=self)
            TrainCertification.objects.get(relate_trainingclass=self)
            TrainOnduty.objects.get(relate_trainingclass=self)
            Total.objects.get(trainingclass=self)
        except Exception as e:
            TrainTuition.objects.create(relate_trainingclass=self, relate_class=self.tra_class)
            Result.objects.create(relate_trainingclass=self, relate_class=self.tra_class)
            TrainWechat.objects.create(relate_trainingclass=self, relate_class=self.tra_class)
            ResultExtra.objects.create(relate_trainingclass=self, relate_class=self.tra_class)
            TrainTextbook.objects.create(relate_trainingclass=self, relate_class=self.tra_class)
            TrainCertification.objects.create(relate_trainingclass=self, relate_class=self.tra_class)
            TrainOnduty.objects.create(relate_trainingclass=self, relate_class=self.tra_class)
            Total.objects.create(trainingclass=self)
        # super(trainingclassBasic, self).save(*args, **kwargs)

    def get_verbose_name(self, field):
        return str(field)

    tra_type = models.CharField(max_length=128, verbose_name='学员类型', blank=True, null=True, default='空')
    tra_number = models.CharField(max_length=128, verbose_name='学号', unique=True)
    tra_group = models.CharField(max_length=128, verbose_name='组名与职务', blank=True, null=True, default='空')
    tra_name = models.CharField(max_length=128, verbose_name='姓名', blank=True, null=True, default='空')
    tra_gender = models.CharField(max_length=16, choices=(('男', '男'), ('女', '女')), verbose_name='性别', blank=True,
                                  null=True, default='空')
    tra_id_number = models.CharField(max_length=128, verbose_name='身份证号', default='空')
    tra_loc = models.CharField(max_length=128, verbose_name='所在地', blank=True, null=True, default='空')
    tra_deg = models.CharField(max_length=128, verbose_name='学历', blank=True, null=True, default='空')
    tra_major = models.CharField(max_length=128, verbose_name='专业', blank=True, null=True, default='空')
    tra_company = models.CharField(max_length=128, verbose_name='工作单位', blank=True, null=True, default='空')
    tra_duty = models.CharField(max_length=128, verbose_name='职务', blank=True, null=True, default='空')
    tra_status = models.CharField(max_length=128, verbose_name='职称', blank=True, null=True, default='空')
    # tra_profession = models.CharField(max_length=128, verbose_name='所属行业', blank=True, null=True)
    tra_origin = models.CharField(max_length=128, verbose_name='生源来源', blank=True, null=True, default='空')
    tra_cellphone = models.CharField(max_length=128, verbose_name='手机号', blank=True, null=True, default='空')
    tra_wechat = models.CharField(max_length=128, verbose_name='微信', blank=True, null=True, default='空')
    tra_qq = models.CharField(max_length=128, verbose_name='邮箱', blank=True, null=True, default='空')
    tra_signup_date = models.CharField(max_length=128, verbose_name='报名日期', blank=True, null=True, default='空')
    tra_signup_people = models.CharField(max_length=128, verbose_name='具体招生人', blank=True, null=True, default='空')
    tra_teacher_level = models.CharField(max_length=32, verbose_name='心师级别', blank=True, null=True, default='空')
    tra_other = models.TextField(verbose_name='备注', blank=True, null=True, default='空')
    tra_class = models.ForeignKey(TrainClass, on_delete=models.CASCADE, verbose_name='班级')
    tra_class_num = models.CharField(max_length=128, verbose_name='班内序号', null=True, blank=True, default='空')
