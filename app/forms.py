from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from .models import FileConversion

class FileConversionForm(ModelForm):
    def clean_original_file(self):
        original_file = self.cleaned_data['original_file']
        if not original_file:
            raise ValidationError("Please upload a file.")
        return original_file

    def clean_original_file_type(self):
        original_file_format = self.cleaned_data['original_file_type']
        if not original_file_format:
            raise ValidationError("Please enter the file format.")
        if original_file_format not in dict(FileConversion.CONVERSION_TYPES):
            raise ValidationError("Invalid conversion format.")
        return original_file_format
    
    def clean_original_file_size(self):
        original_file_size = self.cleaned_data['original_file_size']
        if original_file_size > 1024 * 1024 *5:
            raise ValidationError("File size should be less than 5MB.")
        return original_file_size
    
    class Meta:
        model = FileConversion
        fields = ['original_file', 'original_file_format', 'conversion_type',]
        help_texts = {
            'original_file': 'Upload a file to convert',}
        
    conversion_type = forms.ChoiceField(choices=FileConversion.CONVERSION_TYPES)