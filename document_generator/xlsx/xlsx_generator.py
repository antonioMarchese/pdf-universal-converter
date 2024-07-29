from openpyxl.workbook import Workbook

from document_generator.base_document import BaseDocument


class XlsxGenerator(BaseDocument):
    def __init__(self):
        self.workbook = None
        self.worksheet = None

    def create_workbook(self, file_path):
        self.workbook = Workbook(file_path)
        self.worksheet = self.workbook.add_worksheet()

    def add_data(self, data, row, col):
        if self.worksheet:
            self.worksheet.write(row, col, data)
        else:
            raise ValueError("Worksheet not initialized")

    def save(self, file_path):
        if self.workbook:
            self.workbook.close()
        else:
            raise ValueError("Workbook not initialized")
