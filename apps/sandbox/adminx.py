import xadmin
from django.utils.html import format_html
from .models import SandboxBasic, SandboxCertification, SandboxExam, SandboxTextbook, \
    SandboxTuition, SandboxWechat, SandboxClass, SandboxOnduty, Total
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, BooleanWidget
from django.apps import apps
from .layouts.detailLayouts import BasicLayout, TuitionLayout


# TODO CODEREVIEW 外键后台inline显示的用法
# class TuitionInline(object):
#     model = SandboxTuition
#     extra = 1
#     style='one'
#     readonly_fields=['fee_material', 'fee_exam', 'fee_total',
#                     'fee_exam_extra', 'fee_date', 'fee_method', 'fee_id']


@xadmin.sites.register(SandboxBasic)
class BasicAdmin(object):
    """
    沙盘分析基本信息
    """

    class SandboxBasicResources(resources.ModelResource):
        class ClassForeignWidget(ForeignKeyWidget):
            def get_queryset(self, value, row, *args, **kwargs):
                return SandboxClass.objects.filter(
                    class_name__iexact=row["san_class"]
                )

        san_class = fields.Field(
            attribute='san_class',
            column_name='san_class',
            widget=ClassForeignWidget(SandboxClass, 'class_name')
        )

        class Meta:
            model = SandboxBasic
            import_id_fields = ('san_number',)
            # 导入数据时，如果该条数据未修改过，则会忽略
            skip_unchanged = True
            # 在导入预览页面中显示跳过的记录
            report_skipped = True
            fields = (
                'san_number', 'san_name', 'san_gender', 'san_class', 'san_class_num', 'san_id_number',
                'san_loc', 'san_deg', 'san_major',
                'san_company', 'san_duty',
                'san_status', 'san_origin', 'san_cellphone', 'san_wechat', 'san_email',
                'san_signup_date', 'san_signup_people', 'san_other')

    list_display = ['san_number', 'tuition_state', 'san_gender', 'san_class', 'san_class_num', 'san_type', 'san_group', 'san_id_number',
                    'san_loc', 'san_deg',
                    'san_major',
                    'san_company', 'san_duty',
                    'san_status', 'san_origin', 'san_cellphone', 'san_wechat', 'san_email',
                    'san_signup_date', 'san_signup_people', 'san_other']
    import_export_args = {'import_resource_class': SandboxBasicResources}
    list_filter = ['san_number', 'san_name', 'san_type', 'san_group', 'san_gender', 'san_class', 'san_class_num', 'san_id_number',
                   'san_loc', 'san_deg',
                   'san_major',
                   'san_company', 'san_duty',
                   'san_status', 'san_origin', 'san_cellphone', 'san_wechat', 'san_email',
                   'san_signup_date', 'san_signup_people', 'san_other', 'san_class__class_name', ]
    list_editable = list_display
    search_fields = ['san_number', 'san_name', 'san_class__class_name']
    show_booksanks = False  

    def tuition_state(self, obj):
        info = obj.san_name
        if obj.sandboxtuition.fee_date == '空':
            color_code = 'red'
            # info = '无交费信息'
        else:
            color_code = 'black'
            # info = '已交费'
        return format_html('<span style="color:{};">{}</span>', color_code, info)

    tuition_state.short_description = '姓名'
    tuition_state.admin_order_field = 'san_name'

    # inlines = [TuitionInline]
    def get_form_layout(self):
        self.form_layout = BasicLayout
        return super().get_form_layout()

    # TODO CODEREVIEW Django默认生成的父键查询子键的方法名全部是小写
    # TODO CODEREVIEW 重写save_models方法
    # def save_models(self):
    #     obj = self.new_obj
    #     obj.save()
    #     obj.sandboxtuition_set.create()
    #     obj.sandboxexam_set.create()
    #     obj.sandboxwechat_set.create()
    #     obj.sandboxexamextra_set.create()
    #     obj.sandboxtextbook_set.create()
    #     obj.sandboxcertification_set.create()


@xadmin.sites.register(SandboxClass)
class ClassAdmin(object):
    '''
    班级信息
    '''

    class ClassResources(resources.ModelResource):
        # def __init__(self):
        #     super().__init__()
        #     field_list = apps.get_model('sandbox', 'SandboxClass')._meta.fields
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
            model = SandboxClass
            fields = ('class_name', 'class_teacher', 'class_recruit_teacher', 'class_date')
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
    show_booksanks = False
    ordering = ['-class_index']


