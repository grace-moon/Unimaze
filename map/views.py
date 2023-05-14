from django.shortcuts import render, get_object_or_404
from .models import Unimaze_Post,Unimaze_map, Univ_Contacts
from django.http import HttpResponse

from .forms import PostForm
from django.utils import timezone
from django.shortcuts import redirect


# Create your views here.
def home(request):
    return render(request, '../templates/map/home.html', {})


def contacts_detail(request, pk):
    contract = get_object_or_404(Univ_Contacts, pk=pk)
    return render(request, '../templates/map/contracts_detail.html', {'contract':contract})

def	HRC_map(request, pk):
    vectary_map = get_object_or_404(Unimaze_map,pk=pk)
    map_list = Unimaze_map.objects.filter(building_num=0).order_by('published_date')
    return render(request, '../templates/map/HRC_map_detail.html',{'map':vectary_map, 'list':map_list})

def	C_L_map(request, pk):
    vectary_map = get_object_or_404(Unimaze_map,pk=pk)
    map_list = Unimaze_map.objects.filter(building_num=18).order_by('published_date')
    return render(request, '../templates/map/C_L_map_detail.html',{'map':vectary_map, 'list':map_list})

def	C_M_map(request, pk):
    vectary_map = get_object_or_404(Unimaze_map,pk=pk)
    map_list = Unimaze_map.objects.filter(building_num=18).order_by('published_date')
    return render(request, '../templates/map/C_Mmap_detail.html',{'map':vectary_map, 'list':map_list})

def	TTD_map(request, pk):
    vectary_map = get_object_or_404(Unimaze_map,pk=pk)
    map_list = Unimaze_map.objects.filter(building_num=0).order_by('published_date')
    return render(request, '../templates/map/TTD_map_detail.html',{'map':vectary_map, 'list':map_list})

def	 EP_map(request, pk):
    vectary_map = get_object_or_404(Unimaze_map,pk=pk)
    map_list = Unimaze_map.objects.filter(building_num=8).order_by('published_date')
    return render(request, '../templates/map/EP_map_detail.html',{'map':vectary_map, 'list':map_list})

def	 CH_map(request, pk):
    vectary_map = get_object_or_404(Unimaze_map,pk=pk)
    map_list = Unimaze_map.objects.filter(building_num=1).order_by('published_date')
    return render(request, '../templates/map/CH_map_detail.html',{'map':vectary_map, 'list':map_list})

def	 AS_map(request, pk):
    vectary_map = get_object_or_404(Unimaze_map,pk=pk)
    map_list = Unimaze_map.objects.filter(building_num=2).order_by('published_date')
    return render(request, '../templates/map/AS_map_detail.html',{'map':vectary_map, 'list':map_list})

def	 SH_map(request, pk):
    vectary_map = get_object_or_404(Unimaze_map,pk=pk)
    map_list = Unimaze_map.objects.filter(building_num=3).order_by('published_date')
    return render(request, '../templates/map/SH_map_detail.html',{'map':vectary_map, 'list':map_list})

def	 EN_map(request, pk):
    vectary_map = get_object_or_404(Unimaze_map,pk=pk)
    map_list = Unimaze_map.objects.filter(building_num=4).order_by('published_date')
    return render(request, '../templates/map/EN_map_detail.html',{'map':vectary_map, 'list':map_list})

def	 HS_map(request, pk):
    vectary_map = get_object_or_404(Unimaze_map,pk=pk)
    map_list = Unimaze_map.objects.filter(building_num=6).order_by('published_date')
    return render(request, '../templates/map/HS_map_detail.html',{'map':vectary_map, 'list':map_list})

def	 BS_map(request, pk):
    vectary_map = get_object_or_404(Unimaze_map,pk=pk)
    map_list = Unimaze_map.objects.filter(building_num=7).order_by('published_date')
    return render(request, '../templates/map/BS_map_detail.html',{'map':vectary_map, 'list':map_list})

