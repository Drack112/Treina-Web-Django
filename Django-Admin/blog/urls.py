from django.urls import path

from .views import *

urlpatterns = [
    path("posts", post_get, name="posts"),
    path("post/<int:id>", post_get_id, name="post"),
]
