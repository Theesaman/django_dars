from django.contrib import admin
from .models import Contact,Category,Blog,Portfolio,Team
from django.utils.html import format_html

admin.site.register((Contact,Category,Portfolio)) 

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','author','img')
    readonly_fields = ['slug']
    def img(self, obj):
        return format_html('<img width="100" height="100" src="{}" />'.format(obj.image.url))


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('img', 'full_name', 'job' )
    readonly_fields = ['description']
    def img(sefl, obj):
        return format_html('<img width="100" height="100" src="{}" />'.format(obj.image.url))