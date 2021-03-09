import xadmin
from django.utils.html import format_html
from .models import TeamBasic, TeamCertification, TeamExam, TeamTextbook, \
    TeamTuition, TeamWechat, TeamClass, TeamOnduty, Total
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, BooleanWidget
from django.apps import apps
from .layouts.detailLayouts import BasicLayout, TuitionLayout


# TODO CODEREVIEW 外键后台inline显示的用法
# class TuitionInline(object):
#     model = TeamTuition
#     extra = 1
#     style='one'
#     # readonly_fields=['fee_material', 'fee_exam', 'fee_total',
#                     'fee_exam_extra', 'fee_date', 'fee_method', 'fee_id']


@xadmin.sites.register(TeamBasic)
class BasicAdmin(object):
    """
    团体心理辅导基本信息
    """

    class TeamBasicResources(resources.ModelResource):
        class ClassForeignWidget(ForeignKeyWidget):
            def get_queryset(self, value, row, *args, **kwargs):
                return TeamClass.objects.filter(
                    class_name__iexact=row["tea_class"]
                )

        tea_class = fields.Field(
            attribute='tea_class',
            column_name='tea_class',
            widget=ClassForeignWidget(TeamClass, 'class_name')
        )

        class Meta:
            model = TeamBasic
            import_id_fields = ('tea_number',)
            # 导入数据时，如果该条数据未修改过，则会忽略
            skip_unchanged = True
            # 在导入预览页面中显示跳过的记录
            report_skipped = True
            fields = (
                'tea_number', 'tea_name', 'tea_gender', 'tea_id_number',
                'tea_loc', 'tea_deg', 'tea_major',
                'tea_company', 'tea_duty',
                'tea_status', 'tea_origin', 'tea_cellphone', 'tea_wechat', 'tea_email',
                'tea_signup_date', 'tea_signup_people', 'tea_other', 'tea_class')

    list_display = ['tea_number', 'tuition_state', 'tea_gender', 'tea_class', 'tea_class_num', 'tea_type', 'tea_group',
                    'tea_id_number',
                    'tea_loc', 'tea_deg',
                    'tea_major',
                    'tea_company', 'tea_duty',
                    'tea_status', 'tea_origin', 'tea_cellphone', 'tea_wechat', 'tea_email',
                    'tea_signup_date', 'tea_signup_people', 'tea_other']
    import_export_args = {'import_resource_class': TeamBasicResources}
    list_filter = ['tea_number', 'tea_name', 'tea_type', 'tea_group', 'tea_gender', 'tea_class', 'tea_class_num',
                   'tea_id_number',
                   'tea_loc', 'tea_deg',
                   'tea_major',
                   'tea_company', 'tea_duty',
                   'tea_status', 'tea_origin', 'tea_cellphone', 'tea_wechat', 'tea_email',
                   'tea_signup_date', 'tea_signup_people', 'tea_other', 'tea_class__class_name', ]
    list_editable = list_display
    search_fields = ['tea_number', 'tea_name', 'tea_class__class_name']
    show_bookteaks = False

    def tuition_state(self, obj):
        info = obj.tea_name
        if obj.teamtuition.fee_date == '空':
            color_code = 'red'
            # info = '无交费信息'
        else:
            color_code = 'black'
            # info = '已交费'
        return format_html('<span style="color:{};">{}</span>', color_code, info)

    tuition_state.short_description = '姓名'
    tuition_state.admin_order_field = 'tea_name'

    # inlines = [TuitionInline]
    def get_form_layout(self):
        self.form_layout = BasicLayout
        return super().get_form_layout()

    # TODO CODEREVIEW Django默认生成的父键查询子键的方法名全部是小写
    # TODO CODEREVIEW 重写save_models方法
    # def save_models(self):
    #     obj = self.new_obj
    #     obj.save()
    #     obj.teamtuition_set.create()
    #     obj.teamexam_set.create()
    #     obj.teamwechat_set.create()
    #     obj.teamexamextra_set.create()
    #     obj.teamtextbook_set.create()
    #     obj.teamcertification_set.create()


@xadmin.sites.register(TeamClass)
class ClassAdmin(object):
    '''
    班级信息
    '''

    class ClassResources(resources.ModelResource):
        # def __init__(self):
        #     super().__init__()
        #     field_list = apps.get_model('team', 'TeamClass')._meta.fields
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
            model = TeamClass
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
    show_bookteaks = False
    ordering = ['-class_index']


