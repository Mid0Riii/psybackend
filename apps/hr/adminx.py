import xadmin
from .models import CurrentStaff, DismissStaff, AllStaff
from xadmin import views
from .layouts.detailLayouts import StaffLayout
# from menuLayouts import set_menu
# from utils.xadmin.plugins import add_html, change_update_to_detail,new_filter,custom_buttons,linkage_filter

#
# @xadmin.sites.register(views.CommAdminView)
# class GlobalSetting(object):
#     # 页头
#     site_title = '南大心理咨询师职业技能培训中心办公系统'
#     # 页脚
#     site_footer = 'NCUTEA.Aldrich'
#
#     def get_site_menu(self):
#         return set_menu(self)
#

# 仅做母类，不注册视图
class StaffAdmin(object):
    list_display = ['personal_name', 'personal_gender', 'personal_id_num', 'work_enter_date', 'work_department',
                    'edu_grade', 'work_position', 'work_title',]
    list_filter = ['work_department', 'personal_status', 'personal_gender','personal_birth_date', 'edu_grade', 'personal_soc_ins']
    exclude = ['fav_nums']
    Staff_custom_buttons_allow = True
    # new_filter_allow = True
    show_bookmarks = False
    Linkage_filter_allow = True
    add_html_plugins_allow = True
    list_export = ['xls']


@xadmin.sites.register(CurrentStaff)
class CurrentStaffAdmin(StaffAdmin):

    model_icon = 'fa fa-check'
    Delete_add_bottom_allow = True
    add_html_plugins_allow = True
    change_update_to_detail_allow = True

    def queryset(self):
        qs = super().queryset()
        qs = qs.filter(at_post='在职')
        return qs

    def get_form_layout(self):
        self.form_layout = StaffLayout
        return super().get_form_layout()


@xadmin.sites.register(DismissStaff)
class DismissStaffAdmin(StaffAdmin):
    Delete_add_bottom_allow = True
    show_bookmarks = False
    model_icon = 'fa fa-times'
    add_html_plugins_allow = True
    Linkage_filter_allow = True
    change_update_to_detail_allow = True

    def queryset(self):
        qs = super().queryset()
        qs = qs.filter(at_post='离职')
        return qs

    def get_form_layout(self):
        self.form_layout = StaffLayout
        return super().get_form_layout()


@xadmin.sites.register(AllStaff)
class AllStaffAdmin(StaffAdmin):
    show_bookmarks = False
    list_export = ['xls']
    change_update_to_detail_allow =True
    Linkage_filter_allow = True
    model_icon = 'fa fa-user'

    # duty_filter_allow = True
    def get_form_layout(self):
        self.form_layout = StaffLayout
        return super().get_form_layout()



# xadmin.site.register_plugin(add_html.Add_html_plugins, DetailAdminView)
# xadmin.site.register_plugin(change_update_to_detail.Change_update_to_detail, ListAdminView)
# xadmin.site.register_plugin(change_update_to_detail.Delete_add_bottom, ListAdminView)
# xadmin.site.register_plugin(new_filter.New_filter, ListAdminView)
# xadmin.site.register_plugin(custom_buttons.Staff_custom_buttons,ListAdminView)
# xadmin.site.register_plugin(add_html.Add_dep_iframe,DetailAdminView)
# xadmin.site.register_plugin(linkage_filter.Linkage_filter,UpdateAdminView)
# xadmin.site.register_plugin(linkage_filter.Linkage_filter,CreateAdminView)
# xadmin.site.register_plugin(custom_buttons.Meal_custom_buttons,ListAdminView)