from django.shortcuts import render, get_object_or_404
from .models import Unimaze_Post, Direcrions_Post, Univ_Contacts, HRC, MAC_L, MAC_M, TTD, EP, CH, AS, SH, EN, HS, BS, JL, EE, OM, AD, HC, TSD, MM, TTA, TFD, FS, IAC
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





def direcions_detail(request, pk):
    post = get_object_or_404(Direcrions_Post, pk=pk)
    return render(request, '../templates/map/directions_detail.html', {'post':post})

def contracts_detail(request, pk):
    contract = get_object_or_404(Univ_Contacts, pk=pk)
    return render(request, '../templates/map/contracts_detail.html', {'contract':contract})


#건물별 views
def HRC_map(request, pk):
    vectary_map = get_object_or_404(HRC, pk=pk)
    map_list = HRC.objects.all().order_by('floor')
    return render(request, '../templates/map/HRC_map_detail.html',{'map':vectary_map,'list':map_list})

def MAC_L_map(request, pk):
    vectary_map = get_object_or_404(MAC_L, pk=pk)
    map_list = MAC_L.objects.all().order_by('floor')
    return render(request, '../templates/map/MAC_L_map_detail.html',{'map':vectary_map,'list':map_list})

def MAC_M_map(request, pk):
    vectary_map = get_object_or_404(MAC_M, pk=pk)
    map_list = MAC_M.objects.all().order_by('floor')
    return render(request, '../templates/map/MAC_M_map_detail.html',{'map':vectary_map,'list':map_list})

def TTD_map(request, pk):
    vectary_map = get_object_or_404(TTD, pk=pk)
    map_list = TTD.objects.all().order_by('floor')
    return render(request, '../templates/map/TTD_map_detail.html',{'map':vectary_map,'list':map_list})

def EP_map(request, pk):
    vectary_map = get_object_or_404(EP, pk=pk)
    map_list = EP.objects.all().order_by('floor')
    return render(request, '../templates/map/EP_map_detail.html',{'map':vectary_map,'list':map_list})

def CH_map(request, pk):
    vectary_map = get_object_or_404(CH, pk=pk)
    map_list = CH.objects.all().order_by('floor')
    return render(request, '../templates/map/CH_map_detail.html',{'map':vectary_map,'list':map_list})

def AS_map(request, pk):
    vectary_map = get_object_or_404(AS, pk=pk)
    map_list = AS.objects.all().order_by('floor')
    return render(request, '../templates/map/AS_map_detail.html',{'map':vectary_map,'list':map_list})

def SH_map(request, pk):
    vectary_map = get_object_or_404(SH, pk=pk)
    map_list = SH.objects.all().order_by('floor')
    return render(request, '../templates/map/SH_map_detail.html',{'map':vectary_map,'list':map_list})

def EN_map(request, pk):
    vectary_map = get_object_or_404(EN, pk=pk)
    map_list = EN.objects.all().order_by('floor')
    return render(request, '../templates/map/EN_map_detail.html',{'map':vectary_map,'list':map_list})

def HS_map(request, pk):
    vectary_map = get_object_or_404(HS, pk=pk)
    map_list = HS.objects.all().order_by('floor')
    return render(request, '../templates/map/HS_map_detail.html',{'map':vectary_map,'list':map_list})

def BS_map(request, pk):
    vectary_map = get_object_or_404(BS, pk=pk)
    map_list = BS.objects.all().order_by('floor')
    return render(request, '../templates/map/BS_map_detail.html',{'map':vectary_map,'list':map_list})

def JL_map(request, pk):
    vectary_map = get_object_or_404(JL, pk=pk)
    map_list = JL.objects.all().order_by('floor')
    return render(request, '../templates/map/JL_map_detail.html',{'map':vectary_map,'list':map_list})

def EE_map(request, pk):
    vectary_map = get_object_or_404(EE, pk=pk)
    map_list = EE.objects.all().order_by('floor')
    return render(request, '../templates/map/EE_map_detail.html',{'map':vectary_map,'list':map_list})

def OM_map(request, pk):
    vectary_map = get_object_or_404(OM, pk=pk)
    map_list = OM.objects.all().order_by('floor')
    return render(request, '../templates/map/OM_map_detail.html',{'map':vectary_map,'list':map_list})

def AD_map(request, pk):
    vectary_map = get_object_or_404(AD, pk=pk)
    map_list = AD.objects.all().order_by('floor')
    return render(request, '../templates/map/AD_map_detail.html',{'map':vectary_map,'list':map_list})

def HC_map(request, pk):
    vectary_map = get_object_or_404(HC, pk=pk)
    map_list = HC.objects.all().order_by('floor')
    return render(request, '../templates/map/HC_map_detail.html',{'map':vectary_map,'list':map_list})

def TSD_map(request, pk):
    vectary_map = get_object_or_404(TSD, pk=pk)
    map_list = TSD.objects.all().order_by('floor')
    return render(request, '../templates/map/TSD_map_detail.html',{'map':vectary_map,'list':map_list})

def MM_map(request, pk):
    vectary_map = get_object_or_404(MM, pk=pk)
    map_list = MM.objects.all().order_by('floor')
    return render(request, '../templates/map/MM_map_detail.html',{'map':vectary_map,'list':map_list})

def TTA_map(request, pk):
    vectary_map = get_object_or_404(TTA, pk=pk)
    map_list = TTA.objects.all().order_by('published_date')
    return render(request, '../templates/map/TTA_map_detail.html', {'map':vectary_map,'list':map_list})

def TFD_map(request, pk):
    vectary_map = get_object_or_404(TFD, pk=pk)
    map_list = TFD.objects.all().order_by('floor')
    return render(request, '../templates/map/TFD_map_detail.html', {'map':vectary_map,'list':map_list})

def FS_map(request, pk):
    vectary_map = get_object_or_404(FS, pk=pk)
    map_list = FS.objects.all().order_by('floor')
    return render(request, '../templates/map/FS_map_detail.html', {'map':vectary_map,'list':map_list})

def IAC_map(request, pk):
    vectary_map = get_object_or_404(IAC, pk=pk)
    map_list = IAC.objects.all().order_by('floor')
    return render(request, '../templates/map/IAC_map_detail.html', {'map':vectary_map,'list':map_list})



'''
def result(request):
    query = request.GET['q']
    posts = Unimaze_Post, Direcrions_Post, Univ_Contacts, HRC, MAC_L, MAC_M, TTD, EP, CH, AS, SH, EN, HS, BS, JL, EE, OM, AD, HC, TSD, MM, TTA, TFD, FS, IAC
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
