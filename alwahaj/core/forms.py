from django import forms
from core.models import Systems,Company,Projects,Staff,ProjectSystemJoint,ProjectStaffJoint


# from django.forms import modelformset_factory

class UserForm(forms.Form):
    username=forms.CharField(label='Username',max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


class CompanyForm(forms.ModelForm):

    class Meta:
        model=Company
        fields='__all__'

class SystemsForm(forms.ModelForm):

    class Meta:
        model=Systems
        fields='__all__'

class ProjectsForm(forms.ModelForm):

    class Meta:
        model=Projects
        fields=('name','description','description','type',\
        'location','beneficiary','status','budget','image')

class StaffForm(forms.ModelForm):

    class Meta:
        model=Staff
        fields='__all__'

class ProjectSystemForm(forms.ModelForm):

    class Meta:
        model=ProjectSystemJoint
        fields='__all__'

class ProjectStaffForm(forms.ModelForm):

    class Meta:
        model=ProjectStaffJoint
        fields='__all__'



