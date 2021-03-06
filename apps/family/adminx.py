import xadmin
from django.utils.html import format_html
from .models import FamilyBasic, FamilyCertification, Result, ResultExtra, FamilyTextbook, \
    FamilyTuition, FamilyWechat, FamilyClass, FamilyOnduty, Total
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, BooleanWidget
from django.apps import apps
from .layouts.detailLayouts import BasicLayout, TuitionLayout


# TODO CODEREVIEW 外键后台inline显示的用法
# class TuitionInline(object):
#     model = FamilyTuition
#     extra = 1
#     style='one'
#     # readonly_fields=['fee_material', 'fee_exam', 'fee_total',
#                     'fee_exam_extra', 'fee_date', 'fee_method', 'fee_id']


class FamilyBasicResources(resources.ModelResource):
    # import—export中文列名的最终解决方案
    @classmethod
    def field_from_django_field(cls, field_name, django_field, readonly):
        FieldWidget = cls.widget_from_django_field(django_field)
        widget_kwargs = cls.widget_kwargs_for_field(field_name)
        field = cls.DEFAULT_RESOURCE_FIELD(
            attribute=field_name,
            # 重写column_name
            column_name=django_field.verbose_name,
            widget=FieldWidget(**widget_kwargs),
            readonly=readonly,
            default=django_field.default,
        )
        return field

    class ClassForeignWidget(ForeignKeyWidget):
        def get_queryset(self, value, row, *args, **kwargs):
            return FamilyClass.objects.filter(
                class_name__iexact=row["班级"]
            )

    fam_class = fields.Field(
        attribute='fam_class',
        column_name='fam_class',
        widget=ClassForeignWidget(FamilyClass, 'class_name')
    )

    class Meta:
        model = FamilyBasic
        import_id_fields = ('fam_number',)
        # 导入数据时，如果该条数据未修改过，则会忽略
        skip_unchanged = True
        # 在导入预览页面中显示跳过的记录
        report_skipped = True
        fields = (
            'fam_type', 'fam_group',
            'fam_number', 'fam_name', 'fam_gender', 'fam_class', 'fam_class_num', 'fam_id_number',
            'fam_loc', 'fam_deg', 'fam_major',
            'fam_company', 'fam_duty',
            'fam_status', 'fam_origin', 'fam_cellphone', 'fam_wechat', 'fam_qq',
            'fam_signup_date', 'fam_signup_people', 'fam_other')


@xadmin.sites.register(FamilyBasic)
class BasicAdmin(object):
    """
    家庭基本信息
    """

    list_display = ['fam_type', 'fam_group', 'fam_number', 'tuition_state', 'fam_gender', 'fam_class', 'fam_class_num',
                    'fam_id_number',
                    'fam_loc', 'fam_deg',
                    'fam_major',
                    'fam_company', 'fam_duty',
                    'fam_status', 'fam_origin', 'fam_cellphone', 'fam_wechat', 'fam_qq',
                    'fam_signup_date', 'fam_signup_people', 'fam_other']
    import_export_args = {'import_resource_class': FamilyBasicResources}
    list_filter = ['fam_type', 'fam_group', 'fam_number', 'fam_name', 'fam_gender', 'fam_class', 'fam_class_num',
                   'fam_id_number',
                   'fam_loc', 'fam_deg',
                   'fam_major',
                   'fam_company', 'fam_duty',
                   'fam_status', 'fam_origin', 'fam_cellphone', 'fam_wechat', 'fam_qq',
                   'fam_signup_date', 'fam_signup_people', 'fam_other', 'fam_class__class_name', ]
    list_editable = list_display
    exclude = ['fam_teacher_level', ]
    list_display_links = ['fam_number']
    search_fields = ['fam_number', 'fam_name', 'fam_class__class_name']
    show_bookmarks = False

    def tuition_state(self, obj):
        info = obj.fam_name
        if obj.familytuition.fee_date == '空':
            color_code = 'red'
            # info = '无交费信息'
        else:
            color_code = 'black'
            # info = '已交费'
        return format_html('<span style="color:{};">{}</span>', color_code, info)

    tuition_state.short_description = '姓名'
    tuition_state.admin_order_field = 'fam_name'

    def get_form_layout(self):
        self.form_layout = BasicLayout
        return super().get_form_layout()