@xadmin.sites.register(SandboxTuition)
class TuitionAdmin(object):
    """
    交费信息
    """

    class TuitionResources(resources.ModelResource):
        class TuitionForeignWidget(ForeignKeyWidget):
            def get_queryset(self, value, row, *args, **kwargs):
                return SandboxBasic.objects.filter(
                    san_number__iexact=row["relate_sandbox"]
                )

        relate_sandbox = fields.Field(
            attribute='relate_sandbox',
            column_name='relate_sandbox',
            widget=TuitionForeignWidget(SandboxBasic, 'san_number')
        )

        class Meta:
            model = SandboxTuition
            import_id_fields = ('relate_sandbox',)
            # 导入数据时，如果该条数据未修改过，则会忽略
            skip_unchanged = True
            # 在导入预览页面中显示跳过的记录
            report_skipped = True
            fields = ('relate_sandbox', 'fee_train', 'fee_material', 'fee_exam', 'fee_total', 'fee_date', 'fee_method', 'fee_tax', 'fee_invoice_header',
                      'fee_invoice_id', 'fee_invoice_date', 'fee_other')

    list_display = ['relate_sandbox', 'get_san_name', 'get_san_class', 
                    'fee_train', 'fee_material', 'fee_exam', 'fee_total', 
                    'fee_date', 'fee_method', 'fee_tax',
                    'fee_invoice_header',
                    'fee_invoice_id', 'fee_invoice_date', 'fee_other'
                    ]
    # TODO CODEVIEW filter中外键的处理
    list_filter = ['relate_sandbox__san_name','fee_train', 'fee_material', 'fee_exam', 'fee_total', 'fee_date', 'fee_method',
                    'relate_sandbox__san_class__class_name', 'fee_tax', 'fee_invoice_header',
                    'fee_invoice_id', 'fee_invoice_date', 'fee_other']
    show_booksanks = False
    import_export_args = {'import_resource_class': TuitionResources,
                          }
    search_fields = ['relate_sandbox__san_name', 'relate_sandbox__san_number', 'relate_sandbox__san_number', 'relate_sandbox__san_class__class_name']
    list_editable = ['fee_train', 'fee_material', 'fee_exam', 'fee_total', 'fee_date', 'fee_method', 'fee_id', 'fee_tax', 'fee_invoice_header',
                     'fee_invoice_id', 'fee_invoice_date', 'fee_other']
    readonly_fields = ['relate_sandbox']

    def get_form_layout(self):
        self.form_layout = TuitionLayout
        return super().get_form_layout()


@xadmin.sites.register(SandboxTextbook)
class TextbookAdmin(object):
    """
    教材信息
    """

    class TextbookResources(resources.ModelResource):
        class TextbookForeignWidget(ForeignKeyWidget):
            def get_queryset(self, value, row, *args, **kwargs):
                return SandboxBasic.objects.filter(
                    san_number__iexact=row["relate_sandbox"]
                )

        relate_sandbox = fields.Field(
            attribute='relate_sandbox',
            column_name='relate_sandbox',
            widget=TextbookForeignWidget(SandboxBasic, 'san_number')
        )

        class Meta:
            model = SandboxTextbook
            import_id_fields = ('relate_sandbox',)
            # 导入数据时，如果该条数据未修改过，则会忽略
            skip_unchanged = True
            # 在导入预览页面中显示跳过的记录
            report_skipped = True
            fields = ('relate_sandbox', 'text_sandbox', 'text_two', 'text_three', 'text_train', 'text_manual', 'text_other')

    import_export_args = {'import_resource_class': TextbookResources, }
    list_display = ['relate_sandbox', 'get_san_name', 'get_san_class', 'text_sandbox', 'text_two', 'text_three', 'text_train', 'text_manual', 'text_other']
    list_filter = ['relate_sandbox__san_name', 'relate_sandbox__san_number','text_sandbox', 'text_two', 'text_three', 'text_train', 'text_other', 'relate_sandbox__san_class__class_name']
    search_fields = ['relate_sandbox__san_name', 'relate_sandbox__san_number', 'relate_sandbox__san_class__class_name']
    readonly_fields = ['relate_sandbox']
    list_editable = ['text_sandbox', 'text_two', 'text_three', 'text_train', 'text_manual', 'text_other']
    show_booksanks = False


