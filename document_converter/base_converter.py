import os.path
import uuid
from traceback import format_exc
from typing import Optional

from .dispatcher import converter_dispatcher


class Converter:

    def __init__(self, base_dir=None):
        self.dispatcher = converter_dispatcher
        self.base_dir = base_dir if base_dir is not None else os.path.join('document_converter', 'uploads')

    def convert(self, file_path: str, output_file_name: Optional[str] = None, serve=False) -> Optional[str]:
        """
            Converts the file in 'file_path' to PDF to 'output_file_name.pdf' or some uuid.pdf, if output_file_name
            is not provided.
        """
        try:
            file_extension = file_path.split('.')[-1]
            output_file = "{0}.pdf".format(uuid.uuid4() if not output_file_name else output_file_name)
            converted = self.dispatcher.dispatch(file_extension, payload={
                'output_file_path': os.path.join(self.base_dir, output_file),
                'file_path': file_path
            })
            if converted:
                print("Converted successfully")
                if serve:
                    file = open(os.path.join(self.base_dir, output_file))
                    return file.read()
            else:
                print("Error converting file")

        except Exception as e:
            print(e)
            print(format_exc())
