# Generated by Django 5.1.1 on 2024-09-25 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_fileconversion_converted_file_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileconversion',
            name='original_filename',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]