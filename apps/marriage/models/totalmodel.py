from django.db import models
from .marriagemodel import MarriageBasic
from django.utils.html import format_html
from .classmodel import MarriageClass
from .exammodel import MarriageExam
from .ondutymodel import MarriageOnduty
from .tuitionmodel import MarriageTuition
from .wechatmodel import MarriageWechat

class Total(models.Model):
    class Meta:
        verbose_name="婚姻指导信息总览"
        verbose_name_plural = verbose_name
    marriage = models.OneToOneField(MarriageBasic,on_delete=models.CASCADE,verbose_name="学生")

    def __str__(self):
        return str(self.marriage.mar_number)+"-"+str(self.marriage.mar_name)

    def mar_number(self):
        return self.marriage.mar_number

    mar_number.short_description = "学号"
    def mar_name(self):
        info = self.marriage.mar_name
        if self.marriage.marriagetuition.fee_date == '空':
            color_code = 'red'
        else:
            color_code = 'black'
        return format_html('<span style="color:{};">{}</span>', color_code, info)
    mar_name.short_description = u'姓名'
    mar_name.allow_tags = mar_name.is_column = True

    def mar_gender(self):
        return self.marriage.mar_gender

    mar_gender.short_description = "性别"

    def mar_class(self):
        return self.marriage.mar_class

    mar_class.short_description = "班级"

    def mar_class_num(self):
        return self.marriage.mar_class_num

    mar_class_num.short_description = "班级序号"

    def mar_type(self):
        return self.marriage.mar_type
    
    mar_type.short_description = "学员类型"

    def mar_group(self):
        return self.marriage.mar_group

    mar_group.short_description = "组别和职务"

    def mar_level(self):
        return self.marriage.mar_level

    mar_level.short_description = "级别"

    def mar_id_number(self):
        return self.marriage.mar_id_number

    mar_id_number.short_description = "身份证号"

    def mar_loc(self):
        return self.marriage.mar_loc

    mar_loc.short_description = "所在地"

    def mar_deg(self):
        return self.marriage.mar_deg

    mar_deg.short_description = "学历"

    def mar_major(self):
        return self.marriage.mar_major

    mar_major.short_description = "专业"

    def mar_company(self):
        return self.marriage.mar_company

    mar_company.short_description = "工作单位"

    def mar_duty(self):
        return self.marriage.mar_duty

    mar_duty.short_description = "职务"

    def mar_status(self):
        return self.marriage.mar_status

    mar_status.short_description = "职称"

    def mar_origin(self):
        return self.marriage.mar_origin

    mar_origin.short_description = "生源来源"

    def mar_cellphone(self):
        return self.marriage.mar_cellphone

    mar_cellphone.short_description = "手机号"

    def mar_wechat(self):
        return self.marriage.mar_wechat

    mar_wechat.short_description = "微信"

    def mar_email(self):
        return self.marriage.mar_email

    mar_email.short_description = "邮箱"

    def mar_signup_date(self):
        return self.marriage.mar_signup_date

    mar_signup_date.short_description = "报名日期"

    def mar_signup_people(self):
        return self.marriage.mar_signup_people

    mar_signup_people.short_description = "招生人"

    #def mar_teacher_level(self):
    #    return self.marriage.mar_teacher_level
    #mar_teacher_level.short_description = "心师级别"

    def mar_other(self):
        return self.marriage.mar_other

    mar_other.short_description = "备注"

    def fee_train(self):
        return self.marriage.marriagetuition.fee_train

    fee_train.short_description = "培训费"

    def fee_material(self):
        return self.marriage.marriagetuition.fee_material
    
    fee_material.short_description = "教材费"

    def fee_exam(self):
        return self.marriage.marriagetuition.fee_exam
    
    fee_exam.short_description = "考试费"

    def fee_total(self):
        return self.marriage.marriagetuition.fee_total
    
    fee_total.short_description = "总费用"

    def fee_date(self):
        return self.marriage.marriagetuition.fee_date

    fee_date.short_description = "缴费日期"

    def fee_method(self):
        return self.marriage.marriagetuition.fee_method

    fee_method.short_description = "缴费方式"

    def fee_tax(self):
        return self.marriage.marriagetuition.fee_tax

    fee_tax.short_description = "发票号"

    def fee_invoice_header(self):
        return self.marriage.marriagetuition.fee_invoice_header

    fee_invoice_header.short_description = "发票抬头"

    def fee_invoice_id(self):
        return self.marriage.marriagetuition.fee_invoice_id

    fee_invoice_id.short_description = "发票机构代码"

    def fee_invoice_date(self):
        return self.marriage.marriagetuition.fee_invoice_date

    fee_invoice_date.short_description = "发票开票日期"

    def fee_other(self):
        return self.marriage.marriagetuition.fee_other

    fee_other.short_description = "备注"


    def text_basic(self):
        return self.marriage.marriagetextbook.text_basic

    text_basic.short_description = "基础技能知识"

    def text_skill(self):
        return self.marriage.marriagetextbook.text_skil

    text_skill.short_description = "技能教材"

    def text_workbook(self):
        return self.marriage.marriagetextbook.text_workbook

    text_workbook.short_description = "习题集"

    def text_train(self):
        return self.marriage.marriagetextbook.text_reain

    text_train.short_description = "培训指南"

    def text_manual(self):
        return self.marriage.marriagetextbook.text_manual

    text_manual.short_description = "学员手册"

    def text_other(self):
        return self.marriage.marriagetextbook.text_other

    text_other.short_description = "备注"

    def wechat_number(self):
        return self.marriage.marriagewechat.wechat_number

    wechat_number.short_description = "平台绑定号码"

    def wechat_nickname(self):
        return self.marriage.marriagewechat.wechat_nickname

    wechat_nickname.short_description = "微信昵称"

    def wechat_date(self):
        return self.marriage.marriagewechat.wechat_date

    wechat_date.short_description = "开通日期"

    def wechat_other(self):
        return self.marriage.marriagewechat.wechat_other

    wechat_other.short_description = "备注"


    def exam_batch(self):
        return self.marriage.marriageexam.batch

    exam_batch.short_description = "考核批次"

    def exam_total(self):
        return self.marriage.marriageexam.exam_total

    exam_total.short_description = "总分"

    def exam_nation(self):
        return self.marriage.marriageexam.exam_nation

    exam_nation.short_description = "国考笔试成绩"

    def exam_practice(self):
        return self.marriage.marriageexam.exam_practice

    exam_practice.short_description = "实操考核成绩"

    def exam_other(self):
        return self.marriage.marriageexam.other

    exam_other.short_description = "备注"

    def ass_cert_id(self):
        return self.marriage.marriagecertification.ass_cert_id

    ass_cert_id.short_description = "协会证书编号"

    def ass_cert_date(self):
        return self.marriage.marriagecertification.ass_cert_date

    ass_cert_date.short_description = "协会证书发证日期"

    def ass_cert_draw_people(self):
        return self.marriage.marriagecertification.ass_cert_draw_people

    ass_cert_draw_people.short_description = "协会证书领取人"

    def ass_cert_draw_date(self):
        return self.marriage.marriagecertification.ass_cert_draw_date

    ass_cert_draw_date.short_description = "协会证书领取时间"

    def nation_cert_id(self):
        return self.marriage.marriagecertification.nation_cert_id

    nation_cert_id.short_description = "国证证书编号"

    def nation_cert_date(self):
        return self.marriage.marriagecertification.nation_cert_date

    nation_cert_date.short_description = "国证证书发证日期"

    def nation_cert_draw_people(self):
        return self.marriage.marriagecertification.nation_cert_draw_people

    nation_cert_draw_people.short_description = "国证证书领取人"

    def nation_cert_draw_date(self):
        return self.marriage.marriagecertification.nation_cert_draw_date

    nation_cert_draw_date.short_description = "国证证书领取时间"

    def cert_other(self):
        return self.marriage.marriagecertification.other

    cert_other.short_description = "备注"


    def ond_onduty(self):
        return self.marriage.marriageonduty.onduty

    ond_onduty.short_description = "出勤"

    def ond_homework(self):
        return self.marriage.marriageonduty.homework

    ond_homework.short_description = "作业打卡"

    def ond_other(self):
        return self.marriage.marriageonduty.other

    ond_other.short_description = "备注"







