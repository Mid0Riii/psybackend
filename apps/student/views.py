from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
def createSuperuser(request):
    User.objects.create(username='admin',password='',is_superuser=True,is_staff=True)
    q = User.objects.get(username='admin')
    q.set_password("admin1234")
    q.save()