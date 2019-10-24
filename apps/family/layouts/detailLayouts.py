from django.utils.translation import ugettext as _
from xadmin.layout import Fieldset, Main, Side, Row

BasicLayout = \
    (
        Main(
            Fieldset(_('个人信息'),
                     'fam_number',
                     'fam_name',
                     'fam_gender',
                     'fam_id_number',
                     'fam_loc',
                     'fam_class',
                     'fam_level'
                     ),
            Fieldset(_('学历和专业'),
                     'fam_deg',
                     'fam_major',
                     ),
            Fieldset(_('工作信息'),
                     'fam_company',
                     'fam_duty',
                     'fam_status',
                     'fam_origin',
                     ),
            Fieldset(_('联系方式'),
                     'fam_cellphone',
                     'fam_wechat',
                     'fam_qq',
                     ),
            Fieldset(_('报名信息'),
                     'fam_signup_date',
                     'fam_signup_people',
                     'fam_teacher_level',
                     )
        ),
        Side(
            Fieldset('其他信息',
                     'fam_other')
        ),
    )

TuitionLayout = \
    (
        Main(
            Fieldset(_('学生信息'),
                     'relate_family',
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
                     'fee_id'
                     )
        ),
    )

# ExamLayout = \
#     (
#         Main(
#             Fieldset(_('学生信息'),
#                      'relate_family',
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
