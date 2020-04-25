from django.contrib import admin
from .models import SimpsonCharacter, SimpsonsProject
from tinymce.widgets import TinyMCE
from django.db import models

class SimpsonsProjectAdmin(admin.ModelAdmin):

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }


admin.site.register(SimpsonCharacter)
admin.site.register(SimpsonsProject, SimpsonsProjectAdmin)