from django.shortcuts import render
from django.http import HttpResponse


def staffView(request):
    context=dict(x=1)
    return render(request,"pages/staff.html",context)