from django.urls import path
from django.conf.urls import url, include

from core.views import solutions

urlpatterns = [
    path('', solutions.solutionsView, name='solutions'),
]