from django.contrib import admin
from .models import Map_Post


class MapPostAdmin(admin.ModelAdmin):
    list_display = ['building_name', 'building_num', 'door_num', ]



admin.site.register(Map_Post, MapPostAdmin)