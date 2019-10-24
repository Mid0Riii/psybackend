from django.db import models
from student.models import StudentClass

# Create your models here.

class Teacher(models.Model):
    teacher_name = models.CharField(max_length=128, verbose_name='上课教师')
    teacher_info = models.CharField(max_length=256, verbose_name='上课内容')
    teacher_date = models.DateField(verbose_name='上课时间')
    teacher_fare = models.CharField(max_length=128, verbose_name='课时费用')
    teacher_paid = models.CharField(max_length=16, choices=(('是', '是'), ('否', '否')), verbose_name='课时费是否已支付')
    teacher_class = models.ForeignKey(StudentClass,on_delete=models.CASCADE,verbose_name='教师上课班级')
    class Meta:
        verbose_name = '教师授课信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.teacher_name