@xadmin.sites.register(TeamTuition)
class TuitionAdmin(object):
    """
    交费信息
    """

    class TuitionResources(resources.ModelResource):
        class TuitionForeignWidget(ForeignKeyWidget):
            def get_queryset(self, value, row, *args, **kwargs):
                return TeamBasic.objects.filter(
                    tea_number__iexact=row["relate_team"]
                )

        relate_team = fields.Field(
            attribute='relate_team',
            column_name='relate_team',
            widget=TuitionForeignWidget(TeamBasic, 'tea_number')
        )

        class Meta:
            model = TeamTuition
            import_id_fields = ('relate_team',)
            # 导入数据时，如果该条数据未修改过，则会忽略
            skip_unchanged = True
            # 在导入预览页面中显示跳过的记录
            report_skipped = True
            fields = (
            'relate_team', 'fee_train', 'fee_material', 'fee_exam', 'fee_total', 'fee_date', 'fee_method', 'fee_tax',
            'fee_invoice_header',
            'fee_invoice_id', 'fee_invoice_date', 'fee_other')

    list_display = ['relate_team', 'get_tea_name', 'get_tea_class', 'fee_train', 'fee_material', 'fee_exam',
                    'fee_total', 'fee_date', 'fee_method', 'fee_tax', 'fee_invoice_header',
                    'fee_invoice_id', 'fee_invoice_date', 'fee_other']
    # TODO CODEVIEW filter中外键的处理
    list_filter = ['relate_team__tea_name', 'fee_train', 'fee_material', 'fee_exam', 'fee_total', 'fee_date',
                   'fee_method',
                   'relate_team__tea_class__class_name', 'fee_tax', 'fee_invoice_header',
                   'fee_invoice_id', 'fee_invoice_date', 'fee_other']
    show_bookteaks = False
    import_export_args = {'import_resource_class': TuitionResources,
                          }
    search_fields = ['relate_team__tea_name', 'relate_team__tea_number', 'relate_team__tea_number',
                     'relate_team__tea_class__class_name']
    list_editable = ['fee_train', 'fee_material', 'fee_exam', 'fee_total', 'fee_date', 'fee_method', 'fee_id',
                     'fee_tax', 'fee_invoice_header',
                     'fee_invoice_id', 'fee_invoice_date', 'fee_other']

    # readonly_fields = ['relate_team']

    def get_form_layout(self):
        self.form_layout = TuitionLayout
        return super().get_form_layout()


@xadmin.sites.register(TeamTextbook)
class TextbookAdmin(object):
    """
    教材信息
    """

    class TextbookResources(resources.ModelResource):
        class TextbookForeignWidget(ForeignKeyWidget):
            def get_queryset(self, value, row, *args, **kwargs):
                return TeamBasic.objects.filter(
                    tea_number__iexact=row["relate_team"]
                )

        relate_team = fields.Field(
            attribute='relate_team',
            column_name='relate_team',
            widget=TextbookForeignWidget(TeamBasic, 'tea_number')
        )

        class Meta:
            model = TeamTextbook
            import_id_fields = ('relate_team',)
            # 导入数据时，如果该条数据未修改过，则会忽略
            skip_unchanged = True
            # 在导入预览页面中显示跳过的记录
            report_skipped = True
            fields = ('relate_team', 'text_team', 'text_two', 'text_train', 'text_manual', 'text_other')

    import_export_args = {'import_resource_class': TextbookResources, }
    list_display = ['relate_team', 'get_tea_name', 'get_tea_class', 'text_team', 'text_two', 'text_train',
                    'text_manual', 'text_other']
    list_filter = ['relate_team__tea_name', 'relate_team__tea_number', 'text_team', 'text_two', 'text_train',
                   'text_other', 'relate_team__tea_class__class_name']
    search_fields = ['relate_team__tea_name', 'relate_team__tea_number', 'relate_team__tea_class__class_name']
    # readonly_fields = ['relate_team']
    list_editable = ['text_team', 'text_two', 'text_train', 'text_manual', 'text_other']
    show_bookteaks = False


