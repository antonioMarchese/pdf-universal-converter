from .xlsx import convert_xlsx_to_pdf
from .csv import convert_csv_to_pdf
from ._docx import convert_docx_to_pdf
from .images import convert_image_to_pdf


class Dispatcher:
    def __init__(self):
        self.handlers = {}

    def add_handler(self, name, handler):
        self.handlers[name] = handler

    def dispatch(self, name, payload):
        if name in self.handlers:
            output_file_path = payload.get('output_file_path', None)
            file_path = payload.get('file_path', None)
            return self.handlers[name](file_path, output_file_path)

        raise NotImplementedError("Extension type dispatcher not implemented")


converter_dispatcher = Dispatcher()
converter_dispatcher.add_handler('xlsx', convert_xlsx_to_pdf)
converter_dispatcher.add_handler('csv', convert_csv_to_pdf)
converter_dispatcher.add_handler('docx', convert_docx_to_pdf)
for ext in ['png', 'jpg', 'jpeg']:
    converter_dispatcher.add_handler(ext, convert_image_to_pdf)

