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

    tea_gender.short_description = "性别"

    def tea_class(self):
        return self.team.tea_class

    tea_class.short_description = "班级"

    def tea_class_num(self):
        return self.team.tea_class_num

    tea_class_num.short_description = "班级序号"

    def tea_type(self):
        return self.team.tea_type
    
    tea_type.short_description = "学员类型"

    def tea_group(self):
        return self.team.tea_group

    tea_group.short_description = "组别和职务"

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

    def tea_email(self):
        return self.team.tea_email

    tea_email.short_description = "邮箱"

    def tea_signup_date(self):
        return self.team.tea_signup_date

    tea_signup_date.short_description = "报名日期"

    def tea_signup_people(self):
        return self.team.tea_signup_people

    tea_signup_people.short_description = "招生人"

    #def tea_teacher_level(self):
    #    return self.team.tea_teacher_level
    #tea_teacher_level.short_description = "心师级别"

    def tea_other(self):
        return self.team.tea_other

    tea_other.short_description = "备注"

    def fee_train(self):
        return self.team.teamtuition.fee_train

    fee_train.short_description = "培训费"

    def fee_material(self):
        return self.team.teamtuition.fee_material
    
    fee_material.short_description = "教材费"

    def fee_exam(self):
        return self.team.teamtuition.fee_exam
    
    fee_exam.short_description = "考试费"

    def fee_total(self):
        return self.team.teamtuition.fee_total
    
    fee_total.short_description = "总费用"

    def fee_date(self):
        return self.team.teamtuition.fee_date

    fee_date.short_description = "缴费日期"

    def fee_method(self):
        return self.team.teamtuition.fee_method

    fee_method.short_description = "缴费方式"

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

    def fee_other(self):
        return self.team.teamtuition.fee_other

    fee_other.short_description = "备注"


    def text_team(self):
        return self.team.teamtextbook.text_team

    text_team.short_description = "团体心理辅导"

    def text_two(self):
        return self.team.teamtextbook.text_two

    text_two.short_description = "教材2"

    def text_train(self):
        return self.team.teamtextbook.text_reain

    text_train.short_description = "培训指南"

    def text_manual(self):
        return self.team.teamtextbook.text_manual

    text_manual.short_description = "学员手册"

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

    def wechat_other(self):
        return self.team.teamwechat.wechat_other

    wechat_other.short_description = "备注"


    def exam_batch(self):
        return self.team.teamexam.batch

    exam_batch.short_description = "考核批次"

    def exam_total(self):
        return self.team.teamexam.exam_total

    exam_total.short_description = "总分"

    def exam_nation(self):
        return self.team.teamexam.exam_nation

    exam_nation.short_description = "国考笔试成绩"

    def exam_practice(self):
        return self.team.teamexam.exam_practice

    exam_practice.short_description = "实操考核成绩"

    def exam_other(self):
        return self.team.teamexam.other

    exam_other.short_description = "备注"

    def ass_cert_id(self):
        return self.team.teamcertification.ass_cert_id

    ass_cert_id.short_description = "协会证书编号"

    def ass_cert_date(self):
        return self.team.teamcertification.ass_cert_date

    ass_cert_date.short_description = "协会证书发证日期"

    def ass_cert_draw_people(self):
        return self.team.teamcertification.ass_cert_draw_people

    ass_cert_draw_people.short_description = "协会证书领取人"

    def ass_cert_draw_date(self):
        return self.team.teamcertification.ass_cert_draw_date

    ass_cert_draw_date.short_description = "协会证书领取时间"

    def nation_cert_id(self):
        return self.team.teamcertification.nation_cert_id

    nation_cert_id.short_description = "国证证书编号"

    def nation_cert_date(self):
        return self.team.teamcertification.nation_cert_date

    nation_cert_date.short_description = "国证证书发证日期"

    def nation_cert_draw_people(self):
        return self.team.teamcertification.nation_cert_draw_people

    nation_cert_draw_people.short_description = "国证证书领取人"

    def nation_cert_draw_date(self):
        return self.team.teamcertification.nation_cert_draw_date

    nation_cert_draw_date.short_description = "国证证书领取时间"

    def cert_other(self):
        return self.team.teamcertification.other

    cert_other.short_description = "备注"


    def ond_onduty(self):
        return self.team.teamonduty.onduty

    ond_onduty.short_description = "出勤"

    def ond_homework(self):
        return self.team.teamonduty.homework

    ond_homework.short_description = "作业打卡"

    def ond_other(self):
        return self.team.teamonduty.other

    ond_other.short_description = "备注"







