from django.shortcuts import render


def starting_page(request):
    return render(request, "blog/index.html")


def posts(request):
    return render(request, "blog/all_posts.html")


def post_details(request):
    pass