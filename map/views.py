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
    return render(request, '../templats/map/contracts_detail.html', {'contract':contract})


#건물별 views
def HRC(request, pk):
    vectary_map = get_object_or_404(HRC, pk=pk)
    map_list = HRC.objects.all()
    return render(request, '../templates/map/map_detail.html',{'map':vectary_map}, {'list':map_list})

def MAC_L(request, pk):
    vectary_map = get_object_or_404(MAC_L, pk=pk)
    map_list = MAC_L.objects.all()
    return render(request, '../templates/map/map_detail.html',{'map':vectary_map}, {'list':map_list})

def MAC_M(request, pk):
    vectary_map = get_object_or_404(MAC_M, pk=pk)
    map_list = MAC_M.objects.all()
    return render(request, '../templates/map/map_detail.html',{'map':vectary_map}, {'list':map_list})

def TTD(request, pk):
    vectary_map = get_object_or_404(TTD, pk=pk)
    map_list = TTD.objects.all()
    return render(request, '../templates/map/map_detail.html',{'map':vectary_map}, {'list':map_list})

def EP(request, pk):
    vectary_map = get_object_or_404(EP, pk=pk)
    map_list = EP.objects.all()
    return render(request, '../templates/map/map_detail.html',{'map':vectary_map}, {'list':map_list})

def CH(request, pk):
    vectary_map = get_object_or_404(CH, pk=pk)
    map_list = CH.objects.all()
    return render(request, '../templates/map/map_detail.html',{'map':vectary_map}, {'list':map_list})

def AS(request, pk):
    vectary_map = get_object_or_404(AS, pk=pk)
    map_list = AS.objects.all()
    return render(request, '../templates/map/map_detail.html',{'map':vectary_map}, {'list':map_list})

def SH(request, pk):
    vectary_map = get_object_or_404(SH, pk=pk)
    map_list = SH.objects.all()
    return render(request, '../templates/map/map_detail.html',{'map':vectary_map}, {'list':map_list})

def EN(request, pk):
    vectary_map = get_object_or_404(EN, pk=pk)
    map_list = EN.objects.all()
    return render(request, '../templates/map/map_detail.html',{'map':vectary_map}, {'list':map_list})

def HS(request, pk):
    vectary_map = get_object_or_404(HS, pk=pk)
    map_list = HS.objects.all()
    return render(request, '../templates/map/map_detail.html',{'map':vectary_map}, {'list':map_list})

def BS(request, pk):
    vectary_map = get_object_or_404(BS, pk=pk)
    map_list = BS.objects.all()
    return render(request, '../templates/map/map_detail.html',{'map':vectary_map}, {'list':map_list})

def JL(request, pk):
    vectary_map = get_object_or_404(JL, pk=pk)
    map_list = JL.objects.all()
    return render(request, '../templates/map/map_detail.html',{'map':vectary_map}, {'list':map_list})

def EE(request, pk):
    vectary_map = get_object_or_404(EE, pk=pk)
    map_list = EE.objects.all()
    return render(request, '../templates/map/map_detail.html',{'map':vectary_map}, {'list':map_list})

def OM(request, pk):
    vectary_map = get_object_or_404(OM, pk=pk)
    map_list = OM.objects.all()
    return render(request, '../templates/map/map_detail.html',{'map':vectary_map}, {'list':map_list})

def AD(request, pk):
    vectary_map = get_object_or_404(AD, pk=pk)
    map_list = AD.objects.all()
    return render(request, '../templates/map/map_detail.html',{'map':vectary_map}, {'list':map_list})

def HC(request, pk):
    vectary_map = get_object_or_404(HC, pk=pk)
    map_list = HC.objects.all()
    return render(request, '../templates/map/map_detail.html',{'map':vectary_map}, {'list':map_list})

def TSD(request, pk):
    vectary_map = get_object_or_404(TSD, pk=pk)
    map_list = TSD.objects.all()
    return render(request, '../templates/map/map_detail.html',{'map':vectary_map}, {'list':map_list})

def MM(request, pk):
    vectary_map = get_object_or_404(MM, pk=pk)
    map_list = MM.objects.all()
    return render(request, '../templates/map/map_detail.html',{'map':vectary_map}, {'list':map_list})

def TTA(request, pk):
    vectary_map = get_object_or_404(TTA, pk=pk)
    map_list = TTA.objects.all()
    return render(request, '../templates/map/map_detail.html',{'map':vectary_map}, {'list':map_list})

def TFD(request, pk):
    vectary_map = get_object_or_404(TFD, pk=pk)
    map_list = TFD.objects.all()
    return render(request, '../templates/map/map_detail.html',{'map':vectary_map}, {'list':map_list})

def FS(request, pk):
    vectary_map = get_object_or_404(FS, pk=pk)
    map_list = FS.objects.all()
    return render(request, '../templates/map/map_detail.html',{'map':vectary_map}, {'list':map_list})

def IAC(request, pk):
    vectary_map = get_object_or_404(IAC, pk=pk)
    map_list = IAC.objects.all()
    return render(request, '../templates/map/map_detail.html',{'map':vectary_map}, {'list':map_list})










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
