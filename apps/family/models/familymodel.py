from django.db import models
from .classmodel import FamilyClass
from django.utils.html import format_html
class FamilyBasic(models.Model):
    class Meta:
        verbose_name = '家庭招生信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.fam_number)

    def save(self, *args, **kwargs):
        # TODO CODEVIEW 重写保存方法需要创建外键约束时务必先保存当前对象
        super(FamilyBasic, self).save(*args, **kwargs)
        from .tuitionmodel import FamilyTuition
        from .textbookmodel import FamilyTextbook
        from .wechatmodel import FamilyWechat
        from .resultmodel import Result
        from .resultextramodel import ResultExtra
        from .certificationmodel import FamilyCertification
        from .ondutymodel import FamilyOnduty
        from .totalmodel import Total
        try:
            FamilyTuition.objects.get(relate_family=self)
            Result.objects.get(relate_family=self)
            FamilyWechat.objects.get(relate_family=self)
            ResultExtra.objects.get(relate_family=self)
            FamilyTextbook.objects.get(relate_family=self)
            FamilyCertification.objects.get(relate_family=self)
            FamilyOnduty.objects.get(relate_family=self)
            Total.objects.get(family=self)
        except Exception as e:
            FamilyTuition.objects.create(relate_family=self,relate_class=self.fam_class)
            Result.objects.create(relate_family=self,relate_class=self.fam_class)
            FamilyWechat.objects.create(relate_family=self,relate_class=self.fam_class)
            ResultExtra.objects.create(relate_family=self,relate_class=self.fam_class)
            FamilyTextbook.objects.create(relate_family=self,relate_class=self.fam_class)
            FamilyCertification.objects.create(relate_family=self,relate_class=self.fam_class)
            FamilyOnduty.objects.create(relate_family=self,relate_class=self.fam_class)
            Total.objects.create(family=self)
        # super(familyBasic, self).save(*args, **kwargs)

    def get_verbose_name(self,field):
        return str(field)

    fam_number = models.CharField(max_length=128, verbose_name='学号', unique=True)
    fam_name = models.CharField(max_length=128, verbose_name='姓名',blank=True,null=True,default='空')
    fam_gender = models.CharField(max_length=16, choices=(('男', '男'), ('女', '女')), verbose_name='性别',blank=True,null=True,default='空')
    fam_id_number = models.CharField(max_length=128, verbose_name='身份证号',default='空')
    fam_loc = models.CharField(max_length=128, verbose_name='所在地', blank=True, null=True,default='空')
    fam_deg = models.CharField(max_length=128, verbose_name='学历', blank=True, null=True,default='空')
    fam_major = models.CharField(max_length=128, verbose_name='专业', blank=True, null=True,default='空')
    fam_company = models.CharField(max_length=128, verbose_name='工作单位', blank=True, null=True,default='空')
    fam_duty = models.CharField(max_length=128, verbose_name='职务', blank=True, null=True,default='空')
    fam_status = models.CharField(max_length=128, verbose_name='职称', blank=True, null=True,default='空')
    # fam_profession = models.CharField(max_length=128, verbose_name='所属行业', blank=True, null=True)
    fam_origin = models.CharField(max_length=128, verbose_name='生源来源', blank=True, null=True,default='空')
    fam_cellphone = models.CharField(max_length=128, verbose_name='手机号', blank=True, null=True,default='空')
    fam_wechat = models.CharField(max_length=128, verbose_name='微信', blank=True, null=True,default='空')
    fam_qq = models.CharField(max_length=128, verbose_name='QQ', blank=True, null=True,default='空')
    fam_signup_date = models.CharField(max_length=128,verbose_name='报名日期', blank=True, null=True,default='空')
    fam_signup_people = models.CharField(max_length=128, verbose_name='具体招生人', blank=True, null=True,default='空')
    fam_teacher_level = models.CharField(max_length=32,verbose_name='心师级别',blank=True,null=True,default='空')
    fam_other = models.TextField(verbose_name='备注', blank=True, null=True,default='空')
    fam_class = models.ForeignKey(FamilyClass, on_delete=models.CASCADE, verbose_name='班级')
    fam_class_num = models.CharField(max_length=128,verbose_name='班内序号',null=True,blank=True,default='空')



# TODO 为表格添加jquery-ui中的resizeable方法实现自由改变表格列宽