class ClassResources(resources.ModelResource):
    # import—export中文列名的最终解决方案
    @classmethod
    def field_from_django_field(cls, field_name, django_field, readonly):
        FieldWidget = cls.widget_from_django_field(django_field)
        widget_kwargs = cls.widget_kwargs_for_field(field_name)
        field = cls.DEFAULT_RESOURCE_FIELD(
            attribute=field_name,
            # 重写column_name
            column_name=django_field.verbose_name,
            widget=FieldWidget(**widget_kwargs),
            readonly=readonly,
            default=django_field.default,
        )
        return field

    class Meta:
        model = FamilyClass
        fields = ('class_name', 'class_teacher', 'class_recruit_teacher', 'class_date')
        # 导入数据时，如果该条数据未修改过，则会忽略
        skip_unchanged = True
        # 在导入预览页面中显示跳过的记录
        report_skipped = True
        # 模型主键
        import_id_fields = ('class_name',)


@xadmin.sites.register(FamilyClass)
class ClassAdmin(object):
    '''
    班级信息
    '''

    import_export_args = {'import_resource_class': ClassResources,
                          }
    list_display = ['class_name', 'class_index', 'class_id_example', 'class_teacher', 'class_recruit_teacher',
                    'class_date']
    list_filter = list_display
    search_fields = list_display
    show_bookmarks = False
    ordering = ['-class_index']


class TuitionResources(resources.ModelResource):
    # import—export中文列名的最终解决方案
    @classmethod
    def field_from_django_field(cls, field_name, django_field, readonly):
        FieldWidget = cls.widget_from_django_field(django_field)
        widget_kwargs = cls.widget_kwargs_for_field(field_name)
        field = cls.DEFAULT_RESOURCE_FIELD(
            attribute=field_name,
            # 重写column_name
            column_name=django_field.verbose_name,
            widget=FieldWidget(**widget_kwargs),
            readonly=readonly,
            default=django_field.default,
        )
        return field

    class TuitionForeignWidget(ForeignKeyWidget):
        def get_queryset(self, value, row, *args, **kwargs):
            return FamilyBasic.objects.filter(
                fam_number__iexact=row["relate_family"]
            )

    relate_family = fields.Field(
        attribute='relate_family',
        column_name='relate_family',
        widget=TuitionForeignWidget(FamilyBasic, 'fam_number')
    )

    class Meta:
        model = FamilyTuition
        import_id_fields = ('relate_family',)
        # 导入数据时，如果该条数据未修改过，则会忽略
        skip_unchanged = True
        # 在导入预览页面中显示跳过的记录
        report_skipped = True
        fields = ('relate_family', 'fee_train', 'fee_material', 'fee_date', 'fee_method', 'fee_id', 'fee_tax',
                  'fee_invoice_header',
                  'fee_invoice_id', 'fee_invoice_date', 'fee_invoice_inc')


@xadmin.sites.register(FamilyTuition)
class TuitionAdmin(object):
    """
    交费信息
    """

    list_display = ['relate_family', 'get_fam_name', 'get_fam_class', 'fee_train', 'fee_material', 'fee_exam',
                    'fee_total', 'fee_date', 'fee_method', 'fee_id', 'fee_tax', 'fee_invoice_header',
                    'fee_invoice_id', 'fee_invoice_date', 'fee_invoice_inc']
    # TODO CODEVIEW filter中外键的处理
    list_filter = ['relate_family__fam_name', 'relate_family__fam_class__class_name', 'fee_tax', 'fee_train',
                   'fee_material', 'fee_exam', 'fee_total', 'fee_date', 'fee_method', 'fee_id', 'fee_tax',
                   'fee_invoice_header',
                   'fee_invoice_id', 'fee_invoice_date', 'fee_invoice_inc']
    show_bookmarks = False
    import_export_args = {'import_resource_class': TuitionResources,
                          }
    search_fields = ['relate_family__fam_name', 'relate_family__fam_number', 'relate_family__fam_number',
                     'relate_family__fam_class__class_name']
    list_editable = ['fee_train', 'fee_material', 'fee_date', 'fee_method', 'fee_id', 'fee_tax', 'fee_invoice_header',
                     'fee_invoice_id', 'fee_invoice_date', 'fee_invoice_inc']

    # readonly_fields = ['relate_family']

    def get_form_layout(self):
        self.form_layout = TuitionLayout
        return super().get_form_layout()


