from django.forms import ModelForm
from .models import FileConversion

class FileConversionForm(ModelForm):
    
    
    class Meta:
        model = FileConversion
        fields = ['original_file', 'original_file_type', 'conversion_type',]
