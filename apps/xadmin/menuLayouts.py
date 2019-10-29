from hr.models import CurrentStaff, DismissStaff, AllStaff
from student.models import StudentClass,StudentCertification, StudentBasic, StudentExamExtra, StudentExam, StudentWechat, \
    StudentTextbook, Tuition,Onduty
from teacher.models import Teacher,FamilyTeacher
from filer.models import FakeModel
from filer.models import Folder
from family.models import FamilyClass,FamilyOnduty,FamilyTuition,FamilyBasic,FamilyCertification,FamilyTextbook,FamilyWechat,ResultExtra,Result
# from fileshare.models import FileShare
from family.models import Total as FamilyTotal
from student.models import Total as StudentTotal
def set_menu(self):
    defaultLayoutList = [
        {
            'title': '心理学员信息管理',
            'icon':'fa fa-address-book',
            'menus':
                (
                    {
                        'title': '学员信息总览',
                        'perm': self.get_model_perm(StudentTotal, 'view'),
                        'url': self.get_model_url(StudentTotal, 'changelist'),
                        'icon': 'fa fa-address-book'
                    },
                    {
                        'title': '基本信息',
                        'perm': self.get_model_perm(StudentBasic, 'view'),
                        'url': self.get_model_url(StudentBasic, 'changelist'),
                        'icon': 'fa fa-address-book'
                    },
                    {
                        'title':'班级信息',
                        'perm':self.get_model_perm(StudentClass,'view'),
                        'url':self.get_model_url(StudentClass,'changelist'),
                        'icon':'fa fa-users'
                    },
                    {
                        'title': '交费信息',
                        'perm': self.get_model_perm(Tuition, 'view'),
                        'url': self.get_model_url(Tuition, 'changelist'),
                        'icon': 'fa fa-money'
                    },
                    {
                        'title': '教材信息',
                        'perm': self.get_model_perm(StudentTextbook, 'view'),
                        'url': self.get_model_url(StudentTextbook, 'changelist'),
                        'icon': 'fa fa-book'
                    },
                    {
                        'title': '365开通情况',
                        'perm': self.get_model_perm(StudentWechat, 'view'),
                        'url': self.get_model_url(StudentWechat, 'changelist'),
                        'icon': 'fa fa-weixin'
                    },
                    {
                        'title':'考勤信息',
                        'perm':self.get_model_perm(Onduty,'view'),
                        'url':self.get_model_url(Onduty,'changelist'),
                        'icon':'fa fa-check-square-o'
                    },
                    {
                        'title': '考试信息',
                        'perm': self.get_model_perm(StudentExam, 'view'),
                        'url': self.get_model_url(StudentExam, 'changelist'),
                        'icon': 'fa fa-star'
                    },
                    {
                        'title': '补考信息',
                        'perm': self.get_model_perm(StudentExamExtra, 'view'),
                        'url': self.get_model_url(StudentExamExtra, 'changelist'),
                        'icon': 'fa fa-star-half-o'
                    },
                    {
                        'title': '证书信息',
                        'perm': self.get_model_perm(StudentCertification, 'view'),
                        'url': self.get_model_url(StudentCertification, 'changelist'),
                        'icon': 'fa fa-id-card'
                    }
                )
        },
        {
            'title': '家庭信息管理',
            'icon': 'fa fa-home',
            'menus':
                (
                    {
                        'title': '家庭信息总览',
                        'perm': self.get_model_perm(FamilyTotal, 'view'),
                        'url': self.get_model_url(FamilyTotal, 'changelist'),
                        'icon': 'fa fa-address-book'
                    },
                    {
                        'title': '基本信息',
                        'perm': self.get_model_perm(FamilyBasic, 'view'),
                        'url': self.get_model_url(FamilyBasic, 'changelist'),
                        'icon': 'fa fa-address-book'
                    },
                    {
                        'title': '班级信息',
                        'perm': self.get_model_perm(FamilyClass, 'view'),
                        'url': self.get_model_url(FamilyClass, 'changelist'),
                        'icon': 'fa fa-users'
                    },
                    {
                        'title': '交费信息',
                        'perm': self.get_model_perm(FamilyTuition, 'view'),
                        'url': self.get_model_url(FamilyTuition, 'changelist'),
                        'icon': 'fa fa-money'
                    },
                    {
                        'title': '教材信息',
                        'perm': self.get_model_perm(FamilyTextbook, 'view'),
                        'url': self.get_model_url(FamilyTextbook, 'changelist'),
                        'icon': 'fa fa-book'
                    },
                    {
                        'title': '365开通情况',
                        'perm': self.get_model_perm(FamilyWechat, 'view'),
                        'url': self.get_model_url(FamilyWechat, 'changelist'),
                        'icon': 'fa fa-weixin'
                    },
                    {
                        'title': '考勤信息',
                        'perm': self.get_model_perm(FamilyOnduty, 'view'),
                        'url': self.get_model_url(FamilyOnduty, 'changelist'),
                        'icon': 'fa fa-check-square-o'
                    },
                    {
                        'title': '考试信息',
                        'perm': self.get_model_perm(Result, 'view'),
                        'url': self.get_model_url(Result, 'changelist'),
                        'icon': 'fa fa-star'
                    },
                    {
                        'title': '补考信息',
                        'perm': self.get_model_perm(ResultExtra, 'view'),
                        'url': self.get_model_url(ResultExtra, 'changelist'),
                        'icon': 'fa fa-star-half-o'
                    },
                    {
                        'title': '证书信息',
                        'perm': self.get_model_perm(FamilyCertification, 'view'),
                        'url': self.get_model_url(FamilyCertification, 'changelist'),
                        'icon': 'fa fa-id-card'
                    }
                )
        },
        {
            'title': '教师授课信息管理',
            'icon': 'fa fa-calendar',
            'menus':
                (
                    {
                        'title': '心理教师授课信息管理',
                        'perm': self.get_model_perm(Teacher, 'view'),
                        'url': self.get_model_url(Teacher, 'changelist'),
                        'icon': 'fa fa-calendar'
                    },
                    {
                        'title': '家庭教师授课信息管理',
                        'perm': self.get_model_perm(FamilyTeacher, 'view'),
                        'url': self.get_model_url(FamilyTeacher, 'changelist'),
                        'icon': 'fa fa-home'
                    }
                )
        },
        {
            'title': '员工信息管理',
            # 权限配置参数，有此权限者才显示本菜单
            'icon':'fa fa-user-circle-o',
            'perm': self.get_model_perm(CurrentStaff, 'view'),
            'menus':
                (
                    {
                        'title': '在职员工',
                        'perm': self.get_model_perm(CurrentStaff, 'view'),
                        'url': self.get_model_url(CurrentStaff, 'changelist'),
                        'icon': 'fa fa-check'
                    },
                    {
                        'title': '离职员工',
                        'perm': self.get_model_perm(DismissStaff, 'view'),
                        'url': self.get_model_url(DismissStaff, 'changelist'),
                        'icon': 'fa fa-times'
                    },
                    {
                        'title': '全部员工',
                        'perm': self.get_model_perm(AllStaff, 'view'),
                        'url': self.get_model_url(AllStaff, 'changelist'),
                        'icon': 'fa fa-user'
                    }
                )
        },
        # {
        #     'title':'文件系统',
        #     'icon': 'fa fa-file',
        #     'menus':
        #         (
        #             {
        #                 'title':'文件管理',
        #                 'perm':self.get_model_perm(FakeModel,'view'),
        #                 'url':self.get_model_url(FakeModel,'changelist'),
        #                 'icon':'fa fa-file'
        #             },
        #         )
        # },
    ]
    folderSet = Folder.objects.filter(level=0).order_by('rank')
    folderMenusList = [
        {
            'title': '文件管理',
            'perm': self.get_model_perm(FakeModel, 'view'),
            'url': self.get_model_url(FakeModel, 'changelist'),
            'icon': 'fa fa-file'
        },
    ]
    for querySet in folderSet:
        folderMenusList.append(
            {
                'title': str(querySet.name),
                # 'perm':self.get_model_perm(FakeModel,'view'),
                'url':'/test_view/'+str(querySet.id)+'/',
                'icon':'fa fa-file'
            }
        )
    defaultLayoutList.append(
        {
            'title': '文件系统',
            'icon': 'fa fa-file',
            'menus':tuple(folderMenusList)
        }
    )
    return tuple(defaultLayoutList)
