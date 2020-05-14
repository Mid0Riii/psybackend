from django.utils.translation import ugettext as _
from xadmin.layout import Fieldset, Main, Side, Row

BasicLayout = \
    (
        Main(
            Fieldset(_('个人信息'),
                     'tea_number',
                     'tea_name',
                     'tea_gender',
                     'tea_id_number',
                     'tea_loc',
                     'tea_class',
                     'tea_type',
                     'tea_group'
                     ),
            Fieldset(_('学历和专业'),
                     'tea_deg',
                     'tea_major',
                     ),
            Fieldset(_('工作信息'),
                     'tea_company',
                     'tea_duty',
                     'tea_status',
                     'tea_origin',
                     ),
            Fieldset(_('联系方式'),
                     'tea_cellphone',
                     'tea_wechat',
                     'tea_email',
                     ),
            Fieldset(_('报名信息'),
                     'tea_signup_date',
                     'tea_signup_people',
                     )
        ),
        Side(
            Fieldset('其他信息',
                     'tea_other')
        ),
    )

TuitionLayout = \
    (
        Main(
            Fieldset(_('学生信息'),
                     'relate_team',
                     'relate_class',
                     ),
            Fieldset(_('费用'),
                     'fee_train',
                     'fee_material',
                     'fee_exam',
                     'fee_total',
                     ),
            Fieldset(_('交费信息'),
                     'fee_date',
                     'fee_method',
                     'fee_tax', 
                     )
        ),
    )

# ExamLayout = \
#     (
#         Main(
#             Fieldset(_('学生信息'),
#                      'relate_team',
#                      ),
#             Fieldset(_('报考信息'),
#                      'exam_date'
#                      ),
#             Fieldset(_('理论'),
#                      'exam_theory',
#                      'exam_theory_result'
#                      ),
#             Fieldset(_('实操'),
#                      'exam_practise',
#                      'exam_practise_result'
#                      ),
#             Fieldset(_('综合'),
#                      'exam_total',
#                      'exam_total_result'
#                      ),
#         ),
#         Side(
#             Fieldset(_('考试结果'),
#                      'exam_status'
#                      ),
#         ),
#     )
