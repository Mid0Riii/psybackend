from django.db import models
from .trainingclassmodel import TrainBasic
from .classmodel import TrainClass
from django.utils.html import format_html


class TrainWechat(models.Model):
    class Meta:
        verbose_name = '训练班365开通情况'
        verbose_name_plural = verbose_name

    relate_class = models.ForeignKey(TrainClass, on_delete=models.CASCADE, verbose_name='班级', null=True, blank=True)
    relate_trainingclass = models.OneToOneField(TrainBasic, on_delete=models.CASCADE, verbose_name='学号',
                                                primary_key=True)
    wechat_number = models.CharField(max_length=128, verbose_name='平台绑定号码', blank=True, null=True, default='空')
    wechat_nickname = models.CharField(max_length=128, verbose_name='微信昵称', blank=True, null=True, default='空')
    wechat_date = models.CharField(max_length=128, verbose_name='开通日期', blank=True, null=True, default='空')
    wechat_other = models.CharField(max_length=128, verbose_name='备注', blank=True, null=True, default='空')

    def get_tra_name(self):
        info = self.relate_trainingclass.tra_name
        if self.relate_trainingclass.traintuition.fee_date == '空':
            color_code = 'red'
        else:
            color_code = 'black'
        return format_html('<span style="color:{};">{}</span>', color_code, info)

    get_tra_name.short_description = u'姓名'
    get_tra_name.allow_tags = get_tra_name.is_column = True

    def get_tra_num(self):
        return self.relate_trainingclass.tra_number

    get_tra_num.short_description = '学号'
    get_tra_num.allow_tags = get_tra_num.is_colume = True

    def get_tra_class(self):
        return self.relate_trainingclass.tra_class.class_name

    get_tra_class.short_description = u'班级'
    get_tra_class.allow_tags = get_tra_name.is_column = True

    def __str__(self):
        return str(self.relate_trainingclass.tra_name)