@xadmin.sites.register(SandboxWechat)
class WechatAdmin(object):
    """
    365开通情况
    """

    class WechatResources(resources.ModelResource):
        class WechatForeignWidget(ForeignKeyWidget):
            def get_queryset(self, value, row, *args, **kwargs):
                return SandboxBasic.objects.filter(
                    san_number__iexact=row["relate_sandbox"]
                )

        relate_sandbox = fields.Field(
            attribute='relate_sandbox',
            column_name='relate_sandbox',
            widget=WechatForeignWidget(SandboxBasic, 'san_number')
        )

        class Meta:
            model = SandboxWechat
            import_id_fields = ('relate_sandbox',)
            # 导入数据时，如果该条数据未修改过，则会忽略
            skip_unchanged = True
            # 在导入预览页面中显示跳过的记录
            report_skipped = True
            fields = ('relate_sandbox', 'wechat_number', 'wechat_nickname', 'wechat_date', 'wechat_other')

    import_export_args = {'import_resource_class': WechatResources, }
    list_display = ['relate_sandbox', 'get_san_name', 'get_san_class', 'wechat_number', 'wechat_nickname',
                    'wechat_date', 'wechat_other']
    list_filter = ['relate_sandbox__san_name', 'relate_sandbox__san_number','wechat_number', 'wechat_nickname', 'wechat_date', 'relate_sandbox__san_class__class_name', 'wechat_other']
    search_fields = ['relate_sandbox__san_name', 'relate_sandbox__san_number', 'relate_sandbox__san_class__class_name']
    readonly_fields = ['relate_sandbox']
    list_editable = ['wechat_number', 'wechat_nickname', 'wechat_date', 'wechat_other']
    show_booksanks = False


@xadmin.sites.register(SandboxExam)
class ExamAdmin(object):
    """
    考试信息
    """

    class ExamResources(resources.ModelResource):
        class ExamForeignWidget(ForeignKeyWidget):
            def get_queryset(self, value, row, *args, **kwargs):
                return SandboxBasic.objects.filter(
                    san_number__iexact=row["relate_sandbox"]
                )

        relate_sandbox = fields.Field(
            attribute='relate_sandbox',
            column_name='relate_sandbox',
            widget=ExamForeignWidget(SandboxBasic, 'san_number')
        )

        class Meta:
            model = SandboxExam
            import_id_fields = ('relate_sandbox',)
            # 导入数据时，如果该条数据未修改过，则会忽略
            skip_unchanged = True
            # 在导入预览页面中显示跳过的记录
            report_skipped = True
            fields = (
            'relate_sandbox', 'batch', 'exam_total', 'exam_nation', 'exam_practice', 'other')

    import_export_args = {'import_resource_class': ExamResources, }
    list_display = ['relate_sandbox', 'get_san_name', 'get_san_class', 'batch', 
                    'exam_total', 'exam_nation', 'exam_practice', 'other']
    list_filter = ['relate_sandbox__san_name', 'relate_sandbox__san_number', 'relate_sandbox__san_class__class_name',
                   'batch', 'exam_total', 'exam_nation', 'exam_practice', 'other']
    list_editable = ['batch', 'exam_total', 'exam_nation', 'exam_practice', 'other']
    show_booksanks = False
    search_fields = ['relate_sandbox__san_name', 'relate_sandbox__san_number', 'relate_sandbox__san_class__class_name']
    readonly_fields = ['relate_sandbox']


