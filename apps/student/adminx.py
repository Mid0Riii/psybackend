import xadmin
from .models import StudentBasic, StudentCertification, StudentExam, StudentExamExtra, StudentTextbook, \
    Tuition, StudentWechat, StudentClass, Onduty, Total
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, BooleanWidget
from .layouts.detailLayouts import BasicLayout, TuitionLayout, ExamLayout
from django.utils.html import format_html
from xadmin.plugins.add_html import Change_total_link
from xadmin.views import DetailAdminView, ListAdminView, ModelFormAdminView, UpdateAdminView, CreateAdminView


# TODO CODEREVIEW 外键后台inline显示的用法
# class TuitionInline(object):
#     model = StudentTuition
#     extra = 1
#     style='one'
#     readonly_fields=['fee_material', 'fee_exam', 'fee_total',
#                     'fee_exam_extra', 'fee_date', 'fee_method', 'fee_id']


@xadmin.sites.register(StudentBasic)
class BasicAdmin(object):
    """
    学生基本信息
    """

    class StudentBasicResources(resources.ModelResource):
        class ClassForeignWidget(ForeignKeyWidget):
            def get_queryset(self, value, row, *args, **kwargs):
                return StudentClass.objects.filter(
                    class_name__iexact=row["stu_class"]
                )

        stu_class = fields.Field(
            attribute='stu_class',
            column_name='stu_class',
            widget=ClassForeignWidget(StudentClass, 'class_name')
        )

        class Meta:
            model = StudentBasic
            import_id_fields = ('stu_number',)
            # 导入数据时，如果该条数据未修改过，则会忽略
            skip_unchanged = True
            # 在导入预览页面中显示跳过的记录
            report_skipped = True
            fields = (
                'stu_type', 'stu_group',
                'stu_number', 'stu_name', 'stu_gender', 'stu_class', 'stu_class_num', 'stu_level', 'stu_id_number',
                'stu_loc', 'stu_deg', 'stu_major',
                'stu_company', 'stu_duty',
                'stu_status', 'stu_origin', 'stu_cellphone', 'stu_wechat', 'stu_qq',
                'stu_signup_date', 'stu_signup_people', 'stu_other')

    list_display = ['stu_type', 'stu_group', 'stu_number', 'tuition_state', 'stu_gender', 'stu_class', 'stu_class_num',
                    'stu_level', 'stu_id_number',
                    'stu_loc', 'stu_deg',
                    'stu_major',
                    'stu_company', 'stu_duty',
                    'stu_status', 'stu_origin', 'stu_cellphone', 'stu_wechat', 'stu_qq',
                    'stu_signup_date', 'stu_signup_people', 'stu_other']
    import_export_args = {'import_resource_class': StudentBasicResources}
    list_filter = ['stu_type', 'stu_group', 'stu_number', 'stu_name', 'stu_gender', 'stu_class', 'stu_class_num',
                   'stu_level', 'stu_id_number',
                   'stu_loc', 'stu_deg',
                   'stu_major',
                   'stu_company', 'stu_duty',
                   'stu_status', 'stu_origin', 'stu_cellphone', 'stu_wechat', 'stu_qq',
                   'stu_signup_date', 'stu_signup_people', 'stu_other', 'stu_class__class_name', ]
    list_editable = list_display
    list_display_links = ['stu_number']
    search_fields = ['stu_number', 'stu_level', 'stu_name', 'stu_class__class_name']
    show_bookmarks = False

    def tuition_state(self, obj):
        info = obj.stu_name
        if obj.tuition.fee_date == '空':
            color_code = 'red'
            # info = '无交费信息'
        else:
            color_code = 'black'
            # info = '已交费'
        return format_html('<span style="color:{};">{}</span>', color_code, info)

    tuition_state.short_description = '姓名'

    # inlines = [TuitionInline]
    def get_form_layout(self):
        self.form_layout = BasicLayout
        return super().get_form_layout()

    # TODO CODEREVIEW Django默认生成的父键查询子键的方法名全部是小写
    # TODO CODEREVIEW 重写save_models方法
    # def save_models(self):
    #     obj = self.new_obj
    #     obj.save()
    #     obj.studenttuition_set.create()
    #     obj.studentexam_set.create()
    #     obj.studentwechat_set.create()
    #     obj.studentexamextra_set.create()
    #     obj.studenttextbook_set.create()
    #     obj.studentcertification_set.create()


