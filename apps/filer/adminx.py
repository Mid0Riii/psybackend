import xadmin
from .models import FakeModel
from xadmin.views import DetailAdminView, ListAdminView,ModelFormAdminView,UpdateAdminView,CreateAdminView
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, BooleanWidget
from xadmin.plugins import add_html
from .views import FakeView

from django.contrib import admin

from .models import Clipboard, File, Folder, FolderPermission, ThumbnailOption
from .settings import FILER_IMAGE_MODEL
from .utils.loader import load_model
from filer.admin.clipboardadmin import ClipboardAdmin
from filer.admin.fileadmin import FileAdmin
from filer.admin.folderadmin import FolderAdmin
from filer.admin.imageadmin import ImageAdmin
from filer.admin.permissionadmin import PermissionAdmin
from filer.admin.thumbnailoptionadmin import ThumbnailOptionAdmin


@xadmin.sites.register(FakeModel)
class FakeAdmin(object):
    # pass
    Add_file_iframe_allow=True

xadmin.site.register_view(r'^test_view/(\d+)/$', FakeView, name='for_test')
xadmin.site.register_plugin(add_html.Add_file_iframe,ListAdminView)
# xadmin.site.register(Clipboard,ClipboardAdmin)
# xadmin.site.register(File,FileAdmin)
# xadmin.site.register(Folder,FolderAdmin)
# xadmin.site.register(FolderPermission,ImageAdmin)
# xadmin.site.register(ThumbnailOption,PermissionAdmin)