def	 JL_map(request, pk):
    vectary_map = get_object_or_404(Unimaze_map,pk=pk)
    map_list = Unimaze_map.objects.filter(building_num=10).order_by('published_date')
    return render(request, '../templates/map/JL_map_detail.html',{'map':vectary_map, 'list':map_list})

def	 EE_map(request, pk):
    vectary_map = get_object_or_404(Unimaze_map,pk=pk)
    map_list = Unimaze_map.objects.filter(building_num=11).order_by('published_date')
    return render(request, '../templates/map/EE_map_detail.html',{'map':vectary_map, 'list':map_list})

def	 OM_map(request, pk):
    vectary_map = get_object_or_404(Unimaze_map,pk=pk)
    map_list = Unimaze_map.objects.filter(building_num=12).order_by('published_date')
    return render(request, '../templates/map/OM_map_detail.html',{'map':vectary_map, 'list':map_list})

def	 AD_map(request, pk):
    vectary_map = get_object_or_404(Unimaze_map,pk=pk)
    map_list = Unimaze_map.objects.filter(building_num=14).order_by('published_date')
    return render(request, '../templates/map/AD_map_detail.html',{'map':vectary_map, 'list':map_list})

def	 HC_map(request, pk):
    vectary_map = get_object_or_404(Unimaze_map,pk=pk)
    map_list = Unimaze_map.objects.filter(building_num=15).order_by('published_date')
    return render(request, '../templates/map/HC_map_detail.html',{'map':vectary_map, 'list':map_list})

def	TSD_map(request, pk):
    vectary_map = get_object_or_404(Unimaze_map,pk=pk)
    map_list = Unimaze_map.objects.filter(building_num=16).order_by('published_date')
    return render(request, '../templates/map/TSD_map_detail.html',{'map':vectary_map, 'list':map_list})

def	 MM_map(request, pk):
    vectary_map = get_object_or_404(Unimaze_map,pk=pk)
    map_list = Unimaze_map.objects.filter(building_num=19).order_by('published_date')
    return render(request, '../templates/map/MM_map_detail.html',{'map':vectary_map, 'list':map_list})

def	TTA_map(request, pk):
    vectary_map = get_object_or_404(Unimaze_map, pk=pk)
    map_list = Unimaze_map.objects.filter(building_num=22).order_by('published_date')
    return render(request, '../templates/map/TTA_map_detail.html',{'map':vectary_map, 'list':map_list})

def	TFD_map(request, pk):
    vectary_map = get_object_or_404(Unimaze_map,pk=pk)
    map_list = Unimaze_map.objects.filter(building_num=23).order_by('published_date')
    return render(request, '../templates/map/TFD_map_detail.html',{'map':vectary_map, 'list':map_list})

def	 FS_map(request, pk):
    vectary_map = get_object_or_404(Unimaze_map,pk=pk)
    map_list = Unimaze_map.objects.filter(building_num=24).order_by('published_date')
    return render(request, '../templates/map/FS_map_detail.html',{'map':vectary_map, 'list':map_list})

def	IAC_map(request, pk):
    vectary_map = get_object_or_404(Unimaze_map,pk=pk)
    map_list = Unimaze_map.objects.filter(building_num=25).order_by('published_date')
    return render(request, '../templates/map/IAC_map_detail.html',{'map':vectary_map, 'list':map_list})




def map_result(request):
    query = request.GET['q']
    posts = Unimaze_map.objects.filter(building_name__contains=query)|Unimaze_map.objects.filter(building_num__exact=22)|Unimaze_map.objects.filter(text__contains=query)
#    if 'q' in request.GET:
#        post = post.objects.all().filter(title__contains=query)| Q(description__contains=query)
    return render(request, 'map/map_search_results.html', {'posts':posts})


def contacts_result(request):
    query = request.GET['q']
    contacts = Univ_Contacts.objects.filter(department__contains=query) | Univ_Contacts.objects.filter(name=query) | Univ_Contacts.objects.filter(task__contains=query) #    if 'q' in request.GET:
#        post = post.objects.all().filter(title__contains=query)| Q(description__contains=query)
    return render(request, 'map/map_search_results.html', {'contacts':contacts})

