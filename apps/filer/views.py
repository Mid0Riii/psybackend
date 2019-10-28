# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
import xadmin
from xadmin.views import CommAdminView
from .models import File
from django.shortcuts import render

def canonical(request, uploaded_at, file_id):
    """
    Redirect to the current url of a public file
    """
    filer_file = get_object_or_404(File, pk=file_id, is_public=True)
    if (not filer_file.file or int(uploaded_at) != filer_file.canonical_time):
        raise Http404('No %s matches the given query.' % File._meta.object_name)
    return redirect(filer_file.url)


class FakeView(CommAdminView):
    def get(self,request,relate_id):
        context = super().get_context()
        title = "文件管理"
        context["breadcrumbs"].append({'url': '/cwyadmin/', 'title': title})
        context["title"] = title
        context["relate_id"] = relate_id
        return render(request, 'file/test.html', context)


