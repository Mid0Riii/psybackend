from django.db import models
from .classmodel import FamilyClass
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
        try:
            FamilyTuition.objects.get(relate_family=self)
            Result.objects.get(relate_family=self)
            FamilyWechat.objects.get(relate_family=self)
            ResultExtra.objects.get(relate_family=self)
            FamilyTextbook.objects.get(relate_family=self)
            FamilyCertification.objects.get(relate_family=self)
            FamilyOnduty.objects.get(relate_family=self)
        except Exception as e:
            FamilyTuition.objects.create(relate_family=self)
            Result.objects.create(relate_family=self)
            FamilyWechat.objects.create(relate_family=self)
            ResultExtra.objects.create(relate_family=self)
            FamilyTextbook.objects.create(relate_family=self)
            FamilyCertification.objects.create(relate_family=self)
            FamilyOnduty.objects.create(relate_family=self)
        # super(familyBasic, self).save(*args, **kwargs)
    def get_verbose_name(self,field):
        return str(field)

    def short_loc(self):
        if len(str(self.fam_loc)) > 5:
            return '{}...'.format(str(self.fam_loc)[0:5])
        else:
            return str(self.fam_loc)
    short_loc.short_description = '所在地'
    short_loc.allow_tags = short_loc.is_colume = True

    def short_deg(self):
        if len(str(self.fam_deg)) > 5:
            return '{}...'.format(str(self.fam_deg)[0:5])
        else:
            return str(self.fam_deg)
    short_deg.short_description = '学位'
    short_deg.allow_tags = short_deg.is_colume = True

    def short_major(self):
        if len(str(self.fam_major)) > 5:
            return '{}...'.format(str(self.fam_major)[0:5])
        else:
            return str(self.fam_major)
    short_major.short_description = '专业'
    short_major.allow_tags = short_major.is_colume = True

    def short_company(self):
        if len(str(self.fam_company)) > 5:
            return '{}...'.format(str(self.fam_company)[0:5])
        else:
            return str(self.fam_company)
    short_company.short_description = '工作单位'
    short_company.allow_tags = short_company.is_colume = True

    def short_loc(self):
        if len(str(self.fam_loc)) > 5:
            return '{}...'.format(str(self.fam_loc)[0:5])
        else:
            return str(self.fam_loc)
    short_loc.short_description = '所在地'
    short_loc.allow_tags = short_loc.is_colume = True

    def short_loc(self):
        if len(str(self.fam_loc)) > 5:
            return '{}...'.format(str(self.fam_loc)[0:5])
        else:
            return str(self.fam_loc)
    short_loc.short_description = '所在地'
    short_loc.allow_tags = short_loc.is_colume = True


    fam_number = models.CharField(max_length=128, verbose_name='学号', unique=True)
    fam_name = models.CharField(max_length=128, verbose_name='姓名',blank=True,null=True)
    fam_gender = models.CharField(max_length=16, choices=(('男', '男'), ('女', '女')), verbose_name='性别',blank=True,null=True)
    fam_level = models.CharField(max_length=16,choices=(('二级','二级'),('三级','三级')),verbose_name='级别',null=True,blank=True)
    fam_id_number = models.CharField(max_length=128, verbose_name='身份证号')
    fam_loc = models.CharField(max_length=128, verbose_name='所在地', blank=True, null=True)
    fam_deg = models.CharField(max_length=128, verbose_name='学历', blank=True, null=True)
    fam_major = models.CharField(max_length=128, verbose_name='专业', blank=True, null=True)
    fam_company = models.CharField(max_length=128, verbose_name='工作单位', blank=True, null=True)
    fam_duty = models.CharField(max_length=128, verbose_name='职务', blank=True, null=True)
    fam_status = models.CharField(max_length=128, verbose_name='职称', blank=True, null=True)
    # fam_profession = models.CharField(max_length=128, verbose_name='所属行业', blank=True, null=True)
    fam_origin = models.CharField(max_length=128, verbose_name='生源来源', blank=True, null=True)
    fam_cellphone = models.CharField(max_length=128, verbose_name='手机号', blank=True, null=True)
    fam_wechat = models.CharField(max_length=128, verbose_name='微信', blank=True, null=True)
    fam_qq = models.CharField(max_length=128, verbose_name='QQ', blank=True, null=True)
    fam_signup_date = models.CharField(max_length=128,verbose_name='报名日期', blank=True, null=True)
    fam_signup_people = models.CharField(max_length=128, verbose_name='具体招生人', blank=True, null=True)
    fam_teacher_level = models.CharField(max_length=32,verbose_name='心师级别',blank=True,null=True)
    fam_other = models.TextField(verbose_name='备注', blank=True, null=True)
    fam_class = models.ForeignKey(FamilyClass, on_delete=models.CASCADE, verbose_name='班级')
    fam_class_num = models.CharField(max_length=128,verbose_name='班内序号',null=True,blank=True)



# TODO 筛选非空 增加班级内部序号
# TODO 为表格添加jquery-ui中的resizeable方法实现自由改变表格列宽