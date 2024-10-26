from django.shortcuts import render
from django.http import HttpResponse
from .models import FileConversion
from .forms import FileConversionForm
from .tasks import convert_to_pdf

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
                original_file=uploaded_file,
                original_file_format=file_format,
                conversion_type=form.cleaned_data['conversion_type'],
            )
            
            # validate the model
            conversion_request.full_clean()
            conversion_request.save()

            # generate output pdf path
            output_pdf = f'media/converted_files/{uploaded_file.name.split(".")[0]}.pdf'

            # launch  celery task
            task = convert_to_pdf.delay(
                conversion_request.original_file.path,
                output_pdf
            )
            # store task ID in session to check status
            request.session['task_id'] = task.id

            context = {
                'form': form,
                'conversion_type': FileConversion.CONVERSION_TYPES,
                'task_id': task.id,
            }

        return render(request, 'app/base.html', context)
    else:
        form = FileConversionForm()
        return render(request, 'app/base.html', context)
