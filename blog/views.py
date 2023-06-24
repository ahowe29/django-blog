from django.shortcuts import render
from datetime import date


all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "family.JPG",
        "author": "Allie",
        "date": date(2021, 7, 21),
        "title": "Mountain Hiking",
        "excerpt": "I love hiking I love hiking I love hiking I love hiking I love hiking I love hiking I love hiking",
        "content": """
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore
            et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
            aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum
            dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia
            deserunt mollit anim id est laborum.
            
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore
            et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
            aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum
            dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia
            deserunt mollit anim id est laborum.
        """,
    },
    {
        "slug": "programming-is-fun",
        "image": "allie_pro.jpg",
        "author": "Maximilian",
        "date": date(2022, 3, 10),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": """
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
              aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
              velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

              Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
              aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
              velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

              Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
              aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
              velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
            """
    },
    {
        "slug": "into-the-woods",
        "image": "allie.jpg",
        "author": "Maximilian",
        "date": date(2020, 8, 5),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
              aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
              velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

              Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
              aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
              velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

              Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
              aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
              velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
            """
    }
]


def get_date_from_post(post):
    return post.get("date")


def starting_page(request):
    sorted_by_date = sorted(all_posts, key=get_date_from_post)
    latest_posts = sorted_by_date[-3:]
    return render(request, "blog/index.html", {"posts": latest_posts})


def posts(request):
    return render(request, "blog/all_posts.html", {"all_posts": all_posts})


def post_details(request, slug):
    selected_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post_detail.html", {"post": selected_post})
