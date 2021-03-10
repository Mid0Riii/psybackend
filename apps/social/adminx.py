import xadmin
from django.utils.html import format_html
from .models import SocialBasic, SocialCertification, SocialExam, SocialTextbook, \
    SocialTuition, SocialWechat, SocialClass, SocialOnduty, Total
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, BooleanWidget
from .layouts.detailLayouts import BasicLayout, TuitionLayout


@xadmin.sites.register(SocialBasic)
class BasicAdmin(object):
    """
    社会工作师基本信息
    """

    class SocialBasicResources(resources.ModelResource):
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
                return SocialClass.objects.filter(
                    class_name__iexact=row["social_class"]
                )

        social_class = fields.Field(
            attribute='social_class',
            column_name='social_class',
            widget=ClassForeignWidget(SocialClass, 'class_name')
        )

        class Meta:
            model = SocialBasic
            import_id_fields = ('social_number',)
            # 导入数据时，如果该条数据未修改过，则会忽略
            skip_unchanged = True
            # 在导入预览页面中显示跳过的记录
            report_skipped = True
            fields = (
                'social_number', 'social_name', 'social_gender', 'social_id_number',
                'social_loc', 'social_deg', 'social_major',
                'social_company', 'social_duty',
                'social_status', 'social_origin', 'social_cellphone', 'social_wechat', 'social_email',
                'social_signup_date', 'social_signup_people', 'social_other', 'social_class')

    list_display = ['social_number', 'social_name', 'social_gender', 'social_class', 'social_class_num',
                    'social_type', 'social_group',
                    'social_id_number',
                    'social_loc', 'social_deg',
                    'social_major',
                    'social_company', 'social_duty',
                    'social_status', 'social_origin', 'social_cellphone', 'social_wechat', 'social_email',
                    'social_signup_date', 'social_signup_people', 'social_other']
    import_export_args = {'import_resource_class': SocialBasicResources}
    list_filter = ['social_number', 'social_name', 'social_type', 'social_group', 'social_gender', 'social_class',
                   'social_class_num',
                   'social_id_number',
                   'social_loc', 'social_deg',
                   'social_major',
                   'social_company', 'social_duty',
                   'social_status', 'social_origin', 'social_cellphone', 'social_wechat', 'social_email',
                   'social_signup_date', 'social_signup_people', 'social_other', 'social_class__class_name', ]
    list_editable = list_display
    search_fields = ['social_number', 'social_name', 'social_class__class_name']
    show_bookmarks = False

    def tuition_state(self, obj):
        info = obj.social_name
        if obj.Socialtuition.fee_date == '空':
            color_code = 'red'
            # info = '无交费信息'
        else:
            color_code = 'black'
            # info = '已交费'
        return format_html('<span style="color:{};">{}</span>', color_code, info)

    tuition_state.short_description = '姓名'
    tuition_state.admin_order_field = 'social_name'

    # inlines = [TuitionInline]
    def get_form_layout(self):
        self.form_layout = BasicLayout
        return super().get_form_layout()


@xadmin.sites.register(SocialClass)
class ClassAdmin(object):
    '''
    班级信息
    '''

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
            model = SocialClass
            fields = ('class_name', 'class_teacher', 'class_date')
            # 导入数据时，如果该条数据未修改过，则会忽略
            skip_unchanged = True
            # 在导入预览页面中显示跳过的记录
            report_skipped = True
            # 模型主键
            import_id_fields = ('class_name',)

    import_export_args = {'import_resource_class': ClassResources,
                          }
    list_display = ['class_name', 'class_index', 'class_id_example', 'class_teacher', 'class_recruit_teacher',
                    'class_date']
    list_filter = list_display
    search_fields = list_display
    show_bookmarks = False
    ordering = ['-class_index']


