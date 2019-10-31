import xadmin
from .models import FamilyBasic, FamilyCertification, Result, ResultExtra, FamilyTextbook, \
    FamilyTuition, FamilyWechat, FamilyClass, FamilyOnduty,Total
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, BooleanWidget
from django.apps import apps
from .layouts.detailLayouts import BasicLayout, TuitionLayout


# TODO CODEREVIEW 外键后台inline显示的用法
# class TuitionInline(object):
#     model = FamilyTuition
#     extra = 1
#     style='one'
#     readonly_fields=['fee_material', 'fee_exam', 'fee_total',
#                     'fee_exam_extra', 'fee_date', 'fee_method', 'fee_id']


@xadmin.sites.register(FamilyBasic)
class BasicAdmin(object):
    """
    家庭基本信息
    """

    class FamilyBasicResources(resources.ModelResource):
        class ClassForeignWidget(ForeignKeyWidget):
            def get_queryset(self, value, row, *args, **kwargs):
                return FamilyClass.objects.filter(
                    class_name__iexact=row["fam_class"]
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
                'fam_number', 'fam_name', 'fam_gender', 'fam_class', 'fam_class_num', 'fam_id_number',
                'fam_loc', 'fam_deg', 'fam_major',
                'fam_company', 'fam_duty',
                'fam_status', 'fam_origin', 'fam_cellphone', 'fam_wechat', 'fam_qq',
                'fam_signup_date', 'fam_signup_people','fam_teacher_level',  'fam_other')

    list_display = ['fam_number', 'fam_name', 'fam_gender', 'fam_class', 'fam_class_num', 'fam_level', 'fam_id_number',
                    'fam_loc', 'fam_deg',
                    'fam_major',
                    'fam_company', 'fam_duty',
                    'fam_status', 'fam_origin', 'fam_cellphone', 'fam_wechat', 'fam_qq',
                    'fam_signup_date', 'fam_signup_people','fam_teacher_level','fam_other']
    import_export_args = {'import_resource_class': FamilyBasicResources}
    list_filter = ['fam_number', 'fam_name', 'fam_gender', 'fam_class', 'fam_class_num', 'fam_level', 'fam_id_number',
                   'fam_loc', 'fam_deg',
                   'fam_major',
                   'fam_company', 'fam_duty',
                   'fam_status', 'fam_origin', 'fam_cellphone', 'fam_wechat', 'fam_qq',
                   'fam_signup_date', 'fam_signup_people','fam_teacher_level','fam_other', 'fam_class__class_name', ]
    list_editable = list_display
    search_fields = ['fam_number', 'fam_level', 'fam_name', 'fam_class__class_name']
    show_bookmarks = False

    # inlines = [TuitionInline]
    def get_form_layout(self):
        self.form_layout = BasicLayout
        return super().get_form_layout()

    # TODO CODEREVIEW Django默认生成的父键查询子键的方法名全部是小写
    # TODO CODEREVIEW 重写save_models方法
    # def save_models(self):
    #     obj = self.new_obj
    #     obj.save()
    #     obj.familytuition_set.create()
    #     obj.familyexam_set.create()
    #     obj.familywechat_set.create()
    #     obj.familyexamextra_set.create()
    #     obj.familytextbook_set.create()
    #     obj.familycertification_set.create()


@xadmin.sites.register(FamilyClass)
class ClassAdmin(object):
    '''
    班级信息
    '''

    class ClassResources(resources.ModelResource):
        # def __init__(self):
        #     super().__init__()
        #     field_list = apps.get_model('family', 'FamilyClass')._meta.fields
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
            model = FamilyClass
            fields = ('class_name', 'class_teacher','class_recruit_teacher', 'class_date')
            # 导入数据时，如果该条数据未修改过，则会忽略
            skip_unchanged = True
            # 在导入预览页面中显示跳过的记录
            report_skipped = True
            # 模型主键
            import_id_fields = ('class_name',)

    import_export_args = {'import_resource_class': ClassResources,
                          }
    list_display = ['class_name', 'class_teacher', 'class_recruit_teacher', 'class_date']
    list_filter = list_display
    search_fields = list_display
    show_bookmarks = False


