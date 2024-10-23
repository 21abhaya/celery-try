from django.db import models


class FileConversion(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('PROCESSING', 'Processing'),
        ('COMPLETED', 'Completed'),
        ('FAILED', 'Failed'),
    ]

    CONVERSION_TYPES = [
        ('Converts to PDF', 'PDF'),
        ('Converts to  JPG', 'JPG'),
        ('Converts to PNG', 'PNG'),
        ('Converts to SVG', 'SVG'),
    ]

    original_file = models.FileField(upload_to='original_files/')
    converted_file = models.FileField(upload_to='converted_files/', null=True, blank=True)
    original_filename = models.CharField(max_length=255, null=True, blank=True)
    original_file_size = models.IntegerField(help_text="File size in bytes", null=True, blank=True) 
    original_file_format = models.CharField(max_length=50)
    # converted_file_type = models.CharField(max_length=50)
    conversion_type = models.CharField(max_length=100, choices=CONVERSION_TYPES, null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    error_message = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.original_filename} - {self.status}"

    class Meta:
        ordering = ['-created_at']
