from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.file_upload, name='convert'),
]