@xadmin.sites.register(SocialTuition)
class TuitionAdmin(object):
    """
    交费信息
    """

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

        # class TuitionForeignWidget(ForeignKeyWidget):
        #     def get_queryset(self, value, row, *args, **kwargs):
        #         return SocialBasic.objects.filter(
        #             social_number__iexact=row["relate_social"]
        #         )

        relate_social = fields.Field(
            attribute='relate_social',
            column_name='学号',
            widget=ForeignKeyWidget(SocialBasic, 'social_number')
        )

        class Meta:
            model = SocialTuition
            import_id_fields = ('relate_social',)
            # 导入数据时，如果该条数据未修改过，则会忽略
            skip_unchanged = True
            # 在导入预览页面中显示跳过的记录
            report_skipped = True
            fields = (
                'relate_social', 'fee_train', 'fee_material', 'fee_exam', 'fee_total', 'fee_date', 'fee_method',
                'fee_tax',
                'fee_invoice_header',
                'fee_invoice_id', 'fee_invoice_date', 'fee_other')

    list_display = ['relate_social', 'get_social_name', 'get_social_class',
                    'fee_train', 'fee_material', 'fee_exam', 'fee_total',
                    'fee_date', 'fee_method', 'fee_tax',
                    'fee_invoice_header',
                    'fee_invoice_id', 'fee_invoice_date', 'fee_other']
    # TODO CODEVIEW filter中外键的处理
    list_filter = ['relate_social__social_name', 'fee_train', 'fee_material', 'fee_exam', 'fee_total', 'fee_date',
                   'fee_method',
                   'relate_social__social_class__class_name', 'fee_tax', 'fee_invoice_header',
                   'fee_invoice_id', 'fee_invoice_date', 'fee_other']
    show_bookmarks = False
    import_export_args = {'import_resource_class': TuitionResources,
                          }
    search_fields = ['relate_social__social_name', 'relate_social__social_number', 'relate_social__social_number',
                     'relate_social__social_class__class_name']
    list_editable = ['fee_train', 'fee_material', 'fee_exam', 'fee_total', 'fee_date', 'fee_method', 'fee_id',
                     'fee_tax', 'fee_invoice_header',
                     'fee_invoice_id', 'fee_invoice_date', 'fee_other']

    # readonly_fields = ['relate_social']

    def get_form_layout(self):
        self.form_layout = TuitionLayout
        return super().get_form_layout()


@xadmin.sites.register(SocialTextbook)
class TextbookAdmin(object):
    """
    教材信息
    """

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

        # class TextbookForeignWidget(ForeignKeyWidget):
        #     def get_queryset(self, value, row, *args, **kwargs):
        #         return SocialBasic.objects.filter(
        #             social_number__iexact=row["relate_social"]
        #         )

        relate_social = fields.Field(
            attribute='relate_social',
            column_name='学号',
            widget=ForeignKeyWidget(SocialBasic, 'social_number')
        )

        class Meta:
            model = SocialTextbook
            import_id_fields = ('relate_social',)
            # 导入数据时，如果该条数据未修改过，则会忽略
            skip_unchanged = True
            # 在导入预览页面中显示跳过的记录
            report_skipped = True
            fields = ('relate_social', 'text_basic', 'text_skill', 'text_workbook', 'text_train', 'text_manual', 'text_other')

    import_export_args = {'import_resource_class': TextbookResources, }
    list_display = ['relate_social', 'get_social_name', 'get_social_class', 'text_basic', 'text_skill', 'text_workbook',
                    'text_train', 'text_manual', 'text_other']
    list_filter = ['relate_social__social_name', 'relate_social__social_number', 'text_basic', 'text_skill',
                   'text_workbook',
                   'text_train', 'text_manual', 'text_other', 'relate_social__social_class__class_name']
    search_fields = ['relate_social__social_name', 'relate_social__social_number',
                     'relate_social__social_class__class_name']
    # readonly_fields = ['relate_social']
    list_editable = ['text_basic', 'text_skill', 'text_workbook', 'text_train', 'text_manual', 'text_other']
    show_bookmarks = False


