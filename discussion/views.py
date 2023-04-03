from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Reply
from django.views.generic import ListView
from .forms import PostForm, ReplyForm
from django.contrib import messages


@login_required(login_url="login")
def discussion_home_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        post = form.save(commit=False)
        user = request.user
        post.user = user
        print(post.user.username)
        print(post.title)
        print(post.description)
        post.save()
        return redirect("discussion_home")
    else:
        form = PostForm()
    context = {
        'form': form
    }
    all_posts = Post.objects.all()
    # all_posts.entry_set.all()
    context["all_posts"] = all_posts
    return render(request, "discussion_home.html", context)


@login_required(login_url="login")
def dynamic_post_view(request, id):
    if request.method == "POST":
        form = ReplyForm(request.POST)
        reply = form.save(commit=False)
        user = request.user
        post = Post.objects.get(id=id)
        reply.user = user
        reply.post = post
        reply.save()
        return redirect("discussion_home")
    else:
        form = ReplyForm()
        obj = Post.objects.get(id=id)
    context = {
        "post": obj,
        "form": form
    }
    return render(request, "dynamic_post_view.html", context)


@login_required(login_url="login")
def delete_post_view(request, id):
    obj = Post.objects.get(id=id)
    if (obj.user == request.user):
        obj.delete()
        messages.success(request, "Post deleted")
        return redirect("discussion_home")
    else:
        messages.error(request, "You can only delete posts made by you")
        return redirect("discussion_home")


@login_required(login_url="login")
def delete_reply_view(request, rid):
    obj = Reply.objects.get(id=rid)
    if (obj.user == request.user):
        obj.delete()
        messages.success(request, "Post deleted")
        return redirect("discussion_home")
    else:
        messages.error(request, "You can only delete posts made by you")
        return redirect("discussion_home")
