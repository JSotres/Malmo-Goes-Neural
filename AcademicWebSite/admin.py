from django.contrib import admin
from .models import AcademicGroupInformation, ResearchField, ContactRequest, Publications, Member


admin.site.register(AcademicGroupInformation)
admin.site.register(ResearchField)
admin.site.register(ContactRequest)
admin.site.register(Publications)
admin.site.register(Member)
