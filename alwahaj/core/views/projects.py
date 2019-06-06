from django.shortcuts import render
from django.http import HttpResponse


def projectsView(request):
    context=dict(x=1)
    return render(request,"pages/project.html",context)