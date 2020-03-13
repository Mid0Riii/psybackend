from django.db import models
from .familymodel import FamilyBasic
from django.utils.html import format_html
from .classmodel import FamilyClass
from .resultmodel import Result
from .resultextramodel import ResultExtra
from .ondutymodel import FamilyOnduty
from .tuitionmodel import FamilyTuition
from .wechatmodel import FamilyWechat
class Total(models.Model):
    class Meta:
        verbose_name="家庭信息总览"
        verbose_name_plural = verbose_name
    family = models.OneToOneField(FamilyBasic,on_delete=models.CASCADE,verbose_name="学生")

    def __str__(self):
        return str(self.family.fam_number)+"-"+str(self.family.fam_name)

    def fam_number(self):

        return self.family.fam_number

    fam_number.short_description = "学号"
    def fam_name(self):
        info = self.family.fam_name
        if self.family.familytuition.fee_date == '空':
            color_code = 'red'
        else:
            color_code = 'black'
        return format_html('<span style="color:{};">{}</span>', color_code, info)
    fam_name.short_description = u'姓名'
    fam_name.allow_tags = fam_name.is_column = True

    def fam_gender(self):
        return self.family.fam_gender

    fam_gender.short_description = "年龄"

    def fam_class(self):
        return self.family.fam_class

    fam_class.short_description = "班级"

    def fam_class_num(self):
        return self.family.fam_class_num

    fam_class_num.short_description = "班级序号"

    def fam_level(self):
        return self.family.fam_level

    fam_level.short_description = "级别"

    def fam_id_number(self):
        return self.family.fam_id_number

    fam_id_number.short_description = "身份证号"

    def fam_loc(self):
        return self.family.fam_loc

    fam_loc.short_description = "所在地"

    def fam_deg(self):
        return self.family.fam_deg

    fam_deg.short_description = "学历"

    def fam_major(self):
        return self.family.fam_major

    fam_major.short_description = "专业"

    def fam_company(self):
        return self.family.fam_company

    fam_company.short_description = "工作单位"

    def fam_duty(self):
        return self.family.fam_duty

    fam_duty.short_description = "职务"

    def fam_status(self):
        return self.family.fam_status

    fam_status.short_description = "职称"

    def fam_origin(self):
        return self.family.fam_origin

    fam_origin.short_description = "生源来源"

    def fam_cellphone(self):
        return self.family.fam_cellphone

    fam_cellphone.short_description = "手机号"

    def fam_wechat(self):
        return self.family.fam_wechat

    fam_wechat.short_description = "微信"

    def fam_qq(self):
        return self.family.fam_qq

    fam_qq.short_description = "qq"

    def fam_signup_date(self):
        return self.family.fam_signup_date

    fam_signup_date.short_description = "报名日期"

    def fam_signup_people(self):
        return self.family.fam_signup_people

    fam_signup_people.short_description = "具体招生人"

    def fam_teacher_level(self):
        return self.family.fam_teacher_level
    fam_teacher_level.short_description = "心师级别"

    def fam_other(self):
        return self.family.fam_other

    fam_other.short_description = "备注"

    def fee_train(self):
        return self.family.familytuition.fee_train

    fee_train.short_description = "培训费"

    def fee_date(self):
        return self.family.familytuition.fee_date

    fee_date.short_description = "缴费日期"

    def fee_method(self):
        return self.family.familytuition.fee_method

    fee_method.short_description = "缴费方式"

    def fee_id(self):
        return self.family.familytuition.fee_id

    fee_id.short_description = "收据号"

    def fee_tax(self):
        return self.family.familytuition.fee_tax

    fee_tax.short_description = "发票号"

    def text_basic(self):
        return self.family.familytextbook.text_basic

    text_basic.short_description = "基础技能"

    def text_other(self):
        return self.family.familytextbook.text_other

    text_other.short_description = "备注"

    def wechat_number(self):
        return self.family.familywechat.wechat_number

    wechat_number.short_description = "平台绑定号码"

    def wechat_nickname(self):
        return self.family.familywechat.wechat_nickname

    wechat_nickname.short_description = "微信昵称"

    def wechat_date(self):
        return self.family.familywechat.wechat_date

    wechat_date.short_description = "开通日期"

    def exam_date(self):
        return self.family.result.date

    exam_date.short_description = "考核日期"

    def exam_homework2_result(self):
        return self.family.result.homework_two_result

    exam_homework2_result.short_description = "作业二成绩"

    def exam_homework3_result(self):
        return self.family.result.homework_three_result

    exam_homework3_result.short_description = "作业三成绩"

    def exam_result(self):
        return self.family.result.result

    exam_result.short_description = "合格情况"

    def exam_date_extra(self):
        return self.family.resultextra.date

    exam_date_extra.short_description = "补考日期"

    def exam_homework2_extra(self):
        return self.family.resultextra.homework_two_result

    exam_homework2_extra.short_description = "作业二成绩"

    def exam_homework3_extra(self):
        return self.family.resultextra.homework_three_result

    exam_homework3_extra.short_description = "作业三成绩"

    def exam_result_extra(self):
        return self.family.resultextra.result

    exam_result_extra.short_description = "合格情况"

    def cert_id(self):
        return self.family.familycertification.cert_id

    cert_id.short_description = "证书编号"

    def cert_date(self):
        return self.family.familycertification.cert_date

    cert_date.short_description = "发证日期"

    def cert_draw_people(self):
        return self.family.familycertification.cert_draw_people

    cert_draw_people.short_description = "领取人"

    def cert_draw_date(self):
        return self.family.familycertification.cert_draw_date

    cert_draw_date.short_description = "领取时间"

    def onduty(self):
        return self.family.familyonduty.onduty

    onduty.short_description = "出勤"

    def homework1(self):
        return self.family.familyonduty.homework1

    homework1.short_description = "作业一"
    def homework2(self):
        return self.family.familyonduty.homework2

    homework2.short_description = "作业二"
    def homework3(self):
        return self.family.familyonduty.homework3

    homework3.short_description = "作业三"
    def other(self):
        return self.family.familyonduty.other

    other.short_description = "备注"







