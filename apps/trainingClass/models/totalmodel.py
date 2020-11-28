from django.db import models
from .trainingclassmodel import TrainBasic
from django.utils.html import format_html
from .classmodel import TrainClass
from .resultmodel import Result
from .resultextramodel import ResultExtra
from .ondutymodel import TrainOnduty
from .tuitionmodel import TrainTuition
from .wechatmodel import TrainWechat


class Total(models.Model):
    class Meta:
        verbose_name = "训练班信息总览"
        verbose_name_plural = verbose_name

    trainingclass = models.OneToOneField(TrainBasic, on_delete=models.CASCADE, verbose_name="学生")

    def __str__(self):
        return str(self.trainingclass.tra_number) + "-" + str(self.trainingclass.tra_name)

    def tra_type(self):
        return self.trainingclass.tra_type

    tra_type.short_description = "学员类型"

    def tra_group(self):
        return self.trainingclass.tra_group

    tra_group.short_description = "组别与职务"

    def tra_number(self):

        return self.trainingclass.tra_number

    tra_number.short_description = "学号"

    def tra_name(self):
        info = self.trainingclass.tra_name
        if self.trainingclass.traintuition.fee_date == '空':
            color_code = 'red'
        else:
            color_code = 'black'
        return format_html('<span style="color:{};">{}</span>', color_code, info)

    tra_name.short_description = u'姓名'
    tra_name.allow_tags = tra_name.is_column = True

    def tra_gender(self):
        return self.trainingclass.tra_gender

    tra_gender.short_description = "年龄"

    def tra_class(self):
        return self.trainingclass.tra_class

    tra_class.short_description = "班级"

    def tra_class_num(self):
        return self.trainingclass.tra_class_num

    tra_class_num.short_description = "班级序号"

    # def tra_level(self):
    #     return self.trainingclass.tra_level
    #
    # tra_level.short_description = "级别"

    def tra_id_number(self):
        return self.trainingclass.tra_id_number

    tra_id_number.short_description = "身份证号"

    def tra_loc(self):
        return self.trainingclass.tra_loc

    tra_loc.short_description = "所在地"

    def tra_deg(self):
        return self.trainingclass.tra_deg

    tra_deg.short_description = "学历"

    def tra_major(self):
        return self.trainingclass.tra_major

    tra_major.short_description = "专业"

    def tra_company(self):
        return self.trainingclass.tra_company

    tra_company.short_description = "工作单位"

    def tra_duty(self):
        return self.trainingclass.tra_duty

    tra_duty.short_description = "职务"

    def tra_status(self):
        return self.trainingclass.tra_status

    tra_status.short_description = "职称"

    def tra_origin(self):
        return self.trainingclass.tra_origin

    tra_origin.short_description = "生源来源"

    def tra_cellphone(self):
        return self.trainingclass.tra_cellphone

    tra_cellphone.short_description = "手机号"

    def tra_wechat(self):
        return self.trainingclass.tra_wechat

    tra_wechat.short_description = "微信"

    def tra_qq(self):
        return self.trainingclass.tra_qq

    tra_qq.short_description = "邮箱"

    def tra_signup_date(self):
        return self.trainingclass.tra_signup_date

    tra_signup_date.short_description = "报名日期"

    def tra_signup_people(self):
        return self.trainingclass.tra_signup_people

    tra_signup_people.short_description = "具体招生人"

    # def tra_teacher_level(self):
    #     return self.trainingclass.tra_teacher_level
    # tra_teacher_level.short_description = "心师级别"

    def tra_other(self):
        return self.trainingclass.tra_other

    tra_other.short_description = "备注"

    def fee_train(self):
        return self.trainingclass.traintuition.fee_train

    fee_train.short_description = "培训费"

    def fee_material(self):
        return self.trainingclass.traintuition.fee_material

    fee_material.short_description = "教材费"

    def fee_exam(self):
        return self.trainingclass.traintuition.fee_exam

    fee_exam.short_description = "考试费"

    def fee_total(self):
        return self.trainingclass.traintuition.fee_total

    fee_total.short_description = "总费用"

    def fee_date(self):
        return self.trainingclass.traintuition.fee_date

    fee_date.short_description = "缴费日期"

    def fee_method(self):
        return self.trainingclass.traintuition.fee_method

    fee_method.short_description = "缴费方式"

    def fee_id(self):
        return self.trainingclass.traintuition.fee_id

    fee_id.short_description = "收据号"

    def fee_tax(self):
        return self.trainingclass.traintuition.fee_tax

    fee_tax.short_description = "发票号"

    def fee_invoice_header(self):
        return self.trainingclass.traintuition.fee_invoice_header

    fee_invoice_header.short_description = "发票抬头"

    def fee_invoice_id(self):
        return self.trainingclass.traintuition.fee_invoice_id

    fee_invoice_id.short_description = "发票机构代码"

    def fee_invoice_date(self):
        return self.trainingclass.traintuition.fee_invoice_date

    fee_invoice_date.short_description = "发票开票日期"

    def fee_invoice_inc(self):
        return self.trainingclass.traintuition.fee_invoice_inc

    fee_invoice_inc.short_description = "出票单位"

    def fee_other(self):
        return self.trainingclass.traintuition.fee_info

    fee_other.short_description = "备注"

    def text_basic(self):
        return self.trainingclass.traintextbook.text_basic

    text_basic.short_description = "教材1"

    def text_basic2(self):
        return self.trainingclass.traintextbook.text_basic2

    text_basic2.short_description = "教材2"

    def text_guide(self):
        return self.trainingclass.traintextbook.text_guide

    text_guide.short_description = "培训指南"

    def text_manual(self):
        return self.trainingclass.traintextbook.text_manual

    text_manual.short_description = "学员手册"

    def text_other(self):
        return self.trainingclass.traintextbook.text_other

    text_other.short_description = "备注"

    def wechat_number(self):
        return self.trainingclass.trainwechat.wechat_number

    wechat_number.short_description = "平台绑定号码"

    def wechat_nickname(self):
        return self.trainingclass.trainwechat.wechat_nickname

    wechat_nickname.short_description = "微信昵称"

    def wechat_date(self):
        return self.trainingclass.trainwechat.wechat_date

    wechat_date.short_description = "开通日期"

    def onduty(self):
        return self.trainingclass.trainonduty.onduty

    onduty.short_description = "出勤率"

    def homework(self):
        return self.trainingclass.trainonduty.homework

    homework.short_description = "视频提交"

    def other(self):
        return self.trainingclass.trainonduty.other

    homework.short_description = "视频提交"

    def exam_date(self):
        return self.trainingclass.result.date

    exam_date.short_description = "考试日期"

    def exam_total(self):
        return self.trainingclass.result.total

    exam_total.short_description = "总分"

    def exam_nation(self):
        return self.trainingclass.result.nation_result

    exam_nation.short_description = "国考笔试成绩"

    def exam_pre(self):
        return self.trainingclass.result.pre

    exam_pre.short_description = "说课分"

    def exam_speech(self):
        return self.trainingclass.result.speech

    exam_speech.short_description = "宣讲分"

    def exam_other(self):
        return self.trainingclass.result.other

    exam_other.short_description = "备注"

    # def exam_homework2_result(self):
    #     return self.trainingclass.result.homework_two_result
    #
    # exam_homework2_result.short_description = "作业二成绩"
    #
    # def exam_homework3_result(self):
    #     return self.trainingclass.result.homework_three_result
    #
    # exam_homework3_result.short_description = "作业三成绩"

    # def exam_result(self):
    #     return self.trainingclass.result.result
    #
    # exam_result.short_description = "合格情况"

    # def exam_date_extra(self):
    #     return self.trainingclass.resultextra.date
    #
    # exam_date_extra.short_description = "补考日期"
    #
    # def exam_homework2_extra(self):
    #     return self.trainingclass.resultextra.homework_two_result
    #
    # exam_homework2_extra.short_description = "作业二成绩"
    #
    # def exam_homework3_extra(self):
    #     return self.trainingclass.resultextra.homework_three_result
    #
    # exam_homework3_extra.short_description = "作业三成绩"
    #
    # def exam_result_extra(self):
    #     return self.trainingclass.resultextra.result
    #
    # exam_result_extra.short_description = "合格情况"

    def cert_id(self):
        return self.trainingclass.traincertification.cert_id

    cert_id.short_description = "协会证书编号"

    # def cert_date(self):
    #     return self.trainingclass.traincertification.cert_date
    #
    # cert_date.short_description = "发证日期"

    def cert_draw_people(self):
        return self.trainingclass.traincertification.cert_draw_people

    cert_draw_people.short_description = "领取人"

    def cert_draw_date(self):
        return self.trainingclass.traincertification.cert_draw_date

    cert_draw_date.short_description = "领取时间"

    def cert_nation_id(self):
        return self.trainingclass.traincertification.cert_nation_id

    cert_nation_id.short_description = "国证编号"

    def cert_nation_people(self):
        return self.trainingclass.traincertification.cert_nation_people

    cert_nation_people.short_description = "领取人与日期"

    def cert_other(self):
        return self.trainingclass.traincertification.cert_other

    cert_other.short_description = "备注"
