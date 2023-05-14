from django.shortcuts import render, get_object_or_404
from .models import Unimaze_Post,Unimaze_map, Univ_Contacts
from .forms import PostForm
from django.utils import timezone
from django.shortcuts import redirect


# Create your views here.
def home(request):
    return render(request, '../templates/map/home.html', {})

def post_list(request):
    post = Unimaze_Post.objects.all()
    return render(request, '../templates/map/post_detail.html', {'post', post})

def post_detail(request, pk):
    post = get_object_or_404(Unimaze_Post, pk=pk)
    return render(request, '../templates/map/post_detail.html', {'post':post})


def contacts_detail(request, pk):
    contract = get_object_or_404(Univ_Contacts, pk=pk)
    return render(request, '../templates/map/contracts_detail.html', {'contract':contract})


def TTA_map(request, pk):
    vectary_map = get_object_or_404(Unimaze_map, pk=pk)
    map_list = Unimaze_map.objects.filter(building_num=22).order_by('published_date')
    return render(request, '../templates/map/map_detail.html', {'map':vectary_map,'list':map_list})

'''
def result(request):
    query = request.GET['q']
    posts = Unimaze_Post, Direcrions_Post, Univ_Contacts, HRC, MAC_L, MAC_M, TTD, EP, CH, AS, SH, EN, HS, BS, JL, EE, OM, AD, HC, TSD, MM| Map_detail, TFD, FS, IAC
        Post.objects.filter(title__contains=query) | Post.objects.filter(text__contains=query)
#    if 'q' in request.GET:
#        post = post.objects.all().filter(title__contains=query)| Q(description__contains=query)
    return render(request, 'blog/result.html', {'posts':posts})
'''




def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'map/post_edit.html', {'form': form})


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

