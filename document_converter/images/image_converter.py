import img2pdf

from ..decorators import validate_file_type


@validate_file_type(['png', 'jpg', 'jpeg'])
def convert_image_to_pdf(file_path: str, output_file_path: str):
    try:
        with open(output_file_path, "wb") as f:
            f.write(img2pdf.convert(file_path))

        return True
    except Exception as ex:
        print(ex)
        return False
