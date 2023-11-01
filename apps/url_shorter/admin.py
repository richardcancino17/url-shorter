from django.contrib import admin
from django.contrib.auth.models import Group

from apps.url_shorter.models import UrlShorter

admin.site.unregister(Group)

admin.site.site_header = 'Url Shorter'
admin.site.site_title = 'Url Shorter'
admin.site.index_title = 'Url Shorter'


class UrlShorterAdmin(admin.ModelAdmin):
    list_display = ['id', 'link_original', 'code_shorter', 'times_used',
                    'is_active', 'created_at', 'update_at']
    search_fields = ['link_original', 'code_shorter']


admin.site.register(UrlShorter, UrlShorterAdmin)