@xadmin.sites.register(FamilyTuition)
class TuitionAdmin(object):
    """
    交费信息
    """

    class TuitionResources(resources.ModelResource):
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
            fields = ('relate_family', 'fee_train',  'fee_date', 'fee_method', 'fee_id', 'fee_tax')

    list_display = ['relate_family', 'get_fam_name', 'get_fam_class', 'fee_train', 'fee_date', 'fee_method', 'fee_id', 'fee_tax']
    # TODO CODEVIEW filter中外键的处理
    list_filter = ['fee_train', 'fee_date', 'fee_method',
                   'fee_id', 'relate_family__fam_class__class_name', 'fee_tax']
    show_bookmarks = False
    import_export_args = {'import_resource_class': TuitionResources,
                          }
    search_fields = ['relate_family__fam_name', 'relate_family__fam_number', 'relate_family__fam_class__class_name']
    list_editable = ['fee_train', 'fee_date', 'fee_method', 'fee_id', 'fee_tax']
    readonly_fields = ['relate_family']

    def get_form_layout(self):
        self.form_layout = TuitionLayout
        return super().get_form_layout()


@xadmin.sites.register(FamilyTextbook)
class TextbookAdmin(object):
    """
    教材信息
    """

    class TextbookResources(resources.ModelResource):
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
            fields = ('relate_family', 'text_basic', 'text_other')

    import_export_args = {'import_resource_class': TextbookResources, }
    list_display = ['relate_family', 'get_fam_name', 'get_fam_class', 'text_basic', 'text_other']
    list_filter = ['text_basic','text_other', 'relate_family__fam_class__class_name']
    search_fields = ['relate_family__fam_name', 'relate_family__fam_number', 'relate_family__fam_class__class_name']
    readonly_fields = ['relate_family']
    list_editable = ['text_basic','text_other']
    show_bookmarks = False


@xadmin.sites.register(FamilyWechat)
class WechatAdmin(object):
    """
    365开通情况
    """

    class WechatResources(resources.ModelResource):
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
            fields = ('relate_family', 'wechat_number', 'wechat_nickname', 'wechat_date', )

    import_export_args = {'import_resource_class': WechatResources, }
    list_display = ['relate_family', 'get_fam_name', 'get_fam_class', 'wechat_number', 'wechat_nickname',
                    'wechat_date', ]
    list_filter = ['wechat_number', 'wechat_nickname', 'wechat_date', 'relate_family__fam_class__class_name']
    search_fields = ['relate_family__fam_name', 'relate_family__fam_number', 'relate_family__fam_class__class_name']
    readonly_fields = ['relate_family']
    list_editable = ['wechat_number', 'wechat_nickname', 'wechat_date']
    show_bookmarks = False


@xadmin.sites.register(Result)
class ExamAdmin(object):
    """
    考试信息
    """

    class ExamResources(resources.ModelResource):
        class ExamForeignWidget(ForeignKeyWidget):
            def get_queryset(self, value, row, *args, **kwargs):
                return FamilyBasic.objects.filter(
                    fam_number__iexact=row["relate_family"]
                )

        relate_family = fields.Field(
            attribute='relate_family',
            column_name='relate_family',
            widget=ExamForeignWidget(FamilyBasic, 'fam_number')
        )

        class Meta:
            model = Result
            import_id_fields = ('relate_family',)
            # 导入数据时，如果该条数据未修改过，则会忽略
            skip_unchanged = True
            # 在导入预览页面中显示跳过的记录
            report_skipped = True
            fields = ('relate_family', 'date', 'homework_two_result','homework_three_result','result')

    import_export_args = {'import_resource_class': ExamResources, }
    list_display = ['relate_family', 'get_fam_name', 'get_fam_class', 'date', 'homework_two_result','homework_three_result','result']
    list_filter = ['relate_family__fam_name', 'relate_family__fam_number', 'relate_family__fam_class__class_name',
                   'date', 'homework_two_result','homework_three_result','result']
    list_editable = ['date', 'homework_two_result','homework_three_result','result']
    show_bookmarks = False
    search_fields = ['relate_family__fam_name', 'relate_family__fam_number', 'relate_family__fam_class__class_name']
    readonly_fields = ['relate_family']


