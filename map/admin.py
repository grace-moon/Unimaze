from django.contrib import admin
from .models import Unimaze_Post, Direcrions_Post, Univ_Contacts, HRC, MAC_M, TTD, EP, CH, AS, SH, EN, HS, BS, JL, EE, OM, AD, HC, TSD, MM, TTA, TFD, FS, IAC


class UnimazePostAdmin(admin.ModelAdmin):
    list_display = ['title', 'text',]
admin.site.register(Unimaze_Post, UnimazePostAdmin)


class DirectionsPostAdmin(admin.ModelAdmin):
    list_display = ['building_name', 'building_num', 'floor',]
admin.site.register(Direcrions_Post, DirectionsPostAdmin)


class UnivContactsAdmin(admin.ModelAdmin):
    list_display = ['department', 'name', 'task',]
admin.site.register(Univ_Contacts, UnivContactsAdmin)

#3D map admin
class TTA_Admin(admin.ModelAdmin):
    list_display = ['building_name', 'floor',]
admin.site.register(TTA, TTA_Admin)

class FS_Admin(admin.ModelAdmin):
    list_display = ['building_name', 'floor',]
admin.site.register(FS, FS_Admin)

class HC_Admin(admin.ModelAdmin):
    list_display = ['building_name', 'floor',]
admin.site.register(HC, HC_Admin)

class HS_Admin(admin.ModelAdmin):
    list_display = ['building_name', 'floor',]
admin.site.register(HS, HS_Admin)

class IAC_Admin(admin.ModelAdmin):
    list_display = ['building_name', 'floor',]
admin.site.register(IAC, IAC_Admin)

class TFD_Admin(admin.ModelAdmin):
    list_display = ['building_name', 'floor',]
admin.site.register(TFD, TFD_Admin)

class MM_Admin(admin.ModelAdmin):
    list_display = ['building_name', 'floor',]
admin.site.register(MM, MM_Admin)

class TSD_Admin(admin.ModelAdmin):
    list_display = ['building_name', 'floor',]
admin.site.register(TSD, TSD_Admin)

class AD_Admin(admin.ModelAdmin):
    list_display = ['building_name', 'floor',]
admin.site.register(AD, AD_Admin)

class OM_Admin(admin.ModelAdmin):
    list_display = ['building_name', 'floor',]
admin.site.register(OM, OM_Admin)

class EE_Admin(admin.ModelAdmin):
    list_display = ['building_name', 'floor',]
admin.site.register(EE, EE_Admin)

class JL_Admin(admin.ModelAdmin):
    list_display = ['building_name', 'floor',]
admin.site.register(JL, JL_Admin)

class BS_Admin(admin.ModelAdmin):
    list_display = ['building_name', 'floor',]
admin.site.register(BS, BS_Admin)

class EN_Admin(admin.ModelAdmin):
    list_display = ['building_name', 'floor',]
admin.site.register(EN, EN_Admin)

class SH_Admin(admin.ModelAdmin):
    list_display = ['building_name', 'floor',]
admin.site.register(SH, SH_Admin)

class AS_Admin(admin.ModelAdmin):
    list_display = ['building_name', 'floor',]
admin.site.register(AS, AS_Admin)



