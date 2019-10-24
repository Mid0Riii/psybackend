# from django.db import models
#
#
# class StudentClass(models.Model):
#     class Meta:
#         verbose_name = '班级'
#         verbose_name_plural = '班级'
#
#     class_teacher = models.CharField(max_length=64, verbose_name='负责老师', null=True, blank=True)
#     # class_name = models.CharField(max_length=64, verbose_name='班级名', unique=True, primary_key=True)
#     class_date = models.CharField(max_length=64, verbose_name='开班年份', null=True, blank=True)
#     class_name = models.CharField(max_length=64, verbose_name='班级名')
#
#     def __str__(self):
#         return self.class_name
#
# class StudentBasic(models.Model):
#     class Meta:
#         verbose_name = '基本信息'
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.stu_number
#
#     def save(self, *args, **kwargs):
#         # TODO CODEVIEW 重写保存方法需要创建外键约束时务必先保存当前对象
#         super(StudentBasic, self).save(*args, **kwargs)
#         try:
#             Tuition.objects.get(relate_student=self)
#             StudentExam.objects.get(relate_student=self)
#             StudentWechat.objects.get(relate_student=self)
#             StudentExamExtra.objects.get(relate_student=self)
#             StudentTextbook.objects.get(relate_student=self)
#         except Exception as e:
#             Tuition.objects.create(relate_student=self)
#             StudentExam.objects.create(relate_student=self)
#             StudentWechat.objects.create(relate_student=self)
#             StudentExamExtra.objects.create(relate_student=self)
#             StudentTextbook.objects.create(relate_student=self)
#             StudentCertification.objects.create(relate_student=self)
#         # super(StudentBasic, self).save(*args, **kwargs)
#     def get_verbose_name(self,field):
#         return str(field)
#     stu_number = models.CharField(max_length=128, verbose_name='学号', unique=True)
#     stu_name = models.CharField(max_length=128, verbose_name=get_verbose_name('',stu_number.verbose_name),blank=True,null=True)
#     stu_gender = models.CharField(max_length=16, choices=(('男', '男'), ('女', '女')), verbose_name='性别',blank=True,null=True)
#     stu_id_number = models.CharField(max_length=128, verbose_name='身份证号', unique=True)
#     stu_loc = models.CharField(max_length=128, verbose_name='所在地', blank=True, null=True)
#     stu_deg = models.CharField(max_length=128, verbose_name='学历', blank=True, null=True)
#     stu_major = models.CharField(max_length=128, verbose_name='专业', blank=True, null=True)
#     stu_company = models.CharField(max_length=128, verbose_name='工作单位', blank=True, null=True)
#     stu_duty = models.CharField(max_length=128, verbose_name='职务', blank=True, null=True)
#     stu_status = models.CharField(max_length=128, verbose_name='职称', blank=True, null=True)
#     stu_profession = models.CharField(max_length=128, verbose_name='所属行业', blank=True, null=True)
#     stu_origin = models.CharField(max_length=128, verbose_name='生源来源', blank=True, null=True)
#     stu_cellphone = models.CharField(max_length=128, verbose_name='手机号', blank=True, null=True)
#     stu_wechat = models.CharField(max_length=128, verbose_name='微信', blank=True, null=True)
#     stu_qq = models.CharField(max_length=128, verbose_name='QQ', blank=True, null=True)
#     stu_signup_date = models.DateField(verbose_name='报名日期', blank=True, null=True)
#     stu_signup_people = models.CharField(max_length=128, verbose_name='具体招生人', blank=True, null=True)
#     stu_other = models.TextField(verbose_name='备注', blank=True, null=True)
#     stu_class = models.ForeignKey(StudentClass, on_delete=models.CASCADE, verbose_name='班级')
# ###
#
# class Tuition(models.Model):
#     class Meta:
#         verbose_name = '交费信息'
#         verbose_name_plural = verbose_name
#
#     relate_student = models.OneToOneField(StudentBasic, on_delete=models.CASCADE, verbose_name='学号', primary_key=True)
#     fee_train = models.CharField(max_length=128, verbose_name='培训费', blank=True, null=True)
#     fee_material = models.CharField(max_length=128, verbose_name='资料费', blank=True, null=True)
#     fee_exam = models.CharField(max_length=128, verbose_name='考试费', blank=True, null=True)
#     fee_total = models.CharField(max_length=128, verbose_name='总费用', blank=True, null=True)
#     fee_exam_extra = models.CharField(max_length=128, verbose_name='补考费', blank=True, null=True)
#     fee_date = models.DateField(verbose_name='缴费日期', blank=True, null=True)
#     fee_method = models.CharField(max_length=128, verbose_name='缴费方式', blank=True, null=True)
#     fee_id = models.CharField(max_length=128, verbose_name='收据号', blank=True, null=True)
#
#     # TODO CODEREVICEW:模型的三种继承方式和自定义方法
#     def get_stu_name(self):
#         return self.relate_student.stu_name
#
#     get_stu_name.short_description = u'姓名'
#     get_stu_name.allow_tags = get_stu_name.is_column = True
#
#     def get_stu_class(self):
#         return self.relate_student.stu_class.class_name
#
#     get_stu_class.short_description = u'班级'
#     get_stu_class.allow_tags = get_stu_name.is_column = True
#
#     def get_stu_num(self):
#         return self.relate_student.stu_number
#
#     get_stu_num.short_description = '学号'
#     get_stu_num.allow_tags = get_stu_num.is_colume = True
#
#     def __str__(self):
#         return self.get_stu_name()
#
#
# class StudentTextbook(models.Model):
#     class Meta:
#         verbose_name = '教材'
#         verbose_name_plural = verbose_name
#
#     relate_student = models.OneToOneField(StudentBasic, on_delete=models.CASCADE, verbose_name='学号', primary_key=True)
#     # relate_student = models.ForeignKey(StudentBasic, on_delete=models.DO_NOTHING, verbose_name='学号')
#     text_basic = models.CharField(max_length=128, verbose_name='基础技能', blank=True, null=True)
#     text_sec = models.CharField(max_length=128, verbose_name='二级技能', blank=True, null=True)
#     text_sec_exer = models.CharField(max_length=128, verbose_name='二级习题', blank=True, null=True)
#     text_sec_measure = models.CharField(max_length=128, verbose_name='二级量表', blank=True, null=True)
#     text_thr = models.CharField(max_length=128, verbose_name='三级技能', blank=True, null=True)
#     text_thr_exer = models.CharField(max_length=128, verbose_name='三级习题', blank=True, null=True)
#     text_manual = models.CharField(max_length=128, verbose_name='学员手册', blank=True, null=True)
#     text_exam = models.CharField(max_length=128, verbose_name='模拟试卷', blank=True, null=True)
#     text_other = models.TextField(verbose_name='备注',blank=True,null=True)
#
#     def __str__(self):
#         return self.get_stu_name()
#
#     def get_stu_name(self):
#         return self.relate_student.stu_name
#
#     get_stu_name.short_description = u'姓名'
#     get_stu_name.allow_tags = get_stu_name.is_column = True
#
#     def get_stu_num(self):
#         return self.relate_student.stu_number
#
#     get_stu_num.short_description = '学号'
#     get_stu_num.allow_tags = get_stu_num.is_colume = True
#
#     def get_stu_class(self):
#         return self.relate_student.stu_class.class_name
#
#     get_stu_class.short_description = u'班级'
#     get_stu_class.allow_tags = get_stu_name.is_column = True
#
#
# class StudentWechat(models.Model):
#     class Meta:
#         verbose_name = '365开通情况'
#         verbose_name_plural = verbose_name
#
#     relate_student = models.OneToOneField(StudentBasic, on_delete=models.CASCADE, verbose_name='学号', primary_key=True)
#     # relate_student = models.ForeignKey(StudentBasic, on_delete=models.DO_NOTHING, verbose_name='学号')
#     wechat_number = models.CharField(max_length=128, verbose_name='平台绑定号码', blank=True, null=True)
#     wechat_nickname = models.CharField(max_length=128, verbose_name='微信昵称', blank=True, null=True)
#     wechat_date = models.DateField(verbose_name='开通日期', blank=True, null=True)
#     wechat_onduty = models.CharField(max_length=128, verbose_name='出勤', blank=True, null=True)
#     wechat_homework = models.CharField(max_length=128, verbose_name='作业打卡', blank=True, null=True)
#     wechat_other = models.TextField(verbose_name="备注", null=True, blank=True)
#
#     def get_stu_name(self):
#         return self.relate_student.stu_name
#
#     get_stu_name.short_description = u'姓名'
#     get_stu_name.allow_tags = get_stu_name.is_column = True
#
#     def get_stu_num(self):
#         return self.relate_student.stu_number
#
#     get_stu_num.short_description = '学号'
#     get_stu_num.allow_tags = get_stu_num.is_colume = True
#
#     def get_stu_class(self):
#         return self.relate_student.stu_class.class_name
#
#     get_stu_class.short_description = u'班级'
#     get_stu_class.allow_tags = get_stu_name.is_column = True
#
#     def __str__(self):
#         return self.get_stu_name()
#
#
# class StudentExam(models.Model):
#     class Meta:
#         verbose_name = '报考情况'
#         verbose_name_plural = verbose_name
#
#     relate_student = models.OneToOneField(StudentBasic, on_delete=models.CASCADE, verbose_name='学号', primary_key=True)
#     # relate_student = models.ForeignKey(StudentBasic, on_delete=models.DO_NOTHING, verbose_name='学号')
#     exam_date = models.DateField(verbose_name='报考日期', null=True, blank=True)
#     exam_theory = models.CharField(max_length=128, verbose_name='理论报考', blank=True, null=True)
#     exam_theory_result = models.CharField(max_length=128, verbose_name='理论成绩', blank=True, null=True)
#     exam_practise = models.CharField(max_length=128, verbose_name='实操报考', blank=True, null=True)
#     exam_practise_result = models.CharField(max_length=128, verbose_name='实操成绩', blank=True, null=True)
#     exam_total = models.CharField(max_length=128, verbose_name='综合报考', blank=True, null=True)
#     exam_total_result = models.CharField(max_length=128, verbose_name='综合成绩', blank=True, null=True)
#     exam_status = models.CharField(max_length=128, verbose_name='合格情况', blank=True, null=True)
#
#     def get_stu_name(self):
#         return self.relate_student.stu_name
#
#     get_stu_name.short_description = u'姓名'
#     get_stu_name.allow_tags = get_stu_name.is_column = True
#
#     def get_stu_num(self):
#         return self.relate_student.stu_number
#
#     get_stu_num.short_description = '学号'
#     get_stu_num.allow_tags = get_stu_num.is_colume = True
#
#     def get_stu_class(self):
#         return self.relate_student.stu_class.class_name
#
#     get_stu_class.short_description = u'班级'
#     get_stu_class.allow_tags = get_stu_name.is_column = True
#
#     def __str__(self):
#         return self.get_stu_name()
#
#
# class StudentExamExtra(models.Model):
#     class Meta:
#         verbose_name = '补考情况'
#         verbose_name_plural = verbose_name
#
#     relate_student = models.OneToOneField(StudentBasic, on_delete=models.CASCADE, verbose_name='学号', primary_key=True)
#     # relate_student = models.ForeignKey(StudentBasic, on_delete=models.DO_NOTHING, verbose_name='学号')
#     exam_date = models.DateField(verbose_name='报考日期', null=True, blank=True)
#     exam_theory = models.CharField(max_length=128, verbose_name='理论报考', blank=True, null=True)
#     exam_theory_result = models.CharField(max_length=128, verbose_name='理论成绩', blank=True, null=True)
#     exam_practise = models.CharField(max_length=128, verbose_name='实操报考', blank=True, null=True)
#     exam_practise_result = models.CharField(max_length=128, verbose_name='实操成绩', blank=True, null=True)
#     exam_total = models.CharField(max_length=128, verbose_name='综合报考', blank=True, null=True)
#     exam_total_result = models.CharField(max_length=128, verbose_name='综合成绩', blank=True, null=True)
#     exam_status = models.CharField(max_length=128, verbose_name='合格情况', blank=True, null=True)
#
#     def get_stu_name(self):
#         return self.relate_student.stu_name
#
#     get_stu_name.short_description = u'姓名'
#     get_stu_name.allow_tags = get_stu_name.is_column = True
#
#     def get_stu_num(self):
#         return self.relate_student.stu_number
#
#     get_stu_num.short_description = '学号'
#     get_stu_num.allow_tags = get_stu_num.is_colume = True
#
#     def get_stu_class(self):
#         return self.relate_student.stu_class.class_name
#
#     get_stu_class.short_description = u'班级'
#     get_stu_class.allow_tags = get_stu_name.is_column = True
#
#     def __str__(self):
#         return self.get_stu_name()
#
#
# class StudentCertification(models.Model):
#     class Meta:
#         verbose_name = '证书'
#         verbose_name_plural = verbose_name
#
#     relate_student = models.OneToOneField(StudentBasic, on_delete=models.CASCADE, verbose_name='学号', primary_key=True)
#     # relate_student = models.ForeignKey(StudentBasic, on_delete=models.DO_NOTHING, verbose_name='学号')
#     cert_id = models.CharField(max_length=128, verbose_name='证书编号', blank=True, null=True)
#     cert_date = models.DateField(verbose_name='发证日期', blank=True, null=True)
#     cert_draw_people = models.CharField(max_length=128, verbose_name='领取人', blank=True, null=True)
#     cert_draw_date = models.DateField(verbose_name="领取时间", blank=True, null=True)
#
#     def get_stu_name(self):
#         return self.relate_student.stu_name
#
#     get_stu_name.short_description = u'姓名'
#     get_stu_name.allow_tags = get_stu_name.is_column = True
#
#     def get_stu_num(self):
#         return self.relate_student.stu_number
#
#     get_stu_num.short_description = '学号'
#     get_stu_num.allow_tags = get_stu_num.is_colume = True
#
#     def get_stu_class(self):
#         return self.relate_student.stu_class.class_name
#
#     get_stu_class.short_description = u'班级'
#     get_stu_class.allow_tags = get_stu_name.is_column = True
#
#     def __str__(self):
#         return self.get_stu_name()
