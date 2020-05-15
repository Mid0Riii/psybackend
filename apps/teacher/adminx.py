import xadmin
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, BooleanWidget
from .models import Teacher, FamilyTeacher, TeamTeacher, MarriageTeacher, SandboxTeacher


@xadmin.sites.register(Teacher)
class TeacherAdmin(object):
    class TeacherResources(resources.ModelResource):
        class Meta:
            model = Teacher
            fields = ('teacher_name', 'teacher_class', 'teacher_info', 'teacher_date', 'teacher_fare', 'teacher_paid')
            skip_unchanged = True
            # 在导入预览页面中显示跳过的记录
            report_skipped = True

    import_export_args = {'import_resource_class': TeacherResources}
    search_fields = ['teacher_name']
    list_display = ['teacher_name', 'teacher_class', 'teacher_info', 'teacher_date', 'teacher_fare', 'teacher_paid']
    list_filter = list_display


@xadmin.sites.register(FamilyTeacher)
class FamilyTeacherAdmin(object):
    class TeacherResources(resources.ModelResource):
        class Meta:
            model = Teacher
            fields = ('teacher_name', 'teacher_class', 'teacher_info', 'teacher_date', 'teacher_fare', 'teacher_paid')
            skip_unchanged = True
            # 在导入预览页面中显示跳过的记录
            report_skipped = True

    import_export_args = {'import_resource_class': TeacherResources}
    search_fields = ['teacher_name']
    list_display = ['teacher_name', 'teacher_class', 'teacher_info', 'teacher_date', 'teacher_fare', 'teacher_paid']
    list_filter = list_display


@xadmin.sites.register(MarriageTeacher)
class MarriageTeacherAdmin(object):
    class TeacherResources(resources.ModelResource):
        class Meta:
            model = Teacher
            fields = ('teacher_name', 'teacher_class', 'teacher_info', 'teacher_date', 'teacher_fare', 'teacher_paid')
            skip_unchanged = True
            # 在导入预览页面中显示跳过的记录
            report_skipped = True

    import_export_args = {'import_resource_class': TeacherResources}
    search_fields = ['teacher_name']
    list_display = ['teacher_name', 'teacher_class', 'teacher_info', 'teacher_date', 'teacher_fare', 'teacher_paid']
    list_filter = list_display


@xadmin.sites.register(TeamTeacher)
class TeamTeacherAdmin(object):
    class TeacherResources(resources.ModelResource):
        class Meta:
            model = Teacher
            fields = ('teacher_name', 'teacher_class', 'teacher_info', 'teacher_date', 'teacher_fare', 'teacher_paid')
            skip_unchanged = True
            # 在导入预览页面中显示跳过的记录
            report_skipped = True

    import_export_args = {'import_resource_class': TeacherResources}
    search_fields = ['teacher_name']
    list_display = ['teacher_name', 'teacher_class', 'teacher_info', 'teacher_date', 'teacher_fare', 'teacher_paid']
    list_filter = list_display


@xadmin.sites.register(SandboxTeacher)
class SandboxTeacherAdmin(object):
    class TeacherResources(resources.ModelResource):
        class Meta:
            model = Teacher
            fields = ('teacher_name', 'teacher_class', 'teacher_info', 'teacher_date', 'teacher_fare', 'teacher_paid')
            skip_unchanged = True
            # 在导入预览页面中显示跳过的记录
            report_skipped = True

    import_export_args = {'import_resource_class': TeacherResources}
    search_fields = ['teacher_name']
    list_display = ['teacher_name', 'teacher_class', 'teacher_info', 'teacher_date', 'teacher_fare', 'teacher_paid']
    list_filter = list_display
