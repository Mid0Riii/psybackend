from django.db import models
from .studentmodel import StudentBasic
class Onduty(models.Model):
    class Meta:
        verbose_name = '心理学员考勤信息'
        verbose_name_plural = verbose_name

    relate_student = models.OneToOneField(StudentBasic,on_delete=models.CASCADE,verbose_name='学号',blank=True,null=True)
    onduty = models.CharField(max_length=128, verbose_name='出勤', blank=True, null=True)
    homework = models.CharField(max_length=128, verbose_name='作业打卡', blank=True, null=True)
    other = models.TextField(verbose_name="备注", null=True, blank=True)
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