@xadmin.sites.register(TeamWechat)
class WechatAdmin(object):
    """
    365开通情况
    """

    class WechatResources(resources.ModelResource):
        class WechatForeignWidget(ForeignKeyWidget):
            def get_queryset(self, value, row, *args, **kwargs):
                return TeamBasic.objects.filter(
                    tea_number__iexact=row["relate_team"]
                )

        relate_team = fields.Field(
            attribute='relate_team',
            column_name='relate_team',
            widget=WechatForeignWidget(TeamBasic, 'tea_number')
        )

        class Meta:
            model = TeamWechat
            import_id_fields = ('relate_team',)
            # 导入数据时，如果该条数据未修改过，则会忽略
            skip_unchanged = True
            # 在导入预览页面中显示跳过的记录
            report_skipped = True
            fields = ('relate_team', 'wechat_number', 'wechat_nickname', 'wechat_date', 'wechat_other')

    import_export_args = {'import_resource_class': WechatResources, }
    list_display = ['relate_team', 'get_tea_name', 'get_tea_class', 'wechat_number', 'wechat_nickname',
                    'wechat_date', 'wechat_other']
    list_filter = ['relate_team__tea_name', 'relate_team__tea_number', 'wechat_number', 'wechat_nickname',
                   'wechat_date', 'relate_team__tea_class__class_name', 'wechat_other']
    search_fields = ['relate_team__tea_name', 'relate_team__tea_number', 'relate_team__tea_class__class_name']
    # readonly_fields = ['relate_team']
    list_editable = ['wechat_number', 'wechat_nickname', 'wechat_date', 'wechat_other']
    show_bookteaks = False


@xadmin.sites.register(TeamExam)
class ExamAdmin(object):
    """
    考试信息
    """

    class ExamResources(resources.ModelResource):
        class ExamForeignWidget(ForeignKeyWidget):
            def get_queryset(self, value, row, *args, **kwargs):
                return TeamBasic.objects.filter(
                    tea_number__iexact=row["relate_team"]
                )

        relate_team = fields.Field(
            attribute='relate_team',
            column_name='relate_team',
            widget=ExamForeignWidget(TeamBasic, 'tea_number')
        )

        class Meta:
            model = TeamExam
            import_id_fields = ('relate_team',)
            # 导入数据时，如果该条数据未修改过，则会忽略
            skip_unchanged = True
            # 在导入预览页面中显示跳过的记录
            report_skipped = True
            fields = (
                'relate_team', 'batch', 'exam_total', 'exam_nation', 'exam_practice', 'other')

    import_export_args = {'import_resource_class': ExamResources, }
    list_display = ['relate_team', 'get_tea_name', 'get_tea_id_number', 'get_tea_class', 'batch',
                    'exam_total', 'exam_nation', 'exam_practice', 'result', 'other']
    list_filter = ['relate_team__tea_name', 'relate_team__tea_number', 'relate_team__tea_class__class_name',
                   'batch', 'exam_total', 'exam_nation', 'exam_practice', 'result', 'other']
    list_editable = ['batch', 'exam_total', 'exam_nation', 'exam_practice', 'result', 'other']
    show_bookmarks = False
    search_fields = ['relate_team__tea_name', 'relate_team__tea_number', 'relate_team__tea_class__class_name']
    # readonly_fields = ['relate_team']


