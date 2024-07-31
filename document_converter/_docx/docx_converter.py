from traceback import format_exc

from docx2pdf import convert

from ..decorators import validate_file_type


@validate_file_type(['docx'])
def convert_docx_to_pdf(file_path: str, output_file_path: str):
    try:
        convert(file_path, output_file_path)
        return True
    except Exception as ex:
        print(ex)
        print(format_exc())
        return False
