from django.urls import path
from django.conf.urls import url, include

from core.views import staff

urlpatterns = [
    path('', staff.staffView, name='staff'),
]