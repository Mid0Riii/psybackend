from django.db import models
class FamilyClass(models.Model):
    class Meta:
        verbose_name = '家庭班级'
        verbose_name_plural = '家庭班级'

    class_recruit_teacher = models.CharField(max_length=64, verbose_name='招生老师', null=True, blank=True)
    class_teacher = models.CharField(max_length=64, verbose_name='跟班老师', null=True, blank=True)
    # class_name = models.CharField(max_length=64, verbose_name='班级名', unique=True, primary_key=True)
    class_date = models.CharField(max_length=64, verbose_name='开班年份', null=True, blank=True)
    class_name = models.CharField(max_length=64, verbose_name='班级名')


    def __str__(self):
        return str(self.class_name)
