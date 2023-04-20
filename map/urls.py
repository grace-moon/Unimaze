from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('map/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('directions/<int:pk>/', views.direcions_detail, name='direcions_detail'),

]