@xadmin.sites.register(SandboxCertification)
class CertificationAdmin(object):
    """
    证书信息
    """

    class CertificationResources(resources.ModelResource):
        class CertificationForeignWidget(ForeignKeyWidget):
            def get_queryset(self, value, row, *args, **kwargs):
                return SandboxBasic.objects.filter(
                    san_number__iexact=row["relate_sandbox"]
                )

        relate_sandbox = fields.Field(
            attribute='relate_sandbox',
            column_name='relate_sandbox',
            widget=CertificationForeignWidget(SandboxBasic, 'san_number')
        )

        class Meta:
            model = SandboxCertification
            import_id_fields = ('relate_sandbox',)
            # 导入数据时，如果该条数据未修改过，则会忽略
            skip_unchanged = True
            # 在导入预览页面中显示跳过的记录
            report_skipped = True
            fields = ('relate_sandbox', "ass_cert_id", "ass_cert_date", "ass_cert_draw_people", "ass_cert_draw_date",
                "nation_cert_id", "nation_cert_date", "nation_cert_draw_people", "nation_cert_draw_date", "other" )

    import_export_args = {'import_resource_class': CertificationResources, }
    list_display = ['relate_sandbox', 'get_san_name', 'get_san_class', "ass_cert_id", "ass_cert_date", "ass_cert_draw_people", "ass_cert_draw_date",
                    "nation_cert_id", "nation_cert_date", "nation_cert_draw_people", "nation_cert_draw_date", "other" ]
    list_filter = ['relate_sandbox__san_name', 'relate_sandbox__san_number', "ass_cert_id", "ass_cert_date", "ass_cert_draw_people", "ass_cert_draw_date",
                    "nation_cert_id", "nation_cert_date", "nation_cert_draw_people", "nation_cert_draw_date", "other", 'relate_sandbox__san_class__class_name']
    list_editable = ["ass_cert_id", "ass_cert_date", "ass_cert_draw_people", "ass_cert_draw_date",
                    "nation_cert_id", "nation_cert_date", "nation_cert_draw_people", "nation_cert_draw_date", "other" ]
    show_booksanks = False
    search_fields = ['relate_sandbox__san_name', 'relate_sandbox__san_number', 'relate_sandbox__san_class__class_name']
    readonly_fields = ['relate_sandbox']


@xadmin.sites.register(SandboxOnduty)
class SandboxOndutyAdmin(object):
    """
    出勤信息
    """

    class OndutyResources(resources.ModelResource):
        class OndutyForeignWidget(ForeignKeyWidget):
            def get_queryset(self, value, row, *args, **kwargs):
                return SandboxBasic.objects.filter(
                    san_number__iexact=row["relate_sandbox"]
                )

        relate_sandbox = fields.Field(
            attribute='relate_sandbox',
            column_name='relate_sandbox',
            widget=OndutyForeignWidget(SandboxBasic, 'san_number')
        )

        class Meta:
            model = SandboxOnduty
            import_id_fields = ('relate_sandbox',)
            # 导入数据时，如果该条数据未修改过，则会忽略
            skip_unchanged = True
            # 在导入预览页面中显示跳过的记录
            report_skipped = True
            fields = ('relate_sandbox', 'onduty', 'homework', 'other')

    import_export_args = {'import_resource_class': OndutyResources}
    list_display = ['relate_sandbox', 'get_san_name', 'get_san_class', 'onduty', 'homework', 'other']
    list_filter = ['relate_sandbox__san_name', 'relate_sandbox__san_number', 'relate_sandbox__san_class__class_name']
    list_editable = ['onduty', 'homework', 'other']
    show_booksanks = False
    search_fields = list_filter
    reanonly_fields = ['relate_sandbox']


@xadmin.sites.register(Total)
class TotalAdmin(object):
    """
    总览信息
    """
    list_display_links = ('san_name')
    list_display = [
        'san_number', 'san_name', 'san_gender', 'san_class', 'san_class_num', 'san_id_number',
        'san_type', 'san_group'
        'san_loc', 'san_deg', 'san_major',
        'san_company', 'san_duty',
        'san_status', 'san_origin', 'san_cellphone', 'san_wechat', 'san_email',
        'san_signup_date', 'san_signup_people', 'san_other',
        'fee_train', 'fee_material', 'fee_exam', 'fee_total', 'fee_date', 'fee_method', 'fee_tax', 'fee_invoice_header',
        'fee_invoice_id', 'fee_invoice_date', 'fee_other'
        'text_sandbox', 'text_two', 'text_three', 'text_train', 'text_manual', 'text_other',
        'wechat_number', 'wechat_nickname', 'wechat_date', 'wechat_other',
        'exam_batch', 'exam_total', 'exam_nation', 'exam_practice', 'exam_other',
        'ass_cert_id', 'ass_cert_date', 'ass_cert_draw_people', 'ass_cert_draw_date',
        'nation_cert_id', 'nation_cert_date', 'nation_cert_draw_people', 'nation_cert_draw_date', 'cert_other',
        'ond_onduty', 'ond_homework', 'ond_other'
    ]
    show_booksanks = False
    list_filter = ['sandbox__san_name', 'sandbox__san_cellphone', 'sandbox__san_class__class_name',
                   'sandbox__sandboxtuition__fee_date',
                   'sandbox__sandboxwechat__wechat_number', 'sandbox__exam__total',
                   'sandbox__sandboxcertification__ass_cert_id',
                   'sandbox__sandboxcertification__nation_cert_id']

