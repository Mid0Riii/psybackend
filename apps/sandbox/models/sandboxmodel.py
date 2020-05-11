from django.db import models
from .classmodel import SandboxClass
from django.utils.html import format_html

class SandboxBasic(models.Model):
    class Meta:
        verbose_name = '沙盘分析指导招生信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.san_number)

    def save(self, *args, **kwargs):
        # TODO CODEVIEW 重写保存方法需要创建外键约束时务必先保存当前对象
        super(SandboxBasic, self).save(*args, **kwargs)
        from .tuitionmodel import SandboxTuition
        from .textbookmodel import SandboxTextbook
        from .wechatmodel import SandboxWechat
        from .exammodel import SandboxExam
        from .certificationmodel import SandboxCertification
        from .ondutymodel import SandboxOnduty
        from .totalmodel import Total
        try:
            SandboxTuition.objects.get(relate_sandbox=self)
            SandboxExam.objects.get(relate_sandbox=self)
            SandboxWechat.objects.get(relate_sandbox=self)
            SandboxTextbook.objects.get(relate_sandbox=self)
            SandboxCertification.objects.get(relate_sandbox=self)
            SandboxOnduty.objects.get(relate_sandbox=self)
            Total.objects.get(sandbox=self)

        except Exception as e:
            SandboxTuition.objects.create(relate_sandbox=self,relate_class=self.san_class)
            SandboxExam.objects.create(relate_sandbox=self,relate_class=self.san_class)
            SandboxWechat.objects.create(relate_sandbox=self,relate_class=self.san_class)
            SandboxTextbook.objects.create(relate_sandbox=self,relate_class=self.san_class)
            SandboxCertification.objects.create(relate_sandbox=self,relate_class=self.san_class)
            SandboxOnduty.objects.create(relate_sandbox=self,relate_class=self.san_class)
            Total.objects.create(sandbox=self)
        # super(sandboxBasic, self).save(*args, **kwargs)

    def get_verbose_name(self,field):
        return str(field)

    san_type = models.CharField(max_length=128, verbose_name='学员类型',blank=True,null=True,default='空')
    san_group = models.CharField(max_length=128, verbose_name='组别和职务',blank=True,null=True,default='空')
    san_number = models.CharField(max_length=128, verbose_name='学号', unique=True)
    san_name = models.CharField(max_length=128, verbose_name='姓名',blank=True,null=True,default='空')
    san_gender = models.CharField(max_length=16, choices=(('男', '男'), ('女', '女')), verbose_name='性别',blank=True,null=True,default='空')
    san_id_number = models.CharField(max_length=128, verbose_name='身份证号',default='空')
    san_loc = models.CharField(max_length=128, verbose_name='所在地', blank=True, null=True,default='空')
    san_deg = models.CharField(max_length=128, verbose_name='学历', blank=True, null=True,default='空')
    san_major = models.CharField(max_length=128, verbose_name='专业', blank=True, null=True,default='空')
    san_company = models.CharField(max_length=128, verbose_name='工作单位', blank=True, null=True,default='空')
    san_duty = models.CharField(max_length=128, verbose_name='职务', blank=True, null=True,default='空')
    san_status = models.CharField(max_length=128, verbose_name='职称', blank=True, null=True,default='空')
    # san_profession = models.CharField(max_length=128, verbose_name='所属行业', blank=True, null=True)
    san_origin = models.CharField(max_length=128, verbose_name='生源来源', blank=True, null=True,default='空')
    san_cellphone = models.CharField(max_length=128, verbose_name='手机号', blank=True, null=True,default='空')
    san_wechat = models.CharField(max_length=128, verbose_name='微信', blank=True, null=True,default='空')
    san_email = models.CharField(max_length=128, verbose_name='邮箱', blank=True, null=True,default='空')
    san_signup_date = models.CharField(max_length=128,verbose_name='报名日期', blank=True, null=True,default='空')
    san_signup_people = models.CharField(max_length=128, verbose_name='具体招生人', blank=True, null=True,default='空')
    # san_teacher_level = models.CharField(max_length=32,verbose_name='心师级别',blank=True,null=True,default='空')
    san_other = models.TextField(verbose_name='备注', blank=True, null=True,default='空')
    san_class = models.ForeignKey(SandboxClass, on_delete=models.CASCADE, verbose_name='班级')
    san_class_num = models.CharField(max_length=128,verbose_name='班内序号',null=True,blank=True,default='空')



# TODO 为表格添加jquery-ui中的resizeable方法实现自由改变表格列宽