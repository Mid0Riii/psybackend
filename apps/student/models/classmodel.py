from django.db import models
class StudentClass(models.Model):
    class Meta:
        verbose_name = '学员班级'
        verbose_name_plural = '学员班级'

    class_recruit_teacher = models.CharField(max_length=64, verbose_name='招生老师', null=True, blank=True)
    class_teacher = models.CharField(max_length=64, verbose_name='跟班老师', null=True, blank=True)
    # class_name = models.CharField(max_length=64, verbose_name='班级名', unique=True, primary_key=True)
    class_date = models.CharField(max_length=64, verbose_name='开班年份', null=True, blank=True)
    class_name = models.CharField(max_length=64, verbose_name='班级名')


    def __str__(self):
        return str(self.class_name)


    # TODO 加总览 学号排序别按文字顺序
    # TODO 文件管理新建政策文件放在第一位 中心文件第二 中心公示第三 开班通知第四