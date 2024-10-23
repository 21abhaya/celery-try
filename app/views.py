from django.shortcuts import render
from django.http import HttpResponse

from .models import FileConversion
from .forms import FileConversionForm

import magic

def file_upload(request):
    if request.method == 'POST':
        
        form = FileConversionForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.cleaned_data['file']

            # File type detection
            mime = magic.Magic(mime=True)
            file_format = mime.from_buffer(uploaded_file.read(1024))

            #Reset file pointer
            uploaded_file.seek(0)

            conversion_request = FileConversion.objects.create(
                original_file = uploaded_file,
                original_file_format = file_format,
                conversion_type = form.cleaned_data['conversion_type'],
            )

            context = {
                'form': form,
                'conversion_type': FileConversion.CONVERSION_TYPES,
            }

        return render(request, 'app/base.html', {'form': form, 'conversion_type': FileConversion.CONVERSION_TYPES})
    else:
        form = FileConversionForm()
        return render(request, 'app/base.html', {'form': form, 'conversion_type': FileConversion.CONVERSION_TYPES})
