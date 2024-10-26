from celery import shared_task
from reportlab.pdfgen import canvas
from PIL import Image

@shared_task 
def convert_to_pdf(file_path, output_path):
    pdf_canvas = canvas.Canvas(output_path)
    pdf_canvas.drawString(100, 100, file_path)
    pdf_canvas.save()
    return output_path