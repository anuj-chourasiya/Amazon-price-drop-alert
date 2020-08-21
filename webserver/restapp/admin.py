from django.contrib import admin

from restapp.models import Info

class InfoAdmin(admin.ModelAdmin):
    list_display=['url','email']

admin.site.register(Info,InfoAdmin)
