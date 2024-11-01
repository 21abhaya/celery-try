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
            print("file format:", file_format)

            #Reset file pointer
            uploaded_file.seek(0)

            # generate output pdf path
            output_pdf = f'media/converted_files/{uploaded_file.name.split(".")[0]}.pdf'
            
            #check for file type
            mime_types = [
                            'text/csv',
                            'text/plain',
                            'text/html',
                            'text/xml',
                            'application/pdf',
                            'application/msword',
                            'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
                            'application/vnd.ms-excel',
                            'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                            'application/vnd.ms-powerpoint',
                            'application/vnd.openxmlformats-officedocument.presentationml.presentation',
                        ] 
            if file_format in mime_types:
                # launch  celery task
                task = convert_to_pdf.delay(
                uploaded_file,
                output_pdf
            )
            else:
                return HttpResponse("File type not supported")
            
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
