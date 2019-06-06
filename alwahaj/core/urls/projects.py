from django.urls import path
from django.conf.urls import url, include

from core.views import projects

urlpatterns = [
    path('', projects.projectsView, name='projects'),
]