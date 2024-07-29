from reportlab.lib.pagesizes import letter, landscape
from reportlab.pdfgen import canvas

from document_generator.base_document import BaseDocument


class PDFGenerator(BaseDocument):
    def __init__(self):
        self.canvas = None

    def create_canvas(self, file_path, orientation='portrait'):
        if orientation == 'landscape':
            self.canvas = canvas.Canvas(file_path, pagesize=landscape(letter))
        else:
            self.canvas = canvas.Canvas(file_path, pagesize=letter)

    def add_text(self, text, x, y):
        if self.canvas:
            self.canvas.drawString(x, y, text)
        else:
            raise ValueError("Canvas not initialized")

    def save(self, file_path):
        if self.canvas:
            self.canvas.save()
        else:
            raise ValueError("Canvas not initialized")

    def create_from_html(self, html_content, file_path):
        # Implement method to create PDF from HTML content
        pass
