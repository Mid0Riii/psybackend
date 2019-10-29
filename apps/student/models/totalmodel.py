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
    tuition = models.OneToOneField(Tuition,on_delete=models.CASCADE,verbose_name="财务信息",null=True,blank=True)
    def stu_name(self):
        return self.student.stu_name
    def stu_gender(self):
        return self.student.stu_gender
    def stu_class(self):
        return self.student.stu_class.class_name
    def stu_class_num(self):
        return self.student.stu_class_num
    def stu_level(self):
        return self.student.stu_level
    def stu_id_number(self):
        return self.student.stu_id_number
    def stu_loc(self):
        return self.student.stu_loc
    def stu_deg(self):
        return self.student.stu_deg
    def stu_major(self):
        return self.student.stu_major
    def stu_company(self):
        return self.student.stu_company
    def stu_duty(self):
        return self.student.stu_duty
    def stu_status(self):
        return self.student.stu_status
    def stu_origin(self):
        return self.student.stu_origin
    def stu_cellphone(self):
        return self.student.stu_cellphone
    def stu_wechat(self):
        return self.student.stu_wechat
    def stu_qq(self):
        return self.student.stu_qq
    def stu_signup_date(self):
        return self.student.stu_signup_date
    def stu_signup_people(self):
        return self.student.stu_signup_people
    def stu_other(self):
        return self.student.stu_other
    def fee_train(self):
        return self.student.tuition.fee_train






