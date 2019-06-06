from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.db import IntegrityError
from core.models import Systems,Company,Projects,Staff,ProjectSystemJoint,\
                            ProjectStaffJoint,SystemImages,ProjectImages
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth.decorators import login_required
from core.forms import CompanyForm,SystemsForm,ProjectsForm,StaffForm,\
                        ProjectSystemForm,ProjectStaffForm
from django.forms import modelformset_factory
from django import forms


@login_required
def addCompany(request):
    context=dict()
    if request.method == 'POST':
        form=CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addCompany')
        else:
            context['form']=form
    else:
        context['form']=CompanyForm()
    context['section']="Add Company"
    # print(returnFields(Company))
    context['tableHeader']=['id','name','url']
    context['company']=Company.objects.all()
    # print(Company.objects.all())
    return render(request,"adminSetting.html",context)

@login_required
def addSystem(request):
    imageFormSet=modelformset_factory(SystemImages,fields=('image',),extra=1)
    context=dict()
    if request.method == 'POST':
        form=SystemsForm(request.POST, request.FILES or None)
        formset=imageFormSet(request.POST or None, request.FILES or None)
        if form.is_valid() and formset.is_valid():
            system=form.save()
            form.save()
            print("formset____>",formset)
            for f in formset:
                try:
                    image=SystemImages(system=system, image=f.cleaned_data['image'])
                    print("-------->",image)
                    image.save()
                except Exception as e:
                    break


            return redirect('addSystem')
        else:
            context['form']=form
            context['formset']=formset

    else:
        context['form']=SystemsForm()
        context['formset']=imageFormSet(queryset=SystemImages.objects.none())
    context['section']="Add System"
    context['tableHeader']=['id','name','description','cost','company','image']
    context['Systems']=Systems.objects.all()
    context['SystemImages']=SystemImages.objects.all()
    # print(SystemImages.objects.all().values())
    return render(request,"adminSetting.html",context)

@login_required
def linkSystem(request):
    context=dict()
    if request.method == 'POST':
        form=ProjectSystemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('linkSystem')
        else:
            context['form']=form
    else:
        context['form']=ProjectSystemForm()
    context['section']="Link System"
    context['tableHeader']=['id','Project','System','StartDate','EndDate','Location','Cost']
    context['ProjectSystemJoint']=ProjectSystemJoint.objects.all()
    # print(Company.objects.all())
    return render(request,"adminSetting.html",context)

@login_required
def linkStaff(request):
    context=dict()
    if request.method == 'POST':
        form=ProjectStaffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('linkStaff')
        else:
            context['form']=form
    else:
        context['form']=ProjectStaffForm()
    context['section']="Link Staff"
    context['tableHeader']=['id','Project','Staff','leader','Payroll','beneficiary','budget']
    context['ProjectStaffJoint']=ProjectStaffJoint.objects.all()
    # print(Company.objects.all())
    return render(request,"adminSetting.html",context)

@login_required
def addProject(request):
    imageFormSet=modelformset_factory(ProjectImages,fields=('image',),extra=1)
    context=dict()
    if request.method == 'POST':
        form=ProjectsForm(request.POST, request.FILES or None)
        formset=imageFormSet(request.POST or None, request.FILES or None)
        if form.is_valid() and formset.is_valid():
            project=form.save()
            form.save()

            for f in formset:
                try:
                    image=ProjectImages(project=project, image=f.cleaned_data['image'])
                    image.save()
                except Exception as e:
                    break


            return redirect('addProject')
        else:
            context['form']=form
            context['formset']=formset

    else:
        context['form']=ProjectsForm()
        context['formset']=imageFormSet(queryset=ProjectImages.objects.none())
    context['section']="Add Project"
    context['tableHeader']=['id','name','description','type','location',\
    'beneficiary','status','budget',"image"]

    context['Projects']=Projects.objects.all()
    context['ProjectImages']=ProjectImages.objects.all()
    # print(ProjectImages.objects.all())
    return render(request,"adminSetting.html",context)

@login_required
def addStaff(request):
    context=dict()
    if request.method == 'POST':
        form=StaffForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('addStaff')
        else:
            context['form']=form
    else:
        context['form']=StaffForm()
    context['section']="Add Staff"

    context['tableHeader']=['id','name','description','position','education','payroll','Image']
    context['Staff']=Staff.objects.all()
    # print(Company.objects.all())
    return render(request,"adminSetting.html",context)


def iterateDelete(array,model):
    if model is ProjectImages or model is SystemImages:
        image='media'+array[0].replace('/media','')
        model.objects.filter(image=image).delete()
    else:
        for id in array:
            model.objects.filter(id=id).delete()


def getModel(path):
    print(path)
    if(path=="/addStaff/"):
        return dict(model=Staff, form=StaffForm)
    elif(path=="/addProject/"):
        return dict(model=Projects, form=ProjectsForm)
    elif(path=="/addSystem/"):
        return dict(model=Systems, form=SystemsForm)
    elif(path=="/addCompany/"):
        return dict(model=Company, form=CompanyForm)
    elif(path=="/linkStaff/"):
        return dict(model=ProjectStaffJoint, form=ProjectStaffForm)
    elif(path=="/linkSystem/"):
        return dict(model=ProjectSystemJoint,form=ProjectSystemForm)
    elif(path=="/addProject/images"):
        return dict(model=ProjectImages,form=None)
    elif(path=="/addSystem/images"):
        return dict(model=SystemImages,form=None)

@login_required
def delete(request):
    if request.method == 'POST':
        iterateDelete(request.POST.getlist('row[]', ''),getModel(request.POST.get('model', ''))['model'])
        return render(request,"adminSetting.html",dict())




@login_required
def update(request,key=None):
    if request.method == 'POST':
        if request.POST.get('id','') and request.POST.get('model',''):
            result=getModel(request.POST.get('model',''))
            instance = get_object_or_404(result['model'], id=request.POST.get('id',''))
            form=result['form'](instance=instance)
            context=dict()
            context['form']=form
            return render(request,"adminSetting.html",context)

        path=request.META.get('HTTP_REFERER').split('/')
        relativePath="/"+path[len(path)-2]+"/"
        result=getModel(relativePath)
        insta = result['model'].objects.get(id=request.GET.get('key',''))
        form=result['form'](request.POST, request.FILES or None, instance=insta)
        form.save()

        return redirect(request.META.get('HTTP_REFERER'))