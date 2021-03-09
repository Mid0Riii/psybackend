import xadmin
from django.utils.html import format_html
from .models import MarriageBasic, MarriageCertification, MarriageExam, MarriageTextbook, \
    MarriageTuition, MarriageWechat, MarriageClass, MarriageOnduty, Total
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, BooleanWidget
from django.apps import apps
from .layouts.detailLayouts import BasicLayout, TuitionLayout


# TODO CODEREVIEW 外键后台inline显示的用法
# class TuitionInline(object):
#     model = MarriageTuition
#     extra = 1
#     style='one'
#     # readonly_fields=['fee_material', 'fee_exam', 'fee_total',
#                     'fee_exam_extra', 'fee_date', 'fee_method', 'fee_id']


@xadmin.sites.register(MarriageBasic)
class BasicAdmin(object):
    """
    婚姻基本信息
    """

    class MarriageBasicResources(resources.ModelResource):
        class ClassForeignWidget(ForeignKeyWidget):
            def get_queryset(self, value, row, *args, **kwargs):
                return MarriageClass.objects.filter(
                    class_name__iexact=row["mar_class"]
                )

        mar_class = fields.Field(
            attribute='mar_class',
            column_name='mar_class',
            widget=ClassForeignWidget(MarriageClass, 'class_name')
        )

        class Meta:
            model = MarriageBasic
            import_id_fields = ('mar_number',)
            # 导入数据时，如果该条数据未修改过，则会忽略
            skip_unchanged = True
            # 在导入预览页面中显示跳过的记录
            report_skipped = True
            fields = (
                'mar_number', 'mar_name', 'mar_gender', 'mar_id_number',
                'mar_loc', 'mar_deg', 'mar_major',
                'mar_company', 'mar_duty',
                'mar_status', 'mar_origin', 'mar_cellphone', 'mar_wechat', 'mar_email',
                'mar_signup_date', 'mar_signup_people', 'mar_other', 'mar_class')

    list_display = ['mar_number', 'tuition_state', 'mar_gender', 'mar_class', 'mar_class_num', 'mar_type', 'mar_group', 'mar_id_number',
                    'mar_loc', 'mar_deg',
                    'mar_major',
                    'mar_company', 'mar_duty',
                    'mar_status', 'mar_origin', 'mar_cellphone', 'mar_wechat', 'mar_email',
                    'mar_signup_date', 'mar_signup_people', 'mar_other']
    import_export_args = {'import_resource_class': MarriageBasicResources}
    list_filter = ['mar_number', 'mar_name', 'mar_type', 'mar_group', 'mar_gender', 'mar_class', 'mar_class_num', 'mar_id_number',
                   'mar_loc', 'mar_deg',
                   'mar_major',
                   'mar_company', 'mar_duty',
                   'mar_status', 'mar_origin', 'mar_cellphone', 'mar_wechat', 'mar_email',
                   'mar_signup_date', 'mar_signup_people', 'mar_other', 'mar_class__class_name', ]
    list_editable = list_display
    search_fields = ['mar_number', 'mar_name', 'mar_class__class_name']
    show_bookmarks = False  

    def tuition_state(self, obj):
        info = obj.mar_name
        if obj.marriagetuition.fee_date == '空':
            color_code = 'red'
            # info = '无交费信息'
        else:
            color_code = 'black'
            # info = '已交费'
        return format_html('<span style="color:{};">{}</span>', color_code, info)

    tuition_state.short_description = '姓名'
    tuition_state.admin_order_field = 'mar_name'

    # inlines = [TuitionInline]
    def get_form_layout(self):
        self.form_layout = BasicLayout
        return super().get_form_layout()

    # TODO CODEREVIEW Django默认生成的父键查询子键的方法名全部是小写
    # TODO CODEREVIEW 重写save_models方法
    # def save_models(self):
    #     obj = self.new_obj
    #     obj.save()
    #     obj.marriagetuition_set.create()
    #     obj.marriageexam_set.create()
    #     obj.marriagewechat_set.create()
    #     obj.marriageexamextra_set.create()
    #     obj.marriagetextbook_set.create()
    #     obj.marriagecertification_set.create()


