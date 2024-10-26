from celery import shared_task
from reportlab.pdfgen import canvas
from PIL import Image

@shared_task 
def convert_to_pdf(input_file, output_pdf):
    pdf_canvas = canvas.Canvas(output_pdf)
    pdf_canvas.drawString(100, 100, input_file)
    pdf_canvas.save()
    return output_pdf