@xadmin.sites.register(SocialWechat)
class WechatAdmin(object):
    """
    365开通情况
    """

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

        # class WechatForeignWidget(ForeignKeyWidget):
        #     def get_queryset(self, value, row, *args, **kwargs):
        #         return SocialBasic.objects.filter(
        #             social_number__iexact=row["relate_social"]
        #         )

        relate_social = fields.Field(
            attribute='relate_social',
            column_name='学号',
            widget=ForeignKeyWidget(SocialBasic, 'social_number')
        )

        class Meta:
            model = SocialWechat
            import_id_fields = ('relate_social',)
            # 导入数据时，如果该条数据未修改过，则会忽略
            skip_unchanged = True
            # 在导入预览页面中显示跳过的记录
            report_skipped = True
            fields = ('relate_social', 'wechat_number', 'wechat_nickname', 'wechat_date', 'wechat_other')

    import_export_args = {'import_resource_class': WechatResources, }
    list_display = ['relate_social', 'get_social_name', 'get_social_class', 'wechat_number', 'wechat_nickname',
                    'wechat_date', 'wechat_other']
    list_filter = ['relate_social__social_name', 'relate_social__social_number', 'wechat_number', 'wechat_nickname',
                   'wechat_date', 'relate_social__social_class__class_name', 'wechat_other']
    search_fields = ['relate_social__social_name', 'relate_social__social_number',
                     'relate_social__social_class__class_name']
    # readonly_fields = ['relate_social']
    list_editable = ['wechat_number', 'wechat_nickname', 'wechat_date', 'wechat_other']
    show_bookmarks = False


@xadmin.sites.register(SocialExam)
class ExamAdmin(object):
    """
    考试信息
    """

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

        # class ExamForeignWidget(ForeignKeyWidget):
        #     def get_queryset(self, value, row, *args, **kwargs):
        #         return SocialBasic.objects.filter(
        #             social_number__iexact=row["relate_social"]
        #         )

        relate_social = fields.Field(
            attribute='relate_social',
            column_name='学号',
            widget=ForeignKeyWidget(SocialBasic, 'social_number')
        )

        class Meta:
            model = SocialExam
            import_id_fields = ('relate_social',)
            # 导入数据时，如果该条数据未修改过，则会忽略
            skip_unchanged = True
            # 在导入预览页面中显示跳过的记录
            report_skipped = True
            fields = ('relate_social', 'batch', 'exam_total', 'exam_nation', 'exam_practice', 'result', 'other')

    import_export_args = {'import_resource_class': ExamResources, }
    list_display = ['relate_social', 'get_social_name', 'get_social_id_number', 'get_social_class', 'batch',
                    'exam_total', 'exam_nation', 'exam_practice', 'result', 'other']
    list_filter = ['relate_social__social_name', 'relate_social__social_number',
                   'relate_social__social_class__class_name',
                   'batch', 'exam_total', 'exam_nation', 'exam_practice', 'result', 'other']
    list_editable = ['batch', 'exam_total', 'exam_nation', 'exam_practice', 'result', 'other']
    show_bookmarks = False
    search_fields = ['relate_social__social_name', 'relate_social__social_number',
                     'relate_social__social_class__class_name']
    # readonly_fields = ['relate_social']


@xadmin.sites.register(SocialCertification)
class CertificationAdmin(object):
    """
    证书信息
    """

    class CertificationResources(resources.ModelResource):
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

        # class CertificationForeignWidget(ForeignKeyWidget):
        #     def get_queryset(self, value, row, *args, **kwargs):
        #         return SocialBasic.objects.filter(
        #             social_number__iexact=row["relate_social"]
        #         )

        relate_social = fields.Field(
            attribute='relate_social',
            column_name='学号',
            widget=ForeignKeyWidget(SocialBasic, 'social_number')
        )

        class Meta:
            model = SocialCertification
            import_id_fields = ('relate_social',)
            # 导入数据时，如果该条数据未修改过，则会忽略
            skip_unchanged = True
            # 在导入预览页面中显示跳过的记录
            report_skipped = True
            fields = ('relate_social', "ass_cert_id", "ass_cert_date", "ass_cert_draw_people", "ass_cert_draw_date",
                      "nation_cert_id", "nation_cert_date", "nation_cert_draw_people", "nation_cert_draw_date", "other")

    import_export_args = {'import_resource_class': CertificationResources, }
    list_display = ['relate_social', 'get_social_name', 'get_social_id_number', 'get_social_class', "ass_cert_id",
                    "ass_cert_date", "ass_cert_draw_people", "ass_cert_draw_date",
                    "nation_cert_id", "nation_cert_date", "nation_cert_draw_people", "nation_cert_draw_date", "other"]
    list_filter = ['relate_social__social_name', 'relate_social__social_number', "ass_cert_id", "ass_cert_date",
                   "ass_cert_draw_people", "ass_cert_draw_date",
                   "nation_cert_id", "nation_cert_date", "nation_cert_draw_people", "nation_cert_draw_date", "other",
                   'relate_social__social_class__class_name']
    list_editable = ["ass_cert_id", "ass_cert_date", "ass_cert_draw_people", "ass_cert_draw_date",
                     "nation_cert_id", "nation_cert_date", "nation_cert_draw_people", "nation_cert_draw_date", "other"]
    show_bookmarks = False
    search_fields = ['relate_social__social_name', 'relate_social__social_number',
                     'relate_social__social_class__class_name']
    # readonly_fields = ['relate_social']


