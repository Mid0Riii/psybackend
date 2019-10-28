from django.db import models
from .studentmodel import StudentBasic
from .classmodel import StudentClass
from .exammodel import StudentExam
from .examextramodel import StudentExamExtra
from .ondutymodel import Onduty
from .tuitionmodel import Tuition
from .wechatmodel import StudentWechat
class Total(models.Model):
    class Meta:
        verbose_name="心理学员招生信息总览"
        verbose_name_plural = verbose_name
    student = models.OneToOneField(StudentBasic,on_delete=models.CASCADE,verbose_name="学生")
    tuition = models.OneToOneField(Tuition,on_delete=models.CASCADE,verbose_name="财务信息")
    def stu_name(self):
        return self.student.stu_name
    def stu_gender(self):
        return self.student.stu_gender
    def stu_class(self):
        return self.student.stu_class.class_name
    def stu_class_num(self):
        return self.student.stu_class_num




