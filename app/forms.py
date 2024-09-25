from django.forms import ModelForm
from django.core.exceptions import ValidationError
from .models import FileConversion

class FileConversionForm(ModelForm):
    def clean_original_file_type(self):
        data = self.cleaned_data['original_file_type']
        if data not in ['PDF', 'JPG', 'PNG', 'SVG']:
            raise ValidationError("Invalid file type")
        return data
    
    class Meta:
        model = FileConversion
        fields = ['original_file', 'original_file_type', 'conversion_type',]
        help_texts = {
            'original_file': 'Upload a file to convert',}
        