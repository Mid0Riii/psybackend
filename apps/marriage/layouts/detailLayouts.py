from django.utils.translation import ugettext as _
from xadmin.layout import Fieldset, Main, Side, Row

BasicLayout = \
    (
        Main(
            Fieldset(_('个人信息'),
                     'mar_number',
                     'mar_name',
                     'mar_gender',
                     'mar_id_number',
                     'mar_loc',
                     'mar_class',
                     'mar_type',
                     'mar_group'
                     ),
            Fieldset(_('学历和专业'),
                     'mar_deg',
                     'mar_major',
                     ),
            Fieldset(_('工作信息'),
                     'mar_company',
                     'mar_duty',
                     'mar_status',
                     'mar_origin',
                     ),
            Fieldset(_('联系方式'),
                     'mar_cellphone',
                     'mar_wechat',
                     'mar_email',
                     ),
            Fieldset(_('报名信息'),
                     'mar_signup_date',
                     'mar_signup_people',
                    #  'mar_teacher_level',
                     )
        ),
        Side(
            Fieldset('其他信息',
                     'mar_other')
        ),
    )

TuitionLayout = \
    (
        Main(
            Fieldset(_('学生信息'),
                     'relate_marriage',
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
#                      'relate_marriage',
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
