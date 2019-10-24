from django.db import models
from .tools import modelTools


class Staff(models.Model):
    # Staff类为在/离职以及全部员工的母类

    def __str__(self):
        return self.personal_name

    objects = models.Manager()

    class Meta:
        verbose_name = '员工母类'
        verbose_name_plural = verbose_name


    at_post = models.CharField(verbose_name='职工状态', choices=modelTools.set_choices(['在职', '离职']), max_length=10)
    personal_name = models.CharField(verbose_name='姓名', max_length=50)
    personal_gender = models.CharField(verbose_name='性别', choices=modelTools.set_choices(['女', '男']), max_length=1)
    personal_id_num = models.CharField(verbose_name='身份证号', max_length=20)
    personal_birth_date = models.DateField(verbose_name='出生日期')
    personal_is_marry = models.CharField(verbose_name='婚姻情况',
                                         choices=modelTools.set_choices(['未婚', '已婚', '丧偶', '离婚']), max_length=4, )
    personal_status = models.CharField(verbose_name='政治面貌',
                              choices=modelTools.set_choices(['中共党员', '中共预备党员', '共青团员',
                                                              '民革党员', '民盟党员', '民建会员',
                                                              '民进会员', '农工党党员', '致公党党员',
                                                              '九三学社社员', '台盟盟员', '无党派人士']),max_length=10, )
    personal_folk = models.CharField(verbose_name='民族', max_length=5, )
    personal_reg_location = models.CharField(verbose_name='户籍', max_length=20, )
    personal_soc_ins = models.CharField(verbose_name='是否缴纳社保', choices=modelTools.set_choices(['是', '否']), max_length=2, )
    personal_soc_ins_id = models.CharField(verbose_name='社保卡号', max_length=30, )
    personal_phone = models.CharField(verbose_name='电话', max_length=12, )
    personal_phone_other = models.CharField(verbose_name='其他联系方式', max_length=50, blank=True, null=True)
    personal_emer_people = models.CharField(verbose_name='紧急联系人', max_length=30, blank=True, null=True)
    personal_emer_phone = models.CharField(verbose_name='紧急电话', max_length=20, blank=True, null=True)

    personal_current_location = models.CharField(verbose_name='当前住址', max_length=100, blank=True, null=True)
    personal_on_market = models.CharField(verbose_name='人才市场挂编', choices=modelTools.set_choices(['是', '否']), max_length=3,
                                          blank=True, null=True)
    work_set_rank_date = models.DateField(verbose_name='职称评定时间', blank=True, null=True)
    work_hire_rank_aca_date = models.DateField(verbose_name='院编员工职称聘用时间', blank=True, null=True)
    work_enter_date = models.DateField(verbose_name='入职时间', blank=True, null=True)
    work_dismiss_date = models.DateField(verbose_name='离职时间', blank=True, null=True)
    work_department = models.CharField(max_length=128, verbose_name='部门',null=True, blank=True)
    #duty = models.CharField(verbose_name='行政职务', max_length=10, blank=True, null=True)
    work_duty = models.CharField(max_length=128,verbose_name='行政职务', null=True,blank=True)
    work_duty_hire_date = models.DateField(verbose_name='职务聘用时间', blank=True, null=True)
    work_hire_method = models.CharField(verbose_name='聘用方式', choices=modelTools.set_choices(['校编', '校合同制', '院编', '院聘'])
                                   , max_length=10, blank=True, null=True)
    work_position = models.CharField(verbose_name='岗位', max_length=20, blank=True, null=True)
    work_title = models.CharField(verbose_name='职称', max_length=10, blank=True, null=True)
    edu_background = models.CharField(verbose_name='学历', max_length=50, )
    edu_grade = models.CharField(verbose_name='学位', choices=modelTools.set_choices(['本科', '硕士', '博士', '专科', '其他']),
                                 max_length=5,
                                 )
    edu_learn_exp = models.TextField(verbose_name='学习经历', blank=True, null=True)

    other_more = models.TextField(verbose_name='备注', blank=True, null=True)
    # other_avatar = models.ImageField(verbose_name='员工照片', upload_to='avatar', default='avatar/default.jpg', blank=True,
    #                            null=True)

class DismissStaff(Staff):
    class Meta:
        verbose_name = '离职员工'
        verbose_name_plural = '离职员工'
        proxy = True


class AllStaff(Staff):
    class Meta:
        verbose_name = '全部员工'
        verbose_name_plural = '员工'
        proxy = True


class CurrentStaff(Staff):
    class Meta:
        verbose_name='在职员工'
        verbose_name_plural='在职员工'
        proxy=True




