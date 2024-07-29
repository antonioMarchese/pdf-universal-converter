import os
import pytest

from document_generator import PDFGenerator


@pytest.fixture
def pdf_generator():
    return PDFGenerator()


def test_create_canvas(pdf_generator):
    pdf_generator.create_canvas("test.pdf", orientation='portrait')
    assert pdf_generator.canvas is not None


def test_add_text(pdf_generator):
    pdf_generator.create_canvas("test.pdf", orientation='portrait')
    pdf_generator.add_text("Hello, world!", 100, 750)
    assert "Hello, world!" in pdf_generator.canvas.get_text()


def test_save_pdf(pdf_generator):
    pdf_generator.create_canvas("test.pdf", orientation='portrait')
    pdf_generator.add_text("Hello, world!", 100, 750)
    pdf_generator.save("test.pdf")
    assert os.path.exists("test.pdf")
    os.remove("test.pdf")
