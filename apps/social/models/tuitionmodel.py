from django.db import models
from .classmodel import SocialClass
from .socialmodel import SocialBasic
from django.utils.html import format_html


class SocialTuition(models.Model):
    class Meta:
        verbose_name = '社会工作师交费信息'
        verbose_name_plural = verbose_name

    relate_class = models.ForeignKey(SocialClass, on_delete=models.CASCADE, verbose_name='班级', null=True, blank=True)
    relate_social = models.OneToOneField(SocialBasic, on_delete=models.CASCADE, verbose_name='学号', primary_key=True)
    fee_train = models.CharField(max_length=128, verbose_name='培训费', blank=True, null=True, default='空')
    fee_material = models.CharField(max_length=128, verbose_name='教材费', blank=True, null=True, default='空')
    fee_exam = models.CharField(max_length=128, verbose_name='考试费', blank=True, null=True, default='空')
    fee_total = models.CharField(max_length=128, verbose_name='总费用', blank=True, null=True, default='空')
    fee_date = models.CharField(max_length=128, verbose_name='缴费日期', blank=True, null=True, default='空')
    fee_method = models.CharField(max_length=128, verbose_name='缴费方式', blank=True, null=True, default='空')
    fee_tax = models.CharField(max_length=128, verbose_name='发票号', blank=True, null=True, default='空')
    fee_invoice_header = models.CharField(max_length=128, verbose_name='发票抬头', blank=True, null=True, default='空')
    fee_invoice_id = models.CharField(max_length=128, verbose_name='发票机构代码', blank=True, null=True, default='空')
    fee_invoice_date = models.CharField(max_length=128, verbose_name='发票开票日期', blank=True, null=True, default='空')
    fee_other = models.TextField(verbose_name='备注', blank=True, null=True, default='空')

    # TODO CODEREVICEW:模型的三种继承方式和自定义方法
    def get_social_name(self):
        info = self.relate_social.social_name
        if self.fee_date == '空':
            color_code = 'red'
        else:
            color_code = 'black'

        return format_html('<span style="color:{};">{}</span>', color_code, info)

    get_social_name.short_description = u'姓名'
    get_social_name.allow_tags = get_social_name.is_column = True

    def get_social_class(self):
        return self.relate_social.social_class.class_name

    get_social_class.short_description = u'班级'
    get_social_class.allow_tags = get_social_class.is_column = True

    def get_social_num(self):
        return self.relate_social.social_number

    get_social_num.short_description = '学号'
    get_social_num.allow_tags = get_social_num.is_column = True

    def __str__(self):
        return str(self.relate_social.social_name)
