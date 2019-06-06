from django.shortcuts import render
from django.http import HttpResponse


def contactUs(request):
    context=dict(x=1)
    return render(request,"pages/contactUs.html",context)