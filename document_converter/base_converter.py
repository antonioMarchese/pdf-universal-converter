import os.path
import uuid
from traceback import format_exc
from typing import Optional

from .dispatcher import converter_dispatcher


class Converter:

    def __init__(self, base_dir=None):
        self.dispatcher = converter_dispatcher
        self.base_dir = base_dir if base_dir is not None else os.path.join('document_converter', 'uploads')

    def convert(self, file_path: str, serve=False) -> Optional[str]:
        try:
            file_extension = file_path.split('.')[-1]
            output_file = f"{uuid.uuid4()}.pdf"
            converted = self.dispatcher.dispatch(file_extension, payload={
                'output_file_path': os.path.join(self.base_dir, output_file),
                'file_path': file_path
            })
            if converted:
                print("Converted successfully")
                if serve:
                    file = open(output_file)
                    return file.read()
            else:
                print("Error converting file")

        except Exception as e:
            print(e)
            print(format_exc())
