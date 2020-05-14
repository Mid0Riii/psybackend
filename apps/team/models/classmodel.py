from django.db import models
class TeamClass(models.Model):
    class Meta:
        verbose_name = '团体心理辅导班级'
        verbose_name_plural = '团体心理辅导班级'

    class_name = models.CharField(max_length=64, verbose_name='班级名')
    class_index = models.IntegerField(verbose_name='班级序号', null=True, blank=True)
    class_id_example = models.CharField(max_length=128, verbose_name='学号命名',null=True,blank=True)
    class_recruit_teacher = models.CharField(max_length=64, verbose_name='招生老师', null=True, blank=True,default='空')
    class_teacher = models.CharField(max_length=64, verbose_name='跟班老师', null=True, blank=True,default='空')
    class_date = models.CharField(max_length=64, verbose_name='开班年份', null=True, blank=True,default='空')




    def __str__(self):
        return str(self.class_name)