@xadmin.sites.register(ResultExtra)
class ExamExtraAdmin(object):
    """
    补考信息
    """

    class ExamResources(resources.ModelResource):
        class ExamForeignWidget(ForeignKeyWidget):
            def get_queryset(self, value, row, *args, **kwargs):
                return FamilyBasic.objects.filter(
                    fam_number__iexact=row["relate_family"]
                )

        relate_family = fields.Field(
            attribute='relate_family',
            column_name='relate_family',
            widget=ExamForeignWidget(FamilyBasic, 'fam_number')
        )

        class Meta:
            model = ResultExtra
            import_id_fields = ('relate_family',)
            # 导入数据时，如果该条数据未修改过，则会忽略
            skip_unchanged = True
            # 在导入预览页面中显示跳过的记录
            report_skipped = True
            fields = ('relate_family','date', 'homework_two_result','homework_three_result','result')

    import_export_args = {'import_resource_class': ExamResources, }
    list_display = ['relate_family', 'get_fam_name', 'get_fam_class', 'date', 'homework_two_result',
                    'homework_three_result', 'result']
    list_filter = ['relate_family__fam_name', 'relate_family__fam_number', 'relate_family__fam_class__class_name',
                   'date', 'homework_two_result', 'homework_three_result', 'result']
    list_editable = ['date', 'homework_two_result', 'homework_three_result', 'result']
    show_bookmarks = False
    search_fields = ['relate_family__fam_name', 'relate_family__fam_number', 'relate_family__fam_class__class_name']
    readonly_fields = ['relate_family']


@xadmin.sites.register(FamilyCertification)
class CertificationAdmin(object):
    """
    证书信息
    """

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
            fields = ('relate_family', 'cert_id', 'cert_date', 'cert_draw_people', 'cert_draw_date')

    import_export_args = {'import_resource_class': CertificationResources, }
    list_display = ['relate_family', 'get_fam_name', 'get_fam_class', 'cert_id', 'cert_date', 'cert_draw_people',
                    'cert_draw_date']
    list_filter = ['relate_family__fam_name', 'relate_family__fam_number', 'cert_id', 'cert_date', 'cert_draw_people',
                   'cert_draw_date', 'relate_family__fam_class__class_name']
    list_editable = ['cert_id', 'cert_date', 'cert_draw_people', 'cert_draw_date']
    show_bookmarks = False
    search_fields = ['relate_family__fam_name', 'relate_family__fam_number', 'relate_family__fam_class__class_name']
    readonly_fields = ['relate_family']


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
            fields = ('relate_family', 'onduty', 'homework1','homework2','homework3', 'other')

    import_export_args = {'import_resource_class': OndutyResources}
    list_display = ['relate_family', 'get_fam_name', 'get_fam_class', 'onduty', 'homework1','homework2','homework3', 'other']
    list_filter = ['relate_family__fam_name', 'relate_family__fam_number', 'relate_family__fam_class__class_name']
    list_editable = ['onduty', 'homework1','homework2','homework3', 'other']
    show_bookmarks = False
    search_fields = list_filter
    reanonly_fields = ['relate_family']

@xadmin.sites.register(Total)
class TotalAdmin(object):
    list_display = [
        'fam_number', 'fam_name', 'fam_gender', 'fam_class', 'fam_class_num', 'fam_id_number',
        'fam_loc', 'fam_deg', 'fam_major',
        'fam_company', 'fam_duty',
        'fam_status', 'fam_origin', 'fam_cellphone', 'fam_wechat', 'fam_qq',
        'fam_signup_date', 'fam_signup_people', 'fam_teacher_level', 'fam_other',
        'fee_train', 'fee_date', 'fee_method', 'fee_id', 'fee_tax',
        'text_basic', 'text_other',
        'exam_date', 'exam_homework2_result', 'exam_homework3_result', 'exam_result',
        'exam_date_extra', 'exam_homework2_extra', 'exam_homework3_extra', 'exam_result_extra',
        'cert_id', 'cert_date', 'cert_draw_people', 'cert_draw_date',
    ]
    show_bookmarks=False
    list_filter = ['family__fam_name','family__fam_cellphone','family__fam_class__class_name','family__fam_teacher_level','family__familytuition__fee_date',
                   'family__familywechat__wechat_number','family__result__result','family__familycertification__cert_id']