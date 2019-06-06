from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

from core.forms import UserForm


# def homeView(request):
#     context=dict()
#     if request.method == "POST":
#         username = request.POST.get('username', '')
#         password = request.POST.get('password', '')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             # Redirect to a success page.
#             return render(request,"home.html",context)
#         else:
#             # Return an 'invalid login' error message.
#             return HttpResponse("")
#     return render(request,"home.html",context)

def homeView(request):
    context=dict()
    if request.method == 'POST':
        form=UserForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                context['invalidUser']='true'
                context['form']=form
        else:
            context['form']=form
    else:
        context['form']=UserForm()
    return render(request,"pages/home.html",context)

def logoutUser(request):
    logout(request)
    return redirect('/')