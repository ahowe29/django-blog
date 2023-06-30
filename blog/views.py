from django.shortcuts import render, get_object_or_404
from datetime import date

from .models import Post


def get_date_from_post(post):
    return post.get("date")


def starting_page(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]
    # sorted_by_date = sorted(all_posts, key=get_date_from_post)
    # latest_posts = sorted_by_date[-3:]
    return render(request, "blog/index.html", {"posts": latest_posts})


def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "blog/all_posts.html", {"all_posts": all_posts})


def post_details(request, slug):
    selected_post = get_object_or_404(Post, slug=slug)
    return render(
        request,
        "blog/post_detail.html",
        {
            "post": selected_post,
            "selected_post_tags": selected_post.tags.all()
        }
    )
