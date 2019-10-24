from .models import Staff
from django.shortcuts import render, get_object_or_404,HttpResponse,redirect
from django.http.response import JsonResponse


def staff_form_iframe(request, pk):
    obj = get_object_or_404(Staff, pk=pk)
    dic = {
        'id':pk,
        'name': obj.personal_name,
        'gender': obj.personal_gender,
        'idn_num': obj.personal_id_num,
        'birth_date': obj.personal_birth_date,
        'enter_date': obj.work_enter_date,
        'hire_method': obj.work_hire_method,
        'on_market': obj.personal_on_market,
        'soc_ins': obj.personal_soc_ins,
        'soc_ins_num': obj.personal_soc_ins_id,
        'department': obj.work_department,
        'duty': obj.work_duty,
        'duty_hire_date': obj.work_duty_hire_date,
        'set_rank_date': obj.work_set_rank_date,
        'hire_rank_aca_date': obj.work_hire_rank_aca_date,
        'position': obj.work_position,
        'title': obj.work_title,
        'edu_background': obj.edu_background,
        'edu_grade': obj.edu_grade,
        'is_marry': obj.personal_is_marry,
        'status': obj.personal_status,
        'folk': obj.personal_folk,
        'reg_location': obj.personal_reg_location,
        'phone': obj.personal_phone,
        'phone_other': obj.personal_phone_other,
        'emer_people': obj.personal_emer_people,
        'emer_phone': obj.personal_emer_phone,
        'more': obj.other_more,
        'learn_exp': obj.edu_learn_exp,
        'current_location': obj.personal_current_location,
        'avatar': '/media/' + str(obj.other_avatar),
    }
    for key in dic:
        if str(dic[key]) == 'None':
            dic[key] = ''
    # dic = {'format':format}
    # return render(request,'list_form_iframe.html',dic)
    return render(request, 'list_form_iframe.html', {'dic': dic})
