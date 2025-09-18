from django.http import HttpResponse
from .models import Crossword
from django.shortcuts import render


def index(request):
    crosswords = Crossword.objects.all()
    output = "\n".join(c.code for c in crosswords)
    return render(request, "crosswords/index.html")


def current(request):
    crossword = Crossword.objects.last()
    return render(request, "crosswords/current.html", {"code": crossword.code})
