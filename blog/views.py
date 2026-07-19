from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import BlogForm
from .models import Blog


def index(request):
    blogs = Blog.objects.order_by('-created_at')
    return render(request, 'blog_list.html', {'blogs': blogs})


def detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, 'blog_detail.html', {'blog': blog})


@login_required
def create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_index')
    else:
        form = BlogForm()
    return render(request, 'blog_form.html', {'form': form, 'page_title': 'Create Blog'})


@login_required
def edit(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog_detail', pk=blog.pk)
    else:
        form = BlogForm(instance=blog)
    return render(request, 'blog_form.html', {'form': form, 'page_title': 'Edit Blog'})


@login_required
def delete(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        blog.delete()
        return redirect('blog_index')
    return render(request, 'blog_delete.html', {'blog': blog})