from django.db import models
from .classmodel import StudentClass
class StudentBasic(models.Model):
    class Meta:
        verbose_name = '心理学员招生信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.stu_number)

    def save(self, *args, **kwargs):
        # TODO CODEVIEW 重写保存方法需要创建外键约束时务必先保存当前对象
        super(StudentBasic, self).save(*args, **kwargs)
        from .tuitionmodel import Tuition
        from .textbookmodel import StudentTextbook
        from .wechatmodel import StudentWechat
        from .exammodel import StudentExam
        from .examextramodel import StudentExamExtra
        from .totalmodel import Total
        from .certificationmodel import StudentCertification
        from .ondutymodel import Onduty
        try:
            Tuition.objects.get(relate_student=self)
            StudentExam.objects.get(relate_student=self)
            StudentWechat.objects.get(relate_student=self)
            StudentExamExtra.objects.get(relate_student=self)
            StudentTextbook.objects.get(relate_student=self)
            StudentCertification.objects.get(relate_student=self)
            Onduty.objects.get(relate_student=self)
            Total.objects.get(student=self)
        except Exception as e:
            Tuition.objects.create(relate_student=self)
            StudentExam.objects.create(relate_student=self)
            StudentWechat.objects.create(relate_student=self)
            StudentExamExtra.objects.create(relate_student=self)
            StudentTextbook.objects.create(relate_student=self)
            StudentCertification.objects.create(relate_student=self)
            Total.objects.create(student=self)
            Onduty.objects.create(relate_student=self)
        # super(StudentBasic, self).save(*args, **kwargs)
    def get_verbose_name(self,field):
        return str(field)

    def short_loc(self):
        if len(str(self.stu_loc)) > 5:
            return '{}...'.format(str(self.stu_loc)[0:5])
        else:
            return str(self.stu_loc)
    short_loc.short_description = '所在地'
    short_loc.allow_tags = short_loc.is_colume = True

    def short_deg(self):
        if len(str(self.stu_deg)) > 5:
            return '{}...'.format(str(self.stu_deg)[0:5])
        else:
            return str(self.stu_deg)
    short_deg.short_description = '学位'
    short_deg.allow_tags = short_deg.is_colume = True

    def short_major(self):
        if len(str(self.stu_major)) > 5:
            return '{}...'.format(str(self.stu_major)[0:5])
        else:
            return str(self.stu_major)
    short_major.short_description = '专业'
    short_major.allow_tags = short_major.is_colume = True

    def short_company(self):
        if len(str(self.stu_company)) > 5:
            return '{}...'.format(str(self.stu_company)[0:5])
        else:
            return str(self.stu_company)
    short_company.short_description = '工作单位'
    short_company.allow_tags = short_company.is_colume = True

    def short_loc(self):
        if len(str(self.stu_loc)) > 5:
            return '{}...'.format(str(self.stu_loc)[0:5])
        else:
            return str(self.stu_loc)
    short_loc.short_description = '所在地'
    short_loc.allow_tags = short_loc.is_colume = True

    def short_loc(self):
        if len(str(self.stu_loc)) > 5:
            return '{}...'.format(str(self.stu_loc)[0:5])
        else:
            return str(self.stu_loc)
    short_loc.short_description = '所在地'
    short_loc.allow_tags = short_loc.is_colume = True


    stu_number = models.CharField(max_length=128, verbose_name='学号', unique=True)
    stu_name = models.CharField(max_length=128, verbose_name='姓名',blank=True,null=True)
    stu_gender = models.CharField(max_length=16, choices=(('男', '男'), ('女', '女')), verbose_name='性别',blank=True,null=True)
    stu_level = models.CharField(max_length=16,choices=(('二级','二级'),('三级','三级')),verbose_name='级别',null=True,blank=True)
    stu_id_number = models.CharField(max_length=128, verbose_name='身份证号', unique=True)
    stu_loc = models.CharField(max_length=128, verbose_name='所在地', blank=True, null=True)
    stu_deg = models.CharField(max_length=128, verbose_name='学历', blank=True, null=True)
    stu_major = models.CharField(max_length=128, verbose_name='专业', blank=True, null=True)
    stu_company = models.CharField(max_length=128, verbose_name='工作单位', blank=True, null=True)
    stu_duty = models.CharField(max_length=128, verbose_name='职务', blank=True, null=True)
    stu_status = models.CharField(max_length=128, verbose_name='职称', blank=True, null=True)
    # stu_profession = models.CharField(max_length=128, verbose_name='所属行业', blank=True, null=True)
    stu_origin = models.CharField(max_length=128, verbose_name='生源来源', blank=True, null=True)
    stu_cellphone = models.CharField(max_length=128, verbose_name='手机号', blank=True, null=True)
    stu_wechat = models.CharField(max_length=128, verbose_name='微信', blank=True, null=True)
    stu_qq = models.CharField(max_length=128, verbose_name='QQ', blank=True, null=True)
    stu_signup_date = models.CharField(max_length=128,verbose_name='报名日期', blank=True, null=True)
    stu_signup_people = models.CharField(max_length=128, verbose_name='具体招生人', blank=True, null=True)
    stu_other = models.TextField(verbose_name='备注', blank=True, null=True)
    stu_class = models.ForeignKey(StudentClass, on_delete=models.CASCADE, verbose_name='班级')
    stu_class_num = models.CharField(max_length=128,verbose_name='班内序号',null=True,blank=True)



# TODO 筛选非空 增加班级内部序号
# TODO 为表格添加jquery-ui中的resizeable方法实现自由改变表格列宽