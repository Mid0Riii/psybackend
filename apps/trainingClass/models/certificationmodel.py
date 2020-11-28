from django.db import models
from .trainingclassmodel import TrainBasic
from .classmodel import TrainClass
from django.utils.html import format_html


class TrainCertification(models.Model):
    class Meta:
        verbose_name = '训练班证书'
        verbose_name_plural = verbose_name

    relate_class = models.ForeignKey(TrainClass, on_delete=models.CASCADE, verbose_name='班级', null=True, blank=True)
    relate_trainingclass = models.OneToOneField(TrainBasic, on_delete=models.CASCADE, verbose_name='学号',
                                                primary_key=True)
    cert_id = models.CharField(max_length=128, verbose_name='证书编号', blank=True, null=True, default='空')
    cert_date = models.CharField(max_length=128, verbose_name='发证日期', blank=True, null=True, default='空')
    cert_draw_people = models.CharField(max_length=128, verbose_name='领取人', blank=True, null=True, default='空')
    cert_draw_date = models.CharField(max_length=128, verbose_name="领取时间", blank=True, null=True, default='空')
    cert_nation_id = models.CharField(max_length=128, verbose_name='国证证书编号', null=True, blank=True, default='空')
    cert_nation_people = models.CharField(max_length=128, verbose_name='国证证书领取人与日期', null=True, blank=True, default='空')
    cert_other = models.CharField(max_length=128, verbose_name='备注', null=True, blank=True, default='空')

    def get_tra_name(self):
        info = self.relate_trainingclass.tra_name
        if self.relate_trainingclass.traintuition.fee_date == '空':
            color_code = 'red'
        else:
            color_code = 'black'
        return format_html('<span style="color:{};">{}</span>', color_code, info)

    get_tra_name.short_description = u'姓名'
    get_tra_name.allow_tags = get_tra_name.is_column = True

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
