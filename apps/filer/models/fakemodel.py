from django.db import models

class FakeModel(models.Model):
    class Meta:
        verbose_name = '文件管理'
        verbose_name_plural = verbose_name
    name = models.CharField(max_length=128,verbose_name='关联文件名',blank=True,null=True)
    relate_id = models.CharField(max_length=1024,verbose_name='关联文件夹id',blank=True,null=True)