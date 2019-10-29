from django.db import models
from .familymodel import FamilyBasic
class FamilyOnduty(models.Model):
    class Meta:
        verbose_name = '家庭考勤信息'
        verbose_name_plural = verbose_name

    relate_family = models.OneToOneField(FamilyBasic,on_delete=models.CASCADE,verbose_name='学号',blank=True,null=True)
    onduty = models.CharField(max_length=128, verbose_name='出勤', blank=True, null=True)
    homework1 = models.CharField(max_length=128, verbose_name='作业一', blank=True, null=True)
    homework2 = models.CharField(max_length=128, verbose_name='作业二', blank=True, null=True)
    homework3 = models.CharField(max_length=128, verbose_name='作业三', blank=True, null=True)
    other = models.TextField(verbose_name="备注", null=True, blank=True)
    def get_fam_name(self):
        return self.relate_family.fam_name

    get_fam_name.short_description = u'姓名'
    get_fam_name.allow_tags = get_fam_name.is_column = True

    def get_fam_num(self):
        return self.relate_family.fam_number

    get_fam_num.short_description = '学号'
    get_fam_num.allow_tags = get_fam_num.is_colume = True

    def get_fam_class(self):
        return self.relate_family.fam_class.class_name

    get_fam_class.short_description = u'班级'
    get_fam_class.allow_tags = get_fam_name.is_column = True

    def __str__(self):
        return str(self.get_fam_name())