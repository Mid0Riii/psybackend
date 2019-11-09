from django.db import models
from .classmodel import StudentClass


class StudentBasic(models.Model):
    class Meta:
        verbose_name = '心理学员招生信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.stu_number)

    def save(self, *args, **kwargs):
        # TODO CODEVIEW 重写保存方法需要创建外键约束时务必先保存当前对象
        super(StudentBasic, self).save(*args, **kwargs)
        from .tuitionmodel import Tuition
        from .textbookmodel import StudentTextbook
        from .wechatmodel import StudentWechat
        from .exammodel import StudentExam
        from .examextramodel import StudentExamExtra
        from .totalmodel import Total
        from .certificationmodel import StudentCertification
        from .ondutymodel import Onduty
        try:
            Tuition.objects.get(relate_student=self)
            StudentExam.objects.get(relate_student=self)
            StudentWechat.objects.get(relate_student=self)
            StudentExamExtra.objects.get(relate_student=self)
            StudentTextbook.objects.get(relate_student=self)
            StudentCertification.objects.get(relate_student=self)
            Onduty.objects.get(relate_student=self)
            Total.objects.get(student=self)
        except Exception as e:
            Tuition.objects.create(relate_student=self,relate_class=self.stu_class)
            StudentExam.objects.create(relate_student=self,relate_class=self.stu_class)
            StudentWechat.objects.create(relate_student=self,relate_class=self.stu_class)
            StudentExamExtra.objects.create(relate_student=self,relate_class=self.stu_class)
            StudentTextbook.objects.create(relate_student=self,relate_class=self.stu_class)
            StudentCertification.objects.create(relate_student=self,relate_class=self.stu_class)
            Total.objects.create(student=self)
            Onduty.objects.create(relate_student=self,relate_class=self.stu_class)
        # super(StudentBasic, self).save(*args, **kwargs)

    def get_verbose_name(self, field):
        return str(field)

    stu_number = models.CharField(max_length=128, verbose_name='学号', unique=True)
    stu_name = models.CharField(max_length=128, verbose_name='姓名', blank=True, null=True, default='空')
    stu_gender = models.CharField(max_length=16, choices=(('男', '男'), ('女', '女')), verbose_name='性别', blank=True,
                                  null=True, default='空')
    stu_level = models.CharField(max_length=16, choices=(('二级', '二级'), ('三级', '三级'),('三升二','三升二')), verbose_name='级别', null=True,
                                 blank=True, default='空')
    stu_id_number = models.CharField(max_length=128, verbose_name='身份证号', unique=True, default='空')
    stu_loc = models.CharField(max_length=128, verbose_name='所在地', blank=True, null=True, default='空')
    stu_deg = models.CharField(max_length=128, verbose_name='学历', blank=True, null=True, default='空')
    stu_major = models.CharField(max_length=128, verbose_name='专业', blank=True, null=True, default='空')
    stu_company = models.CharField(max_length=128, verbose_name='工作单位', blank=True, null=True, default='空')
    stu_duty = models.CharField(max_length=128, verbose_name='职务', blank=True, null=True, default='空')
    stu_status = models.CharField(max_length=128, verbose_name='职称', blank=True, null=True, default='空')
    # stu_profession = models.CharField(max_length=128, verbose_name='所属行业', blank=True, null=True)
    stu_origin = models.CharField(max_length=128, verbose_name='生源来源', blank=True, null=True, default='空')
    stu_cellphone = models.CharField(max_length=128, verbose_name='手机号', blank=True, null=True, default='空')
    stu_wechat = models.CharField(max_length=128, verbose_name='微信', blank=True, null=True, default='空')
    stu_qq = models.CharField(max_length=128, verbose_name='QQ', blank=True, null=True, default='空')
    stu_signup_date = models.CharField(max_length=128, verbose_name='报名日期', blank=True, null=True, default='空')
    stu_signup_people = models.CharField(max_length=128, verbose_name='具体招生人', blank=True, null=True, default='空')
    stu_other = models.TextField(verbose_name='备注', blank=True, null=True, default='空')
    stu_class = models.ForeignKey(StudentClass, on_delete=models.CASCADE, verbose_name='班级')
    stu_class_num = models.CharField(max_length=128, verbose_name='班内序号', null=True, blank=True, default='空')

# TODO 筛选非空 增加班级内部序号
# TODO 为表格添加jquery-ui中的resizeable方法实现自由改变表格列宽