@xadmin.sites.register(StudentClass)
class ClassAdmin(object):
    '''
    班级信息
    '''

    class ClassResources(resources.ModelResource):
        class Meta:
            model = StudentClass
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
    show_bookmarks = False
    ordering = ['-class_index']


@xadmin.sites.register(Tuition)
class TuitionAdmin(object):
    """
    交费信息
    """

    class TuitionResources(resources.ModelResource):
        class TuitionForeignWidget(ForeignKeyWidget):
            def get_queryset(self, value, row, *args, **kwargs):
                return StudentBasic.objects.filter(
                    stu_number__iexact=row["relate_student"]
                )

        relate_student = fields.Field(
            attribute='relate_student',
            column_name='relate_student',
            widget=TuitionForeignWidget(StudentBasic, 'stu_number')
        )

        class Meta:
            model = Tuition
            import_id_fields = ('relate_student',)
            # 导入数据时，如果该条数据未修改过，则会忽略
            skip_unchanged = True
            # 在导入预览页面中显示跳过的记录
            report_skipped = True
            fields = ('relate_student', 'fee_train', 'fee_material', 'fee_exam', 'fee_total',
                    'fee_date', 'fee_method', 'fee_id', 'fee_tax', 'fee_invoice_header',
                      'fee_invoice_id', 'fee_invoice_date', 'fee_invoice_inc', 'fee_info')

    list_display = ['relate_student', 'get_stu_name', 'get_stu_class', 'fee_train', 'fee_material', 'fee_exam',
                    'fee_total',
                     'fee_date', 'fee_method', 'fee_id', 'fee_tax', 'fee_invoice_header',
                    'fee_invoice_id', 'fee_invoice_date', 'fee_invoice_inc', 'fee_info']
    # TODO CODEVIEW filter中外键的处理
    list_filter = ['relate_student__stu_name', 'relate_student__stu_number', 'fee_train', 'fee_material', 'fee_exam',
                   'fee_total', 'fee_exam_extra', 'fee_date', 'fee_method',
                   'fee_id', 'relate_student__stu_class__class_name', 'fee_tax', 'fee_invoice_inc', 'fee_info']
    show_bookmarks = False
    import_export_args = {'import_resource_class': TuitionResources, }
    search_fields = ['relate_student__stu_name', 'relate_student__stu_number', 'relate_student__stu_class__class_name']
    list_editable = ['fee_train', 'fee_material', 'fee_exam', 'fee_total',
                     'fee_exam_extra', 'fee_date', 'fee_method', 'fee_id', 'fee_tax', 'fee_invoice_header',
                     'fee_invoice_id', 'fee_invoice_date', 'fee_invoice_inc', 'fee_info']
    exclude = ['relate_class','fee_exam_extra']
    readonly_fields = ['relate_student']

    def get_form_layout(self):
        self.form_layout = TuitionLayout
        return super().get_form_layout()


@xadmin.sites.register(StudentTextbook)
class TextbookAdmin(object):
    """
    教材信息
    """

    class TextbookResources(resources.ModelResource):
        class TextbookForeignWidget(ForeignKeyWidget):
            def get_queryset(self, value, row, *args, **kwargs):
                return StudentBasic.objects.filter(
                    stu_number__iexact=row["relate_student"]
                )

        relate_student = fields.Field(
            attribute='relate_student',
            column_name='relate_student',
            widget=TextbookForeignWidget(StudentBasic, 'stu_number')
        )

        class Meta:
            model = StudentTextbook
            import_id_fields = ('relate_student',)
            # 导入数据时，如果该条数据未修改过，则会忽略
            skip_unchanged = True
            # 在导入预览页面中显示跳过的记录
            report_skipped = True
            fields = (
            'relate_student', 'text_basic', 'text_sec', 'text_sec_exer', 'text_sec_measure', 'text_thr_measure',
            'text_thr',
            'text_thr_exer', 'text_manual', 'text_exam', 'text_CAS', 'text_guide', 'text_other')

    import_export_args = {'import_resource_class': TextbookResources, }
    list_display = ['relate_student', 'get_stu_name', 'get_stu_class', 'text_basic', 'text_sec', 'text_sec_exer',
                    'text_sec_measure',
                    'text_thr',
                    'text_thr_exer', 'text_thr_measure', 'text_manual', 'text_exam', 'text_CAS', 'text_guide',
                    'text_other']
    list_filter = ['relate_student__stu_name', 'relate_student__stu_number', 'text_basic', 'text_sec', 'text_sec_exer',
                   'text_sec_measure', 'text_thr',
                   'text_thr_exer', 'text_thr_measure', 'text_manual', 'text_exam', 'text_CAS', 'text_guide',
                   'text_other', 'relate_student__stu_class__class_name']
    search_fields = ['relate_student__stu_name', 'relate_student__stu_number', 'relate_student__stu_class__class_name']
    readonly_fields = ['relate_student']
    list_editable = ['text_basic', 'text_sec', 'text_sec_exer', 'text_sec_measure',
                     'text_thr', 'text_CAS', 'text_guide',
                     'text_thr_exer', 'text_thr_measure', 'text_manual', 'text_exam', 'text_other']
    show_bookmarks = False


