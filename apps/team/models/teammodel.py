from django.db import models
from .classmodel import TeamClass
from django.utils.html import format_html

class TeamBasic(models.Model):
    class Meta:
        verbose_name = '团体心理辅导招生信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.tea_number)

    def save(self, *args, **kwargs):
        # TODO CODEVIEW 重写保存方法需要创建外键约束时务必先保存当前对象
        super(TeamBasic, self).save(*args, **kwargs)
        from .tuitionmodel import TeamTuition
        from .textbookmodel import TeamTextbook
        from .wechatmodel import TeamWechat
        from .exammodel import TeamExam
        from .certificationmodel import TeamCertification
        from .ondutymodel import TeamOnduty
        from .totalmodel import Total
        try:
            TeamTuition.objects.get(relate_team=self)
            TeamExam.objects.get(relate_team=self)
            TeamWechat.objects.get(relate_team=self)
            TeamTextbook.objects.get(relate_team=self)
            TeamCertification.objects.get(relate_team=self)
            TeamOnduty.objects.get(relate_team=self)
            Total.objects.get(team=self)
        except Exception as e:
            TeamTuition.objects.create(relate_team=self,relate_class=self.tea_class)
            TeamExam.objects.create(relate_team=self,relate_class=self.tea_class)
            TeamWechat.objects.create(relate_team=self,relate_class=self.tea_class)
            TeamTextbook.objects.create(relate_team=self,relate_class=self.tea_class)
            TeamCertification.objects.create(relate_team=self,relate_class=self.tea_class)
            TeamOnduty.objects.create(relate_team=self,relate_class=self.tea_class)
            Total.objects.create(team=self)
        # super(teamBasic, self).save(*args, **kwargs)

    def get_verbose_name(self,field):
        return str(field)

    tea_number = models.CharField(max_length=128, verbose_name='学号', unique=True)
    tea_name = models.CharField(max_length=128, verbose_name='姓名',blank=True,null=True,default='空')
    tea_gender = models.CharField(max_length=16, choices=(('男', '男'), ('女', '女')), verbose_name='性别',blank=True,null=True,default='空')
    tea_type = models.CharField(max_length=128, verbose_name='学员类型',blank=True,null=True,default='空')
    tea_group = models.CharField(max_length=128, verbose_name='组别和职务',blank=True,null=True,default='空')
    tea_id_number = models.CharField(max_length=128, verbose_name='身份证号',default='空')
    tea_loc = models.CharField(max_length=128, verbose_name='所在地', blank=True, null=True,default='空')
    tea_deg = models.CharField(max_length=128, verbose_name='学历', blank=True, null=True,default='空')
    tea_major = models.CharField(max_length=128, verbose_name='专业', blank=True, null=True,default='空')
    tea_company = models.CharField(max_length=128, verbose_name='工作单位', blank=True, null=True,default='空')
    tea_duty = models.CharField(max_length=128, verbose_name='职务', blank=True, null=True,default='空')
    tea_status = models.CharField(max_length=128, verbose_name='职称', blank=True, null=True,default='空')
    # tea_profession = models.CharField(max_length=128, verbose_name='所属行业', blank=True, null=True)
    tea_origin = models.CharField(max_length=128, verbose_name='生源来源', blank=True, null=True,default='空')
    tea_cellphone = models.CharField(max_length=128, verbose_name='手机号', blank=True, null=True,default='空')
    tea_wechat = models.CharField(max_length=128, verbose_name='微信', blank=True, null=True,default='空')
    tea_email = models.CharField(max_length=128, verbose_name='邮箱', blank=True, null=True,default='空')
    tea_signup_date = models.CharField(max_length=128,verbose_name='报名日期', blank=True, null=True,default='空')
    tea_signup_people = models.CharField(max_length=128, verbose_name='具体招生人', blank=True, null=True,default='空')
    # tea_teacher_level = models.CharField(max_length=32,verbose_name='心师级别',blank=True,null=True,default='空')
    tea_other = models.TextField(verbose_name='备注', blank=True, null=True,default='空')
    tea_class = models.ForeignKey(TeamClass, on_delete=models.CASCADE, verbose_name='班级')
    tea_class_num = models.CharField(max_length=128,verbose_name='班内序号',null=True,blank=True,default='空')



# TODO 为表格添加jquery-ui中的resizeable方法实现自由改变表格列宽