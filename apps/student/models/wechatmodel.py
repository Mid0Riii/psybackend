from django.db import models
from .studentmodel import StudentBasic
class StudentWechat(models.Model):
    class Meta:
        verbose_name = '心理学员365开通情况'
        verbose_name_plural = verbose_name

    relate_student = models.OneToOneField(StudentBasic, on_delete=models.CASCADE, verbose_name='学号', primary_key=True)
    wechat_number = models.CharField(max_length=128, verbose_name='平台绑定号码', blank=True, null=True,default='空')
    wechat_nickname = models.CharField(max_length=128, verbose_name='微信昵称', blank=True, null=True,default='空')
    wechat_date = models.CharField(max_length=128,verbose_name='开通日期', blank=True, null=True,default='空')

    def get_stu_name(self):
        return self.relate_student.stu_name

    get_stu_name.short_description = u'姓名'
    get_stu_name.allow_tags = get_stu_name.is_column = True

    def get_stu_num(self):
        return self.relate_student.stu_number

    get_stu_num.short_description = '学号'
    get_stu_num.allow_tags = get_stu_num.is_colume = True

    def get_stu_class(self):
        return self.relate_student.stu_class.class_name

    get_stu_class.short_description = u'班级'
    get_stu_class.allow_tags = get_stu_name.is_column = True

    def __str__(self):
        return str(self.get_stu_name())
