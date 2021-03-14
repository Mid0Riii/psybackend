from django.utils.translation import ugettext as _
from xadmin.layout import Fieldset, Main, Side, Row

BasicLayout = \
    (
        Main(
            Fieldset(_('个人信息'),
                     'social_number',
                     'social_name',
                     'social_gender',
                     'social_id_number',
                     'social_loc',
                     'social_class',
                     'social_type',
                     'social_group'
                     ),
            Fieldset(_('学历和专业'),
                     'social_deg',
                     'social_major',
                     ),
            Fieldset(_('工作信息'),
                     'social_company',
                     'social_duty',
                     'social_status',
                     'social_origin',
                     ),
            Fieldset(_('联系方式'),
                     'social_cellphone',
                     'social_wechat',
                     'social_email',
                     ),
            Fieldset(_('报名信息'),
                     'social_signup_date',
                     'social_signup_people',
                     )
        ),
        Side(
            Fieldset('其他信息',
                     'social_other')
        ),
    )

TuitionLayout = \
    (
        Main(
            Fieldset(_('学生信息'),
                     'relate_social',
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
