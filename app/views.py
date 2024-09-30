from django.shortcuts import render
from django.http import HttpResponse

from .models import FileConversion
from .forms import FileConversionForm

def file_upload(request):
    if request.method == 'POST':
        
        form = FileConversionForm(request.POST, request.FILES)
        
        return 

