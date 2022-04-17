from django.contrib import admin
from .models import Contacttuber


# Register your models here.

class ContacttuberAdmin(admin.ModelAdmin):

    list_display = ('full_name' , 'email',)
    list_display_links = ('full_name',)
    search_fields = ('full_name',)
    list_filter = ('email',)
admin.site.register(Contacttuber,ContacttuberAdmin)
