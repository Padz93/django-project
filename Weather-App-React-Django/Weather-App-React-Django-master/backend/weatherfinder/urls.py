"""weatherfinder URL Configuration

"""
from django.contrib import admin
from django.urls import path, re_path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', views.catchall),
    path('about/', views.about_view)
]
