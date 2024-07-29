import csv

from document_generator.base_document import BaseDocument


class CSVGenerator(BaseDocument):
    def __init__(self):
        self.file_path = None
        self.csvfile = None
        self.writer = None

    def create_csv(self, file_path):
        self.file_path = file_path
        self.csvfile = open(file_path, 'w', newline='')
        self.writer = csv.writer(self.csvfile)

    def add_row(self, row):
        if self.writer:
            self.writer.writerow(row)
        else:
            raise ValueError("CSV writer not initialized")

    def save(self, file_path):
        if self.csvfile:
            self.csvfile.close()
        else:
            raise ValueError("CSV file not initialized")
