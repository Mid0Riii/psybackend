from django.urls import path
from . import views
import xadmin



urlpatterns = [
    path('',xadmin.site.urls),
    path('hr/staffs/', views.staff_list.as_view()),
    path('hr/staffs/<int:pk>/', views.staff_detail.as_view()),
    path('ht/deps/',views.dep_list.as_view()),
    path('hr/deps/<int:pk>/', views.dep_detail.as_view()),
    # 概要
    # path('schema/', schema_view),
    path('hr/api/JobinDep/<int:pk>',views.get_jobs),
    path('hr/api/meal/<int:pk>',views.Meal_personal),
    path('hr/dismissstaff/<int:pk>/detail/custom_form',views.staff_form_iframe),
    path('hr/currentstaff/<int:pk>/detail/custom_form',views.staff_form_iframe),
    path('hr/allstaff/<int:pk>/detail/custom_form',views.staff_form_iframe),
    path('hr/department/<int:pk>/detail/custom_form',views.dep_form_iframe),
    path('hr/meal_allow/statistic',views.Meal_statistic),

]
