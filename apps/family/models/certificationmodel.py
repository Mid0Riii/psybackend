from django.db import models
from .familymodel import FamilyBasic

class FamilyCertification(models.Model):
    class Meta:
        verbose_name = '家庭证书'
        verbose_name_plural = verbose_name

    relate_family = models.OneToOneField(FamilyBasic, on_delete=models.CASCADE, verbose_name='学号', primary_key=True)
    cert_id = models.CharField(max_length=128, verbose_name='证书编号', blank=True, null=True,default='空')
    cert_date = models.CharField(max_length=128,verbose_name='发证日期', blank=True, null=True,default='空')
    cert_draw_people = models.CharField(max_length=128, verbose_name='领取人', blank=True, null=True,default='空')
    cert_draw_date = models.CharField(max_length=128,verbose_name="领取时间", blank=True, null=True,default='空')

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
