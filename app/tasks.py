from celery import shared_task
from reportlab.pdfgen import canvas
from PIL import Image

@shared_task 
def convert_to_pdf(file_path, output_path):
    canvas = canvas.Canvas(output_path)
    canvas.drawImage(file_path, 0, 0)
    canvas.save()
    return output_path
    