@xadmin.sites.register(MarriageClass)
class ClassAdmin(object):
    '''
    班级信息
    '''

    class ClassResources(resources.ModelResource):
        # def __init__(self):
        #     super().__init__()
        #     field_list = apps.get_model('marriage', 'MarriageClass')._meta.fields
        #
        #     # 应用名与模型名
        #     self.verbose_name_dict ={}
        #     # 获取所有字段的verbose_name并存放在verbose_name_dict字典里
        #     for i in field_list:
        #         self.verbose_name_dict[i.name] = i.verbose_name
        #
        # def get_export_fields(self):
        #     fields = self.get_fields()
        #     # 默认导入导出field的column_name为字段的名称
        #     # 这里修改为字段的verbose_name
        #     for field in fields:
        #         field_name = self.get_field_name(field)
        #         if field_name in self.verbose_name_dict.keys():
        #             field.column_name = self.verbose_name_dict[field_name]
        #             # 如果设置过verbose_name，则将column_name替换为verbose_name
        #             # 否则维持原有的字段名
        #     return fields
        class Meta:
            model = MarriageClass
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


@xadmin.sites.register(MarriageTuition)
class TuitionAdmin(object):
    """
    交费信息
    """

    class TuitionResources(resources.ModelResource):
        class TuitionForeignWidget(ForeignKeyWidget):
            def get_queryset(self, value, row, *args, **kwargs):
                return MarriageBasic.objects.filter(
                    mar_number__iexact=row["relate_marriage"]
                )

        relate_marriage = fields.Field(
            attribute='relate_marriage',
            column_name='relate_marriage',
            widget=TuitionForeignWidget(MarriageBasic, 'mar_number')
        )

        class Meta:
            model = MarriageTuition
            import_id_fields = ('relate_marriage',)
            # 导入数据时，如果该条数据未修改过，则会忽略
            skip_unchanged = True
            # 在导入预览页面中显示跳过的记录
            report_skipped = True
            fields = ('relate_marriage', 'fee_train', 'fee_material', 'fee_exam', 'fee_total', 'fee_date', 'fee_method', 'fee_tax', 'fee_invoice_header',
                      'fee_invoice_id', 'fee_invoice_date', 'fee_other')

    list_display = ['relate_marriage', 'get_mar_name', 'get_mar_class', 
                    'fee_train', 'fee_material', 'fee_exam', 'fee_total',
                    'fee_date', 'fee_method', 'fee_tax',
                    'fee_invoice_header',
                    'fee_invoice_id', 'fee_invoice_date', 'result', 'fee_other'
                    ]
    # TODO CODEVIEW filter中外键的处理
    list_filter = ['relate_marriage__mar_name','fee_train', 'fee_material', 'fee_exam', 'fee_total', 'fee_date', 'fee_method',
                    'relate_marriage__mar_class__class_name', 'fee_tax', 'fee_invoice_header',
                    'fee_invoice_id', 'fee_invoice_date', 'fee_other']
    show_bookmarks = False
    import_export_args = {'import_resource_class': TuitionResources,
                          }
    search_fields = ['relate_marriage__mar_name', 'relate_marriage__mar_number', 'relate_marriage__mar_number', 'relate_marriage__mar_class__class_name']
    list_editable = ['fee_train', 'fee_material', 'fee_exam', 'fee_total', 'fee_date', 'fee_method', 'fee_id', 'fee_tax', 'fee_invoice_header',
                     'fee_invoice_id', 'fee_invoice_date', 'fee_other']
    # readonly_fields = ['relate_marriage']

    def get_form_layout(self):
        self.form_layout = TuitionLayout
        return super().get_form_layout()


@xadmin.sites.register(MarriageTextbook)
class TextbookAdmin(object):
    """
    教材信息
    """

    class TextbookResources(resources.ModelResource):
        class TextbookForeignWidget(ForeignKeyWidget):
            def get_queryset(self, value, row, *args, **kwargs):
                return MarriageBasic.objects.filter(
                    mar_number__iexact=row["relate_marriage"]
                )

        relate_marriage = fields.Field(
            attribute='relate_marriage',
            column_name='relate_marriage',
            widget=TextbookForeignWidget(MarriageBasic, 'mar_number')
        )

        class Meta:
            model = MarriageTextbook
            import_id_fields = ('relate_marriage',)
            # 导入数据时，如果该条数据未修改过，则会忽略
            skip_unchanged = True
            # 在导入预览页面中显示跳过的记录
            report_skipped = True
            fields = ('relate_marriage', 'text_basic', 'text_skill', 'text_workbook', 'text_train', 'text_manual', 'text_other')

    import_export_args = {'import_resource_class': TextbookResources, }
    list_display = ['relate_marriage', 'get_mar_name', 'get_mar_class', 'text_basic', 'text_skill', 'text_workbook', 'text_train', 'text_manual', 'text_other']
    list_filter = ['relate_marriage__mar_name', 'relate_marriage__mar_number','text_basic', 'text_skill', 'text_workbook', 'text_train', 'text_manual', 'text_other', 'relate_marriage__mar_class__class_name']
    search_fields = ['relate_marriage__mar_name', 'relate_marriage__mar_number', 'relate_marriage__mar_class__class_name']
    # readonly_fields = ['relate_marriage']
    list_editable = ['text_basic', 'text_skill', 'text_workbook', 'text_train', 'text_manual', 'text_other']
    show_bookmarks = False


