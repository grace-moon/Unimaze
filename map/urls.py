from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('map/map_results', views.map_result, name='map_results'),
    path('map/contacts_results', views.map_result, name='map_results'),
    path('map/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('contact/<int:pk>/', views.contacts_detail, name='contract'),
    path('map_detail/<int:pk>/', views.TTA_map, name='map_detail'),
]