import xadmin
from django.utils.html import format_html
from .models import TrainBasic, TrainCertification, Result, ResultExtra, TrainTextbook, \
    TrainTuition, TrainWechat, TrainClass, TrainOnduty, Total
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, BooleanWidget
from django.apps import apps
from .layouts.detailLayouts import BasicLayout, TuitionLayout


class TrainBasicResources(resources.ModelResource):
    def __init__(self):
        super(TrainBasicResources, self).__init__()
        field_list = apps.get_model('trainClass', 'TrainBasic')._meta.fields
        # 应用名与模型名
        self.verbose_name_dict = {}
        # 获取所有字段的verbose_name并存放在verbose_name_dict字典里
        for i in field_list:
            self.verbose_name_dict[i.name] = i.verbose_name
        fields = self.get_fields()
        # 默认导入导出field的column_name为字段的名称
        # 这里修改为字段的verbose_name
        for field in fields:
            field_name = self.get_field_name(field)
            if field_name in self.verbose_name_dict.keys():
                field.column_name = self.verbose_name_dict[field_name]

    class ClassForeignWidget(ForeignKeyWidget):
        def get_queryset(self, value, row, *args, **kwargs):
            return TrainClass.objects.filter(
                class_name__iexact=row["班级"]
            )

    tra_class = fields.Field(
        attribute='tra_class',
        column_name='tra_class',
        widget=ClassForeignWidget(TrainClass, 'class_name')
    )

    class Meta:
        model = TrainBasic
        import_id_fields = ('tra_number',)
        # 导入数据时，如果该条数据未修改过，则会忽略
        skip_unchanged = True
        # 在导入预览页面中显示跳过的记录
        report_skipped = True
        fields = (
            'tra_type', 'tra_group',
            'tra_number', 'tra_name', 'tra_gender', 'tra_class', 'tra_class_num', 'tra_id_number',
            'tra_loc', 'tra_deg', 'tra_major',
            'tra_company', 'tra_duty',
            'tra_status', 'tra_origin', 'tra_cellphone', 'tra_wechat', 'tra_qq',
            'tra_signup_date', 'tra_signup_people', 'tra_other')


@xadmin.sites.register(TrainBasic)
class BasicAdmin(object):
    """
    训练班基本信息
    """

    list_display = ['tra_type', 'tra_group', 'tra_number', 'tuition_state', 'tra_gender', 'tra_class', 'tra_class_num',
                    'tra_id_number',
                    'tra_loc', 'tra_deg',
                    'tra_major',
                    'tra_company', 'tra_duty',
                    'tra_status', 'tra_origin', 'tra_cellphone', 'tra_wechat', 'tra_qq',
                    'tra_signup_date', 'tra_signup_people', 'tra_other']
    import_export_args = {'import_resource_class': TrainBasicResources}
    list_filter = ['tra_type', 'tra_group', 'tra_number', 'tra_name', 'tra_gender', 'tra_class', 'tra_class_num',
                   'tra_id_number',
                   'tra_loc', 'tra_deg',
                   'tra_major',
                   'tra_company', 'tra_duty',
                   'tra_status', 'tra_origin', 'tra_cellphone', 'tra_wechat', 'tra_qq',
                   'tra_signup_date', 'tra_signup_people', 'tra_other', 'tra_class__class_name', ]
    list_editable = list_display
    exclude = ['tra_teacher_level', ]
    list_display_links = ['tra_number']
    search_fields = ['tra_number', 'tra_name', 'tra_class__class_name']
    show_bookmarks = False

    def tuition_state(self, obj):
        info = obj.tra_name
        if obj.Traintuition.fee_date == '空':
            color_code = 'red'
            # info = '无交费信息'
        else:
            color_code = 'black'
            # info = '已交费'
        return format_html('<span style="color:{};">{}</span>', color_code, info)

    tuition_state.short_description = '姓名'
    tuition_state.admin_order_field = 'tra_name'

    def get_form_layout(self):
        self.form_layout = BasicLayout
        return super().get_form_layout()


