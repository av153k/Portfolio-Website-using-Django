from django.shortcuts import render
from blog.models import Post, Comments
from .forms import comment_form

def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {
        "posts": posts,
    }
    return render(request, "blog_index.html", context)

def blog_category(request, category):
    posts = Post.objects.filter(categories__name__contains=category).order_by('-created_on')
    context = {
        "category": category,
        "posts": posts,
    }
    return render(request, "blog_category.html", context)

def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)

    form = comment_form()
    if request.method == 'POST':
        form = comment_form(request.POST)
        if form.is_valid():
            comment = Comments(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()

    comments = Comments.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": form
    }
    return render(request, "blog_detail.html", context)

