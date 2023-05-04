from django.shortcuts import render, get_object_or_404
from .models import Map_Post, Direcrions_Post
from .forms import PostForm
from django.utils import timezone
from django.shortcuts import redirect


# Create your views here.
def home(request):
    return render(request, '../templates/map/home.html', {})

def post_list(request):
    post = Map_Post.objects.all()
    return render(request, '../templates/map/post_detail.html', {'post', post})

def post_detail(request, pk):
    post = get_object_or_404(Map_Post, pk=pk)
    return render(request, '../templates/map/post_detail.html', {'post':post})

def direcions_detail(request, pk):
    post = get_object_or_404(Direcrions_Post, pk=pk)
    return render(request, '../templates/map/directions_detail.html', {'post':post})


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
