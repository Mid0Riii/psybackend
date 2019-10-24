from django.db import models

class FakeModel(models.Model):
    class Meta:
        verbose_name = '文件管理'
        verbose_name_plural = verbose_name