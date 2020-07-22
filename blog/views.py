from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, CVItem
from .forms import PostForm, CVItemForm


# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def cv_list(request):
    cvitems = CVItem.objects.order_by('priority')
    return render(request, 'cv/cv_list.html', {'items': cvitems})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


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
    return render(request, 'blog/post_edit.html', {'form': form})


def cv_new(request):
    if request.method == "POST":
        form = CVItemForm(request.POST)
        if form.is_valid():
            cvitem = form.save(commit=False)
            cvitem.author = request.user
            cvitem.save()
            return redirect('cv_list')
    else:
        form = CVItemForm()
    return render(request, 'cv/cv_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def cv_edit(request, pk):
    cvitem = get_object_or_404(CVItem, pk=pk)
    if request.method == "POST":
        form = CVItemForm(request.POST, instance=cvitem)
        if form.is_valid():
            cvitem = form.save(commit=False)
            cvitem.author = request.user
            cvitem.save()
            cvitems = CVItem.objects.order_by('priority')
            return render(request, 'cv/cv_list.html', {'items': cvitems})
    else:
        form = CVItemForm(instance=cvitem)
    return render(request, 'cv/cv_edit.html', {'form': form})