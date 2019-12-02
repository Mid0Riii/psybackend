from django.db import models
from .familymodel import FamilyBasic
from .classmodel import FamilyClass
from django.utils.html import format_html
class FamilyTextbook(models.Model):
    class Meta:
        verbose_name = '家庭教材'
        verbose_name_plural = verbose_name

    relate_class = models.ForeignKey(FamilyClass, on_delete=models.CASCADE, verbose_name='班级',null=True,blank=True)
    relate_family = models.OneToOneField(FamilyBasic, on_delete=models.CASCADE, verbose_name='学号', primary_key=True)
    text_basic = models.CharField(max_length=128, verbose_name='教材', blank=True, null=True,default='空')
    text_manual = models.CharField(max_length=128, verbose_name='学员手册', blank=True, null=True, default='空')
    text_other = models.TextField(verbose_name='备注',blank=True,null=True,default='空')

    def __str__(self):
        return str(self.get_fam_name())

    def get_fam_name(self):
        info = self.relate_family.fam_name
        if self.relate_family.familytuition.fee_date == '空':
            color_code = 'red'
        else:
            color_code = 'black'
        return format_html('<span style="color:{};">{}</span>', color_code, info)

    get_fam_name.short_description = u'姓名'
    get_fam_name.allow_tags = get_fam_name.is_column = True

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
