from django.shortcuts import render, get_object_or_404
from .models import Unimaze_Post,Unimaze_map, Univ_Contacts
from django.http import HttpResponse
from .forms import PostForm
from django.utils import timezone
from django.shortcuts import redirect

# Create your views here.
def home(request):
    post_map = Unimaze_map.objects.all()
    post_con = Univ_Contacts.objects.all()
    post_post = Unimaze_Post.objects.all()
    return render(request, '../templates/map/home.html', {'post_map':post_map, 'post_con':post_con, 'post_post':post_post})

def ready(request):
    post_map = Unimaze_map.objects.all()
    post_con = Univ_Contacts.objects.all()
    post_post = Unimaze_Post.objects.all()
    return render(request, '../templates/map/ready.html', {'post_map':post_map, 'post_con':post_con, 'post_post':post_post})


def map_detail(request, building_num, pk,):
    building_num = int(building_num)
    vectary_map = get_object_or_404(Unimaze_map, pk=pk)
    map_list = Unimaze_map.objects.filter(building_num=building_num).order_by('published_date')
    post_map = Unimaze_map.objects.all()
    post_con = Univ_Contacts.objects.all()
    post_post = Unimaze_Post.objects.all()
    template_name = '../templates/map/map_detail.html'
    return render(request, template_name, {'map':vectary_map, 'list':map_list, 'post_map':post_map, 'post_con':post_con, 'post_post':post_post, })

