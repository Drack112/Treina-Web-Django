from django.shortcuts import render
from django.views.decorators.cache import cache_page

from .services.post_service import *

# Create your views here.


@cache_page(30)
def post_get(request):
    posts = listar_posts()
    return render(request, "posts.html", {"posts": posts})


@cache_page(30)
def post_get_id(request, id):
    post = listar_post_id(id=id)
    return render(request, "post.html", {"post": post})
