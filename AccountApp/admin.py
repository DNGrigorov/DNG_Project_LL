from django.contrib import admin
from .models import WebUser, LanguageSkill, Rating

admin.site.register(WebUser)
admin.site.register(LanguageSkill)
admin.site.register(Rating)