@xadmin.sites.register(StudentWechat)
class WechatAdmin(object):
    """
    365开通情况
    """

    class WechatResources(resources.ModelResource):
        class WechatForeignWidget(ForeignKeyWidget):
            def get_queryset(self, value, row, *args, **kwargs):
                return StudentBasic.objects.filter(
                    stu_number__iexact=row["relate_student"]
                )

        relate_student = fields.Field(
            attribute='relate_student',
            column_name='relate_student',
            widget=WechatForeignWidget(StudentBasic, 'stu_number')
        )

        class Meta:
            model = StudentWechat
            import_id_fields = ('relate_student',)
            # 导入数据时，如果该条数据未修改过，则会忽略
            skip_unchanged = True
            # 在导入预览页面中显示跳过的记录
            report_skipped = True
            fields = (
            'relate_student', 'wechat_number', 'wechat_nickname', 'wechat_date', 'wechat_test', 'wechat_date2')

    import_export_args = {'import_resource_class': WechatResources, }
    list_display = ['relate_student', 'get_stu_name', 'get_stu_class', 'wechat_number', 'wechat_nickname',
                    'wechat_date', 'wechat_test', 'wechat_date2']
    list_filter = ['relate_student__stu_name', 'relate_student__stu_number', 'wechat_number', 'wechat_nickname',
                   'wechat_date', 'wechat_test', 'relate_student__stu_class__class_name', 'wechat_date2']
    search_fields = ['relate_student__stu_name', 'relate_student__stu_number', 'relate_student__stu_class__class_name']
    readonly_fields = ['relate_student']
    list_editable = ['wechat_number', 'wechat_nickname', 'wechat_date', 'wechat_test', 'wechat_date2']
    show_bookmarks = False


@xadmin.sites.register(StudentExam)
class ExamAdmin(object):
    """
    考试信息
    """

    class ExamResources(resources.ModelResource):
        class ExamForeignWidget(ForeignKeyWidget):
            def get_queryset(self, value, row, *args, **kwargs):
                return StudentBasic.objects.filter(
                    stu_number__iexact=row["relate_student"]
                )

        relate_student = fields.Field(
            attribute='relate_student',
            column_name='relate_student',
            widget=ExamForeignWidget(StudentBasic, 'stu_number')
        )

        class Meta:
            model = StudentExam
            import_id_fields = ('relate_student',)
            # 导入数据时，如果该条数据未修改过，则会忽略
            skip_unchanged = True
            # 在导入预览页面中显示跳过的记录
            report_skipped = True
            fields = ('relate_student', 'exam_date',  'exam_theory_result',
                      'exam_practise_result', 'exam_total', 'exam_total_result', 'exam_status',
                      'exam_practise_result2','exam_pre','exam_speech','exam_thr_theory','exam_thr_skill','exam_sec_theory','exam_sec_skill','exam_thesis','exam_CAS',)

    import_export_args = {'import_resource_class': ExamResources, }
    list_display = ['relate_student', 'get_stu_name', 'get_stu_class', 'exam_date',
                     'exam_theory_result',
                    'exam_practise_result',
                    'exam_practise_result2','exam_pre','exam_speech','exam_thr_theory','exam_thr_skill','exam_sec_theory','exam_sec_skill','exam_thesis','exam_CAS',
                    'exam_total', 'exam_total_result', 'exam_status']
    list_filter = ['relate_student__stu_name', 'relate_student__stu_number', 'relate_student__stu_class__class_name',
                   'exam_date', 'exam_theory', 'exam_theory_result', 'exam_practise', 'exam_practise_result',
                   'exam_total', 'exam_total_result', 'exam_status', 'exam_practise_result2','exam_pre','exam_speech','exam_thr_theory','exam_thr_skill','exam_sec_theory','exam_sec_skill','exam_thesis','exam_CAS',]
    list_editable = ['exam_date', 'exam_theory', 'exam_theory_result', 'exam_practise',
                     'exam_practise_result', 'exam_total', 'exam_total_result', 'exam_status','exam_practise_result2','exam_pre','exam_speech','exam_thr_theory','exam_thr_skill','exam_sec_theory','exam_sec_skill','exam_thesis','exam_CAS',]
    show_bookmarks = False
    search_fields = ['relate_student__stu_name', 'relate_student__stu_number', 'relate_student__stu_class__class_name']
    readonly_fields = ['relate_student']
    exclude=['exam_theory','exam_practise']

    def get_form_layout(self):
        self.form_layout = ExamLayout
        return super().get_form_layout()


