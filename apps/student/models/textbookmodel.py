from django.db import models
from .studentmodel import StudentBasic
class StudentTextbook(models.Model):
    class Meta:
        verbose_name = '心理学员教材'
        verbose_name_plural = verbose_name

    relate_student = models.OneToOneField(StudentBasic, on_delete=models.CASCADE, verbose_name='学号', primary_key=True)
    # relate_student = models.ForeignKey(StudentBasic, on_delete=models.DO_NOTHING, verbose_name='学号')
    text_basic = models.CharField(max_length=128, verbose_name='基础技能', blank=True, null=True)
    text_sec = models.CharField(max_length=128, verbose_name='二级技能', blank=True, null=True)
    text_sec_exer = models.CharField(max_length=128, verbose_name='二级习题', blank=True, null=True)
    text_sec_measure = models.CharField(max_length=128, verbose_name='二级量表', blank=True, null=True)
    text_thr = models.CharField(max_length=128, verbose_name='三级技能', blank=True, null=True)
    text_thr_exer = models.CharField(max_length=128, verbose_name='三级习题', blank=True, null=True)
    text_manual = models.CharField(max_length=128, verbose_name='学员手册', blank=True, null=True)
    text_exam = models.CharField(max_length=128, verbose_name='模拟试卷', blank=True, null=True)
    text_other = models.TextField(verbose_name='备注',blank=True,null=True)

    def __str__(self):
        return str(self.get_stu_name())

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