class TextbookResources(resources.ModelResource):
    # import—export中文列名的最终解决方案
    @classmethod
    def field_from_django_field(cls, field_name, django_field, readonly):
        FieldWidget = cls.widget_from_django_field(django_field)
        widget_kwargs = cls.widget_kwargs_for_field(field_name)
        field = cls.DEFAULT_RESOURCE_FIELD(
            attribute=field_name,
            # 重写column_name
            column_name=django_field.verbose_name,
            widget=FieldWidget(**widget_kwargs),
            readonly=readonly,
            default=django_field.default,
        )
        return field

    class TextbookForeignWidget(ForeignKeyWidget):
        def get_queryset(self, value, row, *args, **kwargs):
            return FamilyBasic.objects.filter(
                fam_number__iexact=row["relate_family"]
            )

    relate_family = fields.Field(
        attribute='relate_family',
        column_name='relate_family',
        widget=TextbookForeignWidget(FamilyBasic, 'fam_number')
    )

    class Meta:
        model = FamilyTextbook
        import_id_fields = ('relate_family',)
        # 导入数据时，如果该条数据未修改过，则会忽略
        skip_unchanged = True
        # 在导入预览页面中显示跳过的记录
        report_skipped = True
        fields = ('relate_family', 'text_basic', 'text_basic2', 'text_guide', 'text_manual', 'text_other')


@xadmin.sites.register(FamilyTextbook)
class TextbookAdmin(object):
    """
    教材信息
    """
    import_export_args = {'import_resource_class': TextbookResources, }
    list_display = ['relate_family', 'get_fam_name', 'get_fam_class', 'text_basic', 'text_basic2', 'text_guide',
                    'text_manual', 'text_other']
    list_filter = ['relate_family__fam_name', 'relate_family__fam_number', 'text_basic', 'text_other',
                   'relate_family__fam_class__class_name', 'text_basic2', 'text_guide', ]
    search_fields = ['relate_family__fam_name', 'relate_family__fam_number', 'relate_family__fam_class__class_name']
    # readonly_fields = ['relate_family']
    list_editable = ['text_basic', 'text_manual', 'text_other', 'text_basic2', 'text_guide', ]
    show_bookmarks = False


class WechatResources(resources.ModelResource):
    # import—export中文列名的最终解决方案
    @classmethod
    def field_from_django_field(cls, field_name, django_field, readonly):
        FieldWidget = cls.widget_from_django_field(django_field)
        widget_kwargs = cls.widget_kwargs_for_field(field_name)
        field = cls.DEFAULT_RESOURCE_FIELD(
            attribute=field_name,
            # 重写column_name
            column_name=django_field.verbose_name,
            widget=FieldWidget(**widget_kwargs),
            readonly=readonly,
            default=django_field.default,
        )
        return field

    class WechatForeignWidget(ForeignKeyWidget):
        def get_queryset(self, value, row, *args, **kwargs):
            return FamilyBasic.objects.filter(
                fam_number__iexact=row["relate_family"]
            )

    relate_family = fields.Field(
        attribute='relate_family',
        column_name='relate_family',
        widget=WechatForeignWidget(FamilyBasic, 'fam_number')
    )

    class Meta:
        model = FamilyWechat
        import_id_fields = ('relate_family',)
        # 导入数据时，如果该条数据未修改过，则会忽略
        skip_unchanged = True
        # 在导入预览页面中显示跳过的记录
        report_skipped = True
        fields = ('relate_family', 'wechat_number', 'wechat_nickname', 'wechat_date', 'wechat_other')