@xadmin.sites.register(MarriageWechat)
class WechatAdmin(object):
    """
    365开通情况
    """

    class WechatResources(resources.ModelResource):
        class WechatForeignWidget(ForeignKeyWidget):
            def get_queryset(self, value, row, *args, **kwargs):
                return MarriageBasic.objects.filter(
                    mar_number__iexact=row["relate_marriage"]
                )

        relate_marriage = fields.Field(
            attribute='relate_marriage',
            column_name='relate_marriage',
            widget=WechatForeignWidget(MarriageBasic, 'mar_number')
        )

        class Meta:
            model = MarriageWechat
            import_id_fields = ('relate_marriage',)
            # 导入数据时，如果该条数据未修改过，则会忽略
            skip_unchanged = True
            # 在导入预览页面中显示跳过的记录
            report_skipped = True
            fields = ('relate_marriage', 'wechat_number', 'wechat_nickname', 'wechat_date', 'wechat_other')

    import_export_args = {'import_resource_class': WechatResources, }
    list_display = ['relate_marriage', 'get_mar_name', 'get_mar_class', 'wechat_number', 'wechat_nickname',
                    'wechat_date', 'wechat_other']
    list_filter = ['relate_marriage__mar_name', 'relate_marriage__mar_number','wechat_number', 'wechat_nickname', 'wechat_date', 'relate_marriage__mar_class__class_name', 'wechat_other']
    search_fields = ['relate_marriage__mar_name', 'relate_marriage__mar_number', 'relate_marriage__mar_class__class_name']
    # readonly_fields = ['relate_marriage']
    list_editable = ['wechat_number', 'wechat_nickname', 'wechat_date', 'wechat_other']
    show_bookmarks = False


@xadmin.sites.register(MarriageExam)
class ExamAdmin(object):
    """
    考试信息
    """

    class ExamResources(resources.ModelResource):
        class ExamForeignWidget(ForeignKeyWidget):
            def get_queryset(self, value, row, *args, **kwargs):
                return MarriageBasic.objects.filter(
                    mar_number__iexact=row["relate_marriage"]
                )

        relate_marriage = fields.Field(
            attribute='relate_marriage',
            column_name='relate_marriage',
            widget=ExamForeignWidget(MarriageBasic, 'mar_number')
        )

        class Meta:
            model = MarriageExam
            import_id_fields = ('relate_marriage',)
            # 导入数据时，如果该条数据未修改过，则会忽略
            skip_unchanged = True
            # 在导入预览页面中显示跳过的记录
            report_skipped = True
            fields = ('relate_marriage', 'batch', 'exam_total', 'exam_nation', 'exam_practice', 'other')

    import_export_args = {'import_resource_class': ExamResources, }
    list_display = ['relate_marriage', 'get_mar_name', 'get_mar_id_number', 'get_mar_class', 'batch',
                    'exam_total', 'exam_nation', 'exam_practice', 'result', 'other']
    list_filter = ['relate_marriage__mar_name', 'relate_marriage__mar_number', 'relate_marriage__mar_class__class_name',
                   'batch', 'exam_total', 'exam_nation', 'exam_practice', 'result', 'other']
    list_editable = ['batch', 'exam_total', 'exam_nation', 'exam_practice', 'result', 'other']
    show_bookmarks = False
    search_fields = ['relate_marriage__mar_name', 'relate_marriage__mar_number', 'relate_marriage__mar_class__class_name']
    # readonly_fields = ['relate_marriage']


