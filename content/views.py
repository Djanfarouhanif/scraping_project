from django.shortcuts import render

# Create your views here.
from .scraping import run


def index(request):
    return render(request)