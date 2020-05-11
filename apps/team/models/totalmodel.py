from django.db import models
from .teammodel import TeamBasic
from django.utils.html import format_html
from .classmodel import TeamClass
from .exammodel import TeamExam
from .ondutymodel import TeamOnduty
from .tuitionmodel import TeamTuition
from .wechatmodel import TeamWechat

class Total(models.Model):
    class Meta:
        verbose_name="团体心理辅导信息总览"
        verbose_name_plural = verbose_name
    team = models.OneToOneField(TeamBasic,on_delete=models.CASCADE,verbose_name="学生")

    def __str__(self):
        return str(self.team.tea_number)+"-"+str(self.team.tea_name)

    def tea_number(self):
        return self.team.tea_number

    tea_number.short_description = "学号"
    def tea_name(self):
        info = self.team.tea_name
        if self.team.teamtuition.fee_date == '空':
            color_code = 'red'
        else:
            color_code = 'black'
        return format_html('<span style="color:{};">{}</span>', color_code, info)
    tea_name.short_description = u'姓名'
    tea_name.allow_tags = tea_name.is_column = True

    def tea_gender(self):
        return self.team.tea_gender

    tea_gender.short_description = "年龄"

    def tea_class(self):
        return self.team.tea_class

    tea_class.short_description = "班级"

    def tea_class_num(self):
        return self.team.tea_class_num

    tea_class_num.short_description = "班级序号"

    def tea_level(self):
        return self.team.tea_level

    tea_level.short_description = "级别"

    def tea_id_number(self):
        return self.team.tea_id_number

    tea_id_number.short_description = "身份证号"

    def tea_loc(self):
        return self.team.tea_loc

    tea_loc.short_description = "所在地"

    def tea_deg(self):
        return self.team.tea_deg

    tea_deg.short_description = "学历"

    def tea_major(self):
        return self.team.tea_major

    tea_major.short_description = "专业"

    def tea_company(self):
        return self.team.tea_company

    tea_company.short_description = "工作单位"

    def tea_duty(self):
        return self.team.tea_duty

    tea_duty.short_description = "职务"

    def tea_status(self):
        return self.team.tea_status

    tea_status.short_description = "职称"

    def tea_origin(self):
        return self.team.tea_origin

    tea_origin.short_description = "生源来源"

    def tea_cellphone(self):
        return self.team.tea_cellphone

    tea_cellphone.short_description = "手机号"

    def tea_wechat(self):
        return self.team.tea_wechat

    tea_wechat.short_description = "微信"

    def tea_qq(self):
        return self.team.tea_qq

    tea_qq.short_description = "qq"

    def tea_signup_date(self):
        return self.team.tea_signup_date

    tea_signup_date.short_description = "报名日期"

    def tea_signup_people(self):
        return self.team.tea_signup_people

    tea_signup_people.short_description = "具体招生人"

    def tea_teacher_level(self):
        return self.team.tea_teacher_level
    tea_teacher_level.short_description = "心师级别"

    def tea_other(self):
        return self.team.tea_other

    tea_other.short_description = "备注"

    def fee_train(self):
        return self.team.teamtuition.fee_train

    fee_train.short_description = "培训费"

    def fee_date(self):
        return self.team.teamtuition.fee_date

    fee_date.short_description = "缴费日期"

    def fee_method(self):
        return self.team.teamtuition.fee_method

    fee_method.short_description = "缴费方式"

    def fee_id(self):
        return self.team.teamtuition.fee_id

    fee_id.short_description = "收据号"

    def fee_tax(self):
        return self.team.teamtuition.fee_tax

    fee_tax.short_description = "发票号"

    def fee_invoice_header(self):
        return self.team.teamtuition.fee_invoice_header

    fee_invoice_header.short_description = "发票抬头"

    def fee_invoice_id(self):
        return self.team.teamtuition.fee_invoice_id

    fee_invoice_id.short_description = "发票机构代码"

    def fee_invoice_date(self):
        return self.team.teamtuition.fee_invoice_date

    fee_invoice_date.short_description = "发票开票日期"


    def text_basic(self):
        return self.team.teamtextbook.text_basic

    text_basic.short_description = "基础技能"

    def text_other(self):
        return self.team.teamtextbook.text_other

    text_other.short_description = "备注"

    def wechat_number(self):
        return self.team.teamwechat.wechat_number

    wechat_number.short_description = "平台绑定号码"

    def wechat_nickname(self):
        return self.team.teamwechat.wechat_nickname

    wechat_nickname.short_description = "微信昵称"

    def wechat_date(self):
        return self.team.teamwechat.wechat_date

    wechat_date.short_description = "开通日期"

    def exam_date(self):
        return self.team.teamexam.date

    exam_date.short_description = "考核日期"

    def exam_homework2_result(self):
        return self.team.teamexam.homework_two_result

    exam_homework2_result.short_description = "作业二成绩"

    def exam_homework3_result(self):
        return self.team.teamexam.homework_three_result

    exam_homework3_result.short_description = "作业三成绩"

    def exam_result(self):
        return self.team.teamexam.result

    exam_result.short_description = "合格情况"

    def exam_date_extra(self):
        return self.team.teamexamextra.date

    exam_date_extra.short_description = "补考日期"

    def exam_homework2_extra(self):
        return self.team.teamexamextra.homework_two_result

    exam_homework2_extra.short_description = "作业二成绩"

    def exam_homework3_extra(self):
        return self.team.teamexamextra.homework_three_result

    exam_homework3_extra.short_description = "作业三成绩"

    def exam_result_extra(self):
        return self.team.teamexamextra.result

    exam_result_extra.short_description = "合格情况"

    def cert_id(self):
        return self.team.teamcertification.cert_id

    cert_id.short_description = "证书编号"

    def cert_date(self):
        return self.team.teamcertification.cert_date

    cert_date.short_description = "发证日期"

    def cert_draw_people(self):
        return self.team.teamcertification.cert_draw_people

    cert_draw_people.short_description = "领取人"

    def cert_draw_date(self):
        return self.team.teamcertification.cert_draw_date

    cert_draw_date.short_description = "领取时间"

    def onduty(self):
        return self.team.teamonduty.onduty

    onduty.short_description = "出勤"

    def homework1(self):
        return self.team.teamonduty.homework1

    homework1.short_description = "作业一"
    def homework2(self):
        return self.team.teamonduty.homework2

    homework2.short_description = "作业二"
    def homework3(self):
        return self.team.teamonduty.homework3

    homework3.short_description = "作业三"
    def other(self):
        return self.team.teamonduty.other

    other.short_description = "备注"