@xadmin.sites.register(MarriageCertification)
class CertificationAdmin(object):
    """
    证书信息
    """

    class CertificationResources(resources.ModelResource):
        class CertificationForeignWidget(ForeignKeyWidget):
            def get_queryset(self, value, row, *args, **kwargs):
                return MarriageBasic.objects.filter(
                    mar_number__iexact=row["relate_marriage"]
                )

        relate_marriage = fields.Field(
            attribute='relate_marriage',
            column_name='relate_marriage',
            widget=CertificationForeignWidget(MarriageBasic, 'mar_number')
        )

        class Meta:
            model = MarriageCertification
            import_id_fields = ('relate_marriage',)
            # 导入数据时，如果该条数据未修改过，则会忽略
            skip_unchanged = True
            # 在导入预览页面中显示跳过的记录
            report_skipped = True
            fields = ('relate_marriage', "ass_cert_id", "ass_cert_date", "ass_cert_draw_people", "ass_cert_draw_date",
                "nation_cert_id", "nation_cert_date", "nation_cert_draw_people", "nation_cert_draw_date", "other" )

    import_export_args = {'import_resource_class': CertificationResources, }
    list_display = ['relate_marriage', 'get_mar_name', 'get_mar_id_number', 'get_mar_class', "ass_cert_id", "ass_cert_date", "ass_cert_draw_people", "ass_cert_draw_date",
                    "nation_cert_id", "nation_cert_date", "nation_cert_draw_people", "nation_cert_draw_date", "other" ]
    list_filter = ['relate_marriage__mar_name', 'relate_marriage__mar_number', "ass_cert_id", "ass_cert_date", "ass_cert_draw_people", "ass_cert_draw_date",
                    "nation_cert_id", "nation_cert_date", "nation_cert_draw_people", "nation_cert_draw_date", "other", 'relate_marriage__mar_class__class_name']
    list_editable = ["ass_cert_id", "ass_cert_date", "ass_cert_draw_people", "ass_cert_draw_date",
                    "nation_cert_id", "nation_cert_date", "nation_cert_draw_people", "nation_cert_draw_date", "other" ]
    show_bookmarks = False
    search_fields = ['relate_marriage__mar_name', 'relate_marriage__mar_number', 'relate_marriage__mar_class__class_name']
    # readonly_fields = ['relate_marriage']


@xadmin.sites.register(MarriageOnduty)
class MarriageOndutyAdmin(object):
    """
    出勤信息
    """

    class OndutyResources(resources.ModelResource):
        class OndutyForeignWidget(ForeignKeyWidget):
            def get_queryset(self, value, row, *args, **kwargs):
                return MarriageBasic.objects.filter(
                    mar_number__iexact=row["relate_marriage"]
                )

        relate_marriage = fields.Field(
            attribute='relate_marriage',
            column_name='relate_marriage',
            widget=OndutyForeignWidget(MarriageBasic, 'mar_number')
        )

        class Meta:
            model = MarriageOnduty
            import_id_fields = ('relate_marriage',)
            # 导入数据时，如果该条数据未修改过，则会忽略
            skip_unchanged = True
            # 在导入预览页面中显示跳过的记录
            report_skipped = True
            fields = ('relate_marriage', 'onduty', 'homework', 'other')

    import_export_args = {'import_resource_class': OndutyResources}
    list_display = ['relate_marriage', 'get_mar_name', 'get_mar_class', 'onduty', 'homework', 'other']
    list_filter = ['relate_marriage__mar_name', 'relate_marriage__mar_number', 'relate_marriage__mar_class__class_name']
    list_editable = ['onduty', 'homework', 'other']
    show_bookmarks = False
    search_fields = list_filter
    reanonly_fields = ['relate_marriage']


@xadmin.sites.register(Total)
class TotalAdmin(object):
    """
    总览信息
    """
    list_display_links = ('mar_name')
    list_display = [
        'mar_number', 'mar_name', 'mar_gender', 'mar_class', 'mar_class_num', 'mar_id_number',
        'mar_type', 'mar_group',
        'mar_loc', 'mar_deg', 'mar_major',
        'mar_company', 'mar_duty',
        'mar_status', 'mar_origin', 'mar_cellphone', 'mar_wechat', 'mar_email',
        'mar_signup_date', 'mar_signup_people', 'mar_other',
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
    list_filter = ['marriage__mar_name', 'marriage__mar_cellphone', 'marriage__mar_class__class_name',
                   'marriage__marriagetuition__fee_date',
                   'marriage__marriagewechat__wechat_number',
                   'marriage__marriagecertification__ass_cert_id',
                   'marriage__marriagecertification__nation_cert_id']

