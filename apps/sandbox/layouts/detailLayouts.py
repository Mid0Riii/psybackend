from django.utils.translation import ugettext as _
from xadmin.layout import Fieldset, Main, Side, Row

BasicLayout = \
    (
        Main(
            Fieldset(_('个人信息'),
                     'san_number',
                     'san_name',
                     'san_type',
                     'san_gender',
                     'san_id_number',
                     'san_loc',
                     'san_group',
                     'san_class',
                     'san_type',
                     'san_group'
                     ),
            Fieldset(_('学历和专业'),
                     'san_deg',
                     'san_major',
                     ),
            Fieldset(_('工作信息'),
                     'san_company',
                     'san_duty',
                     'san_status',
                     'san_origin',
                     ),
            Fieldset(_('联系方式'),
                     'san_cellphone',
                     'san_wechat',
                     'san_email',
                     ),
            Fieldset(_('报名信息'),
                     'san_signup_date',
                     'san_signup_people',
                    #  'san_teacher_level',
                     )
        ),
        Side(
            Fieldset('其他信息',
                     'san_other')
        ),
    )

TuitionLayout = \
    (
        Main(
            Fieldset(_('学生信息'),
                     'relate_sandbox',
                     'relate_class',
                     ),
            Fieldset(_('费用'),
                     'fee_train',
                     'fee_material',
                     'fee_exam',
                     'fee_total',
                     'fee_exam_extra',
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
#                      'relate_sandbox',
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