class ClassResources(resources.ModelResource):
    def __init__(self):
        super(ClassResources, self).__init__()
        field_list = apps.get_model('trainClass', 'TrainClass')._meta.fields
        # 应用名与模型名
        self.verbose_name_dict = {}
        # 获取所有字段的verbose_name并存放在verbose_name_dict字典里
        for i in field_list:
            self.verbose_name_dict[i.name] = i.verbose_name
        fields = self.get_fields()
        # 默认导入导出field的column_name为字段的名称
        # 这里修改为字段的verbose_name
        for field in fields:
            field_name = self.get_field_name(field)
            if field_name in self.verbose_name_dict.keys():
                field.column_name = self.verbose_name_dict[field_name]

    class Meta:
        model = TrainClass
        fields = ('class_name', 'class_teacher', 'class_recruit_teacher', 'class_date')
        # 导入数据时，如果该条数据未修改过，则会忽略
        skip_unchanged = True
        # 在导入预览页面中显示跳过的记录
        report_skipped = True
        # 模型主键
        import_id_fields = ('class_name',)


@xadmin.sites.register(TrainClass)
class ClassAdmin(object):
    '''
    训练班级信息
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
    def __init__(self):
        super(TuitionResources, self).__init__()
        field_list = apps.get_model('trainClass', 'TrainTuition')._meta.fields
        # 应用名与模型名
        self.verbose_name_dict = {}
        # 获取所有字段的verbose_name并存放在verbose_name_dict字典里
        for i in field_list:
            self.verbose_name_dict[i.name] = i.verbose_name
        fields = self.get_fields()
        # 默认导入导出field的column_name为字段的名称
        # 这里修改为字段的verbose_name
        for field in fields:
            field_name = self.get_field_name(field)
            if field_name in self.verbose_name_dict.keys():
                field.column_name = self.verbose_name_dict[field_name]

    class TuitionForeignWidget(ForeignKeyWidget):
        def get_queryset(self, value, row, *args, **kwargs):
            return TrainBasic.objects.filter(
                tra_number__iexact=row["relate_trainingclass"]
            )

    relate_trainingclass = fields.Field(
        attribute='relate_trainingclass',
        column_name='relate_trainingclass',
        widget=TuitionForeignWidget(TrainBasic, 'tra_number')
    )

    class Meta:
        model = TrainTuition
        import_id_fields = ('relate_trainingclass',)
        # 导入数据时，如果该条数据未修改过，则会忽略
        skip_unchanged = True
        # 在导入预览页面中显示跳过的记录
        report_skipped = True
        fields = ('relate_trainingclass', 'fee_train', 'fee_material', 'fee_date', 'fee_method', 'fee_id', 'fee_tax',
                  'fee_invoice_header',
                  'fee_invoice_id', 'fee_invoice_date', 'fee_invoice_inc')


@xadmin.sites.register(TrainTuition)
class TuitionAdmin(object):
    """
    交费信息
    """

    list_display = ['relate_trainingclass', 'get_tra_name', 'get_tra_class', 'fee_train', 'fee_material', 'fee_date',
                    'fee_method', 'fee_id', 'fee_tax', 'fee_invoice_header',
                    'fee_invoice_id', 'fee_invoice_date', 'fee_invoice_inc'
                    ]
    # TODO CODEVIEW filter中外键的处理
    list_filter = ['relate_trainingclass__tra_name', 'relate_trainingclass__tra_class__class_name', 'fee_tax', 'fee_train',
                   'fee_material', 'fee_date', 'fee_method', 'fee_id', 'fee_tax', 'fee_invoice_header',
                   'fee_invoice_id', 'fee_invoice_date', 'fee_invoice_inc']
    show_bookmarks = False
    import_export_args = {'import_resource_class': TuitionResources,
                          }
    search_fields = ['relate_trainingclass__tra_name', 'relate_trainingclass__tra_number', 'relate_trainingclass__tra_number',
                     'relate_trainingclass__tra_class__class_name']
    list_editable = ['fee_train', 'fee_material', 'fee_date', 'fee_method', 'fee_id', 'fee_tax', 'fee_invoice_header',
                     'fee_invoice_id', 'fee_invoice_date', 'fee_invoice_inc']
    # readonly_fields = ['relate_trainingclass']

    def get_form_layout(self):
        self.form_layout = TuitionLayout
        return super().get_form_layout()


class TextbookResources(resources.ModelResource):
    def __init__(self):
        super(TextbookResources, self).__init__()
        field_list = apps.get_model('trainClass', 'TrainTuition')._meta.fields
        # 应用名与模型名
        self.verbose_name_dict = {}
        # 获取所有字段的verbose_name并存放在verbose_name_dict字典里
        for i in field_list:
            self.verbose_name_dict[i.name] = i.verbose_name
        fields = self.get_fields()
        # 默认导入导出field的column_name为字段的名称
        # 这里修改为字段的verbose_name
        for field in fields:
            field_name = self.get_field_name(field)
            if field_name in self.verbose_name_dict.keys():
                field.column_name = self.verbose_name_dict[field_name]

    class TextbookForeignWidget(ForeignKeyWidget):
        def get_queryset(self, value, row, *args, **kwargs):
            return TrainBasic.objects.filter(
                tra_number__iexact=row["relate_trainingclass"]
            )

    relate_trainingclass = fields.Field(
        attribute='relate_trainingclass',
        column_name='relate_trainingclass',
        widget=TextbookForeignWidget(TrainBasic, 'tra_number')
    )

    class Meta:
        model = TrainTextbook
        import_id_fields = ('relate_trainingclass',)
        # 导入数据时，如果该条数据未修改过，则会忽略
        skip_unchanged = True
        # 在导入预览页面中显示跳过的记录
        report_skipped = True
        fields = ('relate_trainingclass', 'text_basic', 'text_basic2', 'text_guide', 'text_manual', 'text_other')


@xadmin.sites.register(TrainTextbook)
class TextbookAdmin(object):
    """
    教材信息
    """
    import_export_args = {'import_resource_class': TextbookResources, }
    list_display = ['relate_trainingclass', 'get_tra_name', 'get_tra_class', 'text_basic', 'text_basic2', 'text_guide',
                    'text_manual', 'text_other']
    list_filter = ['relate_trainingclass__tra_name', 'relate_trainingclass__tra_number', 'text_basic', 'text_other',
                   'relate_trainingclass__tra_class__class_name', 'text_basic2', 'text_guide', ]
    search_fields = ['relate_trainingclass__tra_name', 'relate_trainingclass__tra_number', 'relate_trainingclass__tra_class__class_name']
    # readonly_fields = ['relate_trainingclass']
    list_editable = ['text_basic', 'text_manual', 'text_other', 'text_basic2', 'text_guide', ]
    show_bookmarks = False

class WechatResources(resources.ModelResource):
    def __init__(self):
        super(WechatResources, self).__init__()
        field_list = apps.get_model('trainClass', 'TrainTuition')._meta.fields
        # 应用名与模型名
        self.verbose_name_dict = {}
        # 获取所有字段的verbose_name并存放在verbose_name_dict字典里
        for i in field_list:
            self.verbose_name_dict[i.name] = i.verbose_name
        fields = self.get_fields()
        # 默认导入导出field的column_name为字段的名称
        # 这里修改为字段的verbose_name
        for field in fields:
            field_name = self.get_field_name(field)
            if field_name in self.verbose_name_dict.keys():
                field.column_name = self.verbose_name_dict[field_name]

    class WechatForeignWidget(ForeignKeyWidget):
        def get_queryset(self, value, row, *args, **kwargs):
            return TrainBasic.objects.filter(
                tra_number__iexact=row["relate_trainingclass"]
            )

    relate_trainingclass = fields.Field(
        attribute='relate_trainingclass',
        column_name='relate_trainingclass',
        widget=WechatForeignWidget(TrainBasic, 'tra_number')
    )

    class Meta:
        model = TrainWechat
        import_id_fields = ('relate_trainingclass',)
        # 导入数据时，如果该条数据未修改过，则会忽略
        skip_unchanged = True
        # 在导入预览页面中显示跳过的记录
        report_skipped = True
        fields = ('relate_trainingclass', 'wechat_number', 'wechat_nickname', 'wechat_date', 'wechat_other')

@xadmin.sites.register(TrainWechat)
class WechatAdmin(object):
    """
    365开通情况
    """
    import_export_args = {'import_resource_class': WechatResources, }
    list_display = ['relate_trainingclass', 'get_tra_name', 'get_tra_class', 'wechat_number', 'wechat_nickname',
                    'wechat_date', 'wechat_other', ]
    list_filter = ['relate_trainingclass__tra_name', 'relate_trainingclass__tra_number', 'wechat_number', 'wechat_nickname',
                   'wechat_date', 'relate_trainingclass__tra_class__class_name']
    search_fields = ['relate_trainingclass__tra_name', 'relate_trainingclass__tra_number', 'relate_trainingclass__tra_class__class_name']
    # readonly_fields = ['relate_trainingclass']
    list_editable = ['wechat_number', 'wechat_nickname', 'wechat_date', 'wechat_other']
    show_bookmarks = False


class ExamResources(resources.ModelResource):
    def __init__(self):
        super(ExamResources, self).__init__()
        field_list = apps.get_model('trainClass', 'TrainTuition')._meta.fields
        # 应用名与模型名
        self.verbose_name_dict = {}
        # 获取所有字段的verbose_name并存放在verbose_name_dict字典里
        for i in field_list:
            self.verbose_name_dict[i.name] = i.verbose_name
        fields = self.get_fields()
        # 默认导入导出field的column_name为字段的名称
        # 这里修改为字段的verbose_name
        for field in fields:
            field_name = self.get_field_name(field)
            if field_name in self.verbose_name_dict.keys():
                field.column_name = self.verbose_name_dict[field_name]
    class ExamForeignWidget(ForeignKeyWidget):
        def get_queryset(self, value, row, *args, **kwargs):
            return TrainBasic.objects.filter(
                tra_number__iexact=row["relate_trainingclass"]
            )

    relate_trainingclass = fields.Field(
        attribute='relate_trainingclass',
        column_name='relate_trainingclass',
        widget=ExamForeignWidget(TrainBasic, 'tra_number')
    )

    class Meta:
        model = Result
        import_id_fields = ('relate_trainingclass',)
        # 导入数据时，如果该条数据未修改过，则会忽略
        skip_unchanged = True
        # 在导入预览页面中显示跳过的记录
        report_skipped = True
        fields = (
            'relate_trainingclass', 'date', 'total', 'nation_result', 'pre', 'speech', 'other')

@xadmin.sites.register(Result)
class ExamAdmin(object):
    """
    考试信息
    """
    import_export_args = {'import_resource_class': ExamResources, }
    list_display = ['relate_trainingclass', 'get_tra_name', 'get_tra_class', 'date',
                    'total', 'nation_result', 'pre', 'speech', 'other']
    list_filter = ['relate_trainingclass__tra_name', 'relate_trainingclass__tra_number', 'relate_trainingclass__tra_class__class_name',
                   'date', 'homework_two_result', 'homework_three_result', 'result', 'total', 'nation_result', 'pre',
                   'speech', 'other']
    list_editable = ['date', 'total', 'nation_result', 'pre', 'speech', 'other']
    show_bookmarks = False
    exclude = ['homework_one_result', 'homework_two_result', 'result']
    search_fields = ['relate_trainingclass__tra_name', 'relate_trainingclass__tra_number', 'relate_trainingclass__tra_class__class_name']
    # readonly_fields = ['relate_trainingclass']

class CertificationResources(resources.ModelResource):
    class CertificationForeignWidget(ForeignKeyWidget):
        def get_queryset(self, value, row, *args, **kwargs):
            return TrainBasic.objects.filter(
                tra_number__iexact=row["relate_trainingclass"]
            )

    relate_trainingclass = fields.Field(
        attribute='relate_trainingclass',
        column_name='relate_trainingclass',
        widget=CertificationForeignWidget(TrainBasic, 'tra_number')
    )

    class Meta:
        model = TrainCertification
        import_id_fields = ('relate_trainingclass',)
        # 导入数据时，如果该条数据未修改过，则会忽略
        skip_unchanged = True
        # 在导入预览页面中显示跳过的记录
        report_skipped = True
        fields = ('relate_trainingclass', 'cert_id', 'cert_date', 'cert_draw_people', 'cert_draw_date', 'cert_nation_id',
                  'cert_nation_people', 'cert_other',)



@xadmin.sites.register(TrainCertification)
class CertificationAdmin(object):
    """
    证书信息
    """
    import_export_args = {'import_resource_class': CertificationResources, }
    list_display = ['relate_trainingclass', 'get_tra_name', 'get_tra_class', 'cert_id', 'cert_date', 'cert_draw_people',
                    'cert_draw_date', 'cert_nation_id', 'cert_nation_people', 'cert_other', ]
    list_filter = ['relate_trainingclass__tra_name', 'relate_trainingclass__tra_number', 'cert_id', 'cert_date', 'cert_draw_people',
                   'cert_draw_date', 'relate_trainingclass__tra_class__class_name', 'cert_nation_id', 'cert_nation_people',
                   'cert_other', ]
    list_editable = ['cert_id', 'cert_date', 'cert_draw_people', 'cert_draw_date', 'cert_nation_id',
                     'cert_nation_people', 'cert_other', ]
    show_bookmarks = False
    search_fields = ['relate_trainingclass__tra_name', 'relate_trainingclass__tra_number', 'relate_trainingclass__tra_class__class_name']
    # readonly_fields = ['relate_trainingclass']


@xadmin.sites.register(TrainOnduty)
class TrainOndutyAdmin(object):
    """
    出勤信息
    """

    class OndutyResources(resources.ModelResource):
        class OndutyForeignWidget(ForeignKeyWidget):
            def get_queryset(self, value, row, *args, **kwargs):
                return TrainBasic.objects.filter(
                    tra_number__iexact=row["relate_trainingclass"]
                )

        relate_trainingclass = fields.Field(
            attribute='relate_trainingclass',
            column_name='relate_trainingclass',
            widget=OndutyForeignWidget(TrainBasic, 'tra_number')
        )

        class Meta:
            model = TrainOnduty
            import_id_fields = ('relate_trainingclass',)
            # 导入数据时，如果该条数据未修改过，则会忽略
            skip_unchanged = True
            # 在导入预览页面中显示跳过的记录
            report_skipped = True
            fields = ('relate_trainingclass', 'onduty', 'homework', 'other')

    import_export_args = {'import_resource_class': OndutyResources}
    list_display = ['relate_trainingclass', 'get_tra_name', 'get_tra_class', 'onduty', 'homework', 'other']
    list_filter = ['relate_trainingclass__tra_name', 'relate_trainingclass__tra_number', 'relate_trainingclass__tra_class__class_name']
    list_editable = ['onduty', 'homwwork', 'homework', 'other']
    show_bookmarks = False
    search_fields = list_filter
    reanonly_fields = ['relate_trainingclass']


@xadmin.sites.register(Total)
class TotalAdmin(object):
    """
    总览信息
    """
    list_display = [
        'tra_type', 'tra_number', 'tra_group',
        'tra_name', 'tra_gender', 'tra_class', 'tra_class_num', 'tra_id_number',
        'tra_loc', 'tra_deg', 'tra_major',
        'tra_company', 'tra_duty',
        'tra_status', 'tra_origin', 'tra_cellphone', 'tra_wechat', 'tra_qq',
        'tra_signup_date', 'tra_signup_people', 'tra_other',
        'fee_train', 'fee_material', 'fee_exam', 'fee_total',
        'fee_date', 'fee_method', 'fee_id', 'fee_tax', 'fee_invoice_header',
        'fee_invoice_id', 'fee_invoice_date', 'fee_other',
        'text_basic', 'text_basic2', 'text_guide', 'text_manual', 'text_other',
        'wechat_number', 'wechat_nickname', 'wechat_date', 'onduty', 'homework', 'other',
        'exam_date', 'exam_total', 'exam_nation', 'exam_pre', 'exam_speech', 'exam_other',
        'cert_id', 'cert_draw_people', 'cert_draw_date', 'cert_nation_id', 'cert_nation_people', 'cert_other'
    ]
    show_bookmarks = False
    list_filter = ['trainingclass__tra_name', 'trainingclass__tra_cellphone', 'trainingclass__tra_class__class_name',
                   'trainingclass__tra_teacher_level', 'trainingclass__traintuition__fee_date',
                   'trainingclass__trainwechat__wechat_number', 'trainingclass__result__result',
                   'trainingclass__traincertification__cert_id']