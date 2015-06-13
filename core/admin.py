from core.models import Pages
from django.contrib import admin


class RCoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'page', 'title',)
    list_filter = ('page', 'title',)
    ordering = ('-id', 'title', 'page')
    save_on_top = True

admin.site.register(Pages, RCoreAdmin)
