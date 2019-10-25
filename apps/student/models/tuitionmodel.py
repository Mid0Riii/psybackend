from django.db import models
from .studentmodel import StudentBasic
class Tuition(models.Model):
    class Meta:
        verbose_name = '心理学员交费信息'
        verbose_name_plural = verbose_name

    relate_student = models.OneToOneField(StudentBasic, on_delete=models.CASCADE, verbose_name='学号', primary_key=True)
    fee_train = models.CharField(max_length=128, verbose_name='培训费', blank=True, null=True)
    fee_material = models.CharField(max_length=128, verbose_name='资料费', blank=True, null=True)
    fee_exam = models.CharField(max_length=128, verbose_name='考试费', blank=True, null=True)
    fee_total = models.CharField(max_length=128, verbose_name='总费用', blank=True, null=True)
    fee_exam_extra = models.CharField(max_length=128, verbose_name='补考费', blank=True, null=True)
    fee_date = models.CharField(max_length=128,verbose_name='缴费日期', blank=True, null=True)
    fee_method = models.CharField(max_length=128, verbose_name='缴费方式', blank=True, null=True)
    fee_id = models.CharField(max_length=128, verbose_name='收据号', blank=True, null=True)
    fee_tax = models.CharField(max_length=128,verbose_name='发票号',blank=True,null=True)

    # TODO CODEREVICEW:模型的三种继承方式和自定义方法
    def get_stu_name(self):
        return self.relate_student.stu_name

    get_stu_name.short_description = u'姓名'
    get_stu_name.allow_tags = get_stu_name.is_column = True

    def get_stu_class(self):
        return self.relate_student.stu_class.class_name

    get_stu_class.short_description = u'班级'
    get_stu_class.allow_tags = get_stu_name.is_column = True

    def get_stu_num(self):
        return self.relate_student.stu_number

    get_stu_num.short_description = '学号'
    get_stu_num.allow_tags = get_stu_num.is_colume = True

    def __str__(self):
        return str(self.get_stu_name())
