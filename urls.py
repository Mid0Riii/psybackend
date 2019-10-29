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
from student.models import StudentBasic,Total as StudentTotal
from family.models import FamilyBasic,Total as FamilyTotal
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

urlpatterns = [
    path('file/', admin.site.urls),
    path('',xadmin.site.urls),
    path('generate/',generate_total)
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
