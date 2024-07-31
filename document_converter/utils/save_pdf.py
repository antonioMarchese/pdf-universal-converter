from io import BytesIO


def save_pdf_file(pdf_data: BytesIO, file_path: str) -> None:
    with open(file_path, "wb") as f:
        f.write(pdf_data.getvalue())