@xadmin.sites.register(TeamCertification)
class CertificationAdmin(object):
    """
    证书信息
    """

    class CertificationResources(resources.ModelResource):
        class CertificationForeignWidget(ForeignKeyWidget):
            def get_queryset(self, value, row, *args, **kwargs):
                return TeamBasic.objects.filter(
                    tea_number__iexact=row["relate_team"]
                )

        relate_team = fields.Field(
            attribute='relate_team',
            column_name='relate_team',
            widget=CertificationForeignWidget(TeamBasic, 'tea_number')
        )

        class Meta:
            model = TeamCertification
            import_id_fields = ('relate_team',)
            # 导入数据时，如果该条数据未修改过，则会忽略
            skip_unchanged = True
            # 在导入预览页面中显示跳过的记录
            report_skipped = True
            fields = ('relate_team', "ass_cert_id", "ass_cert_date", "ass_cert_draw_people", "ass_cert_draw_date",
                      "nation_cert_id", "nation_cert_date", "nation_cert_draw_people", "nation_cert_draw_date", "other")

    import_export_args = {'import_resource_class': CertificationResources, }
    list_display = ['relate_team', 'get_tea_name', 'get_tea_id_number', 'get_tea_class', "ass_cert_id", "ass_cert_date",
                    "ass_cert_draw_people", "ass_cert_draw_date",
                    "nation_cert_id", "nation_cert_date", "nation_cert_draw_people", "nation_cert_draw_date", "other"]
    list_filter = ['relate_team__tea_name', 'relate_team__tea_number', "ass_cert_id", "ass_cert_date",
                   "ass_cert_draw_people", "ass_cert_draw_date",
                   "nation_cert_id", "nation_cert_date", "nation_cert_draw_people", "nation_cert_draw_date", "other",
                   'relate_team__tea_class__class_name']
    list_editable = ["ass_cert_id", "ass_cert_date", "ass_cert_draw_people", "ass_cert_draw_date",
                     "nation_cert_id", "nation_cert_date", "nation_cert_draw_people", "nation_cert_draw_date", "other"]
    show_bookteaks = False
    search_fields = ['relate_team__tea_name', 'relate_team__tea_number', 'relate_team__tea_class__class_name']
    # readonly_fields = ['relate_team']


@xadmin.sites.register(TeamOnduty)
class TeamOndutyAdmin(object):
    """
    出勤信息
    """

    class OndutyResources(resources.ModelResource):
        class OndutyForeignWidget(ForeignKeyWidget):
            def get_queryset(self, value, row, *args, **kwargs):
                return TeamBasic.objects.filter(
                    tea_number__iexact=row["relate_team"]
                )

        relate_team = fields.Field(
            attribute='relate_team',
            column_name='relate_team',
            widget=OndutyForeignWidget(TeamBasic, 'tea_number')
        )

        class Meta:
            model = TeamOnduty
            import_id_fields = ('relate_team',)
            # 导入数据时，如果该条数据未修改过，则会忽略
            skip_unchanged = True
            # 在导入预览页面中显示跳过的记录
            report_skipped = True
            fields = ('relate_team', 'onduty', 'homework', 'other')

    import_export_args = {'import_resource_class': OndutyResources}
    list_display = ['relate_team', 'get_tea_name', 'get_tea_class', 'onduty', 'homework', 'other']
    list_filter = ['relate_team__tea_name', 'relate_team__tea_number', 'relate_team__tea_class__class_name']
    list_editable = ['onduty', 'homework', 'other']
    show_bookteaks = False
    search_fields = list_filter
    reanonly_fields = ['relate_team']


@xadmin.sites.register(Total)
class TotalAdmin(object):
    """
    总览信息
    """
    list_display_links = ('tea_name')
    list_display = [
        'tea_number', 'tea_name', 'tea_gender', 'tea_class', 'tea_class_num', 'tea_id_number',
        'tea_type', 'tea_group',
        'tea_loc', 'tea_deg', 'tea_major',
        'tea_company', 'tea_duty',
        'tea_status', 'tea_origin', 'tea_cellphone', 'tea_wechat', 'tea_email',
        'tea_signup_date', 'tea_signup_people', 'tea_other',
        'fee_train', 'fee_material', 'fee_exam', 'fee_total', 'fee_date', 'fee_method', 'fee_tax', 'fee_invoice_header',
        'fee_invoice_id', 'fee_invoice_date', 'fee_other',
        'text_team', 'text_two', 'text_train', 'text_manual', 'text_other',
        'wechat_number', 'wechat_nickname', 'wechat_date', 'wechat_other',
        'exam_batch', 'exam_total', 'exam_nation', 'exam_practice', 'exam_other',
        'ass_cert_id', 'ass_cert_date', 'ass_cert_draw_people', 'ass_cert_draw_date',
        'nation_cert_id', 'nation_cert_date', 'nation_cert_draw_people', 'nation_cert_draw_date', 'cert_other',
        'ond_onduty', 'ond_homework', 'ond_other',
    ]
    show_bookteaks = False
    list_filter = ['team__tea_name', 'team__tea_cellphone', 'team__tea_class__class_name',
                   'team__teamtuition__fee_date',
                   'team__teamwechat__wechat_number',
                   'team__teamcertification__ass_cert_id',
                   'team__teamcertification__nation_cert_id']
