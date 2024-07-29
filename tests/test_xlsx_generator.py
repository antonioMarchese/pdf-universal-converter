import os
import pytest

from document_generator import XlsxGenerator


@pytest.fixture
def excel_generator():
    return XlsxGenerator()


def test_create_workbook(excel_generator):
    excel_generator.create_workbook("test.xlsx")
    assert excel_generator.workbook is not None


def test_add_data(excel_generator):
    excel_generator.create_workbook("test.xlsx")
    excel_generator.add_data("Hello, world!", 0, 0)
    assert excel_generator.workbook.active.cell(row=1, column=1).value == "Hello, world!"


def test_save_excel(excel_generator):
    excel_generator.create_workbook("test.xlsx")
    excel_generator.add_data("Hello, world!", 0, 0)
    excel_generator.save("test.xlsx")
    assert os.path.exists("test.xlsx")
    os.remove("test.xlsx")
