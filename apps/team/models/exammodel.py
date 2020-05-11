from django.db import models
from .teammodel import TeamBasic
from .classmodel import TeamClass
from django.utils.html import format_html
class TeamExam(models.Model):
    class Meta:
        verbose_name = '团体心理辅导考核成绩'
        verbose_name_plural = verbose_name

    relate_class = models.ForeignKey(TeamClass, on_delete=models.CASCADE, verbose_name='班级',null=True,blank=True)
    relate_team = models.OneToOneField(TeamBasic, on_delete=models.CASCADE, verbose_name='学号', blank=True, null=True)
    batch = models.CharField(max_length=128,verbose_name='考试批次',blank=True,null=True,default='空')
    exam_total = models.CharField(max_length=128,verbose_name='总分',blank=True,null=True,default='空')
    exam_nation = models.CharField(max_length=128,verbose_name='国考笔试成绩',blank=True,null=True,default='空')
    exam_practice = models.CharField(max_length=128,verbose_name='实操考核成绩',blank=True,null=True,default='空')
    # result = models.CharField(max_length=64,verbose_name='合格情况',choices=(('合格','合格'),('不合格','不合格')),blank=True,null=True,default='空')
    other = models.TextField(verbose_name='备注',blank=True,null=True,default='空')

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