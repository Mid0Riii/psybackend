from django.utils.translation import ugettext as _
from xadmin.layout import Fieldset, Main, Side, Row

BasicLayout = \
    (
        Main(
            Fieldset(_('个人信息'),
                     'tra_number',
                     'tra_name',
                     'tra_gender',
                     'tra_id_number',
                     'tra_loc',
                     'tra_class',
                     ),
            Fieldset(_('学历和专业'),
                     'tra_deg',
                     'tra_major',
                     ),
            Fieldset(_('工作信息'),
                     'tra_company',
                     'tra_duty',
                     'tra_status',
                     'tra_origin',
                     ),
            Fieldset(_('联系方式'),
                     'tra_cellphone',
                     'tra_wechat',
                     'tra_qq',
                     ),
            Fieldset(_('报名信息'),
                     'tra_signup_date',
                     'tra_signup_people',
                     'tra_teacher_level',
                     )
        ),
        Side(
            Fieldset('其他信息',
                     'tra_other')
        ),
    )

TuitionLayout = \
    (
        Main(
            Fieldset(_('学生信息'),
                     'relate_trainingclass',
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
                     'fee_id',
                     'fee_tax',
                     )
        ),
    )

# ExamLayout = \
#     (
#         Main(
#             Fieldset(_('学生信息'),
#                      'relate_trainingclass',
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
