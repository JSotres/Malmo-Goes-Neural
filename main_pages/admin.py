from django.contrib import admin
from .models import ContactRequest, Project
from tinymce.widgets import TinyMCE
from django.db import models


class ProjectAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Name", {"fields": ["name", "longName"]}),
        ("Type", {"fields": ["project_type"]}),
        ("Description", {"fields": ["short_description", "short_description2", "long_description"]}),
        ("URL", {"fields": ["url"]}),
        ("Image", {"fields": ["project_image"]})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }


admin.site.register(ContactRequest)
admin.site.register(Project, ProjectAdmin)