# @xadmin.sites.register(StudentExamExtra)
# class ExamExtraAdmin(object):
#     """
#     补考信息
#     """
#
#     class ExamResources(resources.ModelResource):
#         class ExamForeignWidget(ForeignKeyWidget):
#             def get_queryset(self, value, row, *args, **kwargs):
#                 return StudentBasic.objects.filter(
#                     stu_number__iexact=row["relate_student"]
#                 )
#
#         relate_student = fields.Field(
#             attribute='relate_student',
#             column_name='relate_student',
#             widget=ExamForeignWidget(StudentBasic, 'stu_number')
#         )
#
#         class Meta:
#             model = StudentExamExtra
#             import_id_fields = ('relate_student',)
#             # 导入数据时，如果该条数据未修改过，则会忽略
#             skip_unchanged = True
#             # 在导入预览页面中显示跳过的记录
#             report_skipped = True
#             fields = ('relate_student', 'exam_date', 'exam_theory', 'exam_theory_result', 'exam_practise',
#                       'exam_practise_result', 'exam_total', 'exam_total_result', 'exam_status')
#
#     import_export_args = {'import_resource_class': ExamResources, }
#     # TODO CODEREVIEW:自定义列的用法
#     list_display = ['relate_student', 'get_stu_name', 'get_stu_class', 'exam_date', 'exam_theory', 'exam_theory_result',
#                     'exam_practise',
#                     'exam_practise_result', 'exam_total', 'exam_total_result', 'exam_status']
#     list_filter = ['relate_student__stu_name', 'relate_student__stu_number', 'relate_student__stu_class__class_name',
#                    'exam_date', 'exam_theory', 'exam_theory_result',
#                    'exam_practise', 'exam_practise_result',
#                    'exam_total', 'exam_total_result', 'exam_status', 'relate_student__stu_class__class_name']
#     list_editable = ['exam_date', 'exam_theory', 'exam_theory_result', 'exam_practise',
#                      'exam_practise_result', 'exam_total', 'exam_total_result', 'exam_status']
#     show_bookmarks = False
#     search_fields = ['relate_student__stu_name', 'relate_student__stu_number', 'relate_student__stu_class__class_name']
#     readonly_fields = ['relate_student']
#
#     def get_form_layout(self):
#         self.form_layout = ExamLayout
#         return super().get_form_layout()


@xadmin.sites.register(StudentCertification)
class CertificationAdmin(object):
    """
    证书信息
    """

    class CertificationResources(resources.ModelResource):
        class CertificationForeignWidget(ForeignKeyWidget):
            def get_queryset(self, value, row, *args, **kwargs):
                return StudentBasic.objects.filter(
                    stu_number__iexact=row["relate_student"]
                )

        relate_student = fields.Field(
            attribute='relate_student',
            column_name='relate_student',
            widget=CertificationForeignWidget(StudentBasic, 'stu_number')
        )

        class Meta:
            model = StudentCertification
            import_id_fields = ('relate_student',)
            # 导入数据时，如果该条数据未修改过，则会忽略
            skip_unchanged = True
            # 在导入预览页面中显示跳过的记录
            report_skipped = True
            fields = ('relate_student', 'cert_id', 'cert_date', 'cert_draw_people', 'cert_draw_date','cert_nation_id','cert_nation_people','cert_CAS_id','cert_CAS_people','cert_other')

    import_export_args = {'import_resource_class': CertificationResources, }
    list_display = ['relate_student', 'get_stu_name', 'get_stu_class', 'cert_id', 'cert_date', 'cert_draw_people',
                    'cert_draw_date','cert_nation_id','cert_nation_people','cert_CAS_id','cert_CAS_people','cert_other']
    list_filter = ['relate_student__stu_name', 'relate_student__stu_number', 'cert_id', 'cert_date', 'cert_draw_people',
                   'cert_draw_date', 'relate_student__stu_class__class_name','cert_nation_id','cert_nation_people','cert_CAS_id','cert_CAS_people','cert_other']
    list_editable = ['cert_id', 'cert_date', 'cert_draw_people', 'cert_draw_date','cert_nation_id','cert_nation_people','cert_CAS_id','cert_CAS_people','cert_other']
    show_bookmarks = False
    search_fields = ['relate_student__stu_name', 'relate_student__stu_number', 'relate_student__stu_class__class_name']
    readonly_fields = ['relate_student']


