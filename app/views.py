from django.shortcuts import render
from django.http import HttpResponse
from .models import FileConversion
from .forms import FileConversionForm
from .tasks import convert_to_pdf

import magic

def file_upload(request):
    context = {
        'conversion_type' : FileConversion.CONVERSION_TYPES,
    }
    if request.method == 'POST':
        form = FileConversionForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.cleaned_data['file']

            # File type detection
            mime = magic.Magic(mime=True)
            file_format = mime.from_buffer(uploaded_file.read(1024))

            #Reset file pointer
            uploaded_file.seek(0)
            
            # generate output pdf path
            output_pdf = f'media/converted_files/{uploaded_file.name.split(".")[0]}.pdf'
            
                #check for file extension
            if file_format == 'csv':
                # launch  celery task
                task = convert_to_pdf.delay(
                uploaded_file,
                output_pdf
            )
            # store task ID in session to check status
            request.session['task_id'] = task.id

            context.update ({
                    
                'task_id': task.id,
            })
        context['form'] = form
        return render(request, 'app/base.html', context)
    else:
        context = {
            'form': FileConversionForm(),
            
        }
        return render(request, 'app/base.html', context)
