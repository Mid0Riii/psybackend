basic = ['stu_number', 'stu_name', 'stu_gender', 'stu_class', 'stu_class_num', 'stu_level', 'stu_id_number',
                    'stu_loc', 'stu_deg',
                    'stu_major',
                    'stu_company', 'stu_duty',
                    'stu_status', 'stu_origin', 'stu_cellphone', 'stu_wechat', 'stu_qq',
                    'stu_signup_date', 'stu_signup_people', 'stu_other']
tuition = ['fee_train', 'fee_material', 'fee_exam',
                    'fee_total',
                    'fee_exam_extra', 'fee_date', 'fee_method', 'fee_id', 'fee_tax']
text=['text_basic', 'text_sec', 'text_sec_exer',
                    'text_sec_measure',
                    'text_thr',
                    'text_thr_exer', 'text_manual', 'text_exam', 'text_other']
wechat=['wechat_number', 'wechat_nickname',
                    'wechat_date']
exam=['exam_date', 'exam_theory', 'exam_theory_result',
                    'exam_practise',
                    'exam_practise_result', 'exam_total', 'exam_total_result', 'exam_status']
examextra=['exam_date', 'exam_theory', 'exam_theory_result',
                    'exam_practise',
                    'exam_practise_result', 'exam_total', 'exam_total_result', 'exam_status']
cert=['cert_id', 'cert_date', 'cert_draw_people',
                    'cert_draw_date']
duty =['onduty', 'homework', 'other']


for i in range(len(basic)):
    basic[i] = 'student__'+basic[i]
for i in range(len(tuition)):
    tuition[i] = 'student__tuition__'+tuition[i]
print(basic+tuition)