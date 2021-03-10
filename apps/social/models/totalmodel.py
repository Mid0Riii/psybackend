from django.db import models
from .socialmodel import SocialBasic
from django.utils.html import format_html
from .classmodel import SocialClass
from .exammodel import SocialExam
from .ondutymodel import SocialOnduty
from .tuitionmodel import SocialTuition
from .wechatmodel import SocialWechat


class Total(models.Model):
    class Meta:
        verbose_name = "社会工作师信息总览"
        verbose_name_plural = verbose_name

    social = models.OneToOneField(SocialBasic, on_delete=models.CASCADE, verbose_name="学生")

    def __str__(self):
        return str(self.social.social_number) + "-" + str(self.social.social_name)

    def social_number(self):
        return self.social.social_number

    social_number.short_description = "学号"

    def social_name(self):
        info = self.social.social_name
        if self.social.socialtuition.fee_date == '空':
            color_code = 'red'
        else:
            color_code = 'black'
        return format_html('<span style="color:{};">{}</span>', color_code, info)

    social_name.short_description = u'姓名'
    social_name.allow_tags = social_name.is_column = True

    def social_gender(self):
        return self.social.social_gender

    social_gender.short_description = "性别"

    def social_class(self):
        return self.social.social_class

    social_class.short_description = "班级"

    def social_class_num(self):
        return self.social.social_class_num

    social_class_num.short_description = "班级序号"

    def social_type(self):
        return self.social.social_type

    social_type.short_description = "学员类型"

    def social_group(self):
        return self.social.social_group

    social_group.short_description = "组别和职务"

    def social_id_number(self):
        return self.social.social_id_number

    social_id_number.short_description = "身份证号"

    def social_loc(self):
        return self.social.social_loc

    social_loc.short_description = "所在地"

    def social_deg(self):
        return self.social.social_deg

    social_deg.short_description = "学历"

    def social_major(self):
        return self.social.social_major

    social_major.short_description = "专业"

    def social_company(self):
        return self.social.social_company

    social_company.short_description = "工作单位"

    def social_duty(self):
        return self.social.social_duty

    social_duty.short_description = "职务"

    def social_status(self):
        return self.social.social_status

    social_status.short_description = "职称"

    def social_origin(self):
        return self.social.social_origin

    social_origin.short_description = "生源来源"

    def social_cellphone(self):
        return self.social.social_cellphone

    social_cellphone.short_description = "手机号"

    def social_wechat(self):
        return self.social.social_wechat

    social_wechat.short_description = "微信"

    def social_email(self):
        return self.social.social_email

    social_email.short_description = "邮箱"

    def social_signup_date(self):
        return self.social.social_signup_date

    social_signup_date.short_description = "报名日期"

    def social_signup_people(self):
        return self.social.social_signup_people

    social_signup_people.short_description = "招生人"

    # def social_teacher_level(self):
    #    return self.social.social_teacher_level
    # social_teacher_level.short_description = "心师级别"

    def social_other(self):
        return self.social.social_other

    social_other.short_description = "备注"

    def fee_train(self):
        return self.social.socialtuition.fee_train

    fee_train.short_description = "培训费"

    def fee_material(self):
        return self.social.socialtuition.fee_material

    fee_material.short_description = "教材费"

    def fee_exam(self):
        return self.social.socialtuition.fee_exam

    fee_exam.short_description = "考试费"

    def fee_total(self):
        return self.social.socialtuition.fee_total

    fee_total.short_description = "总费用"

    def fee_date(self):
        return self.social.socialtuition.fee_date

    fee_date.short_description = "缴费日期"

    def fee_method(self):
        return self.social.socialtuition.fee_method

    fee_method.short_description = "缴费方式"

    def fee_tax(self):
        return self.social.socialtuition.fee_tax

    fee_tax.short_description = "发票号"

    def fee_invoice_header(self):
        return self.social.socialtuition.fee_invoice_header

    fee_invoice_header.short_description = "发票抬头"

    def fee_invoice_id(self):
        return self.social.socialtuition.fee_invoice_id

    fee_invoice_id.short_description = "发票机构代码"

    def fee_invoice_date(self):
        return self.social.socialtuition.fee_invoice_date

    fee_invoice_date.short_description = "发票开票日期"

    def fee_other(self):
        return self.social.socialtuition.fee_other

    fee_other.short_description = "备注"

    def text_basic(self):
        return self.social.socialtextbook.text_basic

    text_basic.short_description = "基础技能知识"

    def text_skill(self):
        return self.social.socialtextbook.text_skil

    text_skill.short_description = "技能教材"

    def text_workbook(self):
        return self.social.socialtextbook.text_workbook

    text_workbook.short_description = "习题集"

    def text_train(self):
        return self.social.socialtextbook.text_reain

    text_train.short_description = "培训指南"

    def text_manual(self):
        return self.social.socialtextbook.text_manual

    text_manual.short_description = "学员手册"

    def text_other(self):
        return self.social.socialtextbook.text_other

    text_other.short_description = "备注"

    def wechat_number(self):
        return self.social.socialwechat.wechat_number

    wechat_number.short_description = "平台绑定号码"

    def wechat_nickname(self):
        return self.social.socialwechat.wechat_nickname

    wechat_nickname.short_description = "微信昵称"

    def wechat_date(self):
        return self.social.socialwechat.wechat_date

    wechat_date.short_description = "开通日期"

    def wechat_other(self):
        return self.social.socialwechat.wechat_other

    wechat_other.short_description = "备注"

    def exam_batch(self):
        return self.social.socialexam.batch

    exam_batch.short_description = "考核批次"

    def exam_total(self):
        return self.social.socialexam.exam_total

    exam_total.short_description = "总分"

    def exam_nation(self):
        return self.social.socialexam.exam_nation

    exam_nation.short_description = "国考笔试成绩"

    def exam_practice(self):
        return self.social.socialexam.exam_practice

    exam_practice.short_description = "实操考核成绩"

    def exam_other(self):
        return self.social.socialexam.other

    exam_other.short_description = "备注"

    def ass_cert_id(self):
        return self.social.socialcertification.ass_cert_id

    ass_cert_id.short_description = "协会证书编号"

    def ass_cert_date(self):
        return self.social.socialcertification.ass_cert_date

    ass_cert_date.short_description = "协会证书发证日期"

    def ass_cert_draw_people(self):
        return self.social.socialcertification.ass_cert_draw_people

    ass_cert_draw_people.short_description = "协会证书领取人"

    def ass_cert_draw_date(self):
        return self.social.socialcertification.ass_cert_draw_date

    ass_cert_draw_date.short_description = "协会证书领取时间"

    def nation_cert_id(self):
        return self.social.socialcertification.nation_cert_id

    nation_cert_id.short_description = "国证证书编号"

    def nation_cert_date(self):
        return self.social.socialcertification.nation_cert_date

    nation_cert_date.short_description = "国证证书发证日期"

    def nation_cert_draw_people(self):
        return self.social.socialcertification.nation_cert_draw_people

    nation_cert_draw_people.short_description = "国证证书领取人"

    def nation_cert_draw_date(self):
        return self.social.socialcertification.nation_cert_draw_date

    nation_cert_draw_date.short_description = "国证证书领取时间"

    def cert_other(self):
        return self.social.socialcertification.other

    cert_other.short_description = "备注"

    def ond_onduty(self):
        return self.social.socialonduty.onduty

    ond_onduty.short_description = "出勤"

    def ond_homework(self):
        return self.social.socialonduty.homework

    ond_homework.short_description = "作业打卡"

    def ond_other(self):
        return self.social.socialonduty.other

    ond_other.short_description = "备注"
