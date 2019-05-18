from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect

from django.http import JsonResponse


def get_percent_ating_from_post(post):
    float_meta_acum = float(post.meta_acum)
    float_real_acum = float(post.real_acum)
    return "%.2f" % ((float_real_acum / float_meta_acum) * 100)


def get_farol_from_post(post):
    float_percent_ating = float(post.percent_ating)
    if float_percent_ating < 80:
        return 'VERMELHO'
    elif float_percent_ating >= 100.0:
        return 'VERDE'
    else:
        return 'AMARELO'


def get_atingido_ano_from_post(post):
    float_meta_ano = float(post.meta_ano)
    float_real_acum = float(post.real_acum)
    return "%.2f" % ((float_real_acum / float_meta_ano) * 100)


def post_list(request):
    posts = Post.objects.filter(
        published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'placarPPR/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'placarPPR/post_detail.html', {'post': post, 'header_title': post.title})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.percent_ating = get_percent_ating_from_post(post)
            post.atingido_ano = get_atingido_ano_from_post(post)
            post.farol = get_farol_from_post(post)
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'placarPPR/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.percent_ating = get_percent_ating_from_post(post)
            post.atingido_ano = get_atingido_ano_from_post(post)
            post.farol = get_farol_from_post(post)
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'placarPPR/post_edit.html', {'form': form})


def healthcheck(request):
    health_obj = {'Online': True}
    return JsonResponse(health_obj)
