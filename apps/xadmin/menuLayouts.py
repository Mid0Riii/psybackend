from hr.models import CurrentStaff, DismissStaff, AllStaff
from student.models import StudentClass,StudentCertification, StudentBasic, StudentExamExtra, StudentExam, StudentWechat, \
    StudentTextbook, Tuition,Onduty
from teacher.models import Teacher,FamilyTeacher,MarriageTeacher,TeamTeacher,SandboxTeacher
from filer.models import FakeModel
from filer.models import Folder
from family.models import FamilyClass,FamilyOnduty,FamilyTuition,FamilyBasic,FamilyCertification,FamilyTextbook,FamilyWechat,ResultExtra,Result
from sandbox.models import SandboxClass,SandboxOnduty,SandboxTuition,SandboxBasic,SandboxCertification,SandboxTextbook,SandboxWechat,SandboxExam
from marriage.models import MarriageClass,MarriageOnduty,MarriageTuition,MarriageBasic,MarriageCertification,MarriageTextbook,MarriageWechat,MarriageExam
from team.models import TeamClass,TeamOnduty,TeamTuition,TeamBasic,TeamCertification,TeamTextbook,TeamWechat,TeamExam
# from fileshare.models import FileShare
from family.models import Total as FamilyTotal
from student.models import Total as StudentTotal
from sandbox.models import Total as SandboxTotal
from marriage.models import Total as MarriageTotal
from team.models import Total as TeamTotal
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
                    # {
                    #     'title': '补考信息',
                    #     'perm': self.get_model_perm(StudentExamExtra, 'view'),
                    #     'url': self.get_model_url(StudentExamExtra, 'changelist'),
                    #     'icon': 'fa fa-star-half-o'
                    # },
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
                    # {
                    #     'title': '补考信息',
                    #     'perm': self.get_model_perm(ResultExtra, 'view'),
                    #     'url': self.get_model_url(ResultExtra, 'changelist'),
                    #     'icon': 'fa fa-star-half-o'
                    # },
                    {
                        'title': '证书信息',
                        'perm': self.get_model_perm(FamilyCertification, 'view'),
                        'url': self.get_model_url(FamilyCertification, 'changelist'),
                        'icon': 'fa fa-id-card'
                    }
                )
        },
        {
            'title': '沙盘分析指导信息管理',
            'icon': 'fa fa-inbox',
            'menus':
                (
                    {
                        'title': '沙盘分析指导信息总览',
                        'perm': self.get_model_perm(SandboxTotal, 'view'),
                        'url': self.get_model_url(SandboxTotal, 'changelist'),
                        'icon': 'fa fa-address-book'
                    },
                    {
                        'title': '基本信息',
                        'perm': self.get_model_perm(SandboxBasic, 'view'),
                        'url': self.get_model_url(SandboxBasic, 'changelist'),
                        'icon': 'fa fa-address-book'
                    },
                    {
                        'title': '班级信息',
                        'perm': self.get_model_perm(SandboxClass, 'view'),
                        'url': self.get_model_url(SandboxClass, 'changelist'),
                        'icon': 'fa fa-users'
                    },
                    {
                        'title': '交费信息',
                        'perm': self.get_model_perm(SandboxTuition, 'view'),
                        'url': self.get_model_url(SandboxTuition, 'changelist'),
                        'icon': 'fa fa-money'
                    },
                    {
                        'title': '教材信息',
                        'perm': self.get_model_perm(SandboxTextbook, 'view'),
                        'url': self.get_model_url(SandboxTextbook, 'changelist'),
                        'icon': 'fa fa-book'
                    },
                    {
                        'title': '365开通情况',
                        'perm': self.get_model_perm(SandboxWechat, 'view'),
                        'url': self.get_model_url(SandboxWechat, 'changelist'),
                        'icon': 'fa fa-weixin'
                    },
                    {
                        'title': '考勤信息',
                        'perm': self.get_model_perm(SandboxOnduty, 'view'),
                        'url': self.get_model_url(SandboxOnduty, 'changelist'),
                        'icon': 'fa fa-check-square-o'
                    },
                    {
                        'title': '考试信息',
                        'perm': self.get_model_perm(Result, 'view'),
                        'url': self.get_model_url(SandboxExam, 'changelist'),
                        'icon': 'fa fa-star'
                    },
                    {
                        'title': '证书信息',
                        'perm': self.get_model_perm(SandboxCertification, 'view'),
                        'url': self.get_model_url(SandboxCertification, 'changelist'),
                        'icon': 'fa fa-id-card'
                    }
                )
        },
        {
            'title': '团体心理辅导信息管理',
            'icon': 'fa fa-users',
            'menus':
                (
                    {
                        'title': '团体心理辅导信息总览',
                        'perm': self.get_model_perm(TeamTotal, 'view'),
                        'url': self.get_model_url(TeamTotal, 'changelist'),
                        'icon': 'fa fa-address-book'
                    },
                    {
                        'title': '基本信息',
                        'perm': self.get_model_perm(TeamBasic, 'view'),
                        'url': self.get_model_url(TeamBasic, 'changelist'),
                        'icon': 'fa fa-address-book'
                    },
                    {
                        'title': '班级信息',
                        'perm': self.get_model_perm(TeamClass, 'view'),
                        'url': self.get_model_url(TeamClass, 'changelist'),
                        'icon': 'fa fa-users'
                    },
                    {
                        'title': '交费信息',
                        'perm': self.get_model_perm(TeamTuition, 'view'),
                        'url': self.get_model_url(TeamTuition, 'changelist'),
                        'icon': 'fa fa-money'
                    },
                    {
                        'title': '教材信息',
                        'perm': self.get_model_perm(TeamTextbook, 'view'),
                        'url': self.get_model_url(TeamTextbook, 'changelist'),
                        'icon': 'fa fa-book'
                    },
                    {
                        'title': '365开通情况',
                        'perm': self.get_model_perm(TeamWechat, 'view'),
                        'url': self.get_model_url(TeamWechat, 'changelist'),
                        'icon': 'fa fa-weixin'
                    },
                    {
                        'title': '考勤信息',
                        'perm': self.get_model_perm(TeamOnduty, 'view'),
                        'url': self.get_model_url(TeamOnduty, 'changelist'),
                        'icon': 'fa fa-check-square-o'
                    },
                    {
                        'title': '考试信息',
                        'perm': self.get_model_perm(TeamExam, 'view'),
                        'url': self.get_model_url(TeamExam, 'changelist'),
                        'icon': 'fa fa-star'
                    },
                    {
                        'title': '证书信息',
                        'perm': self.get_model_perm(TeamCertification, 'view'),
                        'url': self.get_model_url(TeamCertification, 'changelist'),
                        'icon': 'fa fa-id-card'
                    }
                )
        },
        {
            'title': '婚姻指导信息管理',
            'icon': 'fa fa-heart-o',
            'menus':
                (
                    {
                        'title': '婚姻指导信息总览',
                        'perm': self.get_model_perm(MarriageTotal, 'view'),
                        'url': self.get_model_url(MarriageTotal, 'changelist'),
                        'icon': 'fa fa-address-book'
                    },
                    {
                        'title': '基本信息',
                        'perm': self.get_model_perm(MarriageBasic, 'view'),
                        'url': self.get_model_url(MarriageBasic, 'changelist'),
                        'icon': 'fa fa-address-book'
                    },
                    {
                        'title': '班级信息',
                        'perm': self.get_model_perm(MarriageClass, 'view'),
                        'url': self.get_model_url(MarriageClass, 'changelist'),
                        'icon': 'fa fa-users'
                    },
                    {
                        'title': '交费信息',
                        'perm': self.get_model_perm(MarriageTuition, 'view'),
                        'url': self.get_model_url(MarriageTuition, 'changelist'),
                        'icon': 'fa fa-money'
                    },
                    {
                        'title': '教材信息',
                        'perm': self.get_model_perm(MarriageTextbook, 'view'),
                        'url': self.get_model_url(MarriageTextbook, 'changelist'),
                        'icon': 'fa fa-book'
                    },
                    {
                        'title': '365开通情况',
                        'perm': self.get_model_perm(MarriageWechat, 'view'),
                        'url': self.get_model_url(MarriageWechat, 'changelist'),
                        'icon': 'fa fa-weixin'
                    },
                    {
                        'title': '考勤信息',
                        'perm': self.get_model_perm(MarriageOnduty, 'view'),
                        'url': self.get_model_url(MarriageOnduty, 'changelist'),
                        'icon': 'fa fa-check-square-o'
                    },
                    {
                        'title': '考试信息',
                        'perm': self.get_model_perm(MarriageExam, 'view'),
                        'url': self.get_model_url(MarriageExam, 'changelist'),
                        'icon': 'fa fa-star'
                    },
                    {
                        'title': '证书信息',
                        'perm': self.get_model_perm(MarriageCertification, 'view'),
                        'url': self.get_model_url(MarriageCertification, 'changelist'),
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
                    },
                    {
                        'title': '沙盒教师授课信息管理',
                        'perm': self.get_model_perm(SandboxTeacher, 'view'),
                        'url': self.get_model_url(SandboxTeacher, 'changelist'),
                        'icon': 'fa fa-inbox'
                    },
                    {
                        'title': '婚姻教师授课信息管理',
                        'perm': self.get_model_perm(MarriageTeacher, 'view'),
                        'url': self.get_model_url(MarriageTeacher, 'changelist'),
                        'icon': 'fa fa-heart-o'
                    },
                    {
                        'title': '团体教师授课信息管理',
                        'perm': self.get_model_perm(TeamTeacher, 'view'),
                        'url': self.get_model_url(TeamTeacher, 'changelist'),
                        'icon': 'fa fa-group'
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
    folderMenusList = []
    for querySet in folderSet:
        folderMenusList.append(
            {
                'title': str(querySet.name),
                # 'perm':self.get_model_perm(FakeModel,'view'),
                'url':'/test_view/'+str(querySet.id)+'/',
                'icon':'fa fa-file'
            }
        )
    folderMenusList.append({
            'title': '文件管理',
            'perm': self.get_model_perm(FakeModel, 'view'),
            'url': self.get_model_url(FakeModel, 'changelist'),
            'icon': 'fa fa-file'
        },)
    defaultLayoutList.append(
        {
            'title': '文件系统',
            'icon': 'fa fa-file',
            'menus':tuple(folderMenusList)
        }
    )
    return tuple(defaultLayoutList)
