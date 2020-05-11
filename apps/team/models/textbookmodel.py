from django.db import models
from .teammodel import TeamBasic
from .classmodel import TeamClass
from django.utils.html import format_html
class TeamTextbook(models.Model):
    class Meta:
        verbose_name = '团体心理辅导教材'
        verbose_name_plural = verbose_name

    relate_class = models.ForeignKey(TeamClass, on_delete=models.CASCADE, verbose_name='班级',null=True,blank=True)
    relate_team = models.OneToOneField(TeamBasic, on_delete=models.CASCADE, verbose_name='学号', primary_key=True)
    text_team = models.CharField(max_length=128, verbose_name='团体心理辅导', blank=True, null=True,default='空')
    text_two = models.CharField(max_length=128, verbose_name='教材2', blank=True, null=True,default='空')
    text_train = models.CharField(max_length=128, verbose_name='培训指南', blank=True, null=True,default='空')        
    text_manual = models.CharField(max_length=128, verbose_name='学员手册', blank=True, null=True, default='空')
    text_other = models.TextField(verbose_name='备注',blank=True,null=True,default='空')


    def get_tea_name(self):
        info = self.relate_team.tea_name
        if self.relate_team.teamtuition.fee_date == '空':
            color_code = 'red'
        else:
            color_code = 'black'
        return format_html('<span style="color:{};">{}</span>', color_code, info)

    get_tea_name.short_description = u'姓名'
    get_tea_name.allow_tags = get_tea_name.is_column = True

    get_tea_name.short_description = u'姓名'
    get_tea_name.allow_tags = get_tea_name.is_column = True

    def get_tea_num(self):
        return self.relate_team.tea_number

    get_tea_num.short_description = '学号'
    get_tea_num.allow_tags = get_tea_num.is_colume = True

    def get_tea_class(self):
        return self.relate_team.tea_class.class_name

    get_tea_class.short_description = u'班级'
    get_tea_class.allow_tags = get_tea_name.is_column = True

    def __str__(self):
        return str(self.relate_team.tea_name)