@xadmin.sites.register(Onduty)
class OndutyAdmin(object):
    """
    出勤信息
    """

    class OndutyResources(resources.ModelResource):
        class OndutyForeignWidget(ForeignKeyWidget):
            def get_queryset(self, value, row, *args, **kwargs):
                return StudentBasic.objects.filter(
                    stu_number__iexact=row["relate_student"]
                )

        relate_student = fields.Field(
            attribute='relate_student',
            column_name='relate_student',
            widget=OndutyForeignWidget(StudentBasic, 'stu_number')
        )

        class Meta:
            model = Onduty
            import_id_fields = ('relate_student',)
            # 导入数据时，如果该条数据未修改过，则会忽略
            skip_unchanged = True
            # 在导入预览页面中显示跳过的记录
            report_skipped = True
            fields = ('relate_student', 'onduty', 'homework', 'other')

    import_export_args = {'import_resource_class': OndutyResources}
    list_display = ['relate_student', 'get_stu_name', 'get_stu_class', 'onduty', 'homework', 'other']
    list_filter = ['relate_student__stu_name', 'relate_student__stu_number', 'relate_student__stu_class__class_name']
    list_editable = ['relate_student', 'onduty', 'homework', 'other']
    show_bookmarks = False
    search_fields = list_filter
    reanonly_fields = ['relate_student']


xadmin.site.register_plugin(Change_total_link, ListAdminView)  # 注册插件，用于将总览界面的第一栏超链接重定向至列表视图，而非编辑视图


@xadmin.sites.register(Total)
class TotalAdmin(object):
    """
    总览信息
    """
    Change_total_link_allow = True
    list_display_links = None
    list_display = ['stu_type','stu_number','stu_group', 'stu_name', 'stu_gender', 'stu_class', 'stu_class_num', 'stu_level', 'stu_id_number',
                    'stu_loc', 'stu_deg', 'stu_major', 'stu_company', 'stu_duty', 'stu_status', 'stu_origin',
                    'stu_cellphone', 'stu_wechat', 'stu_qq', 'stu_signup_date', 'stu_signup_people', 'stu_other',
                    'fee_train', 'fee_material', 'fee_exam', 'fee_total', 'fee_date', 'fee_method','fee_id', 'fee_tax', 'fee_invoice_header',
                    'fee_invoice_id', 'fee_invoice_date','fee_invoice_inc','fee_info',
                    'text_basic', 'text_sec', 'text_sec_exer', 'text_sec_measure','text_thr',
                    'text_thr_exer','text_thr_measure','text_manual', 'text_exam','text_CAS','text_guide','text_other',
                    'wechat_number', 'wechat_nickname','wechat_date','wechat_test','wechat_date2',
                    'onduty', 'homework', 'other',
                    'exam_date', 'exam_theory_result',
                    'exam_practise_result','exam_practise_result2','exam_pre','exam_speech','exam_thr_theory','exam_thr_skill',
                    'exam_sec_theory','exam_sec_skill','exam_thesis','exam_CAS','exam_other',
                    'cert_id','cert_draw_people','cert_draw_date','cert_nation_id','cert_nation_people',
                    'cert_CAS_id','cert_CAS_people','cert_other'
                    ]
    show_bookmarks = False
    list_filter = ['student__stu_name', 'student__stu_cellphone', 'student__stu_class__class_name',
                   'student__stu_level', 'student__tuition__fee_date',
                   'student__studentwechat__wechat_number', 'student__studentexam__exam_status',
                   'student__studentcertification__cert_id']