@xadmin.sites.register(FamilyWechat)
class WechatAdmin(object):
    """
    365开通情况
    """
    import_export_args = {'import_resource_class': WechatResources, }
    list_display = ['relate_family', 'get_fam_name', 'get_fam_class', 'wechat_number', 'wechat_nickname',
                    'wechat_date', 'wechat_other', ]
    list_filter = ['relate_family__fam_name', 'relate_family__fam_number', 'wechat_number', 'wechat_nickname',
                   'wechat_date', 'relate_family__fam_class__class_name']
    search_fields = ['relate_family__fam_name', 'relate_family__fam_number', 'relate_family__fam_class__class_name']
    # readonly_fields = ['relate_family']
    list_editable = ['wechat_number', 'wechat_nickname', 'wechat_date', 'wechat_other']
    show_bookmarks = False


class ExamResources(resources.ModelResource):
    # import—export中文列名的最终解决方案
    @classmethod
    def field_from_django_field(cls, field_name, django_field, readonly):
        FieldWidget = cls.widget_from_django_field(django_field)
        widget_kwargs = cls.widget_kwargs_for_field(field_name)
        field = cls.DEFAULT_RESOURCE_FIELD(
            attribute=field_name,
            # 重写column_name
            column_name=django_field.verbose_name,
            widget=FieldWidget(**widget_kwargs),
            readonly=readonly,
            default=django_field.default,
        )
        return field

    relate_family = fields.Field(
        attribute='relate_family',
        column_name='学号',
        widget=ForeignKeyWidget(FamilyBasic, 'fam_number')
    )

    class Meta:
        model = Result
        import_id_fields = ('relate_family',)
        # 导入数据时，如果该条数据未修改过，则会忽略
        skip_unchanged = True
        # 在导入预览页面中显示跳过的记录
        report_skipped = True
        fields = ('relate_family', 'date', 'total', 'nation_result', 'pre', 'speech', 'result', 'other')


@xadmin.sites.register(Result)
class ExamAdmin(object):
    """
    考试信息
    """
    import_export_args = {'import_resource_class': ExamResources, }
    list_display = ['relate_family', 'get_fam_name', 'get_fam_id_number', 'get_fam_class', 'date',
                    'total', 'nation_result', 'pre', 'speech', 'result', 'other']
    list_filter = ['relate_family__fam_name', 'relate_family__fam_number', 'relate_family__fam_class__class_name',
                   'date', 'homework_two_result', 'homework_three_result', 'result', 'total', 'nation_result', 'pre',
                   'speech', 'result', 'other']
    list_editable = ['date', 'total', 'nation_result', 'pre', 'speech', 'result', 'other']
    show_bookmarks = False
    exclude = ['homework_one_result', 'homework_two_result', 'result']
    search_fields = ['relate_family__fam_name', 'relate_family__fam_number', 'relate_family__fam_class__class_name']
    # readonly_fields = ['relate_family']


class CertificationResources(resources.ModelResource):
    class CertificationForeignWidget(ForeignKeyWidget):
        def get_queryset(self, value, row, *args, **kwargs):
            return FamilyBasic.objects.filter(
                fam_number__iexact=row["relate_family"]
            )

    relate_family = fields.Field(
        attribute='relate_family',
        column_name='relate_family',
        widget=CertificationForeignWidget(FamilyBasic, 'fam_number')
    )

    class Meta:
        model = FamilyCertification
        import_id_fields = ('relate_family',)
        # 导入数据时，如果该条数据未修改过，则会忽略
        skip_unchanged = True
        # 在导入预览页面中显示跳过的记录
        report_skipped = True
        fields = ('relate_family', 'cert_id', 'cert_date', 'cert_draw_people', 'cert_draw_date', 'cert_nation_id',
                  'cert_nation_people', 'cert_other',)


