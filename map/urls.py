from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ready', views.ready, name='ready'),
    path('HRC_map_detail/<int:pk>/', views.HRC_map, name='HRC_map_detail'),
    path('C_L_map_detail/<int:pk>/', views.C_L_map, name='C_L_map_detail'),
    path('C_M_map_detail/<int:pk>/', views.C_M_map, name='C_M_map_detail'),
    path('TTD_map_detail/<int:pk>/', views.TTD_map, name='TTD_map_detail'),
    path('EP_map_detail/<int:pk>/', views.EP_map, name='EP_map_detail'),
    path('CH_map_detail/<int:pk>/', views.CH_map, name='CH_map_detail'),
    path('AS_map_detail/<int:pk>/', views.AS_map, name='AS_map_detail'),
    path('SH_map_detail/<int:pk>/', views.SH_map, name='SH_map_detail'),
    path('EN_map_detail/<int:pk>/', views.EN_map, name='EN_map_detail'),
    path('BS_map_detail/<int:pk>/', views.BS_map, name='BS_map_detail'),
    path('JL_map_detail/<int:pk>/', views.JL_map, name='JL_map_detail'),
    path('EE_map_detail/<int:pk>/', views.EE_map, name='EE_map_detail'),
    path('OM_map_detail/<int:pk>/', views.OM_map, name='OM_map_detail'),
    path('AD_map_detail/<int:pk>/', views.AD_map, name='AD_map_detail'),
    path('HC_map_detail/<int:pk>/', views.HC_map, name='HC_map_detail'),
    path('TSD_map_detail/<int:pk>/', views.TSD_map, name='TSD_map_detail'),
    path('MM_map_detail/<int:pk>/', views.MM_map, name='MM_map_detail'),
    path('TTA_map_detail/<int:pk>/', views.TTA_map, name='TTA_map_detail'),
    path('TFD_map_detail/<int:pk>/', views.TFD_map, name='TFD_map_detail'),
    path('FS_map_detail/<int:pk>/', views.FS_map, name='FS_map_detail'),
    path('IAC_map_detail/<int:pk>/', views.IAC_map, name='IAC_map_detail'),

]