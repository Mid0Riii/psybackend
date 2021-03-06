from django.db import models
from .socialmodel import SocialBasic
from .classmodel import SocialClass
from django.utils.html import format_html


class SocialCertification(models.Model):
    class Meta:
        verbose_name = '社会工作师证书'
        verbose_name_plural = verbose_name

    relate_class = models.ForeignKey(SocialClass, on_delete=models.CASCADE, verbose_name='班级', null=True, blank=True)
    relate_social = models.OneToOneField(SocialBasic, on_delete=models.CASCADE, verbose_name='学号', primary_key=True)
    ass_cert_id = models.CharField(max_length=128, verbose_name='协会证书编号', blank=True, null=True, default='空')
    ass_cert_date = models.CharField(max_length=128, verbose_name='协会证书发证日期', blank=True, null=True, default='空')
    ass_cert_draw_people = models.CharField(max_length=128, verbose_name='协会证书领取人', blank=True, null=True, default='空')
    ass_cert_draw_date = models.CharField(max_length=128, verbose_name="协会证书领取时间", blank=True, null=True, default='空')
    nation_cert_id = models.CharField(max_length=128, verbose_name='国证证书编号', blank=True, null=True, default='空')
    nation_cert_date = models.CharField(max_length=128, verbose_name='国征证书发证日期', blank=True, null=True, default='空')
    nation_cert_draw_people = models.CharField(max_length=128, verbose_name='国证证书领取人', blank=True, null=True,
                                               default='空')
    nation_cert_draw_date = models.CharField(max_length=128, verbose_name="国证证书领取时间", blank=True, null=True,
                                             default='空')
    other = models.TextField(verbose_name='备注', blank=True, null=True, default='空')

    def get_social_name(self):
        info = self.relate_social.social_name
        if self.relate_social.socialtuition.fee_date == '空':
            color_code = 'red'
        else:
            color_code = 'black'
        return format_html('<span style="color:{};">{}</span>', color_code, info)

    get_social_name.short_description = u'姓名'
    get_social_name.allow_tags = get_social_name.is_column = True

    get_social_name.short_description = u'姓名'
    get_social_name.allow_tags = get_social_name.is_column = True

    def get_social_num(self):
        return self.relate_social.social_number

    get_social_num.short_description = '学号'
    get_social_num.allow_tags = get_social_num.is_column = True

    def get_social_class(self):
        return self.relate_social.social_class.class_name

    get_social_class.short_description = u'班级'
    get_social_class.allow_tags = get_social_class.is_column = True

    def get_social_id_number(self):
        return self.relate_social.social_id_number

    get_social_id_number.short_description = u'身份证号'
    get_social_id_number.allow_tags = get_social_id_number.is_column = True

    def __str__(self):
        return str(self.relate_social.social_name)