@xadmin.sites.register(FamilyCertification)
class CertificationAdmin(object):
    """
    证书信息
    """
    import_export_args = {'import_resource_class': CertificationResources, }
    list_display = ['relate_family', 'get_fam_name', 'get_fam_id_number', 'get_fam_class', 'cert_id', 'cert_date',
                    'cert_draw_people',
                    'cert_draw_date', 'cert_nation_id', 'cert_nation_people', 'cert_other', ]
    list_filter = ['relate_family__fam_name', 'relate_family__fam_number', 'cert_id', 'cert_date', 'cert_draw_people',
                   'cert_draw_date', 'relate_family__fam_class__class_name', 'cert_nation_id', 'cert_nation_people',
                   'cert_other', ]
    list_editable = ['cert_id', 'cert_date', 'cert_draw_people', 'cert_draw_date', 'cert_nation_id',
                     'cert_nation_people', 'cert_other', ]
    show_bookmarks = False
    search_fields = ['relate_family__fam_name', 'relate_family__fam_number', 'relate_family__fam_class__class_name']
    # readonly_fields = ['relate_family']


@xadmin.sites.register(FamilyOnduty)
class FamilyOndutyAdmin(object):
    """
    出勤信息
    """

    class OndutyResources(resources.ModelResource):
        class OndutyForeignWidget(ForeignKeyWidget):
            def get_queryset(self, value, row, *args, **kwargs):
                return FamilyBasic.objects.filter(
                    fam_number__iexact=row["relate_family"]
                )

        relate_family = fields.Field(
            attribute='relate_family',
            column_name='relate_family',
            widget=OndutyForeignWidget(FamilyBasic, 'fam_number')
        )

        class Meta:
            model = FamilyOnduty
            import_id_fields = ('relate_family',)
            # 导入数据时，如果该条数据未修改过，则会忽略
            skip_unchanged = True
            # 在导入预览页面中显示跳过的记录
            report_skipped = True
            fields = ('relate_family', 'onduty', 'homework', 'other')

    import_export_args = {'import_resource_class': OndutyResources}
    list_display = ['relate_family', 'get_fam_name', 'get_fam_class', 'onduty', 'homework', 'other']
    list_filter = ['relate_family__fam_name', 'relate_family__fam_number', 'relate_family__fam_class__class_name']
    list_editable = ['onduty', 'homwwork', 'homework', 'other']
    show_bookmarks = False
    search_fields = list_filter
    reanonly_fields = ['relate_family']


@xadmin.sites.register(Total)
class TotalAdmin(object):
    """
    总览信息
    """
    list_display = [
        'fam_type', 'fam_number', 'fam_group',
        'fam_name', 'fam_gender', 'fam_class', 'fam_class_num', 'fam_id_number',
        'fam_loc', 'fam_deg', 'fam_major',
        'fam_company', 'fam_duty',
        'fam_status', 'fam_origin', 'fam_cellphone', 'fam_wechat', 'fam_qq',
        'fam_signup_date', 'fam_signup_people', 'fam_other',
        'fee_train', 'fee_material', 'fee_exam', 'fee_total',
        'fee_date', 'fee_method', 'fee_id', 'fee_tax', 'fee_invoice_header',
        'fee_invoice_id', 'fee_invoice_date', 'fee_other',
        'text_basic', 'text_basic2', 'text_guide', 'text_manual', 'text_other',
        'wechat_number', 'wechat_nickname', 'wechat_date', 'onduty', 'homework', 'other',
        'exam_date', 'exam_total', 'exam_nation', 'exam_pre', 'exam_speech', 'exam_other',
        'cert_id', 'cert_draw_people', 'cert_draw_date', 'cert_nation_id', 'cert_nation_people', 'cert_other'
    ]
    show_bookmarks = False
    list_filter = ['family__fam_name', 'family__fam_cellphone', 'family__fam_class__class_name',
                   'family__fam_teacher_level', 'family__familytuition__fee_date',
                   'family__familywechat__wechat_number', 'family__result__result',
                   'family__familycertification__cert_id']
