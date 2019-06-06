from django.shortcuts import render
from django.http import HttpResponse




def solutionsView(request):
    context=dict(x=1)
    return render(request,"pages/solutions.html",context)