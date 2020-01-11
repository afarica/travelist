from django.shortcuts import render
from django.views.generic import View
from .models import *


def index_page(request):
    return render(request, 'index.html')


def about_page(request):
    return render(request, 'about.html')


#
# class IndexPage(View):
#     model = Ad
#     template = 'index.html'
