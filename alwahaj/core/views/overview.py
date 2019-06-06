from django.shortcuts import render
from django.http import HttpResponse


def overviewView(request):
    context=dict(x=1)
    return render(request,"overview.html",context)