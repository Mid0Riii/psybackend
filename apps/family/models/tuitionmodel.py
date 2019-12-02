from django.db import models
from .classmodel import FamilyClass
from .familymodel import FamilyBasic
from django.utils.html import format_html
class FamilyTuition(models.Model):
    class Meta:
        verbose_name = '家庭交费信息'
        verbose_name_plural = verbose_name

    relate_class = models.ForeignKey(FamilyClass, on_delete=models.CASCADE, verbose_name='班级',null=True,blank=True)
    relate_family = models.OneToOneField(FamilyBasic, on_delete=models.CASCADE, verbose_name='学号', primary_key=True)
    fee_train = models.CharField(max_length=128, verbose_name='培训费', blank=True, null=True,default='空')
    fee_date = models.CharField(max_length=128,verbose_name='缴费日期', blank=True, null=True,default='空')
    fee_method = models.CharField(max_length=128, verbose_name='缴费方式', blank=True, null=True,default='空')
    fee_id = models.CharField(max_length=128, verbose_name='收据号', blank=True, null=True,default='空')
    fee_tax = models.CharField(max_length=128,verbose_name='发票号',blank=True,null=True,default='空')


    # TODO CODEREVICEW:模型的三种继承方式和自定义方法
    def get_fam_name(self):
        info = self.relate_family.fam_name
        if self.fee_date == '空':
            color_code = 'red'
        else:
            color_code = 'black'

        return format_html('<span style="color:{};">{}</span>', color_code, info)

    get_fam_name.short_description = u'姓名'
    get_fam_name.allow_tags = get_fam_name.is_column = True

    def get_fam_class(self):
        return self.relate_family.fam_class.class_name

    get_fam_class.short_description = u'班级'
    get_fam_class.allow_tags = get_fam_name.is_column = True

    def get_fam_num(self):
        return self.relate_family.fam_number

    get_fam_num.short_description = '学号'
    get_fam_num.allow_tags = get_fam_num.is_colume = True

    def __str__(self):
        return str(self.get_fam_name())
