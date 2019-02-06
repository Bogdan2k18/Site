
from django.urls import path
from News.models import Post
from News.views import home
from django.views.generic import ListView, DetailView


urlpatterns = [
    path('', ListView.as_view(queryset=Post.objects.all().order_by("-date")[:20], template_name="home.html")),
]
