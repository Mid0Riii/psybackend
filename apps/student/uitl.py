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

lst = basic+tuition+text+wechat+duty+exam+examextra+cert

print(lst)
# with open("disgusting.py",'w+') as file:
    # for i in range(len(basic)):
    #     file.write("def "+str(basic[i])+"(self):\n")
    #     file.write("    return self.student."+str(basic[i])+"\n")
    #     file.write(str(basic[i])+".short_description = \"\"\n")
    # for i in range(len(tuition)):
    #     file.write("def " + str(tuition[i]) + "(self):\n")
    #     file.write("    return self.student.tuition." + str(tuition[i]) + "\n")
    #     file.write(str(tuition[i]) + ".short_description = \"\"\n")
    # for i in range(len(text)):
    #     file.write("def " + str(text[i]) + "(self):\n")
    #     file.write("    return self.student.studenttextbook." + str(text[i]) + "\n")
    #     file.write(str(text[i]) + ".short_description = \"\"\n")
    # for i in range(len(wechat)):
    #     file.write("def " + str(wechat[i]) + "(self):\n")
    #     file.write("    return self.student.studentwechat." + str(wechat[i]) + "\n")
    #     file.write(str(wechat[i]) + ".short_description = \"\"\n")
    # for i in range(len(wechat)):
    #     file.write("def " + str(wechat[i]) + "(self):\n")
    #     file.write("    return self.student.studentwechat." + str(wechat[i]) + "\n")
    #     file.write(str(wechat[i]) + ".short_description = \"\"\n")
    # for i in range(len(exam)):
    #     file.write("def " + str(exam[i]) + "(self):\n")
    #     file.write("    return self.student.studentexam." + str(exam[i]) + "\n")
    #     file.write(str(exam[i]) + ".short_description = \"\"\n")
    # for i in range(len(examextra)):
    #     file.write("def " + str(examextra[i])+"_extra"+"(self):\n")
    #     file.write("    return self.student.studentexamextra." + str(examextra[i]) + "\n")
    #     file.write(str(examextra[i])+"_extra" + ".short_description = \"\"\n")
    # for i in range(len(cert)):
    #     file.write("def " + str(cert[i]) + "(self):\n")
    #     file.write("    return self.student.studentcertification." + str(cert[i]) + "\n")
    #     file.write(str(cert[i]) + ".short_description = \"\"\n")
    # for i in range(len(duty)):
    #     file.write("def " + str(duty[i]) + "(self):\n")
    #     file.write("    return self.student.studentonduty." + str(duty[i]) + "\n")
    #     file.write(str(duty[i]) + ".short_description = \"\"\n")


