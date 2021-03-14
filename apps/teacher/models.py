from django.db import models
from student.models import StudentClass
from family.models import FamilyClass
from marriage.models import MarriageClass
from sandbox.models import SandboxClass
from team.models import TeamClass
from trainingClass.models import TrainClass
from social.models import SocialClass


# Create your models here.

class BaseTeacher(models.Model):
    class Meta:
        abstract = True

    teacher_name = models.CharField(max_length=128, verbose_name='上课教师')
    teacher_info = models.CharField(max_length=256, verbose_name='上课内容')
    teacher_date = models.CharField(max_length=128, verbose_name='上课时间')
    teacher_fare = models.CharField(max_length=128, verbose_name='课时费用')
    teacher_paid = models.CharField(max_length=16, choices=(('是', '是'), ('否', '否')), verbose_name='课时费是否已支付')


class Teacher(BaseTeacher):
    teacher_class = models.ForeignKey(StudentClass, on_delete=models.CASCADE, verbose_name='教师上课班级')

    class Meta:
        verbose_name = '心理教师授课信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.teacher_name


class FamilyTeacher(BaseTeacher):
    teacher_class = models.ForeignKey(FamilyClass, on_delete=models.CASCADE, verbose_name='教师上课班级')

    class Meta:
        verbose_name = '家庭教师授课信息'
        verbose_name_plural = verbose_name


class MarriageTeacher(BaseTeacher):
    teacher_class = models.ForeignKey(MarriageClass, on_delete=models.CASCADE, verbose_name='教师上课班级')

    class Meta:
        verbose_name = '婚姻教师授课信息'
        verbose_name_plural = verbose_name


class SandboxTeacher(BaseTeacher):
    teacher_class = models.ForeignKey(SandboxClass, on_delete=models.CASCADE, verbose_name='教师上课班级')

    class Meta:
        verbose_name = '沙盒教师授课信息'
        verbose_name_plural = verbose_name


class TeamTeacher(BaseTeacher):
    teacher_class = models.ForeignKey(TeamClass, on_delete=models.CASCADE, verbose_name='教师上课班级')

    class Meta:
        verbose_name = '团体教师授课信息'
        verbose_name_plural = verbose_name


class TrainTeacher(BaseTeacher):
    teacher_class = models.ForeignKey(TrainClass, on_delete=models.CASCADE, verbose_name='教师上课班级')

    class Meta:
        verbose_name = '训练班教师授课信息'
        verbose_name_plural = verbose_name


class SocialTeacher(BaseTeacher):
    teacher_class = models.ForeignKey(SocialClass, on_delete=models.CASCADE, verbose_name='教师上课班级')

    class Meta:
        verbose_name = '社会工作师教师授课信息'
        verbose_name_plural = verbose_name
