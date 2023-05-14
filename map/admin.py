from django.contrib import admin
from .models import Unimaze_Post, Univ_Contacts,Unimaze_map


class UnimazePostAdmin(admin.ModelAdmin):
    list_display = ['title', 'text',]
admin.site.register(Unimaze_Post, UnimazePostAdmin)

class UnivContactsAdmin(admin.ModelAdmin):
    list_display = ['department', 'name', 'task',]
admin.site.register(Univ_Contacts, UnivContactsAdmin)



#3D map admin
class Map_Admin(admin.ModelAdmin):
    list_display = ['id','building_name', 'floor',]
admin.site.register(Unimaze_map, Map_Admin)

