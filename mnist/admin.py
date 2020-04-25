from django.contrib import admin
from .models import mnistProject
from tinymce.widgets import TinyMCE
from django.db import models

class mnistProjectAdmin(admin.ModelAdmin):

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }


admin.site.register(mnistProject, mnistProjectAdmin)
