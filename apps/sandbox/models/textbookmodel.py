from django.db import models
from .sandboxmodel import SandboxBasic
from .classmodel import SandboxClass
from django.utils.html import format_html
class SandboxTextbook(models.Model):
    class Meta:
        verbose_name = '沙盘分析分析指导教材'
        verbose_name_plural = verbose_name

    relate_class = models.ForeignKey(SandboxClass, on_delete=models.CASCADE, verbose_name='班级',null=True,blank=True)
    relate_sandbox = models.OneToOneField(SandboxBasic, on_delete=models.CASCADE, verbose_name='学号', primary_key=True)
    text_sandbox = models.CharField(max_length=128, verbose_name='沙盘教材', blank=True, null=True,default='空')
    text_two = models.CharField(max_length=128, verbose_name='教材2', blank=True, null=True,default='空')
    text_three = models.CharField(max_length=128, verbose_name='教材3', blank=True, null=True,default='空')
    text_train = models.CharField(max_length=128, verbose_name='培训指南', blank=True, null=True,default='空')        
    text_manual = models.CharField(max_length=128, verbose_name='学员手册', blank=True, null=True, default='空')
    text_other = models.TextField(verbose_name='备注',blank=True,null=True,default='空')


    def get_san_name(self):
        info = self.relate_sandbox.san_name
        if self.relate_sandbox.sandboxtuition.fee_date == '空':
            color_code = 'red'
        else:
            color_code = 'black'
        return format_html('<span style="color:{};">{}</span>', color_code, info)

    get_san_name.short_description = u'姓名'
    get_san_name.allow_tags = get_san_name.is_column = True

    get_san_name.short_description = u'姓名'
    get_san_name.allow_tags = get_san_name.is_column = True

    def get_san_num(self):
        return self.relate_sandbox.san_number

    get_san_num.short_description = '学号'
    get_san_num.allow_tags = get_san_num.is_colume = True

    def get_san_class(self):
        return self.relate_sandbox.san_class.class_name

    get_san_class.short_description = u'班级'
    get_san_class.allow_tags = get_san_name.is_column = True

    def __str__(self):
        return str(self.relate_sandbox.san_name)
