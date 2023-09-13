from django.shortcuts import render
from django.views.generic import ListView
from .models import Post, Foot
# Create your views here.


class HomeListView(ListView):
    model = Post
    template_name = 'home.html'


class FootListView(ListView):
    model = Foot
    template_name = 'foot.html'

