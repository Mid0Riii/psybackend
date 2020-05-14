"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from student.models import StudentBasic,Tuition,StudentWechat,StudentExamExtra,StudentExam,StudentCertification,StudentTextbook,Total as StudentTotal
from family.models import FamilyBasic,FamilyWechat,FamilyTuition,FamilyOnduty,FamilyTextbook,FamilyCertification,Result,ResultExtra,Total as FamilyTotal
import xadmin
from django.shortcuts import HttpResponse
def generate_total(request):
    q = StudentBasic.objects.all()
    p = FamilyBasic.objects.all()
    for i in p:
        FamilyTotal.objects.create(family=i)
    for j in q:
        StudentTotal.objects.create(student=j)

    return HttpResponse("<h1>迁移成功</h1>")

def generate_tuition(requests):
    q = Tuition.objects.all()
    p  =FamilyTuition.objects.all()
    for i in p:
        if i.fee_date is None:
            i.fee_date = '空'
            i.save()
    for j in q:
        if j.fee_date is None:
            j.fee_date='空'
            j.save()
    return HttpResponse("<h1>迁移完成</h1>")

def generate_class(requests):
    q = StudentBasic.objects.all()
    for i in q:
        t = Tuition.objects.get(relate_student = i)
        t.relate_class = i.stu_class
        t.save()
        w = StudentWechat.objects.get(relate_student=i)
        w.relate_class=i.stu_class
        w.save()
        e = StudentExam.objects.get(relate_student=i)
        e.relate_class=i.stu_class
        e.save()
        ee = StudentExamExtra.objects.get(relate_student=i)
        ee.relate_class=i.stu_class
        ee.save()
        c = StudentCertification.objects.get(relate_student=i)
        c.relate_class=i.stu_class
        c.save()
        tb = StudentTextbook.objects.get(relate_student=i)
        tb.relate_class=i.stu_class
        tb.save()
    p = FamilyBasic.objects.all()
    for i in p:
        t = FamilyTuition.objects.get(relate_family=i)
        t.relate_class = i.fam_class
        t.save()
        w = FamilyWechat.objects.get(relate_family=i)
        w.relate_class = i.fam_class
        w.save()
        e = Result.objects.get(relate_family=i)
        e.relate_class = i.fam_class
        e.save()
        ee = ResultExtra.objects.get(relate_family=i)
        ee.relate_class = i.fam_class
        ee.save()
        c = FamilyCertification.objects.get(relate_family=i)
        c.relate_class = i.fam_class
        c.save()
        tb = FamilyTextbook.objects.get(relate_family=i)
        tb.relate_class = i.fam_class
        tb.save()
    return HttpResponse("<h1>迁移完成</h1>")

urlpatterns = [
    path('file/', admin.site.urls),
    path('',xadmin.site.urls),
    path('generate/',generate_total),
    path('generate_class',generate_class),
    path('generate_tuition', generate_tuition)
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
