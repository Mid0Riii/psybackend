from django.db import models
from .studentmodel import StudentBasic
from .classmodel import StudentClass
from django.utils.html import format_html

class StudentExam(models.Model):
    class Meta:
        verbose_name = '心理学员考试信息'
        verbose_name_plural = verbose_name

    relate_class = models.ForeignKey(StudentClass, on_delete=models.CASCADE, verbose_name='班级',null=True,blank=True)
    relate_student = models.OneToOneField(StudentBasic, on_delete=models.CASCADE, verbose_name='学号', primary_key=True)
    # relate_student = models.ForeignKey(StudentBasic, on_delete=models.DO_NOTHING, verbose_name='学号')
    exam_date = models.CharField(max_length=128, verbose_name='参试时间', null=True, blank=True, default='空')
    exam_theory = models.CharField(max_length=128, verbose_name='国考理论报考', blank=True, null=True, default='空')
    exam_theory_result = models.CharField(max_length=128, verbose_name='国考理论总分', blank=True, null=True, default='空')
    exam_practise = models.CharField(max_length=128, verbose_name='国考实操报考', blank=True, null=True, default='空')
    exam_practise_result = models.CharField(max_length=128, verbose_name='国考实操总分', blank=True, null=True, default='空')
    exam_practise_result2 = models.CharField(max_length=128,verbose_name='实操笔试分',blank=True,null=True,default='空')
    exam_pre = models.CharField(max_length=128,verbose_name='说课分',blank=True,null=True,default='空')
    exam_speech = models.CharField(max_length=128,verbose_name='宣讲分',blank=True,null=True,default='空')
    exam_thr_theory = models.CharField(max_length=128,verbose_name='协会三级理论',blank=True,null=True,default='空')
    exam_thr_skill = models.CharField(max_length=128,verbose_name='协会三级技能',blank=True,null=True,default='空')
    exam_sec_theory = models.CharField(max_length=128,verbose_name='协会二级理论',blank=True,null=True,default='空')
    exam_sec_skill = models.CharField(max_length=128,verbose_name='协会二级技能',blank=True,null=True,default='空')
    exam_thesis = models.CharField(max_length=128,verbose_name='协会论文答辩',blank=True,null=True,default='空')
    exam_CAS = models.CharField(max_length=128,verbose_name='中科院成绩',blank=True,null=True,default='空')
    exam_total = models.CharField(max_length=128, verbose_name='综合报考', blank=True, null=True, default='空')
    exam_total_result = models.CharField(max_length=128, verbose_name='综合成绩', blank=True, null=True, default='空')
    exam_status = models.CharField(max_length=128, verbose_name='合格情况', choices=(('合格', '合格'), ('不合格', '不合格')),
                                   blank=True, null=True, default='空')
    exam_other = models.TextField(verbose_name='备注',blank=True,null=True,default='空')
    def get_stu_name(self):
        info = self.relate_student.stu_name
        if self.relate_student.tuition.fee_date == '空':
            color_code = 'red'
        else:
            color_code = 'black'
        return format_html('<span style="color:{};">{}</span>', color_code, info)

    get_stu_name.short_description = u'姓名'
    get_stu_name.allow_tags = get_stu_name.is_column = True

    def get_stu_num(self):
        return self.relate_student.stu_number

    get_stu_num.short_description = '学号'
    get_stu_num.allow_tags = get_stu_num.is_column = True

    def get_stu_class(self):
        return self.relate_student.stu_class.class_name

    get_stu_class.short_description = u'班级'
    get_stu_class.allow_tags = get_stu_class.is_column = True

    def get_stu_id_number(self):
        return self.relate_student.stu_id_number

    get_stu_id_number.short_description = u'身份证号'
    get_stu_id_number.allow_tags = get_stu_id_number.is_column = True

    def __str__(self):
        return str(self.relate_student.stu_name)
