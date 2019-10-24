from django.db import models
from .studentmodel import StudentBasic

class StudentCertification(models.Model):
    class Meta:
        verbose_name = '学员证书'
        verbose_name_plural = verbose_name

    relate_student = models.OneToOneField(StudentBasic, on_delete=models.CASCADE, verbose_name='学号', primary_key=True)
    # relate_student = models.ForeignKey(StudentBasic, on_delete=models.DO_NOTHING, verbose_name='学号')
    cert_id = models.CharField(max_length=128, verbose_name='证书编号', blank=True, null=True)
    cert_date = models.CharField(max_length=128,verbose_name='发证日期', blank=True, null=True)
    cert_draw_people = models.CharField(max_length=128, verbose_name='领取人', blank=True, null=True)
    cert_draw_date = models.CharField(max_length=128,verbose_name="领取时间", blank=True, null=True)

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
