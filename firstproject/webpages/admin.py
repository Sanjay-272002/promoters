from django.contrib import admin
from .models import Slider,Team
from django.utils.html import format_html
# Register your models here.
class TeamAdmin(admin.ModelAdmin):

    def myphoto(self, object):
        return format_html('<img src="{}" width="40" />'.format(object.photo.url))

    list_display = ('id','myphoto','first_name' , 'role' , 'created_date')
    list_display_links = ('first_name' , 'id')
    search_fields = ('first_name' , 'id')
    list_filter = ('role',)

class sliderAdmin(admin.ModelAdmin):

    def myphoto(self, object):
        return format_html('<img src="{}" width="40" />'.format(object.photo.url))

    list_display = ('headline','button_text','photo',)
    list_display_links = ('headline',)
    search_fields = ('headline',)
    list_filter = ('headline',)



admin.site.register(Slider,sliderAdmin)
admin.site.register(Team, TeamAdmin)