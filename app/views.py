from django.shortcuts import render
from django.http import HttpResponse

from .models import FileConversion
from .forms import FileConversionForm

def file_upload(request):
    if request.method == 'POST':
        
        form = FileConversionForm(request.POST, request.FILES)

        if form.is_valid():        
            
            handle_file_conversion(request.FILES['file'])
            return HttpResponse("File uploaded successfully.")
        else:
            return HttpResponse("Invalid form data.")
        
    else:
        form = FileConversionForm()
        
        return render(request, 'file_upload.html', {'form': form})

