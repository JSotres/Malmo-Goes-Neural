from django.contrib import admin
from .models import FaceMood, FaceProject
from tinymce.widgets import TinyMCE
from django.db import models


class FaceProjectAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }


admin.site.register(FaceMood)
admin.site.register(FaceProject, FaceProjectAdmin)
