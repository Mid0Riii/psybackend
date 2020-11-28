from django.db import models
from .sandboxmodel import SandboxBasic
from django.utils.html import format_html
from .classmodel import SandboxClass
from .exammodel import SandboxExam
from .ondutymodel import SandboxOnduty
from .tuitionmodel import SandboxTuition
from .wechatmodel import SandboxWechat


class Total(models.Model):
    class Meta:
        verbose_name = "沙盘分析指导信息总览"
        verbose_name_plural = verbose_name

    sandbox = models.OneToOneField(SandboxBasic, on_delete=models.CASCADE, verbose_name="学生")

    def __str__(self):
        return str(self.sandbox.san_number) + "-" + str(self.sandbox.san_name)

    def san_number(self):
        return self.sandbox.san_number

    san_number.short_description = "学号"

    def san_name(self):
        info = self.sandbox.san_name
        if self.sandbox.sandboxtuition.fee_date == '空':
            color_code = 'red'
        else:
            color_code = 'black'
        return format_html('<span style="color:{};">{}</span>', color_code, info)

    san_name.short_description = u'姓名'
    san_name.allow_tags = san_name.is_column = True

    def san_gender(self):
        return self.sandbox.san_gender

    san_gender.short_description = "性别"

    def san_class(self):
        return self.sandbox.san_class

    san_class.short_description = "班级"

    def san_class_num(self):
        return self.sandbox.san_class_num

    san_class_num.short_description = "班级序号"

    def san_type(self):
        return self.sandbox.san_type

    san_type.short_description = "学员类型"

    def san_group(self):
        return self.sandbox.san_group

    san_group.short_description = "组别和职务"

    def san_level(self):
        return self.sandbox.san_level

    san_level.short_description = "级别"

    def san_id_number(self):
        return self.sandbox.san_id_number

    san_id_number.short_description = "身份证号"

    def san_loc(self):
        return self.sandbox.san_loc

    san_loc.short_description = "所在地"

    def san_deg(self):
        return self.sandbox.san_deg

    san_deg.short_description = "学历"

    def san_major(self):
        return self.sandbox.san_major

    san_major.short_description = "专业"

    def san_company(self):
        return self.sandbox.san_company

    san_company.short_description = "工作单位"

    def san_duty(self):
        return self.sandbox.san_duty

    san_duty.short_description = "职务"

    def san_status(self):
        return self.sandbox.san_status

    san_status.short_description = "职称"

    def san_origin(self):
        return self.sandbox.san_origin

    san_origin.short_description = "生源来源"

    def san_cellphone(self):
        return self.sandbox.san_cellphone

    san_cellphone.short_description = "手机号"

    def san_wechat(self):
        return self.sandbox.san_wechat

    san_wechat.short_description = "微信"

    def san_email(self):
        return self.sandbox.san_email

    san_email.short_description = "邮箱"

    def san_signup_date(self):
        return self.sandbox.san_signup_date

    san_signup_date.short_description = "报名日期"

    def san_signup_people(self):
        return self.sandbox.san_signup_people

    san_signup_people.short_description = "招生人"

    # def san_teacher_level(self):
    #    return self.sandbox.san_teacher_level
    # san_teacher_level.short_description = "心师级别"

    def san_other(self):
        return self.sandbox.san_other

    san_other.short_description = "备注"

    def fee_train(self):
        return self.sandbox.sandboxtuition.fee_train

    fee_train.short_description = "培训费"

    def fee_material(self):
        return self.sandbox.sandboxtuition.fee_material

    fee_material.short_description = "教材费"

    def fee_exam(self):
        return self.sandbox.sandboxtuition.fee_exam

    fee_exam.short_description = "考试费"

    def fee_total(self):
        return self.sandbox.sandboxtuition.fee_total

    fee_total.short_description = "总费用"

    def fee_date(self):
        return self.sandbox.sandboxtuition.fee_date

    fee_date.short_description = "缴费日期"

    def fee_method(self):
        return self.sandbox.sandboxtuition.fee_method

    fee_method.short_description = "缴费方式"

    def fee_tax(self):
        return self.sandbox.sandboxtuition.fee_tax

    fee_tax.short_description = "发票号"

    def fee_invoice_header(self):
        return self.sandbox.sandboxtuition.fee_invoice_header

    fee_invoice_header.short_description = "发票抬头"

    def fee_invoice_id(self):
        return self.sandbox.sandboxtuition.fee_invoice_id

    fee_invoice_id.short_description = "发票机构代码"

    def fee_invoice_date(self):
        return self.sandbox.sandboxtuition.fee_invoice_date

    fee_invoice_date.short_description = "发票开票日期"

    def fee_other(self):
        return self.sandbox.sandboxtuition.fee_other

    fee_other.short_description = "备注"

    def text_sandbox(self):
        return self.sandbox.sandboxtextbook.text_sandbox

    text_sandbox.short_description = "沙盘教材"

    def text_two(self):
        return self.sandbox.sandboxtextbook.text_two

    text_two.short_description = "教材2"

    def text_three(self):
        return self.sandbox.sandboxtextbook.text_three

    text_three.short_description = "教材3"

    def text_train(self):
        return self.sandbox.sandboxtextbook.text_reain

    text_train.short_description = "培训指南"

    def text_manual(self):
        return self.sandbox.sandboxtextbook.text_manual

    text_manual.short_description = "学员手册"

    def text_other(self):
        return self.sandbox.sandboxtextbook.text_other

    text_other.short_description = "备注"

    def wechat_number(self):
        return self.sandbox.sandboxwechat.wechat_number

    wechat_number.short_description = "平台绑定号码"

    def wechat_nickname(self):
        return self.sandbox.sandboxwechat.wechat_nickname

    wechat_nickname.short_description = "微信昵称"

    def wechat_date(self):
        return self.sandbox.sandboxwechat.wechat_date

    wechat_date.short_description = "开通日期"

    def wechat_other(self):
        return self.sandbox.sandboxwechat.wechat_other

    wechat_other.short_description = "备注"

    def exam_batch(self):
        return self.sandbox.sandboxexam.batch

    exam_batch.short_description = "考核批次"

    def exam_total(self):
        return self.sandbox.sandboxexam.exam_total

    exam_total.short_description = "总分"

    def exam_nation(self):
        return self.sandbox.sandboxexam.exam_nation

    exam_nation.short_description = "国考笔试成绩"

    def exam_practice(self):
        return self.sandbox.sandboxexam.exam_practice

    exam_practice.short_description = "实操考核成绩"

    def exam_other(self):
        return self.sandbox.sandboxexam.other

    exam_other.short_description = "备注"

    def ass_cert_id(self):
        return self.sandbox.sandboxcertification.ass_cert_id

    ass_cert_id.short_description = "协会证书编号"

    def ass_cert_date(self):
        return self.sandbox.sandboxcertification.ass_cert_date

    ass_cert_date.short_description = "协会证书发证日期"

    def ass_cert_draw_people(self):
        return self.sandbox.sandboxcertification.ass_cert_draw_people

    ass_cert_draw_people.short_description = "协会证书领取人"

    def ass_cert_draw_date(self):
        return self.sandbox.sandboxcertification.ass_cert_draw_date

    ass_cert_draw_date.short_description = "协会证书领取时间"

    def nation_cert_id(self):
        return self.sandbox.sandboxcertification.nation_cert_id

    nation_cert_id.short_description = "国证证书编号"

    def nation_cert_date(self):
        return self.sandbox.sandboxcertification.nation_cert_date

    nation_cert_date.short_description = "国证证书发证日期"

    def nation_cert_draw_people(self):
        return self.sandbox.sandboxcertification.nation_cert_draw_people

    nation_cert_draw_people.short_description = "国证证书领取人"

    def nation_cert_draw_date(self):
        return self.sandbox.sandboxcertification.nation_cert_draw_date

    nation_cert_draw_date.short_description = "国证证书领取时间"

    def cert_other(self):
        return self.sandbox.sandboxcertification.other

    cert_other.short_description = "备注"

    def ond_onduty(self):
        return self.sandbox.sandboxonduty.onduty

    ond_onduty.short_description = "出勤"

    def ond_homework(self):
        return self.sandbox.sandboxonduty.homework

    ond_homework.short_description = "作业打卡"

    def ond_other(self):
        return self.sandbox.sandboxonduty.other

    ond_other.short_description = "备注"