@xadmin.sites.register(SocialOnduty)
class SocialOndutyAdmin(object):
    """
    出勤信息
    """

    class OndutyResources(resources.ModelResource):
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

        # class OndutyForeignWidget(ForeignKeyWidget):
        #     def get_queryset(self, value, row, *args, **kwargs):
        #         return SocialBasic.objects.filter(
        #             social_number__iexact=row["relate_social"]
        #         )

        relate_social = fields.Field(
            attribute='relate_social',
            column_name='学号',
            widget=ForeignKeyWidget(SocialBasic, 'social_number')
        )

        class Meta:
            model = SocialOnduty
            import_id_fields = ('relate_social',)
            # 导入数据时，如果该条数据未修改过，则会忽略
            skip_unchanged = True
            # 在导入预览页面中显示跳过的记录
            report_skipped = True
            fields = ('relate_social', 'onduty', 'homework', 'other')

    import_export_args = {'import_resource_class': OndutyResources}
    list_display = ['relate_social', 'get_social_name', 'get_social_class', 'onduty', 'homework', 'other']
    list_filter = ['relate_social__social_name', 'relate_social__social_number',
                   'relate_social__social_class__class_name']
    list_editable = ['onduty', 'homework', 'other']
    show_bookmarks = False
    search_fields = list_filter
    # readonly_fields = ['relate_social']


@xadmin.sites.register(Total)
class TotalAdmin(object):
    """
    总览信息
    """
    list_display_links = ('social_name')
    list_display = [
        'social_number', 'social_name', 'social_gender', 'social_class', 'social_class_num', 'social_id_number',
        'social_type', 'social_group',
        'social_loc', 'social_deg', 'social_major',
        'social_company', 'social_duty',
        'social_status', 'social_origin', 'social_cellphone', 'social_wechat', 'social_email',
        'social_signup_date', 'social_signup_people', 'social_other',
        'fee_train', 'fee_material', 'fee_exam', 'fee_total', 'fee_date', 'fee_method', 'fee_tax', 'fee_invoice_header',
        'fee_invoice_id', 'fee_invoice_date', 'fee_other',
        'text_basic', 'text_skill', 'text_workbook', 'text_train', 'text_manual', 'text_other',
        'wechat_number', 'wechat_nickname', 'wechat_date', 'wechat_other',
        'exam_batch', 'exam_total', 'exam_nation', 'exam_practice', 'exam_other',
        'ass_cert_id', 'ass_cert_date', 'ass_cert_draw_people', 'ass_cert_draw_date',
        'nation_cert_id', 'nation_cert_date', 'nation_cert_draw_people', 'nation_cert_draw_date', 'cert_other',
        'ond_onduty', 'ond_homework', 'ond_other',
    ]
    show_bookmarks = False
    list_filter = ['social__social_name', 'social__social_cellphone', 'social__social_class__class_name',
                   'social__socialtuition__fee_date',
                   'social__socialwechat__wechat_number',
                   'social__socialcertification__ass_cert_id',
                   'social__socialcertification__nation_